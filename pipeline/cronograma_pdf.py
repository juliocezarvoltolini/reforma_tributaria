"""Posição das colunas Teste e Produção na página do PDF original de uma NT.

Evidência mecânica para a leitura por IA de uma pendência do cronograma
(cronograma_nt.py): o texto extraído perde a coluna; o PDF não. Para a altura (y)
de uma linha da tabela, junta os fragmentos que estão na faixa x de cada coluna,
definida pelos cabeçalhos "Teste"/"Homologação" e "Produção" da tabela (os mais
altos da página — o "Detalhamento do Cronograma" abaixo repete os nomes).
"""
from __future__ import annotations

import io
import json
import re
from collections import defaultdict

from comum import MANIFEST, caminho_fonte

TOLERANCIA_Y = 2


def _itens(dados: bytes, pagina: int) -> list[tuple[int, int, str]]:
    from pypdf import PdfReader

    itens = []

    def visitor(texto, cm, tm, fd, fs):
        t = texto.replace("\n", " ").strip()
        if t:
            itens.append((round(tm[4] * cm[1] + tm[5] * cm[3] + cm[5]),
                          round(tm[4] * cm[0] + tm[5] * cm[2] + cm[4]), t))

    PdfReader(io.BytesIO(dados)).pages[pagina - 1].extract_text(visitor_text=visitor)
    return itens


def faixas(itens: list[tuple[int, int, str]]) -> dict[str, tuple[int, int]] | None:
    """Faixa x de cada coluna, pelos cabeçalhos mais altos da página."""
    teste = [(y, x) for y, x, t in itens if re.fullmatch(r"Teste|Homologação", t)]
    prod = [(y, x) for y, x, t in itens if t == "Produção"]
    if not teste or not prod:
        return None
    yt, xt = max(teste)
    _, xp = max(prod)
    # A coluna Teste começa no "Implantação" sobre ela (a descrição ao lado chega
    # perto: "de" em x=376 com a coluna em 392, NT 2021.003 v1.40).
    impl = [x for y, x, t in itens if t == "Implantação" and abs(y - yt) <= 20 and x < xp - 12]
    inicio = max(impl) - 6 if impl else xt - 40
    # Divisa: 6 pontos antes do "Implantação" sobre a coluna Produção (ou 12 antes do
    # "Produção"). O fim de uma data da coluna Teste ("6" de "2026") passa do ponto
    # médio entre os cabeçalhos; o início da de Produção não passa da divisa.
    impl_prod = [x for y, x, t in itens if t == "Implantação" and abs(y - yt) <= 20 and abs(x - xp) <= 20]
    meio = min(impl_prod) - 6 if impl_prod else xp - 12
    return {"teste": (inicio, meio), "producao": (meio, xp + 70)}


def texto_na_coluna(itens, y: int, faixa: tuple[int, int]) -> str:
    brutas = sorted((x, t) for yy, x, t in itens if abs(yy - y) <= TOLERANCIA_Y and faixa[0] <= x < faixa[1])
    # Negrito simulado: o mesmo texto reimpresso ±2 pontos ao lado conta uma vez.
    partes = [p for i, p in enumerate(brutas)
              if not any(q[1] == p[1] and abs(q[0] - p[0]) <= 2 for q in brutas[:i])]
    texto = ""
    for _, t in partes:  # fragmentos de uma data vêm colados ("0", "1", "/202", "6")
        texto += t if (not texto or re.search(r"[\d/]$", texto) and re.match(r"[\d/]", t)) else " " + t
    return " ".join(texto.split())


def _original(rid: str) -> bytes:
    docs = json.loads(MANIFEST.read_text(encoding="utf-8"))["documentos"]
    return caminho_fonte(docs[f"acervo/{rid}"]).read_bytes()


def faixas_da_tabela(dados: bytes, pagina: int):
    """Faixas da página; se ela não repete os cabeçalhos (tabela que continua), as da
    página anterior que os tem (até duas antes)."""
    for p in range(pagina, max(pagina - 3, 0), -1):
        cab = faixas(_itens(dados, p))
        if cab is not None:
            return cab
    return None


def texto_nas_alturas(rid: str, pagina: int, ys: list[int], coluna: str, dados: bytes | None = None) -> str:
    """Texto da coluna ("teste"/"producao") nas alturas dadas, de cima para baixo —
    a célula pode ocupar mais de uma linha visual ("Implementação" / "futura")."""
    dados = dados if dados is not None else _original(rid)
    cab = faixas_da_tabela(dados, pagina)
    if cab is None:
        return ""
    itens = _itens(dados, pagina)
    return " ".join(t for t in (texto_na_coluna(itens, y, cab[coluna]) for y in sorted(ys, reverse=True)) if t)


def colunas_da_pagina(rid: str, pagina: int, dados: bytes | None = None):
    """{y: (rótulo de versão, texto Teste, texto Produção)} e as faixas."""
    dados = dados if dados is not None else _original(rid)
    itens = _itens(dados, pagina)
    cab = faixas_da_tabela(dados, pagina)
    if cab is None:
        return {}, None
    ys = sorted({y for y, _, _ in itens}, reverse=True)
    linhas = {}
    for y in ys:
        versao = next((t for yy, x, t in itens if yy == y and x < 120 and re.fullmatch(r"\d\.\d{2}[a-z]?\**", t)), None)
        linhas[y] = (versao, texto_na_coluna(itens, y, cab["teste"]), texto_na_coluna(itens, y, cab["producao"]))
    return linhas, cab
