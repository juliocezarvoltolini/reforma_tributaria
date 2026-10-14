"""Etapa 4 — PROPÕE a revisão temporal de uma norma. Não aplica nada.

O fatiamento deixa todo dispositivo com `vigencia_inicio` e `efeitos_inicio`
iguais à data do ato e `revisao_temporal_pendente: true`: o parser não infere
vigência nem eficácia (PREMISSAS.md §3; docs/MODELO-DADOS.md). Estes campos vêm
da cláusula de vigência da própria norma e exigem revisão humana.

Este script prepara essa revisão. Lê `normas/` e o original em `fontes/` e grava
uma PROPOSTA em `temporal/propostas/<slug>.yaml`, com:

  - a cláusula de vigência ("entra em vigor: I - em 2027, em relação aos arts. ...")
    aplicada a cada artigo, com a URN do inciso como `fundamento`;
  - os marcos temporais PRÓPRIOS de cada artigo (anos, "a partir de", "até que
    lei...", promulgação, publicação), em trecho literal e sem interpretação,
    porque vigência não é eficácia e é o texto do artigo que diz quando produz
    efeitos;
  - as datas de referência lidas do original (data do ato, publicação no DOU);
  - campos de decisão vazios, para o humano preencher.

Regras que o script respeita:

  - Nada em `normas/` é alterado. A proposta é um documento de trabalho.
  - Texto normativo nunca é digitado: todo trecho citado vem de `normas/`.
  - Conservador: só interpreta o que casa com um padrão exato. O resto vira
    `nao_interpretado`, com o motivo. E se QUALQUER inciso ficar sem
    interpretação, "demais dispositivos" não pode ser resolvido, porque não se
    sabe quais artigos os incisos não interpretados nomeiam.
  - Nunca sobrescreve uma proposta em que já haja decisão humana.

Uso:
    python pipeline/propor_vigencia.py --slug emc-132-2023
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

from comum import (
    DIR_TEMPORAL,
    MANIFEST,
    arquivos_norma,
    caminho_fonte,
    gravar_texto,
    ler_frontmatter,
    urn_dispositivo,
    urn_norma,
)
from fatiar import (
    CATALOGO,
    chave_ordem,
    html_para_linhas,
    linhas_citadas,
    subdivisao_por_linha,
)

DIR_PROPOSTAS = DIR_TEMPORAL / "propostas"

# ---------------------------------------------------------------------------
# Cláusula de vigência
# ---------------------------------------------------------------------------

RE_ENTRA_EM_VIGOR = re.compile(r"\bentra(?:r[áa])?\s+em\s+vigor\b", re.IGNORECASE)
RE_INCISO = re.compile(r"^([IVXLC]+)\s*[-–]\s*(.+)$")
RE_TERMO_ANO = re.compile(r"^em\s+((?:19|20)\d{2})\s*,\s*(.+)$", re.IGNORECASE)
RE_TERMO_PUBLICACAO = re.compile(
    r"^na\s+data\s+de\s+sua\s+publica[çc][ãa]o\s*,\s*(.+)$", re.IGNORECASE
)
RE_ALCANCE_DEMAIS = re.compile(r"^em\s+rela[çc][ãa]o\s+aos\s+demais\s+dispositivos$", re.IGNORECASE)
RE_ALCANCE_ARTIGOS = re.compile(r"^em\s+rela[çc][ãa]o\s+aos?\s+arts?\.\s*(.+)$", re.IGNORECASE)
RE_NUMERO = re.compile(r"^(\d+)\s*[ºo°]?(?:\s*-\s*([A-Z]))?$")


def localizar_clausula(corpos: dict[str, list[str]]) -> list[str]:
    """Artigos cujo CAPUT diz que "entra em vigor". Só o caput conta: "entrada em
    vigor" no meio de outro artigo é referência, não cláusula."""
    return [n for n, linhas in corpos.items() if linhas and RE_ENTRA_EM_VIGOR.search(linhas[0])]


