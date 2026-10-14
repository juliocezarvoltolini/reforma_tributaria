"""Regras temporais derivadas, aprovadas por um humano (PREMISSAS.md §3.4).

Uma regra derivada transforma um texto que não traz a data pronta numa data:
"primeiro dia do quarto mês subsequente ao da sua publicação". A regra é escrita
em `temporal/regras.yaml` e só produz data depois de aprovada uma vez, com
`aprovada: true`, `aprovada_por` e `aprovada_em`. Sem isso, o que depende dela
fica pendente.

Regra é código determinístico, não conhecimento de modelo.
"""
from __future__ import annotations

import datetime as _dt
from pathlib import Path

import yaml

from comum import DIR_TEMPORAL

ARQUIVO_REGRAS = DIR_TEMPORAL / "regras.yaml"

# A regra literal (revisar_por_regra.py) é código e não depende de aprovação. As
# derivadas que ela usou vêm depois de '+': "regra:clausula-literal/v1+ano-primeiro-dia".
REGRA_LITERAL = "clausula-literal/v1"


def carregar_regras(caminho: Path = ARQUIVO_REGRAS) -> dict:
    if not caminho.exists():
        return {}
    return (yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}).get("regras") or {}


def aprovada(regras: dict, nome: str | None) -> bool:
    regra = regras.get(nome) or {}
    return (regra.get("aprovada") is True and bool(regra.get("aprovada_por"))
            and bool(regra.get("aprovada_em")))


def problemas_de_regra(revisado_por, regras: dict) -> list[str]:
    """Por que uma decisão `revisado_por: regra:...` não pode ser aplicada. Vazio
    para decisão humana. Pega a regra revogada depois da decisão."""
    por = str(revisado_por or "")
    if not por.startswith("regra:"):
        return []
    base, *derivadas = por.removeprefix("regra:").split("+")
    if base != REGRA_LITERAL:
        return [f"revisado_por {por!r}: regra que o código não tem (só '{REGRA_LITERAL}')"]
    faltam = [d for d in derivadas if not aprovada(regras, d)]
    if faltam:
        return [f"decisão de regra usa {', '.join(faltam)}, que não está aprovada em "
                "temporal/regras.yaml: rode pipeline/revisar_por_regra.py"]
    return []


def primeiro_dia_do_mes_subsequente(publicacao: str, meses: int) -> str:
    """Dia 1º do mês que fica `meses` meses depois do mês da publicação.

    Regra 'primeiro-dia-do-mes-subsequente': publicação em 16/01, quarto mês
    subsequente → 1º/05.
    """
    data = _dt.date.fromisoformat(publicacao)
    total = data.year * 12 + (data.month - 1) + meses
    return _dt.date(total // 12, total % 12 + 1, 1).isoformat()
