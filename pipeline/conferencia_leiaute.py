"""Conferência das tabelas de campos das Notas Técnicas contra os schemas (XSD).

A tabela de campos da NT, no PDF, sai do extrator com colunas possivelmente
embaralhadas; a tabela lida dos XSD (indices/acervo_texto/, pacotes de schemas)
não. Aqui, cada linha de tabela da NT que trata de IBS, CBS ou IS é procurada no
schema do mesmo documento fiscal, pelo caminho que a própria tabela da NT dá
(subindo pelos pais), e a ocorrência é comparada:

- `confere`: o schema tem o campo nesse caminho, com a mesma ocorrência;
- `ocorrencia_diverge`: tem o campo, com outra ocorrência (a do schema vai junto);
- `ausente_no_schema`: nenhum campo nesse caminho.

A base não sabe qual pacote de schemas corresponde a qual versão da NT: a NT é
comparada com todos os pacotes do mesmo documento fiscal e o relatório NOMEIA o
que mais confere. Divergência não é erro da base: é informação — a NT pode ser
mais nova que o pacote, ou o contrário. Função pura do texto do acervo
(`indexar.py` grava indices/conferencia_leiaute.json e .md).

Formatos de linha medidos em 2026-10-26:
  NF-e (NT 2025.002):  "324.35 UB35 vIBSUF <descrição> E UB17 N 1-1 13v2"
  conjunta (CT-e, BP-e, NF3e, NFCom):  "7 pIBSUF E gIBSUF N 1-1 3,2/3,4 <descrição>"
"""
from __future__ import annotations

import re

from acervo_texto import _do_imposto, _separar

_ELE = r"(?:CE|CG|RC|CC|E|G|A)"
_ID = r"[A-Z]{1,3}\d{1,3}[a-z]?"
# Ocorrência e, logo depois, o tamanho ("13v2", "3v2-4", "3,2/3,4", "6", "1-60", "-").
_OC = r"(?P<oc>\d+-(?:\d+|[Nn]))(?=\s|$)(?:\s+(?P<tam>[\d,/v\-]+)(?=\s|$))?"
_TIPO = r"(?:(?:N|C|D|B64|-)\s+)?"
TEM_OCORRENCIA = re.compile(r"\s\d+-(?:\d+|[Nn])(?=\s|$)")
RE_NFE = re.compile(rf"^(?P<num>\d+(?:\.\d+)?)\s+(?P<id>{_ID})\s+(?P<campo>[a-zA-Z]\w*)\s+(?P<desc>.*?)\s+"
                    rf"(?P<ele>{_ELE})\s+(?P<pai>{_ID}|-)\s+{_TIPO}{_OC}")
RE_CONJUNTA = re.compile(rf"^(?P<num>\d+)\s+(?P<campo>[a-zA-Z]\w*)\s+(?P<ele>{_ELE})\s+(?P<pai>[a-zA-Z]\w*|-)\s+"
                         rf"{_TIPO}{_OC}")
INICIO_NFE = re.compile(rf"^\d+(?:\.\d+)?\s+{_ID}\s+[a-zA-Z]\w*\s")
INICIO_CONJUNTA = re.compile(rf"^\d+\s+[a-zA-Z]\w*\s+{_ELE}\s")


def linhas_de_tabela(md: str) -> list[dict]:
    """Linhas de tabela de campos do texto de uma NT, com a página. Linha quebrada
    pelo extrator (até 3 linhas físicas) é juntada."""
    fisicas = md.split("\n")
    saida, pagina, i = [], None, 0
    while i < len(fisicas):
        linha = fisicas[i].strip()
        m = re.match(r"## Página (\d+)$", linha)
        if m:
            pagina, i = int(m.group(1)), i + 1
            continue
        achou = None
        if INICIO_NFE.match(linha) or INICIO_CONJUNTA.match(linha):
            # Linha que já tem a sua ocorrência não se junta à seguinte: pegaria a dela.
            for n in ((1,) if TEM_OCORRENCIA.search(linha) else (1, 2, 3)):
                junto = " ".join(x.strip() for x in fisicas[i:i + n])
                m = RE_NFE.match(junto) or RE_CONJUNTA.match(junto)
                if m:
                    achou = (m, n)
                    break
        if achou:
            m, n = achou
            d = m.groupdict()
            saida.append({"campo": d["campo"], "id": d.get("id"), "pai": d["pai"],
                          "ocorrencia": d["oc"].replace("n", "N"), "tamanho": d.get("tam"), "pagina": pagina})
            i += n
        else:
            i += 1
    return saida