def _numeros(lista: str) -> list[str] | None:
    """'3º e 11' -> ['3', '11']. None se houver QUALQUER coisa além de números
    separados por vírgula ou 'e' (intervalo 'a', 'exceto', parágrafo...)."""
    saida = []
    for token in re.split(r"\s*,\s*|\s+e\s+", lista.strip()):
        m = RE_NUMERO.match(token.strip())
        if not m:
            return None
        saida.append(m.group(1) + (f"-{m.group(2)}" if m.group(2) else ""))
    return saida


def _interpretar_inciso(texto: str) -> tuple[dict | None, dict | None, str | None]:
    """(termo, alcance, motivo). Motivo preenchido = não interpretado."""
    # "; e" ao fim liga o inciso ao seguinte; ";" e "." encerram.
    texto = re.sub(r"\s*;\s*e\s*$", "", texto).rstrip(" ;.")

    if m := RE_TERMO_ANO.match(texto):
        termo, resto = {"tipo": "ano", "ano": int(m.group(1))}, m.group(2)
    elif m := RE_TERMO_PUBLICACAO.match(texto):
        termo, resto = {"tipo": "publicacao"}, m.group(1)
    else:
        return None, None, ("termo fora dos padrões reconhecidos "
                            "('em <ano>' ou 'na data de sua publicação')")

    if RE_ALCANCE_DEMAIS.match(resto):
        return termo, {"tipo": "demais"}, None
    if m := RE_ALCANCE_ARTIGOS.match(resto):
        artigos = _numeros(m.group(1))
        if artigos is None:
            return termo, None, ("lista de artigos fora do padrão (só números separados "
                                 "por vírgula e 'e'; intervalo, 'exceto' e subdivisão "
                                 "não são interpretados)")
        return termo, {"tipo": "artigos", "artigos": artigos}, None
    return termo, None, "alcance fora dos padrões reconhecidos"


def interpretar_clausula(
    linhas: list[str], urn_base: str, artigo: str, existentes: list[str]
) -> dict:
    """Aplica a cláusula de vigência a cada artigo da norma."""
    incisos = []
    for linha in linhas[1:]:
        m = RE_INCISO.match(linha)
        if not m:
            continue
        rotulo, texto = m.group(1), m.group(2)
        termo, alcance, motivo = _interpretar_inciso(texto)
        incisos.append({
            "urn": urn_dispositivo(urn_base, artigo, inciso=rotulo),
            "rotulo": rotulo,
            "texto": linha,
            "interpretado": motivo is None,
            "termo": termo if motivo is None else None,
            "alcance": alcance if motivo is None else None,
            "motivo": motivo,
        })

    interpretados = [i for i in incisos if i["interpretado"]]
    nao_interpretados = [i["rotulo"] for i in incisos if not i["interpretado"]]
    nomeados: dict[str, list[dict]] = {}
    inexistentes: list[str] = []
    for i in interpretados:
        if i["alcance"]["tipo"] == "artigos":
            for n in i["alcance"]["artigos"]:
                nomeados.setdefault(n, []).append(i)
                if n not in existentes and n not in inexistentes:
                    inexistentes.append(n)
    demais = [i for i in interpretados if i["alcance"]["tipo"] == "demais"]

    mapa = {}
    for n in existentes:
        entrada = {"inciso": None, "termo": None, "fundamento": None, "motivo": None,
                   "ressalva": None}
        nomes = nomeados.get(n, [])
        if len(nomes) > 1:
            entrada["motivo"] = "nomeado em mais de um inciso: " + ", ".join(
                i["rotulo"] for i in nomes)
        elif len(nomes) == 1:
            entrada.update(inciso=nomes[0]["rotulo"], termo=nomes[0]["termo"],
                           fundamento=nomes[0]["urn"])
            if nao_interpretados:
                entrada["ressalva"] = (
                    "inciso(s) " + ", ".join(nao_interpretados) + " não interpretado(s) "
                    "podem também nomear este artigo")
        elif nao_interpretados:
            entrada["motivo"] = (
                "inciso(s) " + ", ".join(nao_interpretados) + " não interpretado(s): não se "
                "sabe se este artigo é nomeado por eles, então 'demais dispositivos' não "
                "pode ser resolvido")
        elif len(demais) == 1:
            entrada.update(inciso=demais[0]["rotulo"], termo=demais[0]["termo"],
                           fundamento=demais[0]["urn"])
        elif len(demais) > 1:
            entrada["motivo"] = "mais de um inciso 'demais dispositivos'"
        else:
            entrada["motivo"] = ("nenhum inciso nomeia este artigo e a cláusula não tem "
                                 "'demais dispositivos'")
        mapa[n] = entrada

    return {
        "urn": urn_dispositivo(urn_base, artigo),
        "caput": linhas[0] if linhas else None,
        "incisos": incisos,
        "mapa": mapa,
        "artigos_inexistentes": inexistentes,
    }


