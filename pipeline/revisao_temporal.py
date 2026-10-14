"""Revisão temporal: do YAML revisado por um humano ao front-matter de normas/.

`propor_vigencia.py` gera `temporal/propostas/<slug>.yaml`. Quem revisa — uma
pessoa, ou `revisar_por_regra.py` no que é literal (PREMISSAS.md §3.4) — preenche,
em cada dispositivo, o bloco `revisao`:

  decisao: aceitar   adota as propostas dos eixos do `escopo`: [vigencia],
                     [efeitos] ou os dois (o padrão). Cada eixo do escopo
                     precisa ter proposta com data.
  decisao: alterar   datas e fundamentos explícitos dos eixos do escopo:
                     vigencia_inicio, efeitos_inicio, fundamento_vigencia,
                     fundamento_efeitos (URNs). Opcionais: vigencia_fim,
                     efeitos_fim, precisao, excecoes_subdivisao.
  decisao: rejeitar  nada é aplicado; o dispositivo continua pendente.

Toda decisão exige `revisado_por` e `revisado_em`. Decidir um eixo só deixa o
outro provisório e o dispositivo pendente (`eixos_revisados`). Decisão de regra
(`revisado_por: regra:...`) só é aplicada se as regras derivadas que ela usou
continuam aprovadas em temporal/regras.yaml.

`fatiar.py` aplica a revisão ao regravar normas/. Tem de ser ali: ele apaga e
regrava a norma inteira a cada execução, e um passo separado seria desfeito pela
próxima reingestão. A revisão só vale para o texto sobre o qual foi feita: se o
`sha256` do original mudou (deriva), nada é aplicado e o fatiamento aborta.

`precisao: {campo: ano}` registra o que o texto diz de fato: "em 2027" é o ano,
não o dia. A data gravada é 1º de janeiro por convenção, e a precisão avisa quem
consulta que o estado dentro daquele ano é incerto.
"""
from __future__ import annotations

import datetime as _dt
from pathlib import Path

import yaml

from regras_temporais import carregar_regras, problemas_de_regra

CAMPOS_DATA = ("vigencia_inicio", "vigencia_fim", "efeitos_inicio", "efeitos_fim")
EIXOS = ("vigencia", "efeitos")
CAMPOS_DO_EIXO = {"vigencia": ("vigencia_inicio", "vigencia_fim"),
                  "efeitos": ("efeitos_inicio", "efeitos_fim")}
PRECISOES = {"ano", "dia"}
DECISOES = {"aceitar", "alterar", "rejeitar"}
FONTES_PUBLICACAO = {"rodape_compilado", "dou"}

# Ordem canônica do front-matter. Determinística, para que a mesma entrada dê
# os mesmos bytes; campos opcionais só aparecem quando há o que dizer.
ORDEM_CAMPOS = (
    "urn", "norma", "norma_slug", "dispositivo", "camada", "hierarquia",
    "data_ato", "publicacao",
    "vigencia_inicio", "vigencia_fim", "efeitos_inicio", "efeitos_fim",
    "precisao", "excecoes_subdivisao", "fundamento_temporal", "status",
    "fonte", "ingerido_em", "remete_a", "remete_a_externo", "subdivisoes",
    "anotacoes_oficiais", "conceitos_definidos", "dispositivos_citados",
    "altera", "alterado_por", "extracao", "eixos_revisados", "revisao_temporal_pendente",
    "revisado_por", "revisado_em",
)


def ordenar_meta(meta: dict) -> dict:
    ordenado = {k: meta[k] for k in ORDEM_CAMPOS if k in meta}
    ordenado.update({k: v for k, v in meta.items() if k not in ordenado})
    return ordenado


# ---------------------------------------------------------------------------
# Datas
# ---------------------------------------------------------------------------

def _iso(valor) -> str | None:
    """'2027-01-01' -> '2027-01-01'. Aceita também `date`: o YAML lido de um
    arquivo editado à mão traz data sem aspas como objeto, não como texto."""
    if isinstance(valor, _dt.datetime):
        return valor.date().isoformat()
    if isinstance(valor, _dt.date):
        return valor.isoformat()
    if isinstance(valor, str):
        try:
            return _dt.date.fromisoformat(valor.strip()).isoformat()
        except ValueError:
            return None
    return None


def _urns_validas(valor) -> bool:
    return (isinstance(valor, list) and bool(valor)
            and all(isinstance(u, str) and u.startswith("urn:lex:") for u in valor))


