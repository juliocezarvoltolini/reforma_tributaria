"""Cronograma de implantação por versão das Notas Técnicas, lido da tabela
"Histórico de Alterações / Cronograma" do texto da NT (indices/acervo_texto/).

Por SCRIPT, e só o inequívoco: uma linha de versão com exatamente duas datas
(ou intervalos) — a primeira é a implantação em teste/homologação, a segunda a de
produção, na ordem das colunas da tabela. O texto da data fica como a NT o
escreve ("01/2026", "De 07/07/2025 até 28/07/2025", "Até 05/10/2026"); asterisco
de rodapé é registrado, não interpretado.

Tudo o que não é inequívoco vira PENDÊNCIA, com motivo, página e trecho — nunca
palpite: `tabela_nao_localizada`, `sem_data`, `uma_data` (não se sabe a coluna),
`datas_demais`. A tabela é lida também na página seguinte, quando continua.

Leitura do documento, não decisão normativa: diz o que a NT declara.
Formatos medidos em 2026-10-28 (NF-e NT 2025.002 v1.52, NT 2026.007 v1.10, CT-e
NT 2025.001 v1.14b). Função pura do texto do acervo (`indexar.py` grava
indices/cronograma_nt.json e .md).
"""
from __future__ import annotations

import functools
import re

from acervo_texto import _separar

RE_CABECALHO = re.compile(r"^Hist[óo]rico\s+de\s+Altera[çc][õo]es\s*/\s*Cronograma\s*$")
# Versão de NT: dois dígitos depois do ponto ("1.09", "1.05a"); "2.1" é seção.
# Letra separada ("1.05 a  Correção", "1.05 a  Correção") é da versão quando o
# próximo caractere não-espaço não é letra minúscula; "1.10 a partir de" não é.
RE_VERSAO = re.compile(r"^(?P<v>\d{1,2}\.\d{2}[a-z]?)(?:\s(?P<letra>[a-z])(?=\s+[^a-zà-ÿ\s]))?(?P<ast>\*+)?(?=\s|$)")
# Fim da tabela: título de seção ("2.1 Seção", "1. Introdução"), linha de tabela de
# campos ("324.35 UB35 ..."), rodapé ("* Implantação ..."), o detalhamento ou a
# "Observação:" abaixo dela.
# Continuação de célula que começa por número ("15 e UB64-20).", "1.949 e 2.949")
# NÃO encerra: o que segue o número é minúscula.
RE_NUMERADA = re.compile(r"^(?:\d+(?:\.\d+)*\.?\s+[A-ZÀ-Ý][a-zà-ÿ]|\d+\.\d+\s+[A-Z]{1,3}\d|\*|Detalhamento\b|Observa[çc][ãa]o\b)")
_MESES = "janeiro|fevereiro|março|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro"
# dd/mm/aaaa, mm/aaaa, ou por extenso ("06 abril 2026", "04 de maio de 2026").
_DATA = rf"\d{{2}}/\d{{2}}/\d{{4}}|\d{{2}}/\d{{4}}|\d{{1,2}}\s+(?:de\s+)?(?:{_MESES})\s+(?:de\s+)?\d{{4}}"
RE_ITEM = re.compile(rf"(?<![\d/])(?P<de>De\s+)?(?P<ate>At[ée]\s+)?(?P<d1>{_DATA})(?P<a1>\*+)?"
                     rf"(?:\s+at[ée]\s+(?P<d2>{_DATA})(?P<a2>\*+)?)?(?![\d/])")


def _itens(texto: str) -> tuple[list[str], list[str]]:
    """(datas ou intervalos como a NT os escreve, asteriscos das datas)."""
    itens, marcas = [], []
    for m in RE_ITEM.finditer(texto):
        if m.group("d2"):
            itens.append(f"De {m.group('d1')} até {m.group('d2')}" if m.group("de")
                         else f"{m.group('d1')} até {m.group('d2')}")
        elif m.group("ate"):
            itens.append(f"Até {m.group('d1')}")
        else:
            itens.append(m.group("d1"))
        marcas += [a for a in (m.group("a1"), m.group("a2")) if a]
    return itens, marcas