# ---------------------------------------------------------------------------
# Marcos temporais próprios de cada artigo
# ---------------------------------------------------------------------------

_MESES = ("janeiro|fevereiro|mar[çc]o|abril|maio|junho|julho|agosto|setembro|outubro|"
          "novembro|dezembro")

# Cada rótulo diz qual padrão casou. É ajuda de leitura, não interpretação.
PADROES_MARCO = [
    ("ano", re.compile(r"\b(?:19|20)\d{2}\b")),
    ("data_explicita", re.compile(rf"\b\d{{1,2}}\s*[ºo°]?\s+de\s+(?:{_MESES})\s+de\s+\d{{4}}\b",
                                  re.IGNORECASE)),
    ("a_partir_de_ate", re.compile(
        rf"\ba\s+partir\s+d[eo]\b|\bat[ée]\s+(?:(?:19|20)\d{{2}}\b|"
        rf"\d{{1,2}}\s*[ºo°]?\s+de\s+(?:{_MESES})\s+de\s+\d{{4}}|o\s+(?:final|fim)\b)",
        re.IGNORECASE)),
    ("evento_publicacao", re.compile(r"\bdata\s+d[ea]\s+(?:sua\s+)?publica[çc][ãa]o\b",
                                     re.IGNORECASE)),
    ("evento_promulgacao", re.compile(r"\bpromulga[çc][ãa]o\b", re.IGNORECASE)),
    ("entrada_em_vigor", re.compile(r"\bentra(?:da|r[áa])?\s+em\s+vigor\b", re.IGNORECASE)),
    ("produz_efeitos", re.compile(r"\bprodu(?:z|zir|zirá|zirão)\s+efeitos\b", re.IGNORECASE)),
    ("condicao_ate_que", re.compile(r"\bat[ée]\s+que\b", re.IGNORECASE)),
    # O efeito de um dispositivo que "remete" a lei complementar futura depende dela.
    # Cobertura PARCIAL: a ausência deste rótulo não prova que não há dependência.
    ("depende_de_lei_futura", re.compile(
        r"\blei\s+complementar\s+(?:definir|estabelecer|dispor|regular|prever|poder)[áa]\b|"
        r"\bnos\s+termos\s+d[ea]\s+lei\s+complementar\b|"
        r"\blei\s+complementar\s+que\s+instituir\b", re.IGNORECASE)),
    ("prazo_relativo", re.compile(
        r"\bem\s+at[ée]\s+\d+\s*\(|\bquinquenal\b|"
        r"\b(?:primeiro|segundo|terceiro|quarto|quinto)\s+ano\b|\bprazos?\b",
        re.IGNORECASE)),
]

# A data de OUTRA lei citada ("Lei nº 9.430, de 27 de dezembro de 1996") não é
# marco temporal desta norma.
RE_NORMA_CITADA_COM_DATA = re.compile(
    r"(?:Lei(?:\s+Complementar)?|Emenda\s+Constitucional|Decreto(?:-Lei)?|"
    r"Medida\s+Provis[óo]ria)\s+n[ºo°.]*\s*[\d.]+(?:-\d+)?,\s+de\s+\d{1,2}\s*[ºo°]?\s+de\s+"
    r"\w+\s+de\s+\d{4}",
    re.IGNORECASE,
)
RE_RISCADO = re.compile(r"~~.*?~~")


