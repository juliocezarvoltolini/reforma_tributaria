"""Etapa 4b — decide POR REGRA o que a cláusula de vigência diz literalmente.

PREMISSAS.md §3.4. Preenche o bloco `revisao` da proposta
(`temporal/propostas/<slug>.yaml`) só onde não há decisão a tomar. Cada eixo é
decidido à parte:

  vigência  a data está na proposta e vem de um termo literal — data escrita,
            "na data de sua publicação" — ou de uma regra derivada aprovada em
            temporal/regras.yaml ("em 2027" → 1º de janeiro, com precisão de ano;
            "quarto mês subsequente ao da publicação");
  efeitos   só na forma em que a cláusula dá os efeitos por inciso (LC 214), e
            só se o artigo foi atribuído sem ressalva, sem motivo de dúvida e
            sem mudança de alcance pela redação posterior do inciso.

Nada é decidido por regra quando:

  - a publicação não está confirmada no DOU (premissa da regra literal);
  - o artigo tem texto de outro ato (incluído, alterado, revogado, vetado,
    promulgado depois) ou foi trazido por outro ato do compilado: a cláusula
    desta norma não é a desse texto;
  - o artigo fixa, no próprio texto, quando algo entra em vigor ou produz
    efeitos, ou é citado por um artigo que faz isso;
  - a proposta tem uma pendência geral que esta regra não conhece.

Com a publicação em aberto (republicação citada no rodapé e não confirmada no
DOU), nada que dependa da data de publicação é decidido; a data escrita, sim.

O que a regra não resolve fica sem decisão, ou com o escopo do eixo que ela
resolveu. Na forma da EC 132 os efeitos nunca são decididos por regra: lá a
proposta de efeitos só existe por ausência de marco detectado, o que não é texto.

Nunca toca uma decisão humana. As decisões de regra são refeitas a cada execução;
se não mudaram, `revisado_em` fica o mesmo.

Uso:
    python pipeline/revisar_por_regra.py --slug lc-214-2025
    python pipeline/fatiar.py --slug lc-214-2025      # aplica a normas/
"""
from __future__ import annotations

import argparse
import copy
import sys

import yaml

import ia as ia_mod
from comum import DIR_TEMPORAL, arquivos_norma, gravar_texto, hoje, ler_frontmatter, urn_norma
from fatiar import CATALOGO
from regras_temporais import REGRA_LITERAL, aprovada, carregar_regras

EIXOS = ["vigencia", "efeitos"]

# Pendências do artigo que tiram tudo dele da regra.
BLOQUEIAM_ARTIGO = {"redacao_de_outro_ato", "parte_de_outro_ato", "clausula_temporal_propria",
                    "alcancado_por_clausula_temporal"}
# Pendências gerais que a regra sabe tratar. Qualquer outra bloqueia a norma toda.
PUBLICACAO_EM_ABERTO = {"rodape_cita_publicacao_nao_confirmada", "republicacao_sem_artigo"}
GERAIS_CONHECIDAS = PUBLICACAO_EM_ABERTO | {"outro_ato_no_compilado", "regra_derivada_nao_aprovada"}
# Termos cuja data sai da data de publicação.
DEPENDEM_DA_PUBLICACAO = {"evento", "relativo"}


def e_humana(revisao: dict) -> bool:
    """Decisão humana: nem de regra nem de IA (que são refeitas a cada execução)."""
    return (revisao.get("decisao") is not None
            and not str(revisao.get("revisado_por") or "").startswith(("regra:", "ia:")))


def _bloqueios_gerais(proposta: dict) -> tuple[bool, bool, set[str]]:
    """(bloqueia a norma toda?, publicação em aberto?, artigos trazidos por outro ato)."""
    tudo, publicacao, trazidos = False, False, set()
    for pendencia in proposta.get("pendencias_gerais") or []:
        pid = pendencia.get("id")
        if pid in PUBLICACAO_EM_ABERTO:
            publicacao = True
        elif pid == "outro_ato_no_compilado":
            if pendencia.get("artigos"):
                trazidos |= set(pendencia["artigos"])
            else:
                tudo = True
        elif pid not in GERAIS_CONHECIDAS:
            tudo = True
    return tudo, publicacao, trazidos


