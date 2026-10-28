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

import re

from acervo_texto import _separar

RE_CABECALHO = re.compile(r"^Hist[óo]rico de Altera[çc][õo]es\s*/\s*Cronograma\s*$")
# Versão de NT: dois dígitos depois do ponto ("1.09", "1.05a"); "2.1" é seção.
RE_VERSAO = re.compile(r"^(?P<v>\d{1,2}\.\d{2}[a-z]?)(?P<ast>\*+)?(?=\s|$)")
RE_NUMERADA = re.compile(r"^\d+(?:\.\d+)*\.?\s")
_DATA = r"\d{2}/\d{2}/\d{4}|\d{2}/\d{4}"
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
        base = {"versao": m.group("v"), "pagina": paginas[j], "trecho": trecho}
        if len(itens) == 2:
            lidas.append(dict(base, teste=itens[0], producao=itens[1], rodape=rodape))
        else:
            motivo = {0: "sem_data", 1: "uma_data"}.get(len(itens), "datas_demais")
            pendencias.append(dict(base, motivo=motivo))

    return {"linhas": lidas, "pendencias": pendencias}


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
                      "teste/producao estao como a NT os escreve. Pendencias nao foram resolvidas."),
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
                   "| versão | teste | produção | rodapé | página |", "|---|---|---|---|---|"]
        linhas += [f"| {x['versao']} | {x['teste']} | {x['producao']} | {x['rodape']} | {x['pagina']} |"
                   for x in n["linhas"]]
    return "\n".join(linhas) + "\n"
