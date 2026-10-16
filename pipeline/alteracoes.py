"""Quem alterou cada dispositivo: as anotações oficiais ligadas ao ato alterador.

No compilado do Planalto, a anotação é um link para o artigo da lei que fez a
alteração (medido na LC 214):

  <a href="Lcp227.htm#art174">(Incluído pela Lei Complementar nº 227, de 2026)</a>

`alteracoes_do_artigo` grava isso em `alterado_por`: a anotação literal, a
subdivisão onde ela está, o link bruto e — só quando o arquivo é de norma
ingerida e a âncora é 'artN' — a URN do artigo alterador. Âncora irregular
("art181-4-a") ou norma não ingerida ficam com `ato: null`: ligação não se
inventa.

`conferir` cruza o link com o texto do artigo alterador, que é outra fonte:
confirma se ele cita o artigo alterado (artigo de alteração) ou o lista no
inciso que nomeia a norma (artigo de revogação).
"""
from __future__ import annotations

import re

from comum import urn_dispositivo, urn_norma

RE_ANOTACAO_LINK = re.compile(
    r"^\(?\s*(?:Inclu[íi]d[oa]|Reda[çc][ãa]o dada|Revogad[oa]|Vide|Vig[êe]ncia|"
    r"Produ[çc][ãa]o de efeito|Vetad[oa]|Promulga[çc][ãa]o)\b", re.IGNORECASE)
RE_ANCORA_ARTIGO = re.compile(r"art(\d+)([a-z])?", re.IGNORECASE)
RE_REVOGACAO = re.compile(r"^Art\.\s*\d+\S*\s+(?:Revogam-se|Ficam\s+revogad)", re.IGNORECASE)
RE_INCISO = re.compile(r"^[IVXLC]+\s*[-–]\s")
RE_ARTIGOS_MENCIONADOS = re.compile(
    r"\barts?\.\s*((?:\d+\s*[ºo°]?(?:-[A-Z])?(?:\s*,\s*|\s+e\s+)?)+)")
RE_NUMERO = re.compile(r"(\d+)\s*[ºo°]?(-[A-Z])?")


def mapa_de_links(catalogo: dict) -> dict[str, str]:
    """{arquivo do compilado em minúsculas: URN da norma}, das normas do catálogo."""
    mapa = {}
    for fonte in catalogo.get("fontes") or []:
        for entrada in fonte.get("urls") or []:
            if entrada.get("tipo") == "texto_compilado":
                arquivo = entrada["url"].rsplit("/", 1)[-1].lower()
                mapa[arquivo] = urn_norma(fonte["autoridade"], fonte["data"], fonte["numero"])
    return mapa


def resolver_link(href: str, mapa: dict[str, str]) -> str | None:
    """URN do artigo apontado pelo link, ou None se não é norma ingerida com âncora 'artN'."""
    arquivo, _, ancora = href.partition("#")
    base = mapa.get(arquivo.rsplit("/", 1)[-1].lower()) if arquivo else None
    m = RE_ANCORA_ARTIGO.fullmatch(ancora or "")
    if not base or not m:
        return None
    return urn_dispositivo(base, m.group(1) + (f"-{m.group(2).upper()}" if m.group(2) else ""))