def _termo(proposta: dict | None, regras: dict, publicacao_fechada: bool) -> tuple[bool, str | None]:
    """(a regra pode adotar esta data?, regra derivada usada)."""
    if not proposta or not proposta.get("data_candidata"):
        return False, None
    tipo = proposta.get("tipo")
    if tipo in DEPENDEM_DA_PUBLICACAO and not publicacao_fechada:
        return False, None
    if tipo in ("data", "evento"):
        return True, None
    if tipo == "ano":
        return aprovada(regras, "ano-primeiro-dia"), "ano-primeiro-dia"
    if tipo == "relativo":
        regra = proposta.get("regra")
        return aprovada(regras, regra), regra
    return False, None


def _excecoes(efeitos: dict, regras: dict, publicacao_fechada: bool) -> tuple[bool, list[str]]:
    """(as exceções por subdivisão podem ser adotadas?, regras derivadas usadas)."""
    excecoes = efeitos.get("excecoes") or []
    tipos = efeitos.get("termos_das_excecoes")
    if not excecoes:
        return True, []
    if not isinstance(tipos, list) or len(tipos) != len(excecoes):
        return False, []
    usadas = []
    for tipo in tipos:
        if tipo == "data" or (tipo == "evento" and publicacao_fechada):
            continue
        if tipo == "ano" and aprovada(regras, "ano-primeiro-dia"):
            usadas.append("ano-primeiro-dia")
            continue
        # 'relativo' numa exceção: a regra que a converte não fica registrada nela.
        return False, []
    return True, usadas


def _decidir(entrada: dict, forma: str | None, regras: dict,
             publicacao_em_aberto: bool) -> tuple[list[str] | None, list[str]]:
    """(escopo decidido por regra, regras derivadas usadas)."""
    vig, efe = entrada.get("vigencia") or {}, entrada.get("efeitos") or {}
    publicacao = (entrada.get("atual_no_pipeline") or {}).get("publicacao") or {}
    pendencias = set(entrada.get("pendencias") or [])
    if publicacao.get("fonte") != "dou" or pendencias & BLOQUEIAM_ARTIGO:
        return None, []
    fechada = not publicacao_em_aberto
    alcance_mudou = "alcance_alterado_pela_redacao_posterior" in pendencias
    escopo: list[str] = []
    usadas: list[str] = []

    ok, regra = _termo(vig.get("proposta"), regras, fechada)
    if (ok and not vig.get("motivo") and not vig.get("ressalva")
            and not (forma == "vigencia_por_inciso" and alcance_mudou)):
        escopo.append("vigencia")
        usadas += [regra] if regra else []

    if (forma == "efeitos_por_inciso" and efe.get("inciso") and not efe.get("motivo")
            and not efe.get("ressalva") and not alcance_mudou):
        ok, regra = _termo(efe.get("proposta"), regras, fechada)
        exc_ok, exc_regras = _excecoes(efe, regras, fechada)
        if ok and exc_ok:
            escopo.append("efeitos")
            usadas += ([regra] if regra else []) + exc_regras
    return (escopo or None), usadas


OBSERVACAO = {
    ("vigencia", "efeitos"): "vigência e efeitos",
    ("vigencia",): "só a vigência; os efeitos ficam para leitura",
    ("efeitos",): "só os efeitos; a vigência fica para leitura",
}
CHAVE_RESUMO = {("vigencia", "efeitos"): "vigencia_e_efeitos", ("vigencia",): "so_vigencia",
                ("efeitos",): "so_efeitos"}


REGRA_TEXTO_ALTERADO = "texto-alterado-por-ato-posterior"
# Campos de uma decisão 'alterar' e o valor que têm quando não há decisão.
VAZIO_ALTERAR = {"vigencia_inicio": None, "vigencia_fim": None, "efeitos_inicio": None,
                 "efeitos_fim": None, "precisao": {}, "fundamento_vigencia": [],
                 "fundamento_efeitos": [], "excecoes_subdivisao": []}