def ler_cronograma(md: str) -> dict:
    corpo = _separar(md)[1] if md.startswith("---\n") else md
    fisicas = corpo.split("\n")
    pagina, inicio = None, None
    paginas = []
    for i, linha in enumerate(fisicas):
        m = re.match(r"## Página (\d+)$", linha.strip())
        if m:
            pagina = int(m.group(1))
        paginas.append(pagina)
        if inicio is None and RE_CABECALHO.match(linha.strip()):
            inicio = i
    if inicio is None:
        return {"linhas": [], "pendencias": [{"versao": None, "motivo": "tabela_nao_localizada",
                                              "pagina": None, "trecho": ""}]}

    # Linhas da tabela: da linha seguinte ao cabeçalho em diante. Na quebra de página,
    # a tabela continua se a página seguinte começa (depois do cabeçalho repetido da
    # página) por uma linha de versão. Linha numerada que não é versão ("2.1 Seção",
    # "324.35 UB35 ...") encerra a tabela.
    linhas_tabela: list[tuple[int, list[str]]] = []
    j = inicio + 1
    while j < len(fisicas):
        texto = fisicas[j].strip()
        if texto.startswith("## Página "):
            proximas = [k for k in range(j + 1, min(j + 25, len(fisicas))) if fisicas[k].strip()][:10]
            k = next((k for k in proximas if RE_VERSAO.match(fisicas[k].strip())), None)
            if k is None:
                break
            j = k
            continue
        if RE_VERSAO.match(texto):
            linhas_tabela.append((j, [texto]))
        elif RE_NUMERADA.match(texto):
            break
        elif linhas_tabela and texto:
            linhas_tabela[-1][1].append(texto)
        j += 1

    lidas, pendencias = [], []
    for j, partes in linhas_tabela:
        trecho = " ".join(partes)
        m = RE_VERSAO.match(trecho)
        itens, marcas = _itens(trecho[m.end():])
        rodape = "; ".join(dict.fromkeys(([m.group("ast")] if m.group("ast") else []) + marcas))
        base = {"versao": m.group("v") + (m.group("letra") or ""), "pagina": paginas[j], "trecho": trecho}
        if len(itens) == 2:
            lidas.append(dict(base, teste=itens[0], producao=itens[1], rodape=rodape))
        else:
            motivo = {0: "sem_data", 1: "uma_data"}.get(len(itens), "datas_demais")
            pendencias.append(dict(base, motivo=motivo))

    return {"linhas": lidas, "pendencias": pendencias}


# --------------------------------------------------- leituras de pendências
# Pendência que o script não lê pode ser lida por pessoa ou por IA, em
# interpretacoes/cronograma_nt/*.yaml (camada 3). A leitura aponta a linha da
# tabela pela ALTURA na página do PDF, e a validação extrai de novo, do original,
# o texto das colunas Teste e Produção naquelas alturas: tem de ser o registrado.
# Leitura de IA não equivale a revisão humana (`origem` diz quem leu).

DIR_LEITURAS = "cronograma_nt"
RESULTADOS = ("lida", "ambigua", "sem_data")
CAMPOS_LEITURA = ("nt", "versao", "pagina", "motivo", "teste", "producao", "resultado", "leitura", "autor", "data")


def carregar_leituras() -> list[dict]:
    import yaml

    from comum import DIR_INTERPRETACOES

    leituras = []
    for caminho in sorted((DIR_INTERPRETACOES / DIR_LEITURAS).glob("*.yaml")):
        leituras += (yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}).get("leituras") or []
    return leituras


def _pendencias(rel: dict, leitura: dict) -> list[dict]:
    return [p for nt in rel["notas_tecnicas"] if nt["id"] == leitura.get("nt") for p in nt["pendencias"]
            if (p.get("versao"), p.get("pagina"), p.get("motivo")) == (
                leitura.get("versao"), leitura.get("pagina"), leitura.get("motivo"))]


def problemas_da_leitura(leitura: dict, rel: dict, obter_original) -> list[str]:
    """Erros de uma leitura: campos, pendência correspondente na saída do script, e o
    texto de cada coluna no PDF, nas alturas dadas, igual ao registrado."""
    import cronograma_pdf
    from acervo import normalizar

    rotulo = f"{leitura.get('nt')} v{leitura.get('versao')} p.{leitura.get('pagina')}"
    probs = [f"{rotulo}: campo {c} ausente" for c in CAMPOS_LEITURA if leitura.get(c) in (None, [])
             and c not in ("teste", "producao")]
    if leitura.get("resultado") not in RESULTADOS:
        probs.append(f"{rotulo}: resultado {leitura.get('resultado')!r} fora de {RESULTADOS}")
    casam = _pendencias(rel, leitura)
    if not casam:
        probs.append(f"{rotulo}: nenhuma pendência {leitura.get('motivo')!r} correspondente na saída do script")
    elif len(casam) > 1:
        probs.append(f"{rotulo}: a chave casa com mais de uma pendência — leitura ambígua")
    if bool(leitura.get("alturas")) == bool(leitura.get("faixa_y")):
        probs.append(f"{rotulo}: informe `alturas` (linhas da célula) ou `faixa_y` (célula inteira), um só")
    if probs:
        return probs
    dados = obter_original(leitura["nt"])
    for coluna in ("teste", "producao"):
        if leitura.get("faixa_y"):
            ymin, ymax = leitura["faixa_y"]
            no_pdf = cronograma_pdf.texto_na_faixa(leitura["nt"], leitura["pagina"], ymin, ymax, coluna, dados=dados)
        else:
            no_pdf = cronograma_pdf.texto_nas_alturas(leitura["nt"], leitura["pagina"], leitura["alturas"], coluna,
                                                      dados=dados)
        if normalizar(no_pdf) != normalizar(str(leitura.get(coluna) or "")):
            probs.append(f"{rotulo}: {coluna} registrado {leitura.get(coluna)!r}, no PDF {no_pdf!r}")
    return probs