def _tamanho_nt(tam: str | None):
    """("dec", inteiros, casas_min, casas_max) | ("fixo", n) | ("faixa", a, b) | None."""
    tam = (tam or "").strip()
    if m := re.fullmatch(r"(\d+)v(\d+)(?:-(\d+))?", tam):
        return ("dec", int(m[1]), int(m[2]), int(m[3] or m[2]))
    if m := re.fullmatch(r"(\d+),(\d+)(?:/(\d+),(\d+))?", tam):
        inteiros = {int(m[1])} | ({int(m[3])} if m[3] else set())
        casas = [int(m[2])] + ([int(m[4])] if m[4] else [])
        return ("dec", max(inteiros), min(casas), max(casas)) if len(inteiros) == 1 else None
    if m := re.fullmatch(r"(\d+)", tam):
        return ("fixo", int(m[1]))
    if m := re.fullmatch(r"(\d+)-(\d+)", tam):
        return ("faixa", int(m[1]), int(m[2]))
    return None


def _tamanho_xsd(campo: dict):
    """A mesma forma, lida do tamanho declarado ou do padrão do XSD."""
    tam, padrao = (campo.get("tamanho") or "").strip(), (campo.get("padrao") or "").strip()
    if m := re.fullmatch(r"(\d+)", tam):
        return ("fixo", int(m[1]))
    if m := re.fullmatch(r"(\d+)-(\d+)", tam):
        return ("faixa", int(m[1]), int(m[2]))
    if m := re.fullmatch(r"\\d\{(\d+)\}|\[0-9\]\{(\d+)\}", padrao):
        return ("fixo", int(m[1] or m[2]))
    # Decimal: a alternativa "[1-9]{1}[0-9]{0,N}(\.[0-9]{a,b})?" dá 1+N inteiros e a..b casas.
    if m := re.search(r"\[1-9\](?:\{1\})?\[0-9\]\{0,(\d+)\}\(\\\.\[0-9\]\{(\d+)(?:,(\d+))?\}\)\?", padrao):
        return ("dec", 1 + int(m[1]), int(m[2]), int(m[3] or m[2]))
    return None


def comparar_tamanho(tam_nt: str | None, campo_xsd: dict) -> str:
    """confere | diverge | nao_comparavel — só quando os dois lados têm forma reconhecida."""
    a, b = _tamanho_nt(tam_nt), _tamanho_xsd(campo_xsd)
    if a is None or b is None:
        return "nao_comparavel"
    return "confere" if a == b else "diverge"


def caminho_na_nt(linhas: list[dict], linha: dict) -> str:
    """Caminho do campo subindo pelos pais que a própria tabela da NT declara (pelo
    ID no formato NF-e, pelo nome no conjunto), até onde ela vai."""
    if linha.get("id"):
        por_chave = {x["id"]: x for x in linhas if x.get("id")}
    else:
        por_chave = {x["campo"]: x for x in linhas if not x.get("id")}
    caminho, atual = [linha["campo"]], linha
    for _ in range(40):
        pai = por_chave.get(atual["pai"])
        if pai is None or pai is atual:
            break
        caminho.insert(0, pai["campo"])
        atual = pai
    # No formato conjunto o pai vem pelo NOME: mesmo sem linha própria na tabela, ele
    # é conhecido. No da NF-e é um ID, que sem a linha não diz o nome.
    if not linha.get("id") and atual["pai"] not in ("-", "") and atual["pai"] not in por_chave:
        caminho.insert(0, atual["pai"])
    return "/".join(caminho)