def _atos_fechados(entrada: dict, atos: list[dict]) -> bool:
    """Toda lei alteradora das alterações do artigo está na base e sem pendência
    geral (republicação, retificação... em aberto)?"""
    for alteracao in entrada.get("alteracoes") or []:
        norma = next((x for x in atos if alteracao["ato"].startswith(x["urn"] + "!")), None)
        if norma is None or set(norma.get("pendencias_gerais") or []) - {"regra_derivada_nao_aprovada"}:
            return False
    return True


def _sem_fundamento(excecao: dict) -> dict:
    return {k: v for k, v in excecao.items() if k != "fundamento"}


def _excecoes_de_alteracoes(entrada: dict, regras: dict) -> list[dict] | None:
    """Uma exceção por trecho alterado; o do caput em `_par0`. None se algum trecho
    não tem proposta ou tem duas leituras diferentes. Com a regra aprovada só no
    contexto da IA, a proposta é o `resultado_se_aprovada`.

    A revogação anotada na linha do caput de artigo com TODO o texto riscado é do
    artigo inteiro: sai com a URN do próprio artigo, não `_par0`."""
    artigo, por_urn = entrada["urn"], {}
    aprovada_aqui = aprovada(regras, REGRA_TEXTO_ALTERADO)
    for alteracao in entrada.get("alteracoes") or []:
        proposta = alteracao.get("proposta") or (
            alteracao.get("resultado_se_aprovada") if aprovada_aqui else None)
        if not proposta or not alteracao.get("subdivisao"):
            return None
        if alteracao["subdivisao"] != artigo:
            urn = alteracao["subdivisao"]
        elif alteracao.get("tipo") == "revogado" and entrada.get("texto_todo_riscado"):
            urn = artigo
        else:
            urn = f"{artigo}_par0"
        fundamento = list(dict.fromkeys(x for x in (
            alteracao["ato"], (alteracao.get("ato_vigencia") or {}).get("fundamento"),
            (alteracao.get("ato_efeitos") or {}).get("fundamento")) if x))
        novo = {"urn": urn, **proposta, "fundamento": fundamento}
        if urn not in por_urn:
            por_urn[urn] = novo
            continue
        if _sem_fundamento(por_urn[urn]) != _sem_fundamento(novo):
            return None
        por_urn[urn]["fundamento"] = list(dict.fromkeys(por_urn[urn]["fundamento"] + fundamento))
    return list(por_urn.values())


def _decidir_texto_alterado(entrada: dict, forma: str | None, regras: dict,
                            publicacao_em_aberto: bool, atos: list[dict]) -> dict | None:
    """Decisão 'alterar' para artigo com texto de outro ato: as datas do artigo pela
    norma alterada, cada trecho alterado como exceção (regra
    'texto-alterado-por-ato-posterior'). None se qualquer trava não passa."""
    pendencias = set(entrada.get("pendencias") or [])
    if ("redacao_de_outro_ato" not in pendencias or not aprovada(regras, REGRA_TEXTO_ALTERADO)
            or not entrada.get("alteracoes") or not entrada.get("alteracoes_cobrem_as_marcas")
            or not _atos_fechados(entrada, atos)):
        return None
    sem = dict(entrada, pendencias=sorted(pendencias - {"redacao_de_outro_ato"}))
    escopo, usadas = _decidir(sem, forma, regras, publicacao_em_aberto)
    excecoes_alteracao = _excecoes_de_alteracoes(entrada, regras)
    if escopo != EIXOS or excecoes_alteracao is None:
        return None
    fim = next((x for x in excecoes_alteracao if x["urn"] == entrada["urn"]), {})
    excecoes_alteracao = [x for x in excecoes_alteracao if x["urn"] != entrada["urn"]]
    vig, efe = entrada["vigencia"], entrada["efeitos"]
    excecoes_clausula = [dict(x) for x in efe.get("excecoes") or []]
    if {x["urn"] for x in excecoes_clausula} & {x["urn"] for x in excecoes_alteracao}:
        return None  # a cláusula e a alteração dizem coisas sobre o mesmo trecho
    precisao = {campo: "ano" for campo, lado in (("vigencia_inicio", vig), ("efeitos_inicio", efe))
                if (lado.get("proposta") or {}).get("precisao") == "ano"}
    return {"vigencia_inicio": vig["proposta"]["data_candidata"],
            "vigencia_fim": fim.get("vigencia_fim"),
            "efeitos_inicio": efe["proposta"]["data_candidata"], "efeitos_fim": fim.get("efeitos_fim"),
            "precisao": precisao,
            # O fim do artigo revogado inteiro vem do ato revogador.
            "fundamento_vigencia": [vig["fundamento"]] + (fim.get("fundamento") or []),
            "fundamento_efeitos": [efe.get("fundamento") or vig["fundamento"]],
            "excecoes_subdivisao": excecoes_clausula + excecoes_alteracao,
            "_usadas": usadas + [REGRA_TEXTO_ALTERADO]}