def _tipos_de_marco(linha: str) -> list[str]:
    """Rótulos dos padrões que casam no texto VIGENTE da linha (sem o riscado e
    sem as datas de outras normas citadas)."""
    texto = RE_NORMA_CITADA_COM_DATA.sub("", RE_RISCADO.sub("", linha))
    return [nome for nome, regex in PADROES_MARCO if regex.search(texto)]


def marcos_proprios(corpo: list[str], urn_base: str, artigo: str) -> dict:
    """Linhas do corpo com marco temporal PRÓPRIO, em trecho literal.

    O texto de outra norma que este artigo insere (entre aspas) não entra: o que
    ele diz sobre o tempo pertence à norma alterada. É só contado à parte.
    """
    citada = linhas_citadas(corpo)
    urns = subdivisao_por_linha(corpo, urn_base, artigo)
    marcos, citado_com_marcos = [], 0
    for linha, e_citada, urn in zip(corpo, citada, urns):
        tipos = _tipos_de_marco(linha)
        if not tipos:
            continue
        if e_citada:
            citado_com_marcos += 1
        else:
            marcos.append({"urn": urn, "tipos": tipos, "trecho": linha})
    return {"marcos": marcos, "citado_com_marcos": citado_com_marcos}


# ---------------------------------------------------------------------------
# Datas de referência, lidas do original
# ---------------------------------------------------------------------------

def _sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if not unicodedata.combining(c))


_NUM_MES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto",
     "setembro", "outubro", "novembro", "dezembro"], 1)}

RE_TITULO = re.compile(
    r"^(?:EMENDA CONSTITUCIONAL|LEI COMPLEMENTAR|LEI|DECRETO)\b.*?\bDE (\d{1,2})[ºO°]? DE "
    r"([A-ZÇÃÉÊ]+) DE (\d{4})\s*$"
)
RE_ASSINATURA = re.compile(r"^Bras[ií]lia,\s+(?:em\s+)?(\d{1,2})\s*[ºo°]?\s+de\s+(\w+)\s+de\s+(\d{4})")
RE_DOU = re.compile(r"publicado\s+no\s+DOU\s+(?:de\s+)?(\d{1,2})\.(\d{1,2})\.(\d{4})")


def _iso(dia: str, mes: str | int, ano: str) -> str | None:
    if isinstance(mes, str):
        mes = int(mes) if mes.isdigit() else _NUM_MES.get(_sem_acento(mes).lower())
    if not mes:
        return None
    return f"{int(ano):04d}-{int(mes):02d}-{int(dia):02d}"


def extrair_referencias(linhas_fonte: list[str]) -> dict:
    """Data do ato (título e linha de assinatura) e publicação no DOU (rodapé do
    compilado), cada uma com o trecho literal. O que não se acha fica nulo."""
    fontes = []
    for linha in linhas_fonte[:40]:
        if m := RE_TITULO.match(linha):
            if iso := _iso(m.group(1), m.group(2), m.group(3)):
                fontes.append({"origem": "titulo", "valor": iso, "trecho": linha})
                break
    for linha in linhas_fonte:
        if m := RE_ASSINATURA.match(linha):
            if iso := _iso(m.group(1), m.group(2), m.group(3)):
                fontes.append({"origem": "assinatura", "valor": iso, "trecho": linha})
                break
    valores = {f["valor"] for f in fontes}
    ato = {
        "valor": fontes[0]["valor"] if fontes else None,
        "fontes": fontes,
        "concordam": (len(valores) == 1) if len(fontes) > 1 else None,
    }

    dou_valores, dou_trechos = [], []
    for linha in linhas_fonte:
        achados = [_iso(d, mes, a) for d, mes, a in RE_DOU.findall(linha)]
        if achados:
            dou_valores.extend(a for a in achados if a)
            dou_trechos.append(linha)
    return {"data_do_ato": ato,
            "publicacao_dou": {"valores": dou_valores, "trechos": dou_trechos}}


# ---------------------------------------------------------------------------
# Montagem da proposta
# ---------------------------------------------------------------------------

RE_REVOGAM_SE = re.compile(r"^Art\.\s*\d+\s*[ºo°]?\.?\s+Revogam-se\b", re.IGNORECASE)