def campos_do_pacote(md: str) -> list[tuple[str, str, str, str]]:
    """(caminho, ocorrência, tamanho, padrão) da tabela de campos do texto de um pacote de
    schemas; o "|" escapado do padrão volta a ser "|"."""
    corpo = _separar(md)[1] if md.startswith("---\n") else md
    if "## Campos de IBS, CBS e IS (lidos dos XSD)" not in corpo:
        return []
    saida = []
    for linha in corpo.split("## Campos de IBS, CBS e IS (lidos dos XSD)", 1)[1].split("\n"):
        if not linha.startswith("| ") or linha.startswith("| caminho |"):
            continue
        celulas = [c.strip() for c in re.split(r"(?<!\\)\|", linha)[1:-1]]
        saida.append((celulas[0], celulas[2], celulas[3], celulas[5].replace("\\|", "|")))
    return saida


def _conferir(campos_nt: list[dict], schema: list[tuple[str, str, str, str]]) -> list[dict]:
    resultado = []
    for c in campos_nt:
        casam = [s for s in schema if s[0] == c["caminho_nt"] or s[0].endswith("/" + c["caminho_nt"])]
        item = dict(c)
        if not casam:
            item["situacao"] = "ausente_no_schema"
            resultado.append(item)
            continue
        mesmo = [s for s in casam if s[1] == c["ocorrencia_nt"]]
        achado = (mesmo or casam)[0]
        if mesmo:
            item.update(situacao="confere", caminho_schema=achado[0])
        else:
            item.update(situacao="ocorrencia_diverge", caminho_schema=achado[0], ocorrencia_schema=achado[1])
        item["tamanho_situacao"] = comparar_tamanho(c.get("tamanho_nt"), {"tamanho": achado[2], "padrao": achado[3]})
        resultado.append(item)
    return resultado


def conferir_nt(md_nt: str, pacotes: dict[str, str]) -> dict:
    """Confere os campos de IBS/CBS/IS da NT contra cada pacote; devolve o que mais
    confere (empate: o de id maior, em geral o mais novo)."""
    linhas = linhas_de_tabela(md_nt)
    campos_nt = []
    for linha in linhas:
        caminho = caminho_na_nt(linhas, linha)
        if any(_do_imposto(parte) for parte in caminho.split("/")):
            campos_nt.append({"campo": linha["campo"], "caminho_nt": caminho,
                              "ocorrencia_nt": linha["ocorrencia"], "tamanho_nt": linha.get("tamanho"),
                              "pagina": linha["pagina"]})
    if not campos_nt:
        return {"pacote": None, "campos": [], "linhas_lidas": len(linhas)}
    melhor = None
    for pid in sorted(pacotes):
        conferido = _conferir(campos_nt, campos_do_pacote(pacotes[pid]))
        nota = sum(c["situacao"] == "confere" for c in conferido)
        if melhor is None or nota >= melhor[0]:
            melhor = (nota, pid, conferido)
    if melhor is None:
        return {"pacote": None, "campos": [dict(c, situacao="sem_pacote") for c in campos_nt],
                "linhas_lidas": len(linhas)}
    if melhor[0] == 0:  # nada confere em nenhum: nomear um pacote seria arbitrário
        return {"pacote": None, "campos": [dict(c, situacao="sem_correspondencia") for c in campos_nt],
                "linhas_lidas": len(linhas)}
    return {"pacote": melhor[1], "campos": melhor[2], "linhas_lidas": len(linhas)}


def _documentos(reg: dict) -> set[str]:
    """Siglas dos documentos fiscais: "CT-e/BP-e/NF3e/NFCom (NT conjunta DFe)" vale
    para os quatro; o parêntese é comentário da listagem."""
    texto = re.sub(r"\([^)]*\)", "", str(reg.get("documento_fiscal") or ""))
    return {d.strip() for d in re.split(r"[,/]", texto) if d.strip()}


