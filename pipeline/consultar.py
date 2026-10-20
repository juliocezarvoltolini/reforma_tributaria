"""Consulta com filtro temporal — a forma correta de ler esta base.

Busca textual crua ignora vigência e devolve dispositivo que ainda não vale.
Este script aplica o filtro temporal ANTES de retornar (PREMISSAS.md §3.2) e
mostra as remissões a seguir antes de concluir (CLAUDE.md, passo 3) e, na
remissão a lei futura, a regulamentação localizada ou a lacuna (passo 5).

Uso:
    python3 pipeline/consultar.py --data 2027-01-01 --termo "credito"
    python3 pipeline/consultar.py --urn "urn:lex:...!art12" --seguir
"""
from __future__ import annotations

import argparse
import json
import datetime as _dt
import re
import sys
import unicodedata

from comum import RAIZ, arquivos_dispositivos, ler_frontmatter, para_data, status_em

ROTULO = {
    "vigente": "vigente e produzindo efeitos",
    "vigente_sem_efeitos": "vigente, mas AINDA NAO produz efeitos",
    "futuro": "ainda NAO vigente",
    "revogado": "REVOGADO",
    "sem_efeitos": "vigente, mas ja NAO produz efeitos",
}


FORA_DE_VIGOR = {"futuro", "revogado", "sem_efeitos"}


def _datas_com_precisao_de_ano(item: dict) -> list[tuple[str, _dt.date]]:
    precisao = item.get("precisao") or {}
    saida = []
    for campo, valor in precisao.items():
        data = para_data(item.get(campo))
        if valor == "ano" and data is not None:
            saida.append((campo, data))
    return saida


def incertezas(meta: dict, referencia: _dt.date) -> list[str]:
    """Avisos para datas de precisão de ano que caem no ano consultado.

    "Em 2027" não diz o dia. A base grava 1º de janeiro por convenção; dentro do
    ano, o estado calculado pode estar errado e quem consulta precisa saber.
    """
    avisos = []
    for item in [meta, *(meta.get("excecoes_subdivisao") or [])]:
        rotulo = "" if item is meta else f" ({item.get('urn', '').split('!')[-1]})"
        for campo, data in _datas_com_precisao_de_ano(item):
            if data.year == referencia.year:
                avisos.append(f"{campo}{rotulo} tem precisao de ANO ({data.year}): o texto "
                              f"nao diz o dia, e o estado em {referencia} e incerto")
    return avisos


def excecoes_na_data(meta: dict, referencia: _dt.date) -> list[tuple[str, str]]:
    """(urn, estado) de cada subdivisão com datas próprias. O que a exceção não
    diz herda do artigo."""
    saida = []
    for exc in meta.get("excecoes_subdivisao") or []:
        datas = {c: exc.get(c, meta.get(c)) for c in
                 ("vigencia_inicio", "vigencia_fim", "efeitos_inicio", "efeitos_fim")}
        saida.append((exc["urn"], status_em(datas, referencia)))
    return saida


def relevante_na_data(meta: dict, referencia: _dt.date) -> bool:
    """O dispositivo entra no resultado da consulta nesta data?

    Não omite o que é incerto (data de precisão de ano no ano consultado), nem o
    artigo que, fora de vigor, tem uma subdivisão em vigor.
    """
    if status_em(meta, referencia) not in FORA_DE_VIGOR:
        return True
    if incertezas(meta, referencia):
        return True
    return any(estado not in FORA_DE_VIGOR for _, estado in excecoes_na_data(meta, referencia))


def normalizar(texto: str) -> str:
    norm = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in norm if not unicodedata.combining(c))


def carregar() -> list[tuple[dict, str]]:
    itens = []
    for caminho in arquivos_dispositivos():
        try:
            itens.append(ler_frontmatter(caminho))
        except ValueError as exc:
            print(f"aviso: {exc}", file=sys.stderr)
    return itens


