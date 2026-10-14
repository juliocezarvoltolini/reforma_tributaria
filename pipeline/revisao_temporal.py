"""Revisão temporal: do YAML revisado por um humano ao front-matter de normas/.

`propor_vigencia.py` gera `temporal/propostas/<slug>.yaml`. Quem revisa preenche,
em cada dispositivo, o bloco `revisao`:

  decisao: aceitar   adota a proposta de vigência E a de efeitos. Só vale se o
                     gerador propôs efeitos (artigo sem marco temporal próprio).
  decisao: alterar   datas e fundamentos explícitos: vigencia_inicio,
                     efeitos_inicio, fundamento_vigencia, fundamento_efeitos
                     (URNs). Opcionais: vigencia_fim, efeitos_fim, precisao,
                     excecoes_subdivisao.
  decisao: rejeitar  nada é aplicado; o dispositivo continua pendente.

Toda decisão exige `revisado_por` e `revisado_em`.

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

CAMPOS_DATA = ("vigencia_inicio", "vigencia_fim", "efeitos_inicio", "efeitos_fim")
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
    "altera", "alterado_por", "extracao", "revisao_temporal_pendente",
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
        if meta.get("revisao_temporal_pendente") is not False:
            erros.append("extracao revisada com revisao_temporal_pendente diferente de false")
        if not meta.get("revisado_por"):
            erros.append("extracao revisada sem revisado_por")
        if _iso(meta.get("revisado_em")) is None:
            erros.append("extracao revisada sem revisado_em (AAAA-MM-DD)")
        fund = meta.get("fundamento_temporal") or {}
        if not (_urns_validas(fund.get("vigencia")) and _urns_validas(fund.get("efeitos"))):
            erros.append("extracao revisada sem fundamento_temporal de vigência e de efeitos")
    elif meta.get("extracao") == "automatica" and meta.get("revisao_temporal_pendente") is not True:
        erros.append("extracao automatica precisa de revisao_temporal_pendente: true")
    return erros, avisos


# ---------------------------------------------------------------------------
# Leitura da revisão
# ---------------------------------------------------------------------------

def _revisao_de(entrada: dict) -> tuple[dict | None, list[str]]:
    """Revisão aplicável de uma entrada da proposta, ou os problemas que a impedem."""
    rev = entrada.get("revisao") or {}
    decisao = rev.get("decisao")
    problemas = []
    if decisao not in DECISOES:
        return None, [f"decisao {decisao!r}: use aceitar, alterar ou rejeitar"]
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
        if not vig or not vig.get("data_candidata"):
            problemas.append("'aceitar' sem proposta de vigência com data: use 'alterar'")
        if not efe or not efe.get("data_candidata"):
            problemas.append("'aceitar' sem proposta de efeitos: use 'alterar' e informe "
                             "efeitos_inicio e fundamento_efeitos")
        # Exceções por subdivisão que a cláusula estabelece ('450, exceto os §§ 1º
        # e 5º'): aceitar a proposta é aceitá-las também.
        excecoes = (entrada.get("efeitos") or {}).get("excecoes") or []
        for exc in excecoes:
            problemas += _problemas_excecao(exc, urn)
        if problemas:
            return None, problemas
        datas = {"vigencia_inicio": vig["data_candidata"], "vigencia_fim": None,
                 "efeitos_inicio": efe["data_candidata"], "efeitos_fim": None}
        precisao = {c: p for c, p in (("vigencia_inicio", vig.get("precisao")),
                                      ("efeitos_inicio", efe.get("precisao"))) if p == "ano"}
        fundamentos = {"vigencia": [fundamento], "efeitos": [fundamento_efeitos]}
    else:  # alterar
        datas = {}
        for campo in CAMPOS_DATA:
            valor = rev.get(campo)
            obrigatorio = campo in ("vigencia_inicio", "efeitos_inicio")
            if valor is None:
                if obrigatorio:
                    problemas.append(f"'alterar' sem {campo}")
                datas[campo] = None
            elif _iso(valor) is None:
                problemas.append(f"{campo} fora do formato AAAA-MM-DD")
            else:
                datas[campo] = _iso(valor)
        for chave in ("fundamento_vigencia", "fundamento_efeitos"):
            if not _urns_validas(rev.get(chave)):
                problemas.append(f"'alterar' sem {chave} (lista de URNs)")
        precisao = {c: p for c, p in (rev.get("precisao") or {}).items() if p != "dia"} \
            if isinstance(rev.get("precisao"), dict) else rev.get("precisao")
        problemas += _problemas_precisao(precisao, datas)
        excecoes = rev.get("excecoes_subdivisao") or []
        for exc in excecoes:
            problemas += _problemas_excecao(exc, urn)
        fundamentos = {"vigencia": rev.get("fundamento_vigencia"),
                       "efeitos": rev.get("fundamento_efeitos")}
        if problemas:
            return None, problemas

    return {
        **datas,
        "precisao": precisao,
        "excecoes_subdivisao": excecoes,
        "fundamento_temporal": fundamentos,
        "revisado_por": rev["revisado_por"],
        "revisado_em": _iso(rev["revisado_em"]),
    }, []


def carregar_revisoes(
    caminho: Path, sha256_fonte: str, urns: set[str]
) -> tuple[dict[str, dict], list[str]]:
    """{urn: revisão aplicável} e os erros que impedem aplicar.

    Qualquer erro deve abortar a escrita: aplicar só parte de uma revisão, ou
    nenhuma em silêncio, deixaria a base num estado que ninguém decidiu.
    """
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
        if problemas:
            erros.append(f"{urn}: " + "; ".join(problemas))
        elif revisao is not None:
            revisoes[urn] = revisao
    return revisoes, erros


# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------

def aplicar_revisao(meta: dict, revisao: dict) -> dict:
    """Novo meta com a revisão aplicada. Não altera o original."""
    novo = dict(meta)
    for campo in CAMPOS_DATA:
        novo[campo] = revisao[campo]
    for opcional in ("precisao", "excecoes_subdivisao"):
        if revisao.get(opcional):
            novo[opcional] = revisao[opcional]
        else:
            novo.pop(opcional, None)
    novo["fundamento_temporal"] = revisao["fundamento_temporal"]
    novo["extracao"] = "revisada"
    novo["revisao_temporal_pendente"] = False
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
        iguais = meta.get("extracao") == "revisada" and all(
            (_iso(meta.get(c)) if meta.get(c) is not None else None) == rev[c]
            for c in CAMPOS_DATA)
        if not iguais:
            erros.append(f"{urn}: revisão decidida e não aplicada — rode pipeline/fatiar.py")
    return erros