def relatorio(regs: list[dict], textos: dict[str, str]) -> dict:
    """Conferência de cada NT do acervo contra os pacotes do mesmo documento fiscal."""
    pacotes = [r for r in regs if r.get("tipo") == "schema" and r["id"] in textos]
    nts = []
    for reg in sorted(regs, key=lambda r: r["id"]):
        if reg.get("tipo") != "nota.tecnica" or reg["id"] not in textos:
            continue
        docs = _documentos(reg)
        candidatos = {p["id"]: textos[p["id"]] for p in pacotes if _documentos(p) & docs}
        r = conferir_nt(textos[reg["id"]], candidatos)
        if not r["campos"]:
            continue
        cont, cont_tam = {}, {}
        for c in r["campos"]:
            cont[c["situacao"]] = cont.get(c["situacao"], 0) + 1
            if c.get("tamanho_situacao"):
                cont_tam[c["tamanho_situacao"]] = cont_tam.get(c["tamanho_situacao"], 0) + 1
        nts.append({"id": reg["id"], "titulo": reg.get("titulo"), "versao": reg.get("versao"),
                    "documento_fiscal": reg.get("documento_fiscal"), "pacote": r["pacote"],
                    "contagem": cont, "contagem_tamanho": cont_tam,
                    "tamanho_diverge": [c for c in r["campos"] if c.get("tamanho_situacao") == "diverge"],
                    "divergencias": [c for c in r["campos"] if c["situacao"] != "confere"]})
    return {"aviso": ("Conferencia mecanica das tabelas de campos das NTs (texto do PDF) contra os schemas "
                      "(XSD) do mesmo documento fiscal. 'pacote' e o que mais confere, nao o oficialmente "
                      "correspondente. Divergencia e informacao, nao erro: a NT pode ser mais nova ou mais "
                      "antiga que o pacote."),
            "notas_tecnicas": nts}


def resumo_markdown(rel: dict) -> str:
    linhas = ["# Conferência das tabelas de campos das NTs contra os schemas", "",
              rel["aviso"], "", "| NT | versão | pacote comparado | confere | diverge | ausente | tamanho confere | "
              "tamanho diverge | tamanho não comparável |", "|---|---|---|---|---|---|---|---|---|"]
    for nt in rel["notas_tecnicas"]:
        c = nt["contagem"]
        linhas.append(f"| {nt['id']} | {nt.get('versao') or ''} | {nt['pacote'] or '(nenhum)'} | "
                      f"{c.get('confere', 0)} | {c.get('ocorrencia_diverge', 0)} | "
                      f"{c.get('ausente_no_schema', 0) + c.get('sem_pacote', 0) + c.get('sem_correspondencia', 0)} | "
                      f"{nt.get('contagem_tamanho', {}).get('confere', 0)} | "
                      f"{nt.get('contagem_tamanho', {}).get('diverge', 0)} | "
                      f"{nt.get('contagem_tamanho', {}).get('nao_comparavel', 0)} |")
    for nt in rel["notas_tecnicas"]:
        if not nt["divergencias"] and not nt.get("tamanho_diverge"):
            continue
        linhas += ["", f"## {nt['id']} (versão {nt.get('versao') or '?'}) × {nt['pacote']}", ""]
        for d in nt["divergencias"]:
            extra = (f"; schema: {d['ocorrencia_schema']} em {d['caminho_schema']}"
                     if d["situacao"] == "ocorrencia_diverge" else "")
            linhas.append(f"- p.{d['pagina']} `{d['caminho_nt']}` ocorrência {d['ocorrencia_nt']}: "
                          f"{d['situacao']}{extra}")
        for d in nt.get("tamanho_diverge") or []:
            linhas.append(f"- p.{d['pagina']} `{d['caminho_nt']}` tamanho {d['tamanho_nt']}: diverge do XSD em "
                          f"{d['caminho_schema']}")
    return "\n".join(linhas) + "\n"