def origem_das_datas(meta: dict) -> list[str]:
    """Quem fixou cada eixo temporal e qual continua provisório (PREMISSAS.md §3.4).

    Decisão de regra e registro de IA não são revisão humana e não aparecem como tal.
    """
    eixos_todos = ["vigencia", "efeitos"]
    if meta.get("extracao") != "revisada":
        return ["vigencia e efeitos PROVISORIOS (revisao_temporal_pendente): datas da primeira "
                "publicacao, ou do ato. Nao usar para decisao sem revisar a fonte."]
    eixos = [e for e in eixos_todos if e in (meta.get("eixos_revisados") or eixos_todos)]
    por = str(meta.get("revisado_por") or "")
    if por.startswith("regra:"):
        quem = f"fixados por regra ({por.removeprefix('regra:')}), sem leitura humana,"
    elif por.startswith("ia:"):
        ids = ", ".join(meta.get("interpretacoes_ia") or []) or "?"
        quem = (f"propostos por IA ({por.removeprefix('ia:')}; interpretacoes: {ids}, ver "
                "temporal/ia.yaml) — NAO equivale a revisao humana —")
    else:
        quem = f"revisados por {por}"
    linhas = [f"{' e '.join(eixos)} {quem} em {meta.get('revisado_em')}"]
    faltam = [e for e in eixos_todos if e not in eixos]
    if faltam:
        linhas.append(f"{' e '.join(faltam)} PROVISORIOS: ainda nao revisados. Nao usar para "
                      "decisao sem revisar a fonte.")
    return linhas


ROTULO_ATO = {"regulamento": "regulamento", "ato_conjunto": "ato conjunto",
              "ato_poder_executivo": "ato do Poder Executivo", "ato_comite_gestor": "ato do Comite Gestor",
              "ato_rfb": "ato da RFB"}


def atos_infralegais_na_consulta(meta: dict) -> list[str]:
    """Avisos de que o texto remete a regulamento ou ato infralegal: a base nao os
    indexa, e o dispositivo sozinho nao diz a regra completa."""
    return [f"ATO INFRALEGAL: {ROTULO_ATO.get(a['tipo'], a['tipo'])} em {a['subdivisao'].split('!')[-1]}"
            " — Nao localizado nas fontes indexadas (a base nao liga o dispositivo ao ato; atos "
            "arquivados, sem fatiamento: consultar.py --acervo)"
            for a in meta.get("remete_a_ato") or []]


def buscar_no_acervo(indice: dict, termo: str) -> list[dict]:
    """Atos do acervo (indices/acervo.json) cujo título, ementa, número ou órgão
    contém o termo, sem acento nem caixa; na ordem do índice."""
    alvo = normalizar(termo)
    campos = ("titulo", "ementa", "numero", "orgao", "documento_fiscal", "id")
    return [a for a in indice.get("atos") or []
            if any(alvo in normalizar(str(a.get(c) or "")) for c in campos)]


def linhas_do_acervo(ato: dict) -> list[str]:
    linhas = [f"{ato.get('titulo')}  [{ato.get('tipo')}, nivel {ato.get('nivel')}]"]
    for campo in ("orgao", "numero", "data", "versao", "documento_fiscal", "situacao", "ementa"):
        if ato.get(campo):
            linhas.append(f"  {campo}: {ato[campo]}")
    linhas.append(f"  url: {ato.get('url')}")
    if ato.get("bloqueio"):
        linhas.append(f"  NAO ARQUIVADO — canal oficial recusou: {ato['bloqueio']}")
    else:
        linhas.append(f"  original: {ato.get('arquivo')}  sha256={ato.get('sha256')}  acesso={ato.get('acesso')}")
    linhas.append("  ACERVO: ato arquivado e conferido, NAO fatiado — a base nao trata a vigencia "
                  "nem os efeitos dele; leia o original e diga isso na resposta.")
    return linhas


