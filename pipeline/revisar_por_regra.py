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

from comum import DIR_TEMPORAL, arquivos_norma, gravar_texto, hoje, ler_frontmatter
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
    return (revisao.get("decisao") is not None
            and not str(revisao.get("revisado_por") or "").startswith("regra:"))


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


def _excecoes_de_alteracoes(entrada: dict) -> list[dict] | None:
    """Uma exceção por trecho alterado; o do caput em `_par0`. None se algum trecho
    não tem proposta ou tem duas leituras diferentes."""
    artigo, por_urn = entrada["urn"], {}
    for alteracao in entrada.get("alteracoes") or []:
        proposta = alteracao.get("proposta")
        if not proposta or not alteracao.get("subdivisao"):
            return None
        urn = alteracao["subdivisao"] if alteracao["subdivisao"] != artigo else f"{artigo}_par0"
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
    excecoes_alteracao = _excecoes_de_alteracoes(entrada)
    if escopo != EIXOS or excecoes_alteracao is None:
        return None
    vig, efe = entrada["vigencia"], entrada["efeitos"]
    excecoes_clausula = [dict(x) for x in efe.get("excecoes") or []]
    if {x["urn"] for x in excecoes_clausula} & {x["urn"] for x in excecoes_alteracao}:
        return None  # a cláusula e a alteração dizem coisas sobre o mesmo trecho
    precisao = {campo: "ano" for campo, lado in (("vigencia_inicio", vig), ("efeitos_inicio", efe))
                if (lado.get("proposta") or {}).get("precisao") == "ano"}
    return {"vigencia_inicio": vig["proposta"]["data_candidata"], "vigencia_fim": None,
            "efeitos_inicio": efe["proposta"]["data_candidata"], "efeitos_fim": None,
            "precisao": precisao, "fundamento_vigencia": [vig["fundamento"]],
            "fundamento_efeitos": [efe.get("fundamento") or vig["fundamento"]],
            "excecoes_subdivisao": excecoes_clausula + excecoes_alteracao,
            "_usadas": usadas + [REGRA_TEXTO_ALTERADO]}


def _igual_a_aplicada_alterar(revisao: dict, meta: dict | None) -> bool:
    if not meta or meta.get("extracao") != "revisada":
        return False
    if meta.get("revisado_por") != revisao["revisado_por"]:
        return False
    return ((meta.get("eixos_revisados") or EIXOS) == EIXOS
            and all(str(meta.get(c)) == str(revisao[c]) for c in ("vigencia_inicio", "efeitos_inicio"))
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


def decidir_por_regra(proposta: dict, regras: dict, data: str,
                      aplicadas: dict[str, dict] | None = None) -> tuple[dict, dict]:
    """(proposta com as decisões de regra, resumo). Não altera a original.

    `aplicadas`: {urn: front-matter de normas/}. Decisão igual à já aplicada
    mantém o `revisado_em` de lá, mesmo com a proposta regenerada.
    """
    nova = copy.deepcopy(proposta)
    forma = (nova.get("resumo") or {}).get("forma_da_clausula")
    tudo, publicacao_em_aberto, trazidos = _bloqueios_gerais(nova)
    atos = nova.get("atos_alteradores") or []
    resumo = {"vigencia_e_efeitos": 0, "so_vigencia": 0, "so_efeitos": 0, "nada": 0, "humanas": 0}
    for entrada in nova.get("dispositivos") or []:
        revisao = entrada.setdefault("revisao", {})
        if e_humana(revisao):
            resumo["humanas"] += 1
            continue
        alterar = None
        if tudo or entrada.get("artigo") in trazidos:
            escopo, usadas = None, []
        else:
            alterar = _decidir_texto_alterado(entrada, forma, regras, publicacao_em_aberto, atos)
            if alterar:
                escopo, usadas = list(EIXOS), alterar.pop("_usadas")
            else:
                escopo, usadas = _decidir(entrada, forma, regras, publicacao_em_aberto)
        anterior = copy.deepcopy(revisao)
        for chave in ("decisao", "escopo", "revisado_por", "revisado_em", "observacao"):
            revisao[chave] = None
        if alterar or anterior.get("decisao") == "alterar":
            revisao.update(copy.deepcopy(VAZIO_ALTERAR))
        if escopo is None:
            resumo["nada"] += 1
            continue
        por = "regra:" + REGRA_LITERAL + "".join(f"+{r}" for r in sorted(set(usadas)))
        if alterar:
            revisao.update(decisao="alterar", escopo=escopo, revisado_por=por, **alterar,
                           observacao="decidido por regra (PREMISSAS.md §3.4): vigência e "
                                      "efeitos pela norma alterada; os trechos incluídos, "
                                      "alterados ou revogados por ato posterior como exceção")
            mesma = (anterior.get("decisao") == "alterar" and anterior.get("revisado_por") == por
                     and all(anterior.get(c) == revisao[c] for c in VAZIO_ALTERAR))
            meta = (aplicadas or {}).get(entrada.get("urn"))
            if mesma:
                revisao["revisado_em"] = anterior.get("revisado_em")
            elif _igual_a_aplicada_alterar(revisao, meta):
                revisao["revisado_em"] = str(meta.get("revisado_em"))
            else:
                revisao["revisado_em"] = data
            resumo["vigencia_e_efeitos"] += 1
            continue
        revisao.update(
            decisao="aceitar", escopo=escopo, revisado_por=por,
            observacao="decidido por regra (PREMISSAS.md §3.4): " + OBSERVACAO[tuple(escopo)],
        )
        mesma = (anterior.get("decisao") == "aceitar" and anterior.get("escopo") == escopo
                 and anterior.get("revisado_por") == por)
        meta = (aplicadas or {}).get(entrada.get("urn"))
        if mesma:
            revisao["revisado_em"] = anterior.get("revisado_em")
        elif _igual_a_aplicada(entrada, escopo, por, meta):
            revisao["revisado_em"] = str(meta.get("revisado_em"))
        else:
            revisao["revisado_em"] = data
        resumo[CHAVE_RESUMO[tuple(escopo)]] += 1
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
    nova, resumo = decidir_por_regra(proposta, carregar_regras(), hoje(), aplicadas)
    gravar_texto(caminho, yaml.safe_dump(nova, allow_unicode=True, sort_keys=False,
                                         default_flow_style=False, width=1000))
    print(f"[{args.slug}] decisoes por regra: vigencia e efeitos {resumo['vigencia_e_efeitos']}, "
          f"so vigencia {resumo['so_vigencia']}, so efeitos {resumo['so_efeitos']}, "
          f"sem decisao {resumo['nada']}; humanas preservadas {resumo['humanas']}")
    print(f"  aplique com: python pipeline/fatiar.py --slug {args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
