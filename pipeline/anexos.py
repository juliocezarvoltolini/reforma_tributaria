"""Anexos da norma: as tabelas a que os artigos remetem ("relacionados no Anexo I
desta Lei Complementar") e que ficavam fora de /normas/.

O compilado do Planalto traz os anexos depois da assinatura e do rodapé. Cada
anexo DA PRÓPRIA LEI começa num cabeçalho "ANEXO <romano>" com a âncora
`<a name="anexoN">`, e os números seguem a ordem I, II, III... Dois sinais
decidem, como no resto do fatiamento:

- a âncora, quando há, diz o número; cabeçalho e âncora que discordam abortam;
- sem âncora, vale a sequência: o próximo número esperado.

Um "ANEXO I" no meio de um anexo, sem âncora e fora da sequência, é o cabeçalho
do anexo de OUTRA lei que este reproduz (LC 214, Anexos XVIII a XXIII: novos
anexos da LC 123). Fica no corpo, e o anexo registra `texto_de_outra_norma`.

Depois do último anexo o arquivo pode trazer outro ato (LC 214: promulgação de
partes vetadas, com "Presidência da República", título e assinatura próprios).
Isso encerra os anexos.

Corpo: uma linha do arquivo por parágrafo fora de tabela e por LINHA DA TABELA,
com as células separadas por " | " (o caractere não ocorre no texto dos
compilados). Texto riscado entre `~~ ~~`, como nos artigos.
"""
from __future__ import annotations

import re

from comum import hoje, status_em

RE_CABECALHO = re.compile(r"^ANEXO\s+([IVXLC]+)\b")
RE_ANCORA_ANEXO = re.compile(r"^anexo(\d+)$", re.IGNORECASE)
RE_PRESIDENCIA = re.compile(r"^Presid[êe]ncia\s+da\s+Rep[úu]blica\b")
# "(Lei Complementar nº 123, de 14 de dezembro de 2006)": a lei cujo anexo este reproduz.
RE_NORMA_ENTRE_PARENTESES = re.compile(
    r"^\(((?:Lei Complementar|Lei|Decreto|Emenda Constitucional)\s+n[ºo°].*)\)$")
# "Anexo I", "Anexos IV e XII", "Anexos XVIII a XXII": o numeral só em maiúsculas.
RE_MENCAO_ANEXO = re.compile(
    r"\b(?i:anexos?)\s+([IVXLC]+(?:\s*(?:,|\be\b|\ba\b)\s*[IVXLC]+)*)\b")
# Anotação que altera ou revoga: não é título. "(Vigência: ...)" do texto de outra
# lei é parte do título dela.
RE_ANOTACAO_DE_ALTERACAO = re.compile(
    r"^\((?:Reda[çc][ãa]o dada|Revogad[oa]|Inclu[íi]d[oa]|Vide|Vetad[oa]|Promulga[çc][ãa]o|"
    r"Produ[çc][ãa]o de efeito)", re.IGNORECASE)
# "o Anexo VII constante do Anexo XXIII": o primeiro é de outra lei.
RE_CONSTANTE = re.compile(r"\bconstantes?\s+d[oa]s?\b", re.IGNORECASE)
SEPARADOR_DE_CELULA = " | "

_ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def romano_para_int(romano: str) -> int:
    total = 0
    for i, letra in enumerate(romano):
        valor = _ROMANOS[letra]
        proximo = _ROMANOS[romano[i + 1]] if i + 1 < len(romano) else 0
        total += -valor if valor < proximo else valor
    return total


def nome_arquivo(numero: int) -> str:
    return f"anexo-{numero:02d}"


def _outro_ato(completa: str) -> bool:
    from fatiar import RE_ASSINATURA, RE_TITULO

    return bool(RE_PRESIDENCIA.match(completa) or RE_TITULO.match(completa)
                or RE_ASSINATURA.match(completa))