def _igual_a_aplicada_alterar(revisao: dict, meta: dict | None) -> bool:
    if not meta or meta.get("extracao") != "revisada":
        return False
    if meta.get("revisado_por") != revisao["revisado_por"]:
        return False
    return ((meta.get("eixos_revisados") or EIXOS) == EIXOS
            and all(str(meta.get(c)) == str(revisao[c])
                    for c in ("vigencia_inicio", "vigencia_fim", "efeitos_inicio", "efeitos_fim"))
            and (meta.get("excecoes_subdivisao") or []) == revisao["excecoes_subdivisao"])


def _igual_a_aplicada(entrada: dict, escopo: list[str], por: str, meta: dict | None) -> bool:
    """A decisão é a mesma que normas/ já tem aplicada? (mesma regra, mesmos eixos,
    mesmas datas). É a memória de `revisado_em` quando a proposta foi regenerada."""
    if not meta or meta.get("extracao") != "revisada" or meta.get("revisado_por") != por:
        return False
    if (meta.get("eixos_revisados") or EIXOS) != escopo:
        return False
    for eixo in escopo:
        lado = entrada.get(eixo) or {}
        adotada = (lado.get("proposta") or {}).get("data_candidata")
        if str(meta.get(f"{eixo}_inicio")) != str(adotada):
            return False
        if eixo == "efeitos" and (meta.get("excecoes_subdivisao") or []) != (lado.get("excecoes") or []):
            return False
    return True


def _tentar(entrada: dict, forma: str | None, regras: dict, gerais: list[dict],
            atos: list[dict]) -> tuple[list[str] | None, list[str], dict | None]:
    """(escopo, regras derivadas usadas, campos de 'alterar' ou None) num contexto."""
    tudo, publicacao_em_aberto, trazidos = _bloqueios_gerais({"pendencias_gerais": gerais})
    if tudo or entrada.get("artigo") in trazidos:
        return None, [], None
    alterar = _decidir_texto_alterado(entrada, forma, regras, publicacao_em_aberto, atos)
    if alterar:
        return list(EIXOS), alterar.pop("_usadas"), alterar
    escopo, usadas = _decidir(entrada, forma, regras, publicacao_em_aberto)
    return escopo, usadas, None


# Aprovação que só vale dentro do contexto da IA: a regra continua NÃO aprovada
# para as decisões de regra (PREMISSAS.md §3.4).
_APROVADA_PELA_IA = {"aprovada": True, "aprovada_por": "ia", "aprovada_em": "ia"}


