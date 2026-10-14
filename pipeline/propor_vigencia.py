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
from fatiar import _iso as _data_por_extenso  # noqa: E402
from fatiar import (
    CATALOGO,
    RE_ANOTACAO,
    RE_ASSINATURA,
    chave_ordem,
    exige_escopo_interno,
    extrair_referencias,
    extrair_remissoes,
    html_para_linhas,
    linhas_citadas,
    subdivisao_por_linha,
)
from regras_temporais import aprovada, carregar_regras, primeiro_dia_do_mes_subsequente

DIR_PROPOSTAS = DIR_TEMPORAL / "propostas"

# ---------------------------------------------------------------------------
# Cláusula de vigência
# ---------------------------------------------------------------------------

RE_ENTRA_EM_VIGOR = re.compile(r"\bentra(?:r[áa])?\s+em\s+vigor\b", re.IGNORECASE)

# Duas formas de cláusula, medidas nos textos reais:
#   EC 132:  "Esta Emenda Constitucional entra em vigor: I - em 2027, em relação..."
#            — os incisos dão a VIGÊNCIA.
#   LC 214:  "Esta Lei Complementar entra em vigor na data de sua publicação,
#            produzindo efeitos: I - a partir de 1º de janeiro de 2025, ..."
#            — a vigência de todos vem do caput; os incisos dão os EFEITOS.
RE_CAPUT_EFEITOS = re.compile(
    r"\bentra(?:r[áa])?\s+em\s+vigor\s+na\s+data\s+de\s+sua\s+publica[çc][ãa]o\s*,\s*"
    r"produzindo\s+efeitos\s*:", re.IGNORECASE)
RE_CAPUT_VIGENCIA = re.compile(r"\bentra(?:r[áa])?\s+em\s+vigor\s*:", re.IGNORECASE)

RE_INCISO = re.compile(r"^([IVXLC]+)\s*[-–]\s*(.+)$")
# Termo e alcance são lidos separadamente: um termo fora do padrão não impede
# saber quais artigos o inciso nomeia.
RE_DIVISAO_ALCANCE = re.compile(r",\s*(?=em\s+rela[çc][ãa]o\s+a)", re.IGNORECASE)

_MESES_TERMO = ("janeiro|fevereiro|mar[çc]o|abril|maio|junho|julho|agosto|setembro|outubro|"
                "novembro|dezembro")
RE_TERMO_DATA = re.compile(
    rf"^(?:em|a\s+partir\s+de)\s+(\d{{1,2}})\s*[ºo°]?\s+de\s+({_MESES_TERMO})\s+de\s+"
    rf"((?:19|20)\d{{2}})$", re.IGNORECASE)
RE_TERMO_ANO = re.compile(r"^(?:em|a\s+partir\s+de)\s+((?:19|20)\d{2})$", re.IGNORECASE)
RE_TERMO_PUBLICACAO = re.compile(r"^na\s+data\s+de\s+sua\s+publica[çc][ãa]o$", re.IGNORECASE)
# "a partir do primeiro dia do quarto mês subsequente ao da sua publicação" (LC 214,
# art. 544, I). O texto é lido aqui; a data só sai pela regra derivada
# 'primeiro-dia-do-mes-subsequente', depois de aprovada (PREMISSAS.md §3.4).
ORDINAIS = {"primeiro": 1, "segundo": 2, "terceiro": 3, "quarto": 4, "quinto": 5, "sexto": 6,
            "sétimo": 7, "setimo": 7, "oitavo": 8, "nono": 9, "décimo": 10, "decimo": 10}
RE_TERMO_RELATIVO = re.compile(
    rf"^a\s+partir\s+do\s+primeiro\s+dia\s+do\s+({'|'.join(ORDINAIS)})\s+m[êe]s\s+subsequente\s+"
    r"ao\s+da\s+sua\s+publica[çc][ãa]o$", re.IGNORECASE)
RE_ALCANCE_DEMAIS = re.compile(r"^em\s+rela[çc][ãa]o\s+aos\s+demais\s+dispositivos$", re.IGNORECASE)
RE_ALCANCE_ARTIGOS = re.compile(r"^em\s+rela[çc][ãa]o\s+aos?\s+arts?\.\s*(.+)$", re.IGNORECASE)

# Leitor do alcance. As subdivisões se ligam ao artigo que as precede e são
# reconhecidas ANTES da separação por ' e ': '450, §§ 1º e 5º' são parágrafos do
# art. 450, não o art. 5. No plural, vírgula só entre números com 'º', para não
# engolir o artigo seguinte ('§§ 1º e 5º, 464').
# Espaço só é consumido junto com o ordinal: "13 e 15" não pode perder o espaço
# antes do "e", ou o separador deixa de casar.
RE_ITEM = re.compile(r"(\d+)(?:\s*[ºo°])?(-[A-Z])?(?:\s+a\s+(\d+)(?:\s*[ºo°])?(-[A-Z])?)?")
_PARAGRAFOS = r"§§\s*\d+(?:\s*º)?(?:\s*,\s*\d+\s*º)*\s+e\s+\d+(?:\s*º)?|§\s*\d+(?:\s*º)?"
RE_QUALIFICADOR = re.compile(rf",\s*(?:(caput)|exceto\s+os?\s+({_PARAGRAFOS})|({_PARAGRAFOS}))")
RE_SEPARADOR = re.compile(r"\s*,\s*|\s+e\s+")


