"""Etapa 3 — gera os índices derivados de /indices/.

Tudo aqui é REGENERÁVEL a partir de /normas/. Nunca editar à mão
(PREMISSAS.md §6.3): a fonte da verdade é única.

Uso:
    python3 pipeline/indexar.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import yaml

from comum import (
    DIR_INDICES,
    DIR_NORMAS,
    RAIZ,
    arquivos_norma,
    hoje,
    ler_frontmatter,
)

GLOSSARIO = RAIZ / "glossario" / "vocabulario.yaml"


def gravar(nome: str, dados) -> None:
    DIR_INDICES.mkdir(parents=True, exist_ok=True)
    (DIR_INDICES / nome).write_text(
        json.dumps(dados, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"  indices/{nome}")


def main() -> int:
    dispositivos: list[tuple[Path, dict]] = []
    for caminho in arquivos_norma():
        meta, _ = ler_frontmatter(caminho)
        dispositivos.append((caminho, meta))

    print(f"{len(dispositivos)} dispositivo(s) em /normas/")

    # -- remissões: o índice de maior retorno --------------------------------
    remissoes = {}
    citado_por = defaultdict(list)
    for _, meta in dispositivos:
        urn = meta["urn"]
        alvos = meta.get("remete_a") or []
        remissoes[urn] = {
            "dispositivo": meta["dispositivo"],
            "norma": meta.get("norma_slug"),
            "remete_a": alvos,
            "remete_a_externo": meta.get("remete_a_externo") or [],
        }
        for alvo in alvos:
            citado_por[alvo].append(urn)
    for urn, dados in remissoes.items():
        dados["citado_por"] = sorted(citado_por.get(urn, []))
    gravar("remissoes.json", remissoes)

    # -- temporal: resolve "estado em D" por filtro, não por semântica -------
    temporal = {
        meta["urn"]: {
            "dispositivo": meta["dispositivo"],
            "norma": meta.get("norma_slug"),
            "publicacao": str(meta.get("publicacao")),
            "vigencia_inicio": str(meta.get("vigencia_inicio")),
            "vigencia_fim": str(meta.get("vigencia_fim")),
            "efeitos_inicio": str(meta.get("efeitos_inicio")),
            "efeitos_fim": str(meta.get("efeitos_fim")),
            "revisao_temporal_pendente": bool(meta.get("revisao_temporal_pendente")),
        }
        for _, meta in dispositivos
    }
    gravar("temporal.json", temporal)

    # -- conceitos com definição legal ---------------------------------------
    conceitos = defaultdict(list)
    for _, meta in dispositivos:
        for termo in meta.get("conceitos_definidos") or []:
            conceitos[termo.lower()].append(meta["urn"])
    gravar("conceitos.json", {k: sorted(v) for k, v in conceitos.items()})

    # -- alterações e revogações ---------------------------------------------
    alteracoes = {
        meta["urn"]: {
            "altera": meta.get("altera") or [],
            "alterado_por": meta.get("alterado_por") or [],
            "anotacoes_oficiais": meta.get("anotacoes_oficiais") or [],
        }
        for _, meta in dispositivos
        if meta.get("altera") or meta.get("alterado_por") or meta.get("anotacoes_oficiais")
    }
    gravar("alteracoes.json", alteracoes)

    # -- vocabulário antigo -> novo (curado em /glossario/) ------------------
    if GLOSSARIO.exists():
        vocab = yaml.safe_load(GLOSSARIO.read_text(encoding="utf-8")) or {}
        urns = {meta["urn"] for _, meta in dispositivos}
        for entrada in vocab.get("equivalencias", []):
            fund = entrada.get("fundamento")
            entrada["fundamento_ingerido"] = bool(
                fund and any(u.startswith(fund.split("!")[0]) for u in urns)
            )
        gravar("vocabulario.json", vocab)

    # -- cobertura: impede presumir o que não está ingerido ------------------
    por_norma = defaultdict(int)
    pendentes = defaultdict(int)
    for _, meta in dispositivos:
        slug = meta.get("norma_slug", "?")
        por_norma[slug] += 1
        if meta.get("revisao_temporal_pendente"):
            pendentes[slug] += 1

    gravar(
        "cobertura.json",
        {
            "gerado_em": hoje(),
            "total_dispositivos": len(dispositivos),
            "normas": {
                slug: {
                    "dispositivos": total,
                    "revisao_temporal_pendente": pendentes.get(slug, 0),
                }
                for slug, total in sorted(por_norma.items())
            },
            "aviso": (
                "Esta base cobre apenas o que esta listado aqui. Nao presuma que "
                "uma norma esta indexada porque ela existe no mundo."
            ),
        },
    )

    if not dispositivos:
        print("\nNenhum dispositivo. Rode baixar.py e fatiar.py antes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
