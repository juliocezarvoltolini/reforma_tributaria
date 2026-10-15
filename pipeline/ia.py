"""Nível C da PREMISSAS.md §3.4: interpretação proposta por IA, com citação literal.

"Uma IA pode propor uma interpretação, mas só com a citação literal do trecho que
a sustenta, verificada mecanicamente contra o texto da camada 1. Um registro
feito por IA leva `revisado_por: ia:<modelo>`, não equivale a revisão humana e
aparece assim na consulta."

As interpretações ficam em `temporal/ia.yaml`. Cada uma tem `id`, `leitura` (o
raciocínio, em texto), `citacoes` ({fonte, trecho}: arquivo de normas/ ou fontes/
e o trecho literal) e o que ela resolve:

  resolve_pendencias  pendências gerais de uma norma (`norma`) que a leitura fecha;
  regra               uma regra derivada que a leitura aplica — só nas decisões de
                      IA; a regra continua não aprovada para as decisões de regra.

`revisar_por_regra.py` só usa a IA onde a regra não decidiu nada, e grava
`revisado_por: ia:<modelo>` com `interpretacoes_ia: [ids]`. A revisão temporal
recusa a decisão de IA cuja interpretação não existe ou tem citação que o texto
citado não contém.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

from comum import DIR_TEMPORAL, RAIZ, ler_frontmatter

ARQUIVO_IA = DIR_TEMPORAL / "ia.yaml"
PASTAS_CITAVEIS = ("normas", "fontes")
_cache: dict[tuple[str, float], str] = {}


def carregar_interpretacoes(caminho: Path = ARQUIVO_IA) -> dict:
    """{"modelo": ..., "por_id": {id: interpretação}}; vazio se não há arquivo."""
    if not caminho.exists():
        return {"modelo": None, "por_id": {}}
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    return {"modelo": dados.get("modelo"),
            "por_id": {i["id"]: i for i in dados.get("interpretacoes") or [] if i.get("id")}}


def _normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", texto)).strip()


def _texto(caminho: Path) -> str:
    chave = (str(caminho), caminho.stat().st_mtime)
    if chave in _cache:
        return _cache[chave]
    sufixo = caminho.suffix.lower()
    if sufixo == ".md":
        texto = ler_frontmatter(caminho)[1]
    elif sufixo in (".html", ".htm"):
        from fatiar import html_para_linhas
        texto = " ".join(linha.completa for linha in html_para_linhas(caminho.read_bytes()))
    elif sufixo == ".pdf":
        from dou_pdf import linhas_do_pdf
        texto = " ".join(linhas_do_pdf(caminho.read_bytes()))
    elif sufixo == ".doc":
        from atos_planalto import linhas_do_doc
        texto = " ".join(linhas_do_doc(caminho))
    else:
        texto = ""
    _cache[chave] = _normalizar(texto)
    return _cache[chave]


def verificar_citacao(citacao: dict, raiz: Path = RAIZ) -> bool:
    """O trecho está, literalmente (espaços normalizados), no arquivo citado de
    normas/ ou fontes/?"""
    fonte, trecho = citacao.get("fonte"), citacao.get("trecho")
    if not fonte or not trecho:
        return False
    relativo = Path(fonte)
    if relativo.is_absolute() or ".." in relativo.parts or relativo.parts[0] not in PASTAS_CITAVEIS:
        return False
    caminho = raiz / relativo
    if not caminho.is_file():
        return False
    return _normalizar(trecho) in _texto(caminho)


def problemas_da_interpretacao(interp: dict, raiz: Path = RAIZ) -> list[str]:
    problemas = []
    if not interp.get("leitura"):
        problemas.append(f"interpretação {interp.get('id')!r} sem leitura")
    citacoes = interp.get("citacoes") or []
    if not citacoes:
        problemas.append(f"interpretação {interp.get('id')!r} sem citação literal")
    for citacao in citacoes:
        if not verificar_citacao(citacao, raiz):
            problemas.append(f"interpretação {interp.get('id')!r}: trecho não encontrado em "
                             f"{citacao.get('fonte')!r}: {str(citacao.get('trecho'))[:80]!r}")
    if not (interp.get("resolve_pendencias") or interp.get("regra")):
        problemas.append(f"interpretação {interp.get('id')!r} não diz o que resolve")
    return problemas


def problemas_de_ia(revisao: dict, interpretacoes: dict, raiz: Path = RAIZ) -> list[str]:
    """Por que uma decisão `revisado_por: ia:...` não pode ser aplicada. Vazio para
    decisão humana ou de regra."""
    por = str(revisao.get("revisado_por") or "")
    if not por.startswith("ia:"):
        return []
    problemas = []
    if por.removeprefix("ia:") != interpretacoes.get("modelo"):
        problemas.append(f"revisado_por {por!r}: modelo diferente do de temporal/ia.yaml")
    ids = revisao.get("interpretacoes_ia") or []
    if not ids:
        problemas.append("decisão de IA sem interpretacoes_ia")
    for id_ in ids:
        interp = interpretacoes["por_id"].get(id_)
        if interp is None:
            problemas.append(f"interpretação {id_!r} não está em temporal/ia.yaml")
        else:
            problemas += problemas_da_interpretacao(interp, raiz)
    return problemas


def contexto(interpretacoes: dict, slug: str, bases: dict[str, str]) -> dict:
    """O que a IA resolve ao decidir a norma `slug`: as pendências gerais dela, as
    das normas alteradoras (por URN da norma) e as regras derivadas que aplica.
    `bases`: {URN da norma: slug}."""
    slugs_por_urn = {s: u for u, s in bases.items()}
    ctx = {"modelo": interpretacoes.get("modelo"), "resolve_pendencias": {}, "regras": {},
           "atos": {}}
    for id_, interp in interpretacoes["por_id"].items():
        if interp.get("regra"):
            ctx["regras"][interp["regra"]] = id_
        norma = interp.get("norma")
        for pendencia in interp.get("resolve_pendencias") or []:
            if norma == slug:
                ctx["resolve_pendencias"][pendencia] = id_
            elif norma in slugs_por_urn:
                ctx["atos"].setdefault(slugs_por_urn[norma], {})[pendencia] = id_
    return ctx