def localizar_clausula(corpos: dict[str, list[str]]) -> list[str]:
    """Artigos cujo CAPUT diz que "entra em vigor". Só o caput conta: "entrada em
    vigor" no meio de outro artigo é referência, não cláusula."""
    return [n for n, linhas in corpos.items() if linhas and RE_ENTRA_EM_VIGOR.search(linhas[0])]


def ler_alcance(lista: str) -> list[dict] | None:
    """'3º, 58, caput, 60, § 3º, 480 a 484 e 541' -> itens. None se sobrar
    QUALQUER coisa que não seja artigo, intervalo ou subdivisão reconhecida."""
    lista = lista.strip()
    itens, pos = [], 0
    while True:
        m = RE_ITEM.match(lista, pos)
        if not m:
            return None
        ini, suf_ini, fim, suf_fim = m.groups()
        if fim:
            # intervalo entre artigos com sufixo ('4º-A a 4º-C') não é interpretado
            if suf_ini or suf_fim or int(fim) <= int(ini):
                return None
            item = {"artigos": [str(n) for n in range(int(ini), int(fim) + 1)],
                    "intervalo": [int(ini), int(fim)], "somente": None, "exceto": None}
        else:
            item = {"artigos": [ini + (suf_ini or "")], "intervalo": None,
                    "somente": None, "exceto": None}
        pos = m.end()
        q = RE_QUALIFICADOR.match(lista, pos)
        if q:
            if item["intervalo"]:
                return None
            caput, exceto, somente = q.groups()
            if caput:
                item["somente"] = ["par0"]
            elif exceto:
                item["exceto"] = [f"par{n}" for n in re.findall(r"\d+", exceto)]
            else:
                item["somente"] = [f"par{n}" for n in re.findall(r"\d+", somente)]
            pos = q.end()
        itens.append(item)
        if pos == len(lista):
            return itens
        s = RE_SEPARADOR.match(lista, pos)
        if not s or s.end() == len(lista):
            return None
        pos = s.end()


def _ler_termo(texto: str) -> dict | None:
    texto = texto.strip()
    if m := RE_TERMO_DATA.match(texto):
        data = _data_por_extenso(m.group(1), m.group(2), m.group(3))
        return {"tipo": "data", "data": data} if data else None
    if m := RE_TERMO_ANO.match(texto):
        return {"tipo": "ano", "ano": int(m.group(1))}
    if RE_TERMO_PUBLICACAO.match(texto):
        return {"tipo": "publicacao"}
    if m := RE_TERMO_RELATIVO.match(texto):
        return {"tipo": "relativo_publicacao", "regra": "primeiro-dia-do-mes-subsequente",
                "meses": ORDINAIS[m.group(1).lower()]}
    return None


def _ler_inciso(linha: str, urn_base: str, artigo: str) -> dict | None:
    texto = RE_ANOTACAO.sub("", linha).strip()
    m = RE_INCISO.match(texto)
    if not m:
        return None
    rotulo, corpo = m.group(1), m.group(2)
    # "; e" ao fim liga o inciso ao seguinte; ";" e "." encerram.
    corpo = re.sub(r"\s*;\s*e\s*$", "", corpo).rstrip(" ;.")
    partes = RE_DIVISAO_ALCANCE.split(corpo, maxsplit=1)
    termo = _ler_termo(partes[0])
    alcance = None
    if len(partes) == 2:
        if RE_ALCANCE_DEMAIS.match(partes[1]):
            alcance = {"tipo": "demais"}
        elif am := RE_ALCANCE_ARTIGOS.match(partes[1]):
            itens = ler_alcance(am.group(1))
            if itens is not None:
                alcance = {"tipo": "artigos", "itens": itens}
    motivos = []
    if termo is None:
        motivos.append("termo fora dos padrões reconhecidos ('em <ano>', 'a partir de <data>', "
                       "'na data de sua publicação', 'a partir do primeiro dia do <ordinal> mês "
                       "subsequente ao da sua publicação')")
    if alcance is None:
        motivos.append("alcance fora dos padrões (só artigos, intervalos 'a', 'caput', '§', "
                       "'§§ x e y', 'exceto os §§' e 'demais dispositivos'; qualquer sobra "
                       "invalida a lista inteira)")
    return {
        "urn": urn_dispositivo(urn_base, artigo, inciso=rotulo),
        "rotulo": rotulo,
        "texto": linha,
        "interpretado": termo is not None and alcance is not None,
        "alcance_interpretado": alcance is not None,
        "termo": termo,
        "alcance": alcance,
        "motivo": "; ".join(motivos) or None,
    }