def controverso_na_data(meta: dict, referencia: _dt.date) -> list[str]:
    """Linhas de aviso se a data cai num intervalo `controverso`: ali as leituras
    discordam, e o estado calculado pelas datas não basta. Fora dele, nada."""
    linhas = []
    for item in meta.get("controverso") or []:
        inicio, fim = para_data(item.get("inicio")), para_data(item.get("fim"))
        if not inicio or not fim or not inicio <= referencia < fim:
            continue
        eixo, campo = item.get("eixo"), f"{item.get('eixo')}_inicio"
        linhas.append(f"CONTROVERSO ({eixo}) de {item['inicio']} a {item['fim']} (exclusive): as "
                      "leituras discordam nesta data; fora do intervalo, concordam:")
        for leitura in item.get("leituras") or []:
            linhas.append(f"  - {leitura.get('descricao')}: {eixo} a partir de {leitura.get(campo)} "
                          f"({', '.join(leitura.get('fundamento') or [])})")
    return linhas


RE_RISCADO = re.compile(r"~~.*?~~")


def aviso_de_texto_riscado(meta: dict, corpo: str, referencia: _dt.date) -> str | None:
    """O compilado mostra TODO o texto do dispositivo riscado (superado ou revogado),
    e as datas não dizem isso na data consultada: datas provisórias de um anexo ou
    artigo revogado ainda não revisado dariam 'vigente'. Aviso, com as anotações."""
    from fatiar import RE_ANOTACAO

    if "~~" not in corpo or status_em(meta, referencia) in {"revogado", "sem_efeitos"}:
        return None
    sem_riscado = RE_RISCADO.sub("", corpo)
    if RE_ANOTACAO.sub("", sem_riscado).replace("|", "").strip():
        return None
    anotacoes = "; ".join(m.group(0) for m in RE_ANOTACAO.finditer(sem_riscado))
    return ("no compilado, TODO o texto deste dispositivo esta riscado (superado ou revogado)"
            + (f": {anotacoes}" if anotacoes else "")
            + " — o estado acima vem das datas e NAO reflete isso")


def _autoria(registro: dict, feito: str = "proposta") -> str:
    autor = str(registro.get("autor") or "")
    if autor.startswith("ia:"):
        return f"{feito} por IA ({autor.removeprefix('ia:')}) — NAO equivale a revisao humana"
    return f"{feito} por {autor}"


def ligacoes_a_lei_futura(meta: dict, registros: dict, indice: dict,
                          referencia: _dt.date) -> list[str]:
    """Remissão a lei futura deste dispositivo: a regulamentação localizada, com o
    estado de cada regulador na data, ou a lacuna; e, no regulador, a remissão que
    ele regula. Calar isso faria o leitor concluir 'não regulamentado'."""
    from regulamentacao import urn_do_artigo

    def do_artigo(citacoes: list[dict]) -> list[dict]:
        return [c for c in citacoes or [] if urn_do_artigo(str(c.get("urn"))) == meta["urn"]]

    linhas = []
    for rel, reg, _ in registros["regulamentacoes"]:
        proprias = do_artigo(reg.get("remissoes"))
        if proprias:
            linhas.append(f"REMISSAO A LEI FUTURA — regulamentacao localizada ({rel}; "
                          f"{_autoria(reg)}; confianca: {reg.get('confianca')}):")
            for remissao in proprias:
                linhas.append(f"  {remissao['urn'].split('!')[-1]} regulada por:")
            for regulador in reg.get("regulado_por") or []:
                alvo = indice.get(urn_do_artigo(str(regulador.get("urn"))))
                estado = ROTULO.get(status_em(alvo[0], referencia), "?") if alvo else "fora da base"
                linhas.append(f"    - {regulador.get('urn')} — em {referencia}: {estado}")
        if do_artigo(reg.get("regulado_por")):
            urns = ", ".join(str(r.get("urn")) for r in reg.get("remissoes") or [])
            linhas.append(f"regulamenta remissao a lei futura de: {urns} ({rel}; {_autoria(reg)}; "
                          f"confianca: {reg.get('confianca')})")
    for rel, lac, _ in registros["lacunas"]:
        for remissao in do_artigo(lac.get("remissoes")):
            linhas.append(f"LACUNA ({rel}): {remissao['urn'].split('!')[-1]} — Nao localizado nas "
                          f"fontes indexadas (pesquisado em {', '.join(lac.get('pesquisado_em') or [])}; "
                          f"{_autoria(lac, 'busca feita')}, {lac.get('data')})")
    return linhas