def _inicio_proposto(termo: dict, refs: dict) -> dict:
    if termo["tipo"] == "ano":
        return {
            "tipo": "ano",
            "ano": termo["ano"],
            "data_candidata": f"{termo['ano']}-01-01",
            "precisao": "ano",
            "nota": "o texto diz só o ano; 1º de janeiro é CONVENÇÃO (primeiro dia do ano), "
                    "não está no texto",
        }
    valores = refs["publicacao_dou"]["valores"]
    return {
        "tipo": "evento",
        "evento": "publicacao",
        "data_candidata": valores[0] if len(valores) == 1 else None,
        "precisao": "dia",
        "nota": "data lida do rodapé do texto compilado; confirmar no DOU (in.gov.br), "
                "que não está ingerido" if len(valores) == 1
                else "publicação não localizada ou ambígua no original: preencher à mão",
    }


def _decisoes(refs: dict, gravadas: set[str], dispositivos: list[dict]) -> list[dict]:
    decisoes = []
    if any(d["vigencia"]["proposta"] and d["vigencia"]["proposta"]["tipo"] == "ano"
           for d in dispositivos):
        decisoes.append({
            "id": "ano_sem_dia",
            "pergunta": "Quando a cláusula diz 'em <ano>', o campo vigencia_inicio exige uma "
                        "data completa. A proposta usa 1º de janeiro como candidata, por "
                        "convenção e não por texto. Aceitar a convenção, fixar outra data, ou "
                        "ampliar o modelo para aceitar ano?",
        })
    dou = refs["publicacao_dou"]["valores"]
    ato = refs["data_do_ato"]["valor"]
    if gravadas and dou and set(dou) != gravadas:
        decisoes.append({
            "id": "publicacao_x_data_do_ato",
            "pergunta": f"O pipeline grava como `publicacao` a data do ato ({', '.join(sorted(gravadas))}), "
                        f"e é dela que partem vigencia_inicio e efeitos_inicio provisórios. A "
                        f"cláusula 'na data de sua publicação' refere-se à publicação no DOU, "
                        f"que o rodapé do compilado informa ser {', '.join(dou)} (data do ato lida do "
                        f"original: {ato}). Separar `data_do_ato` de `publicacao` no modelo?",
        })
    if any(len(d["marcos_proprios"]) > 1 for d in dispositivos):
        decisoes.append({
            "id": "datas_por_subdivisao",
            "pergunta": "Vários artigos têm marcos temporais por subdivisão (incisos e "
                        "parágrafos). O front-matter guarda um par vigência/efeitos por "
                        "artigo. Registrar por subdivisão, ou manter por artigo e remeter ao "
                        "texto?",
        })
    inseridos = [d["artigo"] for d in dispositivos if "texto_inserido_em_outra_norma" in d["pendencias"]]
    if inseridos:
        decisoes.append({
            "id": "norma_alterada_nao_ingerida",
            "pergunta": f"Os artigos {', '.join(inseridos)} inserem texto em outra norma "
                        "(Constituição e/ou ADCT), que não está ingerida. A vigência do "
                        "artigo desta norma é a da cláusula; quando o texto inserido produz "
                        "efeitos depende do próprio texto inserido. Ingerir a norma alterada, "
                        "ou registrar a pendência em /lacunas/?",
        })
    if any({"condicao_regulamentacao", "depende_de_lei_futura"} & set(d["pendencias"])
           for d in dispositivos):
        decisoes.append({
            "id": "depende_de_lei_futura",
            "pergunta": "Há artigos que dependem de lei futura: transitórios ('Até que lei "
                        "complementar...') ou que remetem a ela ('Lei complementar "
                        "definirá...'). Se a lei foi editada, o efeito muda, mas verificar "
                        "isso é interpretação (camada 3) e exige a norma regulamentadora. "
                        "Registrar como pendente em /lacunas/ até lá? O rótulo "
                        "`depende_de_lei_futura` tem cobertura parcial: sua ausência não "
                        "prova que não há dependência.",
        })
    return decisoes