def _contexto_ia(ia: dict, regras: dict, gerais: list[dict], atos: list[dict]):
    """(regras, pendências gerais, atos) com o que as interpretações de IA resolvem,
    e os ids delas por uso: 'norma', 'atos', e {regra: id}."""
    resolve = ia.get("resolve_pendencias") or {}
    gerais_ia = [g for g in gerais if g.get("id") not in resolve]
    ids_norma = sorted({resolve[g["id"]] for g in gerais if g.get("id") in resolve})
    regras_ia = {**regras, **{nome: _APROVADA_PELA_IA for nome in (ia.get("regras") or {})
                              if not aprovada(regras, nome)}}
    atos_ia, ids_atos = [], set()
    for ato in atos:
        resolvidas = (ia.get("atos") or {}).get(ato.get("urn"), {})
        ids_atos |= {resolvidas[p] for p in ato.get("pendencias_gerais") or [] if p in resolvidas}
        atos_ia.append(dict(ato, pendencias_gerais=[p for p in ato.get("pendencias_gerais") or []
                                                    if p not in resolvidas]))
    regras_por_id = {nome: id_ for nome, id_ in (ia.get("regras") or {}).items()
                     if not aprovada(regras, nome)}
    return regras_ia, gerais_ia, atos_ia, ids_norma, sorted(ids_atos), regras_por_id


# Formas cuja cláusula só dá a vigência (EC 132, LC 235): dos efeitos ela não diz.
FORMAS_SO_VIGENCIA = {"vigencia_por_inciso", "vigencia_unica"}
# Onde a leitura "sem cláusula de efeitos, efeitos na vigência" não vale: o texto
# do artigo fixa o próprio tempo, depende de lei futura, tem data por subdivisão
# ou revoga com data (a data É o efeito do artigo).
FORA_DE_EFEITOS_DA_VIGENCIA = BLOQUEIAM_ARTIGO | {
    "depende_de_lei_futura", "condicao_regulamentacao", "datas_por_subdivisao",
    "revogacao_expressa", "alcance_alterado_pela_redacao_posterior"}


def _alterar_efeitos_da_vigencia(entrada: dict) -> dict:
    """Decisão 'alterar' com os efeitos na data da vigência, com a mesma precisão e
    o mesmo fundamento (a cláusula de vigência)."""
    vig = entrada["vigencia"]
    data = vig["proposta"]["data_candidata"]
    precisao = ({"vigencia_inicio": "ano", "efeitos_inicio": "ano"}
                if vig["proposta"].get("precisao") == "ano" else {})
    return {"vigencia_inicio": data, "vigencia_fim": None, "efeitos_inicio": data,
            "efeitos_fim": None, "precisao": precisao,
            "fundamento_vigencia": [vig["fundamento"]], "fundamento_efeitos": [vig["fundamento"]],
            "excecoes_subdivisao": []}


# Marcas que a leitura "menção a entrada em vigor é conteúdo" tira, só dos
# dispositivos que a interpretação lista.
MARCAS_DE_CLAUSULA_PROPRIA = {"clausula_temporal_propria", "alcancado_por_clausula_temporal"}


def _leituras_ia(entrada: dict, ia: dict) -> tuple[dict, list[str]]:
    """A entrada como as interpretações de IA a leem, e os ids das que mudaram algo:
    'conteudo' (a menção a entrada em vigor ou a efeitos é conteúdo, nos
    dispositivos listados) e 'vetado' (item vetado não tem texto)."""
    alvo, ids = entrada, []
    id_conteudo = (ia.get("conteudo") or {}).get(entrada.get("urn"))
    if id_conteudo and set(entrada.get("pendencias") or []) & MARCAS_DE_CLAUSULA_PROPRIA:
        alvo = copy.deepcopy(entrada)
        alvo["pendencias"] = [p for p in alvo["pendencias"] if p not in MARCAS_DE_CLAUSULA_PROPRIA]
        ids.append(id_conteudo)
    if ia.get("vetado") and (sem_vetado := _sem_vetado(alvo)) is not None:
        alvo = sem_vetado
        ids.append(ia["vetado"])
    return alvo, ids


