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


# ------------------------------------------- confirmação das não conferidas
# Linha que a posição não confirma pode ser confirmada por leitura (pessoa ou IA) em
# interpretacoes/cronograma_nt/conferencias.yaml, com a evidência apontada no PDF:
#   posicao_rotulo  `alturas` do par nas colunas e `rotulo_y` do rótulo da versão
#   fragmento       `alturas` do fragmento único (teste e produção em ordem) e `rotulo_y`
#   texto_da_pagina página girada: o trecho da linha traz teste antes de produção
# Conferido: os valores estão ali; o rótulo da versão está em rotulo_y; e nenhum OUTRO
# rótulo de versão fica entre as datas e ele (célula alta, rótulo centralizado). A linha
# vira `confirmada_ia` (ou `confirmada` por pessoa) — nunca `confere`, que é só da posição.

ARQUIVO_CONFIRMACOES = "conferencias.yaml"
EVIDENCIAS = ("posicao_rotulo", "fragmento", "texto_da_pagina")


def carregar_confirmacoes() -> list[dict]:
    import yaml

    from comum import DIR_INTERPRETACOES

    caminho = DIR_INTERPRETACOES / "cronograma_nt" / ARQUIVO_CONFIRMACOES
    if not caminho.exists():
        return []
    return (yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}).get("confirmacoes") or []


def _linha_alvo(rel: dict, conf: dict) -> list[dict]:
    return [x for nt in rel["notas_tecnicas"] if nt["id"] == conf.get("nt") for x in nt["linhas"]
            if not x.get("origem") and (x.get("versao"), x.get("pagina"), x.get("teste"), x.get("producao"),
                                        x.get("conferencia_pdf")) ==
            (conf.get("versao"), conf.get("pagina"), conf.get("teste"), conf.get("producao"), conf.get("situacao"))]


def problemas_da_confirmacao(conf: dict, rel: dict, obter_original) -> list[str]:
    rotulo = f"{conf.get('nt')} v{conf.get('versao')} p.{conf.get('pagina')}"
    probs = [f"{rotulo}: campo {c} ausente" for c in ("nt", "versao", "pagina", "situacao", "evidencia", "leitura",
                                                      "autor", "data") if not conf.get(c)]
    if conf.get("evidencia") not in EVIDENCIAS:
        probs.append(f"{rotulo}: evidência {conf.get('evidencia')!r} fora de {EVIDENCIAS}")
    if len(_linha_alvo(rel, conf)) != 1:
        probs.append(f"{rotulo}: nenhuma (ou mais de uma) linha não conferida com esses valores")
    if probs:
        return probs
    alvo_t, alvo_p = _norm(conf["teste"]), _norm(conf["producao"])
    if conf["evidencia"] == "texto_da_pagina":
        trecho = _norm(_linha_alvo(rel, conf)[0].get("trecho", ""))
        i, j = trecho.find(alvo_t), trecho.rfind(alvo_p)
        return [] if 0 <= i < j else [f"{rotulo}: o trecho não traz teste antes de produção"]
    pagina = _pagina(obter_original(conf["nt"]), conf["pagina"])
    if pagina is None:
        return [f"{rotulo}: página sem cabeçalho de colunas — use texto_da_pagina"]
    por_y, ys, rotulos = pagina
    perto = lambda alvo: min(ys, key=lambda y: abs(y - alvo))  # noqa: E731
    alturas = [perto(y) for y in conf.get("alturas") or []]
    if conf["evidencia"] == "posicao_rotulo":
        if _norm("".join(por_y[y]["teste"] for y in alturas)) != alvo_t:
            probs.append(f"{rotulo}: teste não está na coluna Teste nas alturas {conf.get('alturas')}")
        if _norm("".join(por_y[y]["producao"] for y in alturas)) != alvo_p:
            probs.append(f"{rotulo}: produção não está na coluna Produção nas alturas {conf.get('alturas')}")
    elif not any(_norm(por_y[y]["teste"] + por_y[y]["producao"]) == alvo_t + alvo_p and not por_y[y]["producao"]
                 for y in alturas):
        probs.append(f"{rotulo}: nenhum fragmento único com teste e produção em ordem na coluna, nas alturas")
    ry = conf.get("rotulo_y")
    no_rotulo = [v for y, v in rotulos if abs(y - (ry or -999)) <= 2]
    if conf["versao"] not in no_rotulo:
        probs.append(f"{rotulo}: o rótulo em y={ry} não é {conf['versao']} (há {no_rotulo})")
    elif alturas:
        baixo, alto = sorted((min(alturas + [ry]), max(alturas + [ry])))
        entre = [v for y, v in rotulos if baixo < y < alto and abs(y - ry) > 2]
        if entre:
            probs.append(f"{rotulo}: outro rótulo de versão entre as datas e o rótulo apontado: {entre}")
    return probs


def aplicar_confirmacoes(rel: dict, confirmacoes: list[dict]) -> dict:
    for conf in confirmacoes:
        for x in _linha_alvo(rel, conf):
            x["conferencia_original"] = x["conferencia_pdf"]
            x["conferencia_pdf"] = "confirmada_ia" if str(conf["autor"]).startswith("ia:") else "confirmada"
            x["conferida_por"] = conf["autor"]
            x["leitura_conferencia"] = conf["leitura"]
    return rel


def confirmacoes_conferidas(rel: dict, confirmacoes: list[dict], obter_original) -> tuple[list[dict], list[str]]:
    validas, erros = [], []
    for conf in confirmacoes:
        probs = problemas_da_confirmacao(conf, rel, obter_original)
        (erros.extend(probs) if probs else validas.append(conf))
    return validas, erros


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