def _montar(fonte: list) -> list[dict]:
    """Uma entrada por parágrafo fora de tabela e por linha da tabela."""
    from fatiar import _normalizar

    saida, i = [], 0
    while i < len(fonte):
        ln = fonte[i]
        if ln.celula is None:
            saida.append({"marcada": ln.marcada, "vigente": ln.vigente, "completa": ln.completa,
                          "links": list(ln.links), "link_externo": ln.link_externo,
                          "tabela": False})
            i += 1
            continue
        chave, colunas = ln.celula[:2], {}
        while i < len(fonte) and fonte[i].celula is not None and fonte[i].celula[:2] == chave:
            colunas.setdefault(fonte[i].celula[2], []).append(fonte[i])
            i += 1

        def junta(campo: str, manter_vazias: bool) -> str:
            celulas = [_normalizar(" ".join(getattr(p, campo) for p in cel)) for cel in colunas.values()]
            return SEPARADOR_DE_CELULA.join(c for c in celulas if manter_vazias or c)

        saida.append({"marcada": junta("marcada", True), "vigente": junta("vigente", False),
                      "completa": junta("completa", True),
                      "links": [lk for cel in colunas.values() for p in cel for lk in p.links],
                      "link_externo": None, "tabela": True})
    return saida


def _novo(numero: int, romano: str) -> dict:
    return {"numero": numero, "romano": romano, "fonte": []}


def fatiar_anexos(linhas: list) -> tuple[list[dict], list[str]]:
    """(anexos, avisos) a partir das linhas que seguem o fim do texto da norma.

    Cada anexo: numero, romano, linhas (corpo, com o riscado marcado), vigentes,
    completas, links e `tabela` de cada linha. Aviso que começa com 'ERRO'
    impede a gravação."""
    anexos, avisos = [], []
    esperado, atual = 1, None
    for linha in linhas:
        completa = linha.completa
        if atual is not None and _outro_ato(completa):
            break
        m = RE_CABECALHO.match(completa)
        if m:
            numero = romano_para_int(m.group(1))
            ancoras = [int(a.group(1)) for nome in linha.ancoras
                       if (a := RE_ANCORA_ANEXO.match(nome))]
            if ancoras and ancoras[0] != numero:
                avisos.append(f"ERRO cabeçalho '{completa[:30]}' com âncora anexo{ancoras[0]}")
                continue
            if ancoras and numero != esperado:
                avisos.append(f"ERRO anexo {m.group(1)} fora de sequência: esperado o "
                              f"{esperado}º anexo da lei")
                continue
            if numero == esperado:
                atual = _novo(numero, m.group(1))
                anexos.append(atual)
                esperado += 1
        if atual is not None:
            atual["fonte"].append(linha)
    nomes = {"marcada": "linhas", "vigente": "vigentes", "completa": "completas", "links": "links",
             "link_externo": "links_externos", "tabela": "tabelas"}
    for anexo in anexos:
        montadas = _montar(anexo.pop("fonte"))
        for campo, nome in nomes.items():
            anexo[nome] = [m[campo] for m in montadas]
    return anexos, avisos


def texto_de_outra_norma(anexo: dict) -> dict | None:
    """{norma, anexo} se o anexo reproduz o anexo de outra lei: logo depois do
    cabeçalho, "(Lei Complementar nº ...)" com link para outro arquivo, e o
    cabeçalho do anexo dela."""
    completas = anexo["completas"]
    if len(completas) < 3:
        return None
    m = RE_NORMA_ENTRE_PARENTESES.match(completas[1])
    if not (m and anexo["links_externos"][1] and RE_CABECALHO.match(completas[2])):
        return None
    return {"norma": m.group(1), "anexo": completas[2]}


def titulo(anexo: dict) -> str | None:
    """A primeira linha de texto depois do cabeçalho (e, se o anexo reproduz o de
    outra lei, depois da lei e do cabeçalho dela), com os parênteses que a seguem.
    Anotação de alteração ("(Revogado pela ...)") não entra."""
    partes: list[str] = []
    inicio = 3 if texto_de_outra_norma(anexo) else 1
    for completa, e_tabela in zip(anexo["completas"][inicio:], anexo["tabelas"][inicio:]):
        if e_tabela:
            break
        if RE_ANOTACAO_DE_ALTERACAO.match(completa):
            continue
        if not partes:
            partes.append(completa)
        elif completa.startswith("(") and completa.endswith(")"):
            partes.append(completa)
        else:
            break
    return " ".join(partes) or None


def _expandir(grupo: str) -> list[int]:
    numeros, faixa = [], False
    for token in re.findall(r"[IVXLC]+|\ba\b", grupo):
        if token == "a":
            faixa = True
            continue
        n = romano_para_int(token)
        if faixa and numeros:
            numeros.extend(range(numeros[-1] + 1, n + 1))
        else:
            numeros.append(n)
        faixa = False
    return numeros


