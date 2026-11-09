"""Confere pela posição no PDF as linhas do cronograma que o SCRIPT leu do texto.

O script (cronograma_nt.py) lê pela ordem do texto extraído — que já enganou em notas
coladas à tabela e em linhas cortadas na quebra de página. Aqui cada linha lida é
procurada na página do PDF original, só abaixo do cabeçalho da tabela de cronograma: o
valor de teste na coluna Teste e o de produção na coluna Produção (cada um em até 3
linhas visuais, a ≤ 26 pontos, com linhas da descrição no meio), em alturas próximas
(≤ 15 pontos), e o rótulo de versão mais próximo tem de ser a versão lida.

`conferencia_pdf` de cada linha (não decide nada, só diz o que a posição mostra):
  confere          colunas e rótulo conferem
  um_fragmento     teste e produção num só pedaço de texto que atravessa as colunas
                   (a ordem está provada, a coluna não)
  rotulo_diverge   o par está nas colunas, mas o rótulo mais próximo é outra versão (célula
                   alta com o rótulo centralizado engana a proximidade — revisar)
  nao_achado       o par não está nas colunas da página
  sem_prova        página sem cabeçalho de colunas (girada, texto em pedaços verticais)

Leituras de regra ou de IA (`origem`) já foram conferidas pela posição ao serem
aceitas e não passam por aqui.
"""
from __future__ import annotations

import re

import cronograma_pdf as P
from acervo import normalizar

LIMITE_CELULA = 26  # distância vertical máxima entre as linhas visuais de uma célula
LIMITE_PAR = 15     # distância vertical máxima entre o teste e a produção da mesma linha


def _norm(texto: str) -> str:
    return normalizar((texto or "").replace("*", ""))


def _janelas(por_y: dict, ys: list[int], coluna: str) -> list[tuple[float, str]]:
    saida = []
    for i, y in enumerate(ys):
        if not por_y[y][coluna]:
            continue
        texto, usados = "", []
        for y2 in ys[i:]:
            if y - y2 > LIMITE_CELULA or len(usados) == 3:
                break
            parte = por_y[y2][coluna]
            if not parte:  # linha da descrição entre as linhas visuais da célula
                continue
            texto += _norm(parte)
            usados.append(y2)
            saida.append((sum(usados) / len(usados), texto))
    return saida


def _pagina(dados: bytes, pagina: int):
    """(por_y, ys, rótulos) da área da tabela, ou None se a página não tem cabeçalho."""
    cab = P.faixas_da_tabela(dados, pagina)
    if cab is None:
        return None
    itens = P._itens(dados, pagina)
    cabecalhos = [y for y, _, t in itens if t in ("Teste", "Homologação", "Produção", "Implantação")]
    topo = max(cabecalhos) if cabecalhos else 10_000  # sem cabeçalho na página: a tabela vem do alto
    ys = []  # alturas a até 2 pontos são a mesma linha visual (negrito simulado)
    for y in sorted({y for y, _, _ in itens if 55 < y < topo - 4}, reverse=True):
        if not ys or ys[-1] - y > 2:
            ys.append(y)
    por_y = {y: {c: P.texto_na_coluna(itens, y, cab[c]) for c in ("teste", "producao")} for y in ys}
    por_rotulo: dict = {}
    for y, x, t in sorted(itens, key=lambda i: i[1]):
        if x < 100 and t.strip() and 55 < y < topo - 4:
            por_rotulo[y] = por_rotulo.get(y, "") + t.replace(" ", "")
    rotulos = [(y, t.rstrip("*")) for y, t in por_rotulo.items() if re.fullmatch(r"\d\.\d{2}[a-z]?\**", t)]
    return por_y, ys, rotulos


def situacao(linha: dict, pagina) -> str:
    if pagina is None:
        return "sem_prova"
    por_y, ys, rotulos = pagina
    alvo_t, alvo_p = _norm(linha.get("teste")), _norm(linha.get("producao"))
    pares = [(yt + yp) / 2 for yt, tt in _janelas(por_y, ys, "teste") if tt == alvo_t
             for yp, tp in _janelas(por_y, ys, "producao") if tp == alvo_p and abs(yt - yp) <= LIMITE_PAR]
    resultado = "confere"
    if not pares:
        pares = [y for y in ys if _norm(por_y[y]["teste"] + por_y[y]["producao"]) == alvo_t + alvo_p]
        if not pares:
            return "nao_achado"
        resultado = "um_fragmento"
    if not rotulos:
        return "rotulo_diverge"
    perto = {min(rotulos, key=lambda r: abs(r[0] - yc))[1] for yc in pares}
    return resultado if linha.get("versao") in perto else "rotulo_diverge"


def conferir_linhas(rel: dict, obter_original) -> dict:
    """Acrescenta `conferencia_pdf` a cada linha lida pelo script (sem `origem`)."""
    for nt in rel["notas_tecnicas"]:
        lidas = [x for x in nt["linhas"] if not x.get("origem")]
        if not lidas:
            continue
        dados = obter_original(nt["id"])
        paginas: dict = {}
        for x in lidas:
            if x["pagina"] not in paginas:
                paginas[x["pagina"]] = _pagina(dados, x["pagina"])
            x["conferencia_pdf"] = situacao(x, paginas[x["pagina"]])
    return rel