def _sem_vetado(entrada: dict) -> dict | None:
    """A entrada lida com a interpretação de item vetado (sem texto, não muda as
    datas do resto do artigo), ou None se ela não se aplica: caput vetado, ou
    anotação que não é VETADO nem alteração ligada."""
    vetados = entrada.get("vetados") or {}
    if (not vetados.get("ocorrencias") or vetados.get("caput_vetado")
            or "redacao_de_outro_ato" not in (entrada.get("pendencias") or [])):
        return None
    todas = entrada.get("alteracoes") or []
    if len(todas) + vetados["ocorrencias"] != entrada.get("marcas_ocorrencias"):
        return None
    vetadas = set(vetados.get("subdivisoes") or [])
    nova = copy.deepcopy(entrada)
    # Item vetado não tem texto: a alteração que o incluiu não vira exceção.
    nova["alteracoes"] = [a for a in todas if a.get("subdivisao") not in vetadas]
    if nova["alteracoes"]:
        nova["alteracoes_cobrem_as_marcas"] = True
    else:
        nova["pendencias"] = [p for p in nova["pendencias"] if p != "redacao_de_outro_ato"]
    return nova


def decidir_por_regra(proposta: dict, regras: dict, data: str,
                      aplicadas: dict[str, dict] | None = None,
                      ia: dict | None = None) -> tuple[dict, dict]:
    """(proposta com as decisões de regra — e de IA —, resumo). Não altera a original.

    `aplicadas`: {urn: front-matter de normas/}. Decisão igual à já aplicada
    mantém o `revisado_em` de lá, mesmo com a proposta regenerada.

    `ia`: contexto das interpretações de IA (ia.contexto). Só onde a regra não
    decide nada, a mesma decisão é tentada com o que as interpretações resolvem; o
    resultado sai com `revisado_por: ia:<modelo>` e `interpretacoes_ia`.
    """
    nova = copy.deepcopy(proposta)
    forma = (nova.get("resumo") or {}).get("forma_da_clausula")
    gerais = nova.get("pendencias_gerais") or []
    atos = nova.get("atos_alteradores") or []
    if ia:
        regras_ia, gerais_ia, atos_ia, ids_norma, ids_atos, regras_por_id = _contexto_ia(
            ia, regras, gerais, atos)
    resumo = {"vigencia_e_efeitos": 0, "so_vigencia": 0, "so_efeitos": 0, "nada": 0,
              "humanas": 0, "por_ia": 0}
    for entrada in nova.get("dispositivos") or []:
        revisao = entrada.setdefault("revisao", {})
        if e_humana(revisao):
            resumo["humanas"] += 1
            continue
        escopo, usadas, alterar = _tentar(copy.deepcopy(entrada), forma, regras, gerais, atos)
        por_ia, ids = False, []
        alvo = entrada
        if ia:
            alvo, ids_leituras = _leituras_ia(entrada, ia)
            if escopo is None:
                esc, us, alt = _tentar(copy.deepcopy(alvo), forma, regras_ia, gerais_ia, atos_ia)
                ids_esc = sorted(set(ids_norma + (ids_atos if alt else []) + ids_leituras
                                     + [regras_por_id[r] for r in us if r in regras_por_id]))
                if esc is not None and ids_esc:  # só vale se alguma leitura da IA foi usada
                    escopo, usadas, alterar, ids, por_ia = esc, us, alt, ids_esc, True
            # Forma cuja cláusula só dá a vigência: a leitura dos efeitos completa.
            if (ia.get("efeitos_da_vigencia") and escopo == ["vigencia"] and not alterar
                    and forma in FORMAS_SO_VIGENCIA
                    and not set(alvo.get("pendencias") or []) & FORA_DE_EFEITOS_DA_VIGENCIA):
                escopo, alterar = list(EIXOS), _alterar_efeitos_da_vigencia(alvo)
                ids, por_ia = sorted(set(ids + [ia["efeitos_da_vigencia"]])), True

        anterior = copy.deepcopy(revisao)
        for chave in ("decisao", "escopo", "revisado_por", "revisado_em", "observacao"):
            revisao[chave] = None
        revisao.pop("interpretacoes_ia", None)
        if alterar or anterior.get("decisao") == "alterar":
            revisao.update(copy.deepcopy(VAZIO_ALTERAR))
        if escopo is None:
            resumo["nada"] += 1
            continue

        if por_ia:
            por = f"ia:{ia['modelo']}"
            origem = ("proposto por IA (PREMISSAS.md §3.4) — NÃO equivale a revisão humana; "
                      f"interpretações: {', '.join(ids)}: ")
        else:
            por = "regra:" + REGRA_LITERAL + "".join(f"+{r}" for r in sorted(set(usadas)))
            origem = "decidido por regra (PREMISSAS.md §3.4): "
        if alterar:
            revisao.update(decisao="alterar", escopo=escopo, revisado_por=por, **alterar,
                           observacao=origem + "vigência e efeitos pela norma alterada; os "
                                      "trechos incluídos, alterados ou revogados por ato "
                                      "posterior como exceção")
        else:
            revisao.update(decisao="aceitar", escopo=escopo, revisado_por=por,
                           observacao=origem + OBSERVACAO[tuple(escopo)])
        if por_ia:
            revisao["interpretacoes_ia"] = ids

        campos = ("decisao", "escopo", "revisado_por", "interpretacoes_ia") + (
            tuple(VAZIO_ALTERAR) if alterar else ())
        mesma = all(anterior.get(c) == revisao.get(c) for c in campos)
        meta = (aplicadas or {}).get(entrada.get("urn"))
        if meta is not None and meta.get("interpretacoes_ia") != revisao.get("interpretacoes_ia"):
            meta = None
        if mesma:
            revisao["revisado_em"] = anterior.get("revisado_em")
        elif alterar and _igual_a_aplicada_alterar(revisao, meta):
            revisao["revisado_em"] = str(meta.get("revisado_em"))
        elif not alterar and _igual_a_aplicada(entrada, escopo, por, meta):
            revisao["revisado_em"] = str(meta.get("revisado_em"))
        else:
            revisao["revisado_em"] = data
        resumo[CHAVE_RESUMO[tuple(escopo)]] += 1
        resumo["por_ia"] += por_ia
    return nova, resumo


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", required=True)
    args = ap.parse_args()

    caminho = DIR_TEMPORAL / "propostas" / f"{args.slug}.yaml"
    if not caminho.exists():
        print(f"{caminho} nao existe — rode pipeline/propor_vigencia.py antes", file=sys.stderr)
        return 2
    proposta = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    aplicadas = {}
    for arquivo in arquivos_norma(args.slug):
        meta, _ = ler_frontmatter(arquivo)
        aplicadas[meta["urn"]] = meta
    # Interpretações de IA (temporal/ia.yaml): todas verificadas antes de usar.
    interpretacoes = ia_mod.carregar_interpretacoes()
    problemas = [p for i in interpretacoes["por_id"].values()
                 for p in ia_mod.problemas_da_interpretacao(i)]
    if problemas:
        for p in problemas:
            print(f"ERRO temporal/ia.yaml: {p}", file=sys.stderr)
        return 2
    contexto = None
    if interpretacoes["por_id"]:
        catalogo = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))
        bases = {urn_norma(f["autoridade"], f["data"], f["numero"]): f["slug"]
                 for f in catalogo.get("fontes") or []}
        contexto = ia_mod.contexto(interpretacoes, args.slug, bases)
    nova, resumo = decidir_por_regra(proposta, carregar_regras(), hoje(), aplicadas, contexto)
    gravar_texto(caminho, yaml.safe_dump(nova, allow_unicode=True, sort_keys=False,
                                         default_flow_style=False, width=1000))
    print(f"[{args.slug}] decisoes por regra: vigencia e efeitos {resumo['vigencia_e_efeitos']}, "
          f"so vigencia {resumo['so_vigencia']}, so efeitos {resumo['so_efeitos']}, "
          f"sem decisao {resumo['nada']}; humanas preservadas {resumo['humanas']}; "
          f"das decididas, por IA: {resumo['por_ia']}")
    print(f"  aplique com: python pipeline/fatiar.py --slug {args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