def aplicar_leituras(rel: dict, leituras: list[dict]) -> dict:
    """Cada pendência com leitura vira linha (com `origem`, `resultado`, `leitura`,
    `etapa`); várias leituras da mesma pendência (etapas) viram várias linhas."""
    por_chave: dict = {}
    for lt in leituras:
        por_chave.setdefault((lt["nt"], lt["versao"], lt["pagina"], lt["motivo"]), []).append(lt)
    for nt in rel["notas_tecnicas"]:
        restantes = []
        for p in nt["pendencias"]:
            lidas = por_chave.get((nt["id"], p.get("versao"), p.get("pagina"), p.get("motivo")))
            if not lidas:
                restantes.append(p)
                continue
            for lt in lidas:
                nt["linhas"].append({"versao": p["versao"], "pagina": p["pagina"], "teste": lt.get("teste") or "",
                                     "producao": lt.get("producao") or "", "rodape": "", "trecho": p["trecho"],
                                     "origem": lt["autor"], "resultado": lt["resultado"],
                                     "leitura": lt["leitura"], "etapa": lt.get("etapa")})
        nt["pendencias"] = restantes
    return rel


def leituras_conferidas(rel: dict, leituras: list[dict], obter_original) -> tuple[list[dict], list[str]]:
    """(leituras que passam na conferência, erros) — contra o relatório do SCRIPT."""
    validas, erros = [], []
    for lt in leituras:
        probs = problemas_da_leitura(lt, rel, obter_original)
        (erros.extend(probs) if probs else validas.append(lt))
    return validas, erros


@functools.lru_cache(maxsize=None)
def obter_original(rid: str) -> bytes:
    import json

    from comum import MANIFEST, caminho_fonte

    return caminho_fonte(json.loads(MANIFEST.read_text(encoding="utf-8"))["documentos"][f"acervo/{rid}"]).read_bytes()


def relatorio(regs: list[dict], textos: dict[str, str]) -> dict:
    nts = []
    for reg in sorted(regs, key=lambda r: r["id"]):
        if reg.get("tipo") != "nota.tecnica" or reg["id"] not in textos:
            continue
        r = ler_cronograma(textos[reg["id"]])
        nts.append({"id": reg["id"], "titulo": reg.get("titulo"), "versao": reg.get("versao"),
                    "documento_fiscal": reg.get("documento_fiscal"), "url": reg.get("url"), **r})
    return {"aviso": ("Cronograma de implantacao lido por script da tabela 'Historico de Alteracoes / "
                      "Cronograma' de cada NT: o que o documento declara, nao decisao normativa. "
                      "teste/producao estao como a NT os escreve. Linha com origem ia:... foi lida por IA a partir da "
                      "posicao no PDF (interpretacoes/cronograma_nt/): nao equivale a revisao humana; resultado "
                      "'ambigua' lista as datas da celula sem dizer a qual item cada uma se aplica."),
            "notas_tecnicas": nts}


def resumo_markdown(rel: dict) -> str:
    nts = rel["notas_tecnicas"]
    linhas = ["# Cronograma de implantação das NTs (leitura por script)", "", rel["aviso"], "",
              f"- NTs: {len(nts)}; com linhas lidas: {sum(bool(n['linhas']) for n in nts)}",
              f"- linhas lidas: {sum(len(n['linhas']) for n in nts)}; "
              f"pendências: {sum(len(n['pendencias']) for n in nts)}", "",
              "| NT | versão do documento | linhas lidas | pendências |", "|---|---|---|---|"]
    for n in nts:
        linhas.append(f"| {n['id']} | {n.get('versao') or ''} | {len(n['linhas'])} | {len(n['pendencias'])} |")
    for n in nts:
        if not n["linhas"]:
            continue
        linhas += ["", f"## {n['id']} (versão {n.get('versao') or '?'})", "",
                   "| versão | etapa | teste | produção | rodapé | página | origem | resultado |",
                   "|---|---|---|---|---|---|---|---|"]
        linhas += [f"| {x['versao']} | {x.get('etapa') or ''} | {x['teste']} | {x['producao']} | {x['rodape']} | "
                   f"{x['pagina']} | {x.get('origem', 'regra:cronograma-nt/v1')} | {x.get('resultado', 'lida')} |"
                   for x in n["linhas"]]
    return "\n".join(linhas) + "\n"