def imprimir(meta: dict, corpo: str, referencia: _dt.date, trecho: str | None,
             ligacoes: list[str] = ()) -> None:
    estado = status_em(meta, referencia)
    print(f"\n{'=' * 72}")
    print(f"{meta['norma']} — {meta['dispositivo']}")
    print(f"URN: {meta['urn']}")
    controverso = controverso_na_data(meta, referencia)
    if controverso:
        print(f"Estado em {referencia}: CONTROVERSO — pelas datas gravadas: "
              f"{ROTULO.get(estado, estado)}; ver as leituras abaixo")
        for linha in controverso:
            print(f"  ATENCAO: {linha}" if linha.startswith("CONTROVERSO") else f"  {linha}")
    else:
        print(f"Estado em {referencia}: {ROTULO.get(estado, estado)}")
    print(f"  vigencia: {meta.get('vigencia_inicio')} -> {meta.get('vigencia_fim') or 'sem termo'}")
    print(f"  efeitos:  {meta.get('efeitos_inicio')} -> {meta.get('efeitos_fim') or 'sem termo'}")
    pub = meta.get("publicacao")
    if isinstance(pub, dict):
        origem = {"dou": "DOU", "rodape_compilado": "rodape do compilado, NAO confirmada no DOU"}
        print(f"  ato: {meta.get('data_ato')}   publicacao: {', '.join(pub.get('datas') or []) or 'nao localizada'}"
              f" ({origem.get(pub.get('fonte'), '-')})")
    if meta.get("titulo"):
        print(f"  titulo: {meta['titulo']}")
    for aviso in incertezas(meta, referencia):
        print(f"  ATENCAO: {aviso}")
    if riscado := aviso_de_texto_riscado(meta, corpo, referencia):
        print(f"  ATENCAO: {riscado}")
    for urn, estado_exc in excecoes_na_data(meta, referencia):
        print(f"  subdivisao com datas proprias: {urn.split('!')[-1]} — "
              f"{ROTULO.get(estado_exc, estado_exc)}")
    fundamento = meta.get("fundamento_temporal") or {}
    if fundamento:
        print(f"  fundamento temporal: vigencia {fundamento.get('vigencia')}; "
              f"efeitos {fundamento.get('efeitos')}")
    for linha in origem_das_datas(meta):
        alerta = "PROVISORI" in linha or "NAO equivale" in linha
        print(f"  {'ATENCAO' if alerta else 'origem das datas'}: {linha}")
    if meta.get("hierarquia"):
        print(f"  contexto: {' > '.join(meta['hierarquia'])}")
    print(f"  fonte: {meta['fonte']['url']} (acesso {meta['fonte']['acesso']})")

    for linha in atos_infralegais_na_consulta(meta):
        print(f"  {linha}")
    remissoes = meta.get("remete_a") or []
    if remissoes:
        print(f"\n  SEGUIR ANTES DE CONCLUIR ({len(remissoes)} remissao/oes):")
        for alvo in remissoes:
            print(f"    - {alvo}")
    if ligacoes:
        print()
        for linha in ligacoes:
            print(f"  {linha}")

    print()
    print(trecho if trecho else corpo)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", help="data de referencia (AAAA-MM-DD)")
    ap.add_argument("--termo", help="busca textual no corpo do dispositivo")
    ap.add_argument("--urn", help="dispositivo especifico")
    ap.add_argument("--seguir", action="store_true",
                    help="exibe tambem os dispositivos referidos por remissao")
    ap.add_argument("--incluir-nao-vigentes", action="store_true",
                    help="nao filtra por estado na data de referencia")
    ap.add_argument("--acervo", metavar="TERMO",
                    help="busca no acervo (decretos, atos infralegais, Ajustes SINIEF, Notas "
                         "Tecnicas): arquivados e conferidos, sem fatiamento")
    args = ap.parse_args()

    if args.acervo:
        caminho = RAIZ / "indices" / "acervo.json"
        indice_acervo = json.loads(caminho.read_text(encoding="utf-8")) if caminho.exists() else {}
        achados = buscar_no_acervo(indice_acervo, args.acervo)
        if not achados:
            print("Nao localizado no acervo indexado.", file=sys.stderr)
            return 1
        for ato in achados:
            print("\n".join(linhas_do_acervo(ato)) + "\n")
        return 0

    if not args.termo and not args.urn:
        ap.error("informe --termo, --urn ou --acervo")

    if args.data:
        referencia = _dt.date.fromisoformat(args.data)
    else:
        referencia = _dt.date.today()
        print(f"AVISO: data de referencia nao informada. Assumindo hoje ({referencia}).\n"
              "A transicao da reforma e escalonada por exercicio — informe --data "
              "para perguntas sobre outro ano.", file=sys.stderr)

    itens = carregar()
    if not itens:
        print("Base vazia: nenhum dispositivo em /normas/.\n"
              "Nada a responder — rode o pipeline de ingestao.", file=sys.stderr)
        return 1

    indice = {m["urn"]: (m, c) for m, c in itens}
    from regulamentacao import carregar_registros

    try:
        registros = carregar_registros()
    except ValueError as exc:
        registros = {"regulamentacoes": [], "lacunas": []}
        print(f"AVISO: registros de /interpretacoes/ ou /lacunas/ ilegiveis ({exc}). A consulta "
              "NAO mostra a regulamentacao das remissoes a lei futura.", file=sys.stderr)

    def ligacoes(meta: dict) -> list[str]:
        return ligacoes_a_lei_futura(meta, registros, indice, referencia)
    resultados: list[tuple[dict, str, str | None]] = []

    if args.urn:
        if args.urn not in indice:
            print(f"URN nao localizada nas fontes indexadas: {args.urn}", file=sys.stderr)
            return 1
        meta, corpo = indice[args.urn]
        resultados.append((meta, corpo, None))
    else:
        alvo = normalizar(args.termo)
        for meta, corpo in itens:
            if alvo in normalizar(corpo):
                linhas = [ln for ln in corpo.split("\n") if alvo in normalizar(ln)]
                resultados.append((meta, corpo, "\n\n".join(linhas[:3])))

    if not args.incluir_nao_vigentes:
        antes = len(resultados)
        resultados = [r for r in resultados if relevante_na_data(r[0], referencia)]
        filtrados = antes - len(resultados)
        if filtrados:
            print(f"({filtrados} dispositivo(s) omitido(s) por nao estarem em vigor "
                  f"em {referencia} — use --incluir-nao-vigentes para ve-los)",
                  file=sys.stderr)

    if not resultados:
        print("Nao localizado nas fontes indexadas para a data de referencia.",
              file=sys.stderr)
        return 1

    for meta, corpo, trecho in resultados:
        imprimir(meta, corpo, referencia, trecho, ligacoes(meta))
        if args.seguir:
            for alvo in meta.get("remete_a") or []:
                if alvo in indice:
                    m2, c2 = indice[alvo]
                    print(f"\n  --- remissao a partir de {meta['dispositivo']} ---")
                    imprimir(m2, c2, referencia, None, ligacoes(m2))

    print(f"\n{'=' * 72}")
    print(f"{len(resultados)} dispositivo(s). Data de referencia: {referencia}.")
    print("Cite a URN de todo dispositivo usado e rotule literal/derivado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
