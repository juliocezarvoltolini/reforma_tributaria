"""Atos infralegais que o texto manda editar: regulamento, ato conjunto, ato do
Poder Executivo, do Comitê Gestor, da RFB.

A base não indexa nenhum ato infralegal (só EC e LC). "Na forma do regulamento" e
"ato conjunto do Ministro da Fazenda e do Comitê Gestor" dizem que a regra depende
de um ato que a base não tem — e, sem aviso, quem lê concluiria que a regra está
completa no dispositivo. A detecção é mecânica (menção literal, sem interpretar);
cada ocorrência vai para `remete_a_ato`, com a subdivisão e o trecho.

Fica de fora, de propósito: a lei futura (EC e LC: ver /lacunas/ e
/interpretacoes/regulamentacao/) e a legislação estadual, distrital e municipal.
"""
from __future__ import annotations

import re

TIPOS = {
    "regulamento": re.compile(r"\bregulamento\b", re.IGNORECASE),
    "ato_conjunto": re.compile(r"\bato\s+conjunto\b", re.IGNORECASE),
    "ato_poder_executivo": re.compile(r"\bato\s+do\s+Poder\s+Executivo\b", re.IGNORECASE),
    "ato_comite_gestor": re.compile(r"\bato\s+do\s+Comit[êe]\s+Gestor\b", re.IGNORECASE),
    "ato_rfb": re.compile(r"\bato\s+da\s+RFB\b", re.IGNORECASE),
}


def atos_infralegais(linhas: list[str], urn_base: str, artigo: str) -> list[dict]:
    """[{tipo, subdivisao, trecho}] do texto PRÓPRIO e em vigor do artigo (sem o
    riscado e sem o texto citado de outra norma), na ordem do texto: um por tipo e
    subdivisão."""
    from fatiar import subdivisao_por_linha

    achados: list[dict] = []
    vistos: set[tuple[str, str]] = set()
    for linha, sub in zip(linhas, subdivisao_por_linha(linhas, urn_base, artigo)):
        na_linha = sorted(
            ((m.start(), tipo, m.group(0)) for tipo, regex in TIPOS.items() for m in regex.finditer(linha)))
        for _, tipo, trecho in na_linha:
            if (tipo, sub) not in vistos:
                vistos.add((tipo, sub))
                achados.append({"tipo": tipo, "subdivisao": sub, "trecho": trecho})
    return achados