def _nomeados(inciso: dict) -> set[str]:
    alcance = inciso.get("alcance") or {}
    return {a for item in alcance.get("itens") or [] for a in item["artigos"]}


def interpretar_clausula(
    linhas: list[str], urn_base: str, artigo: str, existentes: list[str]
) -> dict:
    """Aplica a cláusula de vigência a cada artigo da norma.

    Devolve, por artigo, o inciso que o alcança, o termo, o fundamento e as
    exceções por subdivisão ('58, caput', '450, exceto os §§ 1º e 5º'). O que o
    texto não decide fica com `inciso: None` e o `motivo`.
    """
    caput = linhas[0] if linhas else ""
    if RE_CAPUT_EFEITOS.search(caput):
        forma = "efeitos_por_inciso"
        vigencia = {"termo": {"tipo": "publicacao"}, "fundamento": urn_dispositivo(urn_base, artigo)}
    elif RE_CAPUT_VIGENCIA.search(caput):
        forma, vigencia = "vigencia_por_inciso", None
    else:
        forma, vigencia = None, None

    incisos, anteriores = [], {}
    for linha in linhas[1:]:
        if linha.startswith("~~"):
            # Redação anterior, riscada: só serve para ver o que a nova mudou.
            antigo = _ler_inciso(linha.strip("~").strip(), urn_base, artigo)
            if antigo:
                anteriores[antigo["rotulo"]] = antigo
            continue
        inciso = _ler_inciso(linha, urn_base, artigo)
        if inciso:
            incisos.append(inciso)

    alcance_desconhecido = [i["rotulo"] for i in incisos if not i["alcance_interpretado"]]
    demais = [i for i in incisos if i["alcance_interpretado"] and i["alcance"]["tipo"] == "demais"]
    nomeacoes: dict[str, list[tuple[dict, dict]]] = {}
    intervalos: list[tuple[int, int, str]] = []
    for inc in incisos:
        for item in (inc["alcance"] or {}).get("itens") or []:
            for a in item["artigos"]:
                nomeacoes.setdefault(a, []).append((inc, item))
            if item["intervalo"]:
                intervalos.append((*item["intervalo"], inc["rotulo"]))
    inexistentes = [a for a in nomeacoes if a not in existentes]
    alterados = set()
    for rotulo, antigo in anteriores.items():
        atual = next((i for i in incisos if i["rotulo"] == rotulo), None)
        if atual and antigo["alcance_interpretado"] and atual["alcance_interpretado"]:
            alterados |= _nomeados(atual) ^ _nomeados(antigo)

    def excecao(sub: str, n: str, inc: dict) -> dict:
        return {"subdivisao": sub, "urn": urn_dispositivo(urn_base, n, paragrafo=sub[3:]),
                "inciso": inc["rotulo"], "termo": inc["termo"], "fundamento": inc["urn"]}

    def resolver(n: str) -> tuple[dict | None, list[dict], str | None]:
        """(inciso principal, exceções, motivo de indeterminação)."""
        if forma is None:
            return None, [], "caput fora das formas reconhecidas ('entra em vigor:' ou 'entra em " \
                             "vigor na data de sua publicação, produzindo efeitos:')"
        noms = nomeacoes.get(n, [])
        if not noms and "-" in n:
            base = int(n.split("-")[0])
            dentro = [f"'{a} a {b}' do inciso {r}" for a, b, r in intervalos if a <= base <= b]
            if dentro:
                return None, [], (f"art. {n} tem sufixo e fica dentro do intervalo {dentro[0]}: "
                                  "se o intervalo o abrange é interpretação")
        inteiros = [(i, it) for i, it in noms if not it["somente"]]
        parciais = [(i, it) for i, it in noms if it["somente"]]
        if len(inteiros) > 1:
            return None, [], "nomeado em mais de um inciso: " + ", ".join(i["rotulo"] for i, _ in inteiros)
        if inteiros and parciais and not inteiros[0][1]["exceto"]:
            return None, [], (f"nomeado inteiro no inciso {inteiros[0][0]['rotulo']} e em parte "
                              f"no {parciais[0][0]['rotulo']}: qual prevalece é interpretação")
        principal = inteiros[0][0] if inteiros else None
        if principal is None:
            if alcance_desconhecido:
                return None, [], (f"inciso(s) {', '.join(alcance_desconhecido)} com alcance não "
                                  "interpretado: não se sabe se este artigo é nomeado por eles, "
                                  "então 'demais dispositivos' não pode ser resolvido")
            if len(demais) != 1:
                return None, [], ("mais de um inciso 'demais dispositivos'" if demais else
                                  "nenhum inciso nomeia este artigo e a cláusula não tem "
                                  "'demais dispositivos'")
            principal = demais[0]
        excecoes, vistos = [], set()
        for inc, item in parciais:
            for sub in item["somente"]:
                if sub in vistos:
                    return None, [], f"subdivisão {sub} nomeada em mais de um inciso"
                vistos.add(sub)
                excecoes.append(excecao(sub, n, inc))
        for sub in (inteiros[0][1]["exceto"] or []) if inteiros else []:
            if sub in vistos:
                continue
            if len(demais) != 1 or alcance_desconhecido:
                return None, [], (f"{sub} é excetuada e não é nomeada em outro inciso, e "
                                  "'demais dispositivos' não pode ser resolvido")
            excecoes.append(excecao(sub, n, demais[0]))
        return principal, excecoes, None

    mapa = {}
    for n in existentes:
        principal, excecoes, motivo = resolver(n)
        entrada = {"inciso": None, "termo": None, "fundamento": None, "excecoes": [],
                   "motivo": motivo, "ressalva": None,
                   "alterado_pela_redacao_posterior": n in alterados}
        if principal is not None:
            entrada.update(inciso=principal["rotulo"], termo=principal["termo"],
                           fundamento=principal["urn"], excecoes=excecoes)
            if principal["termo"] is None:
                entrada["motivo"] = f"termo do inciso {principal['rotulo']} não interpretado: " \
                                    f"{principal['motivo']}"
            if alcance_desconhecido and nomeacoes.get(n):
                entrada["ressalva"] = (f"inciso(s) {', '.join(alcance_desconhecido)} não "
                                       "interpretado(s) podem também nomear este artigo")
        mapa[n] = entrada

    return {
        "urn": urn_dispositivo(urn_base, artigo),
        "caput": caput or None,
        "forma": forma,
        "vigencia": vigencia,
        "incisos": incisos,
        "redacoes_anteriores": list(anteriores.values()),
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


# Um artigo que diz, no próprio texto, quando ele (ou outro dispositivo) entra em
# vigor ou produz efeitos ("II - somente entrará em vigor com...") não recebe a
# data da cláusula sem leitura.
TIPOS_CLAUSULA_PROPRIA = {"produz_efeitos", "entrada_em_vigor"}
RE_ARTIGO_DA_URN = re.compile(r"!art(\d+(?:-[A-Z]+)?)")


def clausula_temporal_propria(
    marcos: list[dict], urn_base: str, artigo: str, exigir_escopo: bool
) -> tuple[bool, list[str]]:
    """(o artigo tem cláusula temporal própria?, outros artigos desta norma que ela cita)."""
    linhas = [m["trecho"] for m in marcos if TIPOS_CLAUSULA_PROPRIA & set(m["tipos"])]
    citados = []
    for linha in linhas:
        for urn in extrair_remissoes(RE_RISCADO.sub("", linha), urn_base, artigo, exigir_escopo):
            m = RE_ARTIGO_DA_URN.search(urn)
            if m and m.group(1) != artigo and m.group(1) not in citados:
                citados.append(m.group(1))
    return bool(linhas), citados


# ---------------------------------------------------------------------------
# Texto que veio de outro ato
# ---------------------------------------------------------------------------

RE_PREAMBULO = re.compile(r"^O\s+PRESIDENTE\s+DA\s+REP[ÚU]BLICA\b")
RE_ARTIGO_CITADO = re.compile(r"^[“\"]\s*Art\.\s*(\d+)\s*[ºo°]?\s*(-[A-Z])?")


def marcas_de_outro_ato(corpo: list[str]) -> list[str]:
    """Anotações oficiais do compilado no artigo, inclusive no texto riscado, na
    ordem: incluído, alterado, revogado, vetado ou promulgado por outro ato, ou
    remetido a ele. A cláusula de vigência desta norma não decide esse texto."""
    marcas: list[str] = []
    for linha in corpo:
        for m in RE_ANOTACAO.finditer(linha):
            if m.group(0) not in marcas:
                marcas.append(m.group(0))
    return marcas


def artigos_de_outros_atos(linhas: list[str]) -> list[dict]:
    """Para cada assinatura depois da primeira, os artigos desta norma que aquele
    ato traz, citados entre aspas depois do preâmbulo dele ("O PRESIDENTE DA
    REPÚBLICA Faço saber..."). `artigos` é None quando não dá para saber: sem
    preâmbulo, o bloco não é delimitado; sem citação, não se sabe o que ele trouxe."""
    assinaturas = [i for i, linha in enumerate(linhas) if RE_ASSINATURA.match(linha)]
    blocos = []
    for anterior, atual in zip(assinaturas, assinaturas[1:]):
        trecho = linhas[anterior + 1:atual]
        inicio = max((k for k, linha in enumerate(trecho) if RE_PREAMBULO.match(linha)),
                     default=None)
        artigos = None
        if inicio is not None:
            achados = [m.group(1) + (m.group(2) or "") for linha in trecho[inicio + 1:]
                       if (m := RE_ARTIGO_CITADO.match(linha))]
            artigos = list(dict.fromkeys(achados)) or None
        blocos.append({"assinatura": linhas[atual], "artigos": artigos})
    return blocos


# ---------------------------------------------------------------------------
# Montagem da proposta
# ---------------------------------------------------------------------------

RE_REVOGAM_SE = re.compile(r"^Art\.\s*\d+\s*[ºo°]?\.?\s+Revogam-se\b", re.IGNORECASE)


def _inicio_proposto(termo: dict, pub: dict, regras: dict | None = None) -> dict:
    if termo["tipo"] == "relativo_publicacao":
        # A data só é proposta com a regra aprovada; sem ela, a proposta mostra o
        # que a regra daria, para quem decide aprová-la.
        datas = pub.get("datas") or []
        base = datas[0] if (pub.get("fonte") == "dou" and datas) or len(datas) == 1 else None
        resultado = primeiro_dia_do_mes_subsequente(base, termo["meses"]) if base else None
        ok = aprovada(regras or {}, termo["regra"])
        return {
            "tipo": "relativo", "regra": termo["regra"], "meses": termo["meses"],
            "data_candidata": resultado if ok else None, "resultado_se_aprovada": resultado,
            "precisao": "dia",
            "nota": (f"regra '{termo['regra']}' aprovada em temporal/regras.yaml" if ok else
                     f"regra '{termo['regra']}' não aprovada em temporal/regras.yaml: sem data"),
        }
    if termo["tipo"] == "data":
        return {"tipo": "data", "data_candidata": termo["data"], "precisao": "dia",
                "nota": "data escrita no inciso"}
    if termo["tipo"] == "ano":
        return {
            "tipo": "ano",
            "ano": termo["ano"],
            "data_candidata": f"{termo['ano']}-01-01",
            "precisao": "ano",
            "nota": "o texto diz só o ano: grava-se AAAA-01-01 com `precisao: ano`, e a "
                    "consulta avisa quando a data consultada cai nesse ano",
        }
    datas = pub.get("datas") or []
    if pub.get("fonte") == "dou" and datas:
        dou = pub.get("dou") or {}
        candidata = datas[0]
        nota = (f"publicação no DOU, lida da página do ato arquivada (edição {dou.get('edicao')}, "
                f"seção {dou.get('secao')}, página {dou.get('pagina')})")
    elif len(datas) == 1:
        candidata = datas[0]
        nota = ("data lida do rodapé do texto compilado; confirmar no DOU (in.gov.br), "
                "que não está ingerido")
    else:
        candidata = None
        nota = "publicação não localizada ou ambígua no original: preencher à mão"
    return {"tipo": "evento", "evento": "publicacao", "data_candidata": candidata,
            "precisao": "dia", "nota": nota}


def _decisoes(dispositivos: list[dict]) -> list[dict]:
    """O que o modelo de dados ainda não responde. Data do ato x publicação,
    precisão de ano e datas por subdivisão já são campos do front-matter."""
    decisoes = []
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


INSTRUCOES_REVISAO = (
    "Primeiro rode pipeline/revisar_por_regra.py: ele decide o que a cláusula diz "
    "literalmente (revisado_por: regra:...) e deixa o resto em branco. Em cada dispositivo "
    "sem decisão, preencha `revisao`. escopo: [vigencia], [efeitos] ou os dois (padrão) diz "
    "quais eixos a decisão cobre; o eixo de fora continua provisório. decisao: aceitar "
    "adota as propostas dos eixos do escopo, e só vale se cada um tiver proposta com data. "
    "decisao: alterar exige, para os eixos do escopo, vigencia_inicio/efeitos_inicio e "
    "fundamento_vigencia/fundamento_efeitos (listas de URN); opcionais: vigencia_fim, "
    "efeitos_fim, precisao ({campo: ano}, com a data em AAAA-01-01) e excecoes_subdivisao "
    "(urn de § ou inciso do próprio artigo, as datas que diferem e fundamento). decisao: "
    "rejeitar mantém o dispositivo pendente. Toda decisão exige revisado_por e revisado_em; "
    "a decisão humana prevalece e nunca é refeita por regra. Depois, rode "
    "pipeline/fatiar.py: é ele que aplica a revisão a normas/. Se o original mudar "
    "(sha256), a revisão deixa de ser aplicada e precisa ser refeita."
)


def _pendencias_gerais(refs: dict, pub: dict, outros: list[dict] | None = None) -> list[dict]:
    artigos_por_assinatura = {o["assinatura"]: o["artigos"] for o in outros or []}
    pendencias = []
    if pub.get("fonte") == "dou":
        sem_confirmacao = sorted(set((pub.get("rodape_compilado") or {}).get("datas") or [])
                                 - set(pub.get("datas") or []))
        if sem_confirmacao:
            pendencias.append({
                "id": "rodape_cita_publicacao_nao_confirmada",
                "descricao": "O rodapé do texto compilado cita publicação em "
                             f"{', '.join(sem_confirmacao)}, que a página do DOU arquivada não "
                             "confirma. Pode ser republicação de parte do ato; arquivar essa "
                             "edição do DOU antes de usar a data.",
            })
    elif refs["publicacao_dou"]["valores"]:
        pendencias.append({
            "id": "publicacao_nao_confirmada_no_dou",
            "descricao": "A data de publicação vem do rodapé do texto compilado "
                         f"({'; '.join(refs['publicacao_dou']['trechos'])}). O texto publicado "
                         "no DOU prevalece (PREMISSAS.md §1.4) e ainda não está ingerido.",
        })
    else:
        pendencias.append({
            "id": "publicacao_nao_localizada",
            "descricao": "O original não informa a publicação no DOU. As propostas que "
                         "dependem dela ficam sem data candidata.",
        })
    for extra in refs.get("rodapes_adicionais") or []:
        artigos = artigos_por_assinatura.get(extra["assinatura"])
        pendencias.append({
            "id": "outro_ato_no_compilado",
            "descricao": "O compilado traz, depois do texto da norma, outro bloco assinado "
                         f"({extra['assinatura']}) com rodapé próprio ({extra['trecho']}). É "
                         "outro ato publicado em outra data; os dispositivos que ele trouxe "
                         "podem ter vigência própria. "
                         + (f"Pelo texto do bloco, ele traz partes dos arts. {', '.join(artigos)}."
                            if artigos else
                            "Não foi possível identificar, no bloco, quais artigos ele traz: "
                            "identificar antes de revisar."),
            # None: não identificados. revisar_por_regra.py não decide nada da norma.
            "artigos": artigos,
        })
    return pendencias


def construir(slug: str, regras: dict | None = None) -> dict:
    """Monta a proposta (dicionário) sem gravar nada. `regras`: as regras derivadas
    (temporal/regras.yaml, se não informadas)."""
    if regras is None:
        regras = carregar_regras()
    catalogo = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))
    fonte = next((f for f in catalogo.get("fontes") or [] if f["slug"] == slug), None)
    if fonte is None:
        raise SystemExit(f"slug '{slug}' nao esta em fontes.yaml")
    base = urn_norma(fonte["autoridade"], fonte["data"], fonte["numero"])
    exigir_escopo = exige_escopo_interno(fonte)

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
    linhas_fonte = [ln.completa for ln in html_para_linhas(caminho_fonte(registro).read_bytes())]
    refs = extrair_referencias(linhas_fonte)
    outros = artigos_de_outros_atos(linhas_fonte)
    trazidos = {a for o in outros for a in o["artigos"] or []}

    # A publicação que fatiar.py gravou: do DOU, se arquivado; senão, do rodapé.
    publicacao = metas[ordem[0]].get("publicacao") or {}

    candidatos = localizar_clausula(corpos)
    if len(candidatos) == 1:
        clausula = interpretar_clausula(corpos[candidatos[0]], base, candidatos[0], ordem)
    else:
        clausula = {"urn": None, "forma": None, "vigencia": None, "incisos": [],
                    "redacoes_anteriores": [], "artigos_inexistentes": [],
                    "mapa": {n: {"inciso": None, "termo": None, "fundamento": None,
                                 "excecoes": [], "alterado_pela_redacao_posterior": False,
                                 "motivo": "cláusula de vigência não localizada de forma única "
                                           f"(candidatos: {candidatos})", "ressalva": None}
                             for n in ordem}}

    forma = clausula.get("forma")
    artigo_clausula = candidatos[0] if len(candidatos) == 1 else None
    proprias: dict[str, list[str]] = {}
    for n in ordem:
        if n == artigo_clausula:
            continue
        tem, citados_na_clausula = clausula_temporal_propria(
            marcos_proprios(corpos[n], base, n)["marcos"], base, n, exigir_escopo)
        if tem:
            proprias[n] = citados_na_clausula
    alcancados = {c for cs in proprias.values() for c in cs}

    dispositivos = []
    for n in ordem:
        meta, corpo = metas[n], corpos[n]
        m = clausula["mapa"][n]
        marcos = marcos_proprios(corpo, base, n)
        tipos = {t for x in marcos["marcos"] for t in x["tipos"]}
        citados = list(meta.get("dispositivos_citados") or [])
        pendencias = []

        # Vigência: na forma da LC, do caput para todos; na da EC, do inciso.
        if forma == "efeitos_por_inciso":
            vig_termo, vig_fundamento, vig_inciso, vig_motivo, vig_ressalva = (
                clausula["vigencia"]["termo"], clausula["vigencia"]["fundamento"], None, None, None)
        else:
            vig_termo, vig_fundamento, vig_inciso, vig_motivo, vig_ressalva = (
                m["termo"], m["fundamento"], m["inciso"], m["motivo"], m["ressalva"])
        inicio_vig = _inicio_proposto(vig_termo, publicacao, regras) if vig_termo else None
        if inicio_vig is None:
            pendencias.append("vigencia_nao_determinada")

        termos = [vig_termo]
        if forma == "efeitos_por_inciso":
            # Os efeitos vêm do inciso, com as exceções por subdivisão que ele
            # estabelece, no formato que revisao_temporal.py aceita.
            inicio_efe = _inicio_proposto(m["termo"], publicacao, regras) if m["termo"] else None
            excecoes, termos_excecoes, sem_data = [], [], []
            for e in m["excecoes"]:
                cand = _inicio_proposto(e["termo"], publicacao, regras) if e["termo"] else None
                if not cand or not cand["data_candidata"]:
                    sem_data.append(e["urn"].split("!")[-1])
                    continue
                exc = {"urn": e["urn"], "efeitos_inicio": cand["data_candidata"],
                       "fundamento": [e["fundamento"]]}
                if cand["precisao"] == "ano":
                    exc["precisao"] = {"efeitos_inicio": "ano"}
                excecoes.append(exc)
                termos_excecoes.append(cand["tipo"])
                termos.append(e["termo"])
            motivo_efe = m["motivo"]
            if sem_data:
                inicio_efe = None
                motivo_efe = (f"exceção sem data ({', '.join(sem_data)}): o termo do inciso que "
                              "a alcança não foi interpretado ou depende de regra não aprovada")
            efeitos = {"inciso": m["inciso"], "fundamento": m["fundamento"],
                       "natureza": "derivado" if m["inciso"] else None, "proposta": inicio_efe,
                       "excecoes": excecoes,
                       # De onde vem a data de cada exceção (data, ano, evento, relativo):
                       # a revisão por regra só aceita exceção cujo termo ela pode adotar.
                       "termos_das_excecoes": termos_excecoes,
                       "motivo": motivo_efe, "ressalva": m["ressalva"]}
            termos.append(m["termo"])
            if m["inciso"] is None:
                pendencias.append("efeitos_nao_determinados")
            elif m["termo"] is None:
                pendencias.append("termo_nao_interpretado")
            if m["excecoes"]:
                pendencias.append("datas_por_subdivisao")
        else:
            # Forma da EC: a cláusula só dá a vigência. Efeitos são propostos iguais
            # a ela apenas quando o artigo não tem marco próprio nem texto inserido.
            if m.get("excecoes"):
                proposta_efe, motivo_efe = None, ("exceções por subdivisão numa cláusula de "
                                                  "vigência: revisar à mão")
                pendencias.append("datas_por_subdivisao")
            elif inicio_vig is None:
                proposta_efe, motivo_efe = None, m["motivo"]
            elif marcos["marcos"] or citados:
                causas = []
                if marcos["marcos"]:
                    causas.append("tem marco(s) temporal(is) ou dependência de lei futura no "
                                  "próprio texto (ver `marcos_proprios`)")
                if citados:
                    causas.append("insere texto em outra norma, ainda não ingerida")
                proposta_efe = None
                motivo_efe = ("os efeitos não decorrem só da cláusula de vigência: o "
                              "dispositivo " + " e ".join(causas))
            else:
                # Cópia, não o mesmo objeto: senão o YAML grava âncora (&id001/*id001)
                # e quem revisa o arquivo à mão não vê a proposta de efeitos.
                proposta_efe = dict(inicio_vig)
                motivo_efe = ("nenhum marco temporal detectado pelos padrões do script (isto NÃO "
                              "garante que não exista): LER O TEXTO antes de aceitar que os "
                              "efeitos acompanham a vigência")
            efeitos = {"inciso": None, "fundamento": None, "natureza": None,
                       "proposta": proposta_efe, "excecoes": [], "motivo": motivo_efe,
                       "ressalva": None}

        if any(t and t["tipo"] == "ano" for t in termos):
            pendencias.append("ano_sem_dia")
        if vig_termo and vig_termo["tipo"] == "publicacao" and publicacao.get("fonte") != "dou":
            pendencias.append("publicacao_nao_confirmada_no_dou")
        if m.get("alterado_pela_redacao_posterior"):
            pendencias.append("alcance_alterado_pela_redacao_posterior")
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
        marcas = marcas_de_outro_ato(corpo)
        if marcas:
            pendencias.append("redacao_de_outro_ato")
        if n in trazidos:
            pendencias.append("parte_de_outro_ato")
        if n in proprias:
            pendencias.append("clausula_temporal_propria")
        if n in alcancados:
            pendencias.append("alcancado_por_clausula_temporal")
        if any(t and t["tipo"] == "relativo_publicacao" and not aprovada(regras, t["regra"])
               for t in termos):
            pendencias.append("regra_derivada_nao_aprovada")

        dispositivos.append({
            "urn": meta["urn"],
            "artigo": n,
            "vigencia": {
                "inciso": vig_inciso,
                "fundamento": vig_fundamento,
                "natureza": "derivado" if inicio_vig else None,
                "proposta": inicio_vig,
                "motivo": vig_motivo,
                "ressalva": vig_ressalva,
            },
            "efeitos": efeitos,
            "atual_no_pipeline": {
                "data_ato": meta.get("data_ato"),
                # Só datas e fonte: o registro completo é o mesmo para a norma inteira.
                "publicacao": {k: (meta.get("publicacao") or {}).get(k) for k in ("datas", "fonte")},
                "vigencia_inicio": meta.get("vigencia_inicio"),
                "efeitos_inicio": meta.get("efeitos_inicio"),
            },
            "marcos_proprios": marcos["marcos"],
            "texto_inserido": {"artigos": citados, "linhas_com_marcos": marcos["citado_com_marcos"]},
            # Anotações do compilado que mostram texto vindo de outro ato.
            "marcas_de_outro_ato": marcas,
            "pendencias": pendencias,
            "revisao": {
                "decisao": None,  # aceitar | alterar | rejeitar (ver instrucoes_revisao)
                "vigencia_inicio": None,
                "vigencia_fim": None,
                "efeitos_inicio": None,
                "efeitos_fim": None,
                "precisao": {},
                "fundamento_vigencia": [],
                "fundamento_efeitos": [],
                "excecoes_subdivisao": [],
                "revisado_por": None,
                "revisado_em": None,
                "observacao": None,
            },
        })

    # Contagem pelo inciso que a cláusula usa para cada artigo: o da vigência na
    # forma da EC, o dos efeitos na forma da LC.
    por_inciso: dict[str, int] = {}
    for d in dispositivos:
        lado = d["efeitos"] if forma == "efeitos_por_inciso" else d["vigencia"]
        k = lado["inciso"] or "indeterminado"
        por_inciso[k] = por_inciso.get(k, 0) + 1

    pendencias_gerais = _pendencias_gerais(refs, publicacao, outros)
    # Regra derivada que a cláusula usa e ninguém aprovou: uma decisão só, que
    # resolve todos os artigos que dependem dela.
    nao_aprovadas: dict[str, dict] = {}
    for d in dispositivos:
        for lado in (d["vigencia"], d["efeitos"]):
            p = lado.get("proposta") or {}
            if p.get("tipo") == "relativo" and p.get("data_candidata") is None:
                item = nao_aprovadas.setdefault(p["regra"], {"artigos": [], "resultados": set(),
                                                             "fundamentos": set()})
                item["artigos"].append(d["artigo"])
                item["resultados"].add(p.get("resultado_se_aprovada"))
                item["fundamentos"].add(lado.get("fundamento"))
    for nome, item in nao_aprovadas.items():
        resultados = sorted(r for r in item["resultados"] if r)
        pendencias_gerais.append({
            "id": "regra_derivada_nao_aprovada",
            "regra": nome,
            "fundamento": sorted(f for f in item["fundamentos"] if f),
            "artigos": item["artigos"],
            "resultado_se_aprovada": resultados,
            "descricao": f"O termo de {', '.join(sorted(f for f in item['fundamentos'] if f))} "
                         f"só vira data pela regra '{nome}', que não está aprovada em "
                         "temporal/regras.yaml. Aprovada, ela daria "
                         f"{', '.join(resultados) or 'nenhuma data (publicação não localizada)'} "
                         f"para {len(item['artigos'])} artigo(s). Até lá, sem data.",
        })

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
        # A revisão só vale para este texto: se o original mudar, fatiar.py não a aplica.
        "fonte_sha256": registro["sha256"],
        "instrucoes_revisao": INSTRUCOES_REVISAO,
        "referencias": refs,
        "clausula_de_vigencia": {k: v for k, v in clausula.items() if k != "mapa"},
        "pendencias_gerais": pendencias_gerais,
        "decisoes_necessarias": _decisoes(dispositivos),
        "resumo": {
            "dispositivos": len(dispositivos),
            "forma_da_clausula": forma,
            "por_inciso": por_inciso,
            "com_marcos_proprios": sum(1 for d in dispositivos if d["marcos_proprios"]),
            "com_texto_inserido_em_outra_norma": sum(
                1 for d in dispositivos if d["texto_inserido"]["artigos"]),
        },
        "dispositivos": dispositivos,
    }


def gravar_proposta(caminho: Path, proposta: dict) -> bool:
    """Grava a proposta. Recusa (False) se o arquivo existente já tem decisão HUMANA.

    Decisão de regra (`revisado_por: regra:...`) não impede: ela é refeita por
    revisar_por_regra.py depois de regenerar.
    """
    if caminho.exists():
        existente = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
        if any((d.get("revisao") or {}).get("decisao") is not None
               and not str((d.get("revisao") or {}).get("revisado_por") or "").startswith("regra:")
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
    print("  NADA em /normas/ foi alterado. Proximo passo: "
          f"python pipeline/revisar_por_regra.py --slug {args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