def _problemas_precisao(precisao, datas: dict) -> list[str]:
    if precisao in (None, {}):
        return []
    if not isinstance(precisao, dict):
        return ["precisao deve ser um mapa {campo: ano|dia}"]
    problemas = []
    for campo, valor in precisao.items():
        if campo not in CAMPOS_DATA:
            problemas.append(f"precisao de campo desconhecido: {campo}")
        elif valor not in PRECISOES:
            problemas.append(f"precisao '{valor}' em {campo}: use 'ano' ou 'dia'")
        elif valor == "ano":
            data = _iso(datas.get(campo))
            if data is None:
                problemas.append(f"precisao de ano em {campo}, mas {campo} não tem data")
            elif not data.endswith("-01-01"):
                problemas.append(f"precisao de ano em {campo} exige a convenção AAAA-01-01 "
                                 f"(achado {data})")
    return problemas


def _problemas_excecao(exc, urn_artigo: str) -> list[str]:
    if not isinstance(exc, dict):
        return ["exceção por subdivisão deve ser um mapa"]
    problemas = []
    urn = exc.get("urn")
    if not (isinstance(urn, str) and urn.startswith(f"{urn_artigo}_")):
        problemas.append(f"exceção {urn!r} não é subdivisão de {urn_artigo}")
    datas = [c for c in CAMPOS_DATA if c in exc]
    if not datas:
        problemas.append(f"exceção {urn!r} sem nenhuma data")
    for campo in datas:
        if exc[campo] is not None and _iso(exc[campo]) is None:
            problemas.append(f"exceção {urn!r}: {campo} fora do formato AAAA-MM-DD")
    if not _urns_validas(exc.get("fundamento")):
        problemas.append(f"exceção {urn!r} sem fundamento (lista de URNs)")
    problemas += [f"exceção {urn!r}: {p}" for p in _problemas_precisao(exc.get("precisao"), exc)]
    return problemas


# ---------------------------------------------------------------------------
# Validação do front-matter (usada pelo validar.py)
# ---------------------------------------------------------------------------

def problemas_no_dispositivo(meta: dict) -> tuple[list[str], list[str]]:
    """(erros, avisos) dos campos temporais de um dispositivo de normas/."""
    erros: list[str] = []
    avisos: list[str] = []

    if "data_ato" in meta and _iso(meta["data_ato"]) is None:
        erros.append("data_ato fora do formato AAAA-MM-DD")

    if "publicacao" in meta:
        pub = meta["publicacao"]
        if not isinstance(pub, dict) or not isinstance(pub.get("datas"), list):
            erros.append("publicacao deve ser um mapa com 'datas' (lista)")
        else:
            ruins = [d for d in pub["datas"] if _iso(d) is None]
            if ruins:
                erros.append(f"publicacao.datas fora do formato AAAA-MM-DD: {ruins}")
            if pub.get("fonte") not in FONTES_PUBLICACAO | {None}:
                erros.append(f"publicacao.fonte inválida: {pub.get('fonte')!r}")
            if pub["datas"] and not pub.get("fonte"):
                erros.append("publicacao.datas sem fonte")
            if not pub["datas"]:
                avisos.append("publicação não localizada no original")
            rodape = (pub.get("rodape_compilado") or {}).get("datas") or []
            if any(_iso(d) is None for d in rodape):
                erros.append("publicacao.rodape_compilado.datas fora do formato AAAA-MM-DD")
            sem_confirmacao = sorted({_iso(d) for d in rodape} - {_iso(d) for d in pub["datas"]})
            if pub.get("fonte") == "dou" and sem_confirmacao:
                avisos.append("o rodapé do compilado cita publicação não confirmada no DOU: "
                              + ", ".join(d for d in sem_confirmacao if d))

    erros += _problemas_precisao(meta.get("precisao"), meta)
    for exc in meta.get("excecoes_subdivisao") or []:
        erros += _problemas_excecao(exc, meta.get("urn", ""))

    if meta.get("extracao") == "revisada":
        eixos = meta.get("eixos_revisados") or list(EIXOS)
        if not isinstance(eixos, list) or not set(eixos) <= set(EIXOS):
            erros.append(f"eixos_revisados inválido: {eixos!r}")
            eixos = []
        elif meta.get("revisao_temporal_pendente") is not (set(eixos) != set(EIXOS)):
            erros.append("revisao_temporal_pendente incoerente com eixos_revisados: só é false "
                         "quando vigência e efeitos foram revisados")
        if not meta.get("revisado_por"):
            erros.append("extracao revisada sem revisado_por")
        if _iso(meta.get("revisado_em")) is None:
            erros.append("extracao revisada sem revisado_em (AAAA-MM-DD)")
        fund = meta.get("fundamento_temporal") or {}
        sem = [e for e in eixos if not _urns_validas(fund.get(e))]
        if sem and set(sem) == set(EIXOS):
            erros.append("extracao revisada sem fundamento_temporal de vigência e de efeitos")
        elif sem:
            erros.append(f"extracao revisada sem fundamento_temporal de {sem[0]}")
    elif meta.get("extracao") == "automatica" and meta.get("revisao_temporal_pendente") is not True:
        erros.append("extracao automatica precisa de revisao_temporal_pendente: true")
    return erros, avisos


