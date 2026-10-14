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

from comum import DIR_TEMPORAL, gravar_texto, hoje
from regras_temporais import REGRA_LITERAL, aprovada, carregar_regras

EIXOS = ["vigencia", "efeitos"]

# Pendências do artigo que tiram tudo dele da regra.
BLOQUEIAM_ARTIGO = {"redacao_de_outro_ato", "parte_de_outro_ato", "clausula_temporal_propria",
                    "alcancado_por_clausula_temporal"}
# Pendências gerais que a regra sabe tratar. Qualquer outra bloqueia a norma toda.
PUBLICACAO_EM_ABERTO = {"rodape_cita_publicacao_nao_confirmada"}
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


def decidir_por_regra(proposta: dict, regras: dict, data: str) -> tuple[dict, dict]:
    """(proposta com as decisões de regra, resumo). Não altera a original."""
    nova = copy.deepcopy(proposta)
    forma = (nova.get("resumo") or {}).get("forma_da_clausula")
    tudo, publicacao_em_aberto, trazidos = _bloqueios_gerais(nova)
    resumo = {"vigencia_e_efeitos": 0, "so_vigencia": 0, "so_efeitos": 0, "nada": 0, "humanas": 0}
    for entrada in nova.get("dispositivos") or []:
        revisao = entrada.setdefault("revisao", {})
        if e_humana(revisao):
            resumo["humanas"] += 1
            continue
        if tudo or entrada.get("artigo") in trazidos:
            escopo, usadas = None, []
        else:
            escopo, usadas = _decidir(entrada, forma, regras, publicacao_em_aberto)
        anterior = dict(revisao)
        for chave in ("decisao", "escopo", "revisado_por", "revisado_em", "observacao"):
            revisao[chave] = None
        if escopo is None:
            resumo["nada"] += 1
            continue
        por = "regra:" + REGRA_LITERAL + "".join(f"+{r}" for r in sorted(set(usadas)))
        revisao.update(
            decisao="aceitar", escopo=escopo, revisado_por=por,
            observacao="decidido por regra (PREMISSAS.md §3.4): " + OBSERVACAO[tuple(escopo)],
        )
        mesma = (anterior.get("decisao") == "aceitar" and anterior.get("escopo") == escopo
                 and anterior.get("revisado_por") == por)
        revisao["revisado_em"] = anterior.get("revisado_em") if mesma else data
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
    nova, resumo = decidir_por_regra(proposta, carregar_regras(), hoje())
    gravar_texto(caminho, yaml.safe_dump(nova, allow_unicode=True, sort_keys=False,
                                         default_flow_style=False, width=1000))
    print(f"[{args.slug}] decisoes por regra: vigencia e efeitos {resumo['vigencia_e_efeitos']}, "
          f"so vigencia {resumo['so_vigencia']}, so efeitos {resumo['so_efeitos']}, "
          f"sem decisao {resumo['nada']}; humanas preservadas {resumo['humanas']}")
    print(f"  aplique com: python pipeline/fatiar.py --slug {args.slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