def extrair_remissoes_a_anexos(texto: str, urn_base: str, exigir_escopo_interno: bool) -> list[str]:
    """URNs dos anexos DESTA norma mencionados no texto.

    Mesma política das remissões a artigo (fatiar.extrair_remissoes): "desta Lei"
    resolve; "da Lei Complementar nº 123" e "constante do" não; sem qualificador,
    resolve, salvo onde se exige escopo afirmado. A janela do qualificador vai
    até a próxima menção a anexo ou artigo, para que o "desta Lei" do Anexo XXIII
    não valha para o Anexo VII que o precede, e não passa do parágrafo (num
    anexo, a linha seguinte da tabela não qualifica a menção)."""
    from fatiar import RE_ESCOPO_EXTERNO, RE_ESCOPO_INTERNO

    achados: list[str] = []
    for m in RE_MENCAO_ANEXO.finditer(texto):
        janela = texto[m.end():m.end() + 90]
        corte = re.search(r"[.;:\n]|\bart|\b(?i:anexos?)\b", janela)
        janela = janela[:corte.start()] if corte else janela
        if RE_ESCOPO_INTERNO.search(janela):
            pass
        elif RE_ESCOPO_EXTERNO.search(janela) or RE_CONSTANTE.search(janela):
            continue
        elif exigir_escopo_interno:
            continue
        for numero in _expandir(m.group(1)):
            urn = f"{urn_base}!anx{numero}"
            if urn not in achados:
                achados.append(urn)
    return achados


def montar_meta_anexo(anexo: dict, fonte: dict, registro: dict, base: str, publicacao: dict,
                      exigir_escopo: bool, mapa_links: dict[str, str]) -> tuple[dict, str]:
    """(front-matter, corpo) de um anexo, com datas provisórias como as dos artigos."""
    from alteracoes import RE_ANOTACAO_LINK, resolver_link
    from fatiar import RE_ANOTACAO, extrair_externas
    from revisao_temporal import ordenar_meta

    urn = f"{base}!anx{anexo['numero']}"
    outra = texto_de_outra_norma(anexo)
    vigente = "\n\n".join(v for v in anexo["vigentes"] if v)
    # Sem o cabeçalho ("ANEXO I" não é remissão) e, se o texto é de outra lei,
    # sem nada: as remissões dele pertencem àquela lei.
    proprio = "" if outra else "\n\n".join(v for v in anexo["vigentes"][1:] if v)
    remete_a = [u for u in extrair_remissoes_a_anexos(proprio, base, exigir_escopo) if u != urn]
    alterado_por = [
        {"anotacao": texto if texto.startswith("(") else f"({texto})", "subdivisao": urn,
         "link": href, "ato": resolver_link(href, mapa_links)}
        for links in anexo["links"] for href, texto in links if RE_ANOTACAO_LINK.match(texto)]
    provisoria = publicacao["datas"][0] if publicacao["datas"] else fonte["data"]
    meta = {
        "urn": urn,
        "norma": fonte["titulo"],
        "norma_slug": fonte["slug"],
        "dispositivo": f"anexo {anexo['romano']}",
        "titulo": titulo(anexo),
        "camada": 1,
        "hierarquia": [],
        "data_ato": fonte["data"],
        "publicacao": publicacao,
        "vigencia_inicio": provisoria,
        "vigencia_fim": None,
        "efeitos_inicio": provisoria,
        "efeitos_fim": None,
        "status": None,
        "fonte": {"url": registro["url"], "tipo": registro["tipo_documento"],
                  "acesso": registro["acesso"], "sha256": registro["sha256"]},
        "ingerido_em": hoje(),
        "remete_a": remete_a,
        "remete_a_externo": extrair_externas(vigente),
        "subdivisoes": [],
        "anotacoes_oficiais": [re.sub(r"\s+", " ", m.group(0)) for m in RE_ANOTACAO.finditer(vigente)],
        "conceitos_definidos": [],
        "dispositivos_citados": [],
        # O anexo reproduz o anexo de outra lei (a que ele dá nova redação).
        "texto_de_outra_norma": outra,
        "altera": [],
        "alterado_por": alterado_por,
        "extracao": "automatica",
        "revisao_temporal_pendente": True,
        "revisado_por": None,
        "revisado_em": None,
    }
    import datetime as _dt

    meta["status"] = status_em(meta, _dt.date.today())
    return ordenar_meta(meta), "\n\n".join(anexo["linhas"])