def construir(slug: str) -> dict:
    """Monta a proposta (dicionário) sem gravar nada."""
    catalogo = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))
    fonte = next((f for f in catalogo.get("fontes") or [] if f["slug"] == slug), None)
    if fonte is None:
        raise SystemExit(f"slug '{slug}' nao esta em fontes.yaml")
    base = urn_norma(fonte["autoridade"], fonte["data"], fonte["numero"])

    metas, corpos = {}, {}
    for caminho in arquivos_norma(slug):
        meta, corpo = ler_frontmatter(caminho)
        numero = meta["dispositivo"].removeprefix("art. ")
        metas[numero] = meta
        corpos[numero] = [ln for ln in corpo.strip().split("\n\n") if ln]
    if not metas:
        raise SystemExit(f"nenhum dispositivo de '{slug}' em normas/ — rode fatiar.py antes")
    ordem = sorted(metas, key=chave_ordem)
    corpos = {n: corpos[n] for n in ordem}

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    registro = manifest["documentos"][f"{slug}/texto_compilado"]
    refs = extrair_referencias(
        [ln.completa for ln in html_para_linhas(caminho_fonte(registro).read_bytes())])

    candidatos = localizar_clausula(corpos)
    if len(candidatos) == 1:
        clausula = interpretar_clausula(corpos[candidatos[0]], base, candidatos[0], ordem)
    else:
        clausula = {"urn": None, "incisos": [], "artigos_inexistentes": [],
                    "mapa": {n: {"inciso": None, "termo": None, "fundamento": None,
                                 "motivo": "cláusula de vigência não localizada de forma única "
                                           f"(candidatos: {candidatos})", "ressalva": None}
                             for n in ordem}}

    dispositivos = []
    for n in ordem:
        meta, corpo = metas[n], corpos[n]
        m = clausula["mapa"][n]
        marcos = marcos_proprios(corpo, base, n)
        tipos = {t for x in marcos["marcos"] for t in x["tipos"]}
        citados = list(meta.get("dispositivos_citados") or [])

        pendencias = []
        if m["inciso"] is None:
            pendencias.append("vigencia_nao_determinada")
        elif m["termo"]["tipo"] == "ano":
            pendencias.append("ano_sem_dia")
        elif m["termo"]["tipo"] == "publicacao":
            pendencias.append("publicacao_nao_confirmada_no_dou")
        if marcos["marcos"]:
            pendencias.append("marcos_proprios")
        if "condicao_ate_que" in tipos:
            pendencias.append("condicao_regulamentacao")
        if "depende_de_lei_futura" in tipos:
            pendencias.append("depende_de_lei_futura")
        if tipos & {"evento_publicacao", "evento_promulgacao", "entrada_em_vigor"}:
            pendencias.append("evento_relativo")
        if corpo and RE_REVOGAM_SE.match(corpo[0]):
            pendencias.append("revogacao_expressa")
        if citados:
            pendencias.append("texto_inserido_em_outra_norma")

        inicio = _inicio_proposto(m["termo"], refs) if m["inciso"] else None
        if inicio is None:
            efeitos = {"proposta": None, "motivo": m["motivo"]}
        elif marcos["marcos"] or citados:
            causas = []
            if marcos["marcos"]:
                causas.append("tem marco(s) temporal(is) ou dependência de lei futura no "
                              "próprio texto (ver `marcos_proprios`)")
            if citados:
                causas.append("insere texto em outra norma, ainda não ingerida")
            efeitos = {"proposta": None,
                       "motivo": "os efeitos não decorrem só da cláusula de vigência: o "
                                 "dispositivo " + " e ".join(causas)}
        else:
            efeitos = {"proposta": inicio,
                       "motivo": "nenhum marco temporal detectado pelos padrões do script (isto NÃO "
                                 "garante que não exista): LER O TEXTO antes de aceitar que os "
                                 "efeitos acompanham a vigência"}

        dispositivos.append({
            "urn": meta["urn"],
            "artigo": n,
            "vigencia": {
                "inciso": m["inciso"],
                "fundamento": m["fundamento"],
                "natureza": "derivado" if m["inciso"] else None,
                "proposta": inicio,
                "motivo": m["motivo"],
                "ressalva": m["ressalva"],
            },
            "efeitos": efeitos,
            "atual_no_pipeline": {
                "publicacao": str(meta.get("publicacao")),
                "vigencia_inicio": str(meta.get("vigencia_inicio")),
                "efeitos_inicio": str(meta.get("efeitos_inicio")),
            },
            "marcos_proprios": marcos["marcos"],
            "texto_inserido": {"artigos": citados, "linhas_com_marcos": marcos["citado_com_marcos"]},
            "pendencias": pendencias,
            "revisao": {
                "decisao": None,  # aceitar | alterar | rejeitar
                "vigencia_inicio_final": None,
                "efeitos_inicio_final": None,
                "revisado_por": None,
                "revisado_em": None,
                "observacao": None,
            },
        })

    gravadas = {d["atual_no_pipeline"]["publicacao"] for d in dispositivos}
    por_inciso: dict[str, int] = {}
    for d in dispositivos:
        k = d["vigencia"]["inciso"] or "indeterminado"
        por_inciso[k] = por_inciso.get(k, 0) + 1

    return {
        "norma": slug,
        "urn_norma": base,
        "titulo": fonte["titulo"],
        "gerado_por": "pipeline/propor_vigencia.py",
        "status": "proposta",
        "aviso": "PROPOSTA MECÂNICA, NÃO APLICADA. Nada em /normas/ foi alterado. Cada dispositivo "
                 "exige decisão humana em `revisao`. O script só interpreta padrões exatos; o "
                 "resto está marcado como não interpretado. Vigência não é eficácia: os marcos "
                 "próprios de cada artigo estão em `marcos_proprios`, em trecho literal.",
        "referencias": {**refs, "publicacao_gravada_hoje_nos_dispositivos": sorted(gravadas)},
        "clausula_de_vigencia": {k: v for k, v in clausula.items() if k != "mapa"},
        "decisoes_necessarias": _decisoes(refs, gravadas, dispositivos),
        "resumo": {
            "dispositivos": len(dispositivos),
            "por_inciso": por_inciso,
            "com_marcos_proprios": sum(1 for d in dispositivos if d["marcos_proprios"]),
            "com_texto_inserido_em_outra_norma": sum(
                1 for d in dispositivos if d["texto_inserido"]["artigos"]),
        },
        "dispositivos": dispositivos,
    }