def alteracoes_do_artigo(linhas: list[str], links: list[tuple], urn_base: str, artigo: str,
                         mapa: dict[str, str]) -> list[dict]:
    """`alterado_por` de um artigo: um registro por anotação com link."""
    from fatiar import MARCA_RISCADO, RE_ANOTACAO, subdivisao_por_linha

    # Sem as marcas do riscado: o dispositivo revogado ("~~§ 2º ...~~ (Revogado
    # pela ...)") é a subdivisão da anotação, e o rótulo dele está no riscado.
    sem_marca = [linha.replace(MARCA_RISCADO, "") for linha in linhas]
    subdivisoes = subdivisao_por_linha(sem_marca, urn_base, artigo)
    saida = []
    for linha, subdivisao, links_da_linha in zip(sem_marca, subdivisoes, links):
        # Anotação sozinha na linha: não se sabe a que trecho ela se refere. Na LC
        # 214 é a do título inserido logo depois, que caiu no artigo anterior.
        isolada = not RE_ANOTACAO.sub("", linha).strip()
        for href, texto in links_da_linha:
            if not RE_ANOTACAO_LINK.match(texto):
                continue
            anotacao = texto if texto.startswith("(") else f"({texto})"
            registro = {"anotacao": anotacao, "subdivisao": None if isolada else subdivisao}
            if isolada:
                registro["isolada"] = True
            registro.update(link=href, ato=resolver_link(href, mapa))
            saida.append(registro)
    return saida


def _nomeia(texto: str, nome_norma: str) -> bool:
    texto = texto.replace("n°", "nº").replace("N°", "Nº")
    return re.search(re.escape(nome_norma.replace("n°", "nº")) + r"(?!\d)", texto) is not None


def _artigos_mencionados(texto: str) -> set[str]:
    return {n + (s or "") for grupo in RE_ARTIGOS_MENCIONADOS.findall(texto)
            for n, s in RE_NUMERO.findall(grupo)}


# "o Anexo XIV" numa lista de revogação; "“ANEXO XX" abrindo o texto citado. O
# cabeçalho entre aspas SIMPLES é de anexo de outra lei citado dentro dele.
RE_ANEXO_MENCIONADO = re.compile(r"\bAnexos?\s+([IVXLC]+)\b")
RE_ANEXO_CITADO = re.compile(r"^[“\"]?ANEXO\s+([IVXLC]+)\b")


def conferir_anexo(numero: int, nome_norma: str, alvo_corpo: str) -> str | None:
    """O artigo alterador confirma que alterou o anexo `numero` da norma `nome_norma`?

    'citacao': o caput nomeia a norma e o texto citado abre o anexo ("“ANEXO XX").
    'lista_de_revogacao': artigo de revogação, e "o Anexo XIV" está no inciso que
    nomeia a norma. None: não confirma."""
    from anexos import romano_para_int

    linhas = [linha for linha in alvo_corpo.splitlines() if linha.strip()]
    if not linhas:
        return None
    if _nomeia(linhas[0], nome_norma) and any(
            (m := RE_ANEXO_CITADO.match(linha)) and romano_para_int(m.group(1)) == numero
            for linha in linhas[1:]):
        return "citacao"
    if RE_REVOGACAO.match(linhas[0]):
        da_norma = False
        for linha in linhas[1:]:
            if RE_INCISO.match(linha):
                da_norma = _nomeia(linha, nome_norma)
            if da_norma and any(romano_para_int(m.group(1)) == numero
                                for m in RE_ANEXO_MENCIONADO.finditer(linha)):
                return "lista_de_revogacao"
    return None


def conferir(numero: str, nome_norma: str, alvo_meta: dict, alvo_corpo: str) -> str | None:
    """O artigo alterador confirma que alterou o art. `numero` da norma `nome_norma`?

    'citacao': o caput nomeia a norma e o artigo está entre os citados.
    'lista_de_revogacao': artigo de revogação, e o art. está no inciso que nomeia a norma.
    None: não confirma.
    """
    linhas = [linha for linha in alvo_corpo.split("\n") if linha.strip()]
    if not linhas:
        return None
    caput = linhas[0]
    if _nomeia(caput, nome_norma) and numero in (alvo_meta.get("dispositivos_citados") or []):
        return "citacao"
    if RE_REVOGACAO.match(caput):
        da_norma, trecho = False, []
        for linha in linhas[1:]:
            if RE_INCISO.match(linha):
                da_norma = _nomeia(linha, nome_norma)
            if da_norma:
                trecho.append(linha)
        if numero in _artigos_mencionados(" ".join(trecho)):
            return "lista_de_revogacao"
    return None
