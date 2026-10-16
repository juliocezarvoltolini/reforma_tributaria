"""Revisão temporal dos anexos — nível C (temporal/ia.yaml, `trata: anexos`).

A cláusula de vigência fala da lei e dos artigos ("Esta Lei Complementar entra em
vigor...", "produzindo efeitos ... em relação aos arts. ..."); nenhum inciso
nomeia anexo. A leitura registrada: o anexo é a lista que o artigo aplica
("relacionados no Anexo I desta Lei Complementar"), e passa a valer e a produzir
efeitos com a PRIMEIRA menção a ele no texto próprio da lei:

- menção no texto atual: as datas do artigo, ou as da subdivisão que tem datas
  próprias (`excecoes_subdivisao`) e a contém;
- menção em redação superada (riscada): as datas do artigo — é a redação original;
- texto que a lei insere em OUTRA lei (entre aspas) não conta: é daquela lei.

Anexo todo riscado com "(Revogado pela ...)" ligado a ato da base, conferido no
texto dele: deixa de valer quando o revogador produz efeitos (a regra
'texto-alterado-por-ato-posterior', na leitura de IA já registrada para ela).

Decide só quando tudo o que usa está decidido: cada artigo que menciona o anexo
revisado nos dois eixos, sem precisão de ano e sem fim de vigência ou de efeitos;
o revogador, revisado. Senão, nada — o anexo continua provisório.

Não é decisão de regra: grava `revisado_por: ia:<modelo>` com os ids das
interpretações usadas, como as decisões de IA dos artigos.
"""
from __future__ import annotations

import re

RE_RISCADO = re.compile(r"~~(.*?)~~")
RE_REVOGADO = re.compile(r"^\(?\s*Revogad[oa]\b", re.IGNORECASE)
REGRA_TEXTO_ALTERADO = "texto-alterado-por-ato-posterior"


def mencoes(urn_anexo: str, artigos: list[tuple[dict, str]], base: str,
            exigir_escopo: bool) -> list[dict]:
    """Onde o texto próprio dos artigos menciona o anexo: {artigo, subdivisao, riscada}."""
    from anexos import extrair_remissoes_a_anexos
    from fatiar import linhas_citadas, subdivisao_por_linha

    saida: list[dict] = []
    for meta, corpo in artigos:
        linhas = [linha for linha in corpo.split("\n") if linha.strip()]
        sem_marca = [linha.replace("~~", "") for linha in linhas]
        subs = subdivisao_por_linha(sem_marca, base, meta["urn"].partition("!art")[2])
        for linha, sub, citada in zip(linhas, subs, linhas_citadas(linhas)):
            if citada:
                continue
            trechos = [(RE_RISCADO.sub("", linha), False)] + [(r, True) for r in RE_RISCADO.findall(linha)]
            for texto, riscada in trechos:
                achado = {"artigo": meta, "subdivisao": sub, "riscada": riscada}
                if (urn_anexo in extrair_remissoes_a_anexos(texto, base, exigir_escopo)
                        and achado not in saida):
                    saida.append(achado)
    return saida


def _cobre(excecao: str, sub: str, artigo: str) -> bool:
    if excecao == f"{artigo}_par0":  # o caput, com os incisos dele
        return sub == artigo or sub.startswith(f"{artigo}_inc")
    return sub == excecao or sub.startswith(f"{excecao}_")


def _datas(mencao: dict) -> dict | None:
    """Datas da menção; None se a data usada tem precisão de ano."""
    meta = mencao["artigo"]
    datas = {"vigencia_inicio": meta["vigencia_inicio"], "efeitos_inicio": meta["efeitos_inicio"],
             "precisao": dict(meta.get("precisao") or {}), "fonte": mencao["subdivisao"]}
    if not mencao["riscada"]:
        for exc in meta.get("excecoes_subdivisao") or []:
            if _cobre(exc["urn"], mencao["subdivisao"], meta["urn"]):
                datas.update({c: exc[c] for c in ("vigencia_inicio", "efeitos_inicio") if c in exc})
                datas["precisao"].update(exc.get("precisao") or {})
    if set(datas["precisao"]) & {"vigencia_inicio", "efeitos_inicio"}:
        return None
    return datas


def _decidido(meta: dict) -> bool:
    return (meta.get("extracao") == "revisada" and not meta.get("revisao_temporal_pendente")
            and set(meta.get("eixos_revisados") or ["vigencia", "efeitos"]) == {"vigencia", "efeitos"}
            and not meta.get("vigencia_fim") and not meta.get("efeitos_fim"))