# ---------------------------------------------------------------------------
# Leitura da revisão
# ---------------------------------------------------------------------------

def _revisao_de(entrada: dict) -> tuple[dict | None, list[str]]:
    """Revisão aplicável de uma entrada da proposta, ou os problemas que a impedem.

    `escopo` diz quais eixos a decisão cobre ([vigencia], [efeitos] ou os dois, o
    padrão). Decidir só a vigência deixa os efeitos provisórios e o dispositivo
    pendente.
    """
    rev = entrada.get("revisao") or {}
    decisao = rev.get("decisao")
    problemas = []
    if decisao not in DECISOES:
        return None, [f"decisao {decisao!r}: use aceitar, alterar ou rejeitar"]
    escopo = rev.get("escopo") or list(EIXOS)
    if not isinstance(escopo, list) or not set(escopo) <= set(EIXOS):
        return None, [f"escopo {escopo!r}: use [vigencia], [efeitos] ou os dois"]
    eixos = [e for e in EIXOS if e in escopo]
    campos = [c for e in eixos for c in CAMPOS_DO_EIXO[e]]
    if not rev.get("revisado_por"):
        problemas.append("sem revisado_por")
    if _iso(rev.get("revisado_em")) is None:
        problemas.append("sem revisado_em (AAAA-MM-DD)")
    if decisao == "rejeitar":
        return None, problemas

    urn = entrada.get("urn", "")
    if decisao == "aceitar":
        vig = (entrada.get("vigencia") or {}).get("proposta")
        efe = (entrada.get("efeitos") or {}).get("proposta")
        fundamento = (entrada.get("vigencia") or {}).get("fundamento")
        # Na forma da LC 214 os efeitos têm fundamento próprio (o inciso); na da
        # EC 132 acompanham a vigência.
        fundamento_efeitos = (entrada.get("efeitos") or {}).get("fundamento") or fundamento
        if "vigencia" in eixos and (not vig or not vig.get("data_candidata")):
            problemas.append("'aceitar' sem proposta de vigência com data: use 'alterar'")
        if "efeitos" in eixos and (not efe or not efe.get("data_candidata")):
            problemas.append("'aceitar' sem proposta de efeitos: use 'alterar' e informe "
                             "efeitos_inicio e fundamento_efeitos, ou escopo: [vigencia]")
        # Exceções por subdivisão que a cláusula estabelece ('450, exceto os §§ 1º
        # e 5º'): aceitar a proposta de efeitos é aceitá-las também.
        excecoes = ((entrada.get("efeitos") or {}).get("excecoes") or []) if "efeitos" in eixos else []
        for exc in excecoes:
            problemas += _problemas_excecao(exc, urn)
        if problemas:
            return None, problemas
        datas, precisao, fundamentos = {}, {}, {}
        if "vigencia" in eixos:
            datas.update(vigencia_inicio=vig["data_candidata"], vigencia_fim=None)
            if vig.get("precisao") == "ano":
                precisao["vigencia_inicio"] = "ano"
            fundamentos["vigencia"] = [fundamento]
        if "efeitos" in eixos:
            datas.update(efeitos_inicio=efe["data_candidata"], efeitos_fim=None)
            if efe.get("precisao") == "ano":
                precisao["efeitos_inicio"] = "ano"
            fundamentos["efeitos"] = [fundamento_efeitos]
    else:  # alterar
        datas = {}
        for campo in campos:
            valor = rev.get(campo)
            if valor is None:
                if campo.endswith("_inicio"):
                    problemas.append(f"'alterar' sem {campo}")
                datas[campo] = None
            elif _iso(valor) is None:
                problemas.append(f"{campo} fora do formato AAAA-MM-DD")
            else:
                datas[campo] = _iso(valor)
        fundamentos = {}
        for eixo in eixos:
            if not _urns_validas(rev.get(f"fundamento_{eixo}")):
                problemas.append(f"'alterar' sem fundamento_{eixo} (lista de URNs)")
            fundamentos[eixo] = rev.get(f"fundamento_{eixo}")
        precisao = {c: p for c, p in (rev.get("precisao") or {}).items() if p != "dia"} \
            if isinstance(rev.get("precisao"), dict) else rev.get("precisao")
        if isinstance(precisao, dict):
            fora = [c for c in precisao if c not in campos]
            if fora:
                problemas.append(f"precisao de campo fora do escopo: {fora}")
        problemas += _problemas_precisao(precisao, datas)
        excecoes = rev.get("excecoes_subdivisao") or []
        for exc in excecoes:
            problemas += _problemas_excecao(exc, urn)
            if isinstance(exc, dict) and [c for c in CAMPOS_DATA if c in exc and c not in campos]:
                problemas.append(f"exceção {exc.get('urn')!r} com data de eixo fora do escopo")
        if problemas:
            return None, problemas

    return {
        **datas,
        "eixos": eixos,
        "precisao": precisao,
        "excecoes_subdivisao": excecoes,
        "fundamento_temporal": fundamentos,
        "revisado_por": rev["revisado_por"],
        "revisado_em": _iso(rev["revisado_em"]),
    }, []