def gravar_proposta(caminho: Path, proposta: dict) -> bool:
    """Grava a proposta. Recusa (False) se o arquivo existente já tem decisão humana."""
    if caminho.exists():
        existente = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
        if any((d.get("revisao") or {}).get("decisao") is not None
               for d in existente.get("dispositivos") or []):
            return False
    caminho.parent.mkdir(parents=True, exist_ok=True)
    gravar_texto(caminho, yaml.safe_dump(
        proposta, allow_unicode=True, sort_keys=False, default_flow_style=False, width=1000))
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", required=True, help="norma, como em pipeline/fontes.yaml")
    args = ap.parse_args()

    proposta = construir(args.slug)
    destino = DIR_PROPOSTAS / f"{args.slug}.yaml"
    if not gravar_proposta(destino, proposta):
        print(f"[{args.slug}] {destino.relative_to(DIR_TEMPORAL.parent)} ja tem decisao humana "
              "— nao sobrescrevo. Mova ou apague o arquivo se quiser regenerar.", file=sys.stderr)
        return 2

    r = proposta["resumo"]
    print(f"[{args.slug}] proposta gravada em {destino.relative_to(DIR_TEMPORAL.parent)}")
    print(f"  dispositivos: {r['dispositivos']}   por inciso: {r['por_inciso']}")
    print(f"  com marcos temporais proprios: {r['com_marcos_proprios']}   "
          f"inserindo texto em outra norma: {r['com_texto_inserido_em_outra_norma']}")
    print(f"  decisoes necessarias: {[d['id'] for d in proposta['decisoes_necessarias']]}")
    print("  NADA em /normas/ foi alterado. Revise, preencha `revisao` e so entao aplique.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