def _fim_por_revogacao(meta_anexo: dict, atos: dict, ctx: dict) -> tuple[str, list[str], set[str], str] | None:
    """(vigencia_fim, fundamento, ids, revisado_em do ato) do anexo revogado; None se
    a revogação não está ligada, conferida e datada."""
    from alteracoes import conferir_anexo
    from propor_vigencia import combinar_alteracao

    revogacoes = [a for a in meta_anexo.get("alterado_por") or [] if RE_REVOGADO.match(a["anotacao"])]
    regra = (ctx.get("regras") or {}).get(REGRA_TEXTO_ALTERADO)
    if len(revogacoes) != 1 or not regra or revogacoes[0].get("ato") not in atos:
        return None
    ato = revogacoes[0]["ato"]
    meta_ato, corpo_ato = atos[ato]
    numero = int(meta_anexo["urn"].rpartition("!anx")[2])
    nome = meta_anexo["norma"].split(",")[0].strip()
    if (meta_ato.get("extracao") != "revisada" or meta_ato.get("revisao_temporal_pendente")
            or not conferir_anexo(numero, nome, corpo_ato)):
        return None
    combinada = combinar_alteracao("revogado", True, meta_ato.get("vigencia_inicio"),
                                   meta_ato.get("efeitos_inicio"), None, None, {})
    fim = (combinada["resultado_se_aprovada"] or {}).get("vigencia_fim")
    if not fim:
        return None
    fundamento = [ato] + list((meta_ato.get("fundamento_temporal") or {}).get("efeitos") or [])
    ids = {regra} | set(((ctx.get("atos") or {}).get(ato.split("!")[0]) or {}).values())
    return fim, fundamento, ids, str(meta_ato.get("revisado_em"))


def aplicar_aos_anexos(anexos: list[tuple[dict, str]], artigos: list[tuple[dict, str]], base: str,
                      exigir_escopo: bool, slug: str, catalogo: dict) -> tuple[list[tuple[dict, str]], list[str]]:
    """Os anexos com a revisão aplicada, onde há decisão; e os avisos. Os artigos já
    trazem as datas decididas. Interpretação com problema: nada se decide."""
    import datetime as _dt

    import ia as ia_mod
    from comum import arquivos_dispositivos, ler_frontmatter, status_em, urn_norma
    from revisao_temporal import aplicar_revisao

    if not anexos:
        return anexos, []
    interpretacoes = ia_mod.carregar_interpretacoes()
    problemas = [p for i in interpretacoes["por_id"].values() for p in ia_mod.problemas_da_interpretacao(i)]
    if problemas:
        return anexos, [f"temporal/ia.yaml com problema, anexos sem decisão: {problemas[0]}"]
    bases = {urn_norma(f["autoridade"], f["data"], f["numero"]): f["slug"]
             for f in catalogo.get("fontes") or []}
    ctx = {**ia_mod.contexto(interpretacoes, slug, bases),
           "registrado_em": {i: x.get("registrado_em") for i, x in interpretacoes["por_id"].items()}}
    # Os atos que revogam anexos estão em outras normas, já em normas/.
    atos = {}
    for caminho in arquivos_dispositivos():
        if caminho.parent.name != slug:
            meta, corpo = ler_frontmatter(caminho)
            atos[meta["urn"]] = (meta, corpo)
    saida, hoje = [], _dt.date.today()
    for meta, corpo in anexos:
        revisao = decidir(meta, corpo, artigos, base, exigir_escopo, atos, ctx)
        if revisao:
            meta = aplicar_revisao(meta, revisao)
            meta["status"] = status_em(meta, hoje)
        saida.append((meta, corpo))
    return saida, []


def decidir(meta_anexo: dict, corpo_anexo: str, artigos: list[tuple[dict, str]], base: str,
            exigir_escopo: bool, atos: dict[str, tuple[dict, str]], ctx: dict) -> dict | None:
    """Revisão do anexo (formato de revisao_temporal.aplicar_revisao), ou None."""
    from propor_vigencia import texto_todo_riscado

    if not ctx.get("anexos"):
        return None
    achadas = mencoes(meta_anexo["urn"], artigos, base, exigir_escopo)
    if not achadas or not all(_decidido(m["artigo"]) for m in achadas):
        return None
    datas = [_datas(m) for m in achadas]
    if any(d is None for d in datas):
        return None
    vig = min(d["vigencia_inicio"] for d in datas)
    efe = min(d["efeitos_inicio"] for d in datas)
    fundamento = {
        "vigencia": list(dict.fromkeys(d["fonte"] for d in datas if d["vigencia_inicio"] == vig)),
        "efeitos": list(dict.fromkeys(d["fonte"] for d in datas if d["efeitos_inicio"] == efe))}
    ids = {ctx["anexos"]}
    revisado_em = max(str(m["artigo"].get("revisado_em")) for m in achadas)
    fim = None
    if texto_todo_riscado([linha for linha in corpo_anexo.split("\n") if linha.strip()]):
        revogacao = _fim_por_revogacao(meta_anexo, atos, ctx)
        if revogacao is None:
            return None
        fim, fundamento_fim, ids_fim, revisado_ato = revogacao
        fundamento["vigencia"] += [u for u in fundamento_fim if u not in fundamento["vigencia"]]
        ids |= ids_fim
        revisado_em = max(revisado_em, revisado_ato)
    # Decidido quando o último insumo existia: a data dos artigos, do revogador e
    # do registro das interpretações usadas.
    registros = [str(d) for i in ids if (d := (ctx.get("registrado_em") or {}).get(i))]
    revisado_em = max([revisado_em] + registros)
    return {"eixos": ["vigencia", "efeitos"], "vigencia_inicio": vig, "vigencia_fim": fim,
            "efeitos_inicio": efe, "efeitos_fim": None, "precisao": {}, "excecoes_subdivisao": [],
            "fundamento_temporal": fundamento, "revisado_por": f"ia:{ctx.get('modelo')}",
            "revisado_em": revisado_em, "interpretacoes_ia": sorted(ids)}