def carregar_revisoes(
    caminho: Path, sha256_fonte: str, urns: set[str], regras: dict | None = None
) -> tuple[dict[str, dict], list[str]]:
    """{urn: revisão aplicável} e os erros que impedem aplicar.

    Qualquer erro deve abortar a escrita: aplicar só parte de uma revisão, ou
    nenhuma em silêncio, deixaria a base num estado que ninguém decidiu.

    `regras`: as regras derivadas (temporal/regras.yaml, se não informadas). Uma
    decisão de regra que usa regra derivada não mais aprovada é erro.
    """
    if regras is None:
        regras = carregar_regras()
    if not caminho.exists():
        return {}, []
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    entradas = dados.get("dispositivos") or []
    decididas = [e for e in entradas if (e.get("revisao") or {}).get("decisao") is not None]
    if not decididas:
        return {}, []

    if dados.get("fonte_sha256") != sha256_fonte:
        return {}, [
            f"{caminho.name}: a revisão foi feita sobre outro texto da fonte "
            f"(sha256 {str(dados.get('fonte_sha256'))[:12]}..., atual {sha256_fonte[:12]}...). "
            "Nada foi aplicado. Revise de novo sobre o texto atual."
        ]

    revisoes, erros = {}, []
    for entrada in decididas:
        urn = entrada.get("urn", "")
        if urn not in urns:
            erros.append(f"{urn}: revisão para dispositivo que a norma não tem")
            continue
        revisao, problemas = _revisao_de(entrada)
        problemas = problemas_de_regra((entrada.get("revisao") or {}).get("revisado_por"),
                                       regras) + problemas
        if problemas:
            erros.append(f"{urn}: " + "; ".join(problemas))
        elif revisao is not None:
            revisoes[urn] = revisao
    return revisoes, erros


# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------

def aplicar_revisao(meta: dict, revisao: dict) -> dict:
    """Novo meta com a revisão aplicada. Não altera o original.

    Só os campos dos eixos revisados mudam; com um eixo só, o outro continua
    provisório e o dispositivo continua pendente.
    """
    novo = dict(meta)
    eixos = revisao.get("eixos") or list(EIXOS)
    campos = [c for e in eixos for c in CAMPOS_DO_EIXO[e]]
    for campo in campos:
        novo[campo] = revisao[campo]
    precisao = {c: p for c, p in (meta.get("precisao") or {}).items() if c not in campos}
    precisao.update(revisao.get("precisao") or {})
    if precisao:
        novo["precisao"] = precisao
    else:
        novo.pop("precisao", None)
    if revisao.get("excecoes_subdivisao"):
        novo["excecoes_subdivisao"] = revisao["excecoes_subdivisao"]
    elif set(eixos) == set(EIXOS):
        novo.pop("excecoes_subdivisao", None)
    novo["fundamento_temporal"] = revisao["fundamento_temporal"]
    novo["extracao"] = "revisada"
    novo["eixos_revisados"] = eixos
    novo["revisao_temporal_pendente"] = set(eixos) != set(EIXOS)
    novo["revisado_por"] = revisao["revisado_por"]
    novo["revisado_em"] = revisao["revisado_em"]
    return ordenar_meta(novo)


def revisoes_nao_aplicadas(revisoes: dict[str, dict], metas: list[dict]) -> list[str]:
    """Decisões tomadas que normas/ ainda não reflete (falta rodar fatiar.py)."""
    por_urn = {m.get("urn"): m for m in metas}
    erros = []
    for urn, rev in revisoes.items():
        meta = por_urn.get(urn)
        if meta is None:
            erros.append(f"{urn}: revisão para dispositivo ausente de normas/")
            continue
        campos = [c for e in rev.get("eixos") or EIXOS for c in CAMPOS_DO_EIXO[e]]
        iguais = meta.get("extracao") == "revisada" and all(
            (_iso(meta.get(c)) if meta.get(c) is not None else None) == rev[c]
            for c in campos)
        if not iguais:
            erros.append(f"{urn}: revisão decidida e não aplicada — rode pipeline/fatiar.py")
    return erros
