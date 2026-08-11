"""Etapa 4 — validação. Roda na CI e antes de qualquer commit.

Premissa que não é verificada por máquina é intenção, não garantia
(PREMISSAS.md §7). Este script transforma as premissas em falha de build.

Uso:
    python3 pipeline/validar.py
    python3 pipeline/validar.py --estrito   # avisos também falham
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from comum import (
    CAMPOS_OBRIGATORIOS,
    DIR_FONTES,
    DIR_INTERPRETACOES,
    DIR_NORMAS,
    MANIFEST,
    MARCA_NAO_VERIFICADO,
    STATUS_VALIDOS,
    arquivos_norma,
    ler_frontmatter,
    para_data,
    sha256_arquivo,
)

erros: list[str] = []
avisos: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def aviso(msg: str) -> None:
    avisos.append(msg)


def rel(caminho: Path) -> str:
    return str(caminho.relative_to(DIR_NORMAS.parent))


# ---------------------------------------------------------------------------

def validar_dispositivos() -> list[dict]:
    metas: list[dict] = []
    por_urn: dict[str, list[str]] = defaultdict(list)

    for caminho in arquivos_norma():
        try:
            meta, corpo = ler_frontmatter(caminho)
        except ValueError as exc:
            erro(str(exc))
            continue

        for campo in CAMPOS_OBRIGATORIOS:
            if meta.get(campo) in (None, "", []):
                erro(f"{rel(caminho)}: campo obrigatorio ausente ou vazio: '{campo}'")

        if meta.get("camada") != 1:
            erro(f"{rel(caminho)}: /normas/ so aceita camada 1 (achado: {meta.get('camada')})")

        if meta.get("status") and meta["status"] not in STATUS_VALIDOS:
            aviso(f"{rel(caminho)}: status '{meta['status']}' fora do vocabulario padrao")

        fonte = meta.get("fonte") or {}
        for campo in ("url", "tipo", "acesso", "sha256"):
            if not fonte.get(campo):
                erro(f"{rel(caminho)}: fonte.{campo} ausente — sem procedencia verificavel")

        if MARCA_NAO_VERIFICADO in corpo:
            erro(f"{rel(caminho)}: contem marca {MARCA_NAO_VERIFICADO} — "
                 "conteudo nao verificado nao entra na camada 1")

        if not corpo.strip():
            erro(f"{rel(caminho)}: corpo vazio — dispositivo sem texto normativo")

        vi = para_data(meta.get("vigencia_inicio"))
        vf = para_data(meta.get("vigencia_fim"))
        if vi and vf and vf <= vi:
            erro(f"{rel(caminho)}: vigencia_fim ({vf}) nao e posterior a vigencia_inicio ({vi})")

        ei = para_data(meta.get("efeitos_inicio"))
        ef = para_data(meta.get("efeitos_fim"))
        if ei and ef and ef <= ei:
            erro(f"{rel(caminho)}: efeitos_fim ({ef}) nao e posterior a efeitos_inicio ({ei})")

        if meta.get("urn"):
            por_urn[meta["urn"]].append(rel(caminho))

        metas.append(meta)

    for urn, caminhos in por_urn.items():
        if len(caminhos) > 1:
            erro(f"URN duplicada em {len(caminhos)} arquivos: {urn} -> {', '.join(caminhos)}")

    return metas


def validar_remissoes(metas: list[dict]) -> None:
    """Remissão órfã dentro de norma já ingerida é erro; para norma ainda não
    ingerida é apenas aviso — a base não finge cobrir o que não cobre."""
    existentes = {m["urn"] for m in metas if m.get("urn")}
    normas_ingeridas = {u.split("!")[0] for u in existentes}

    for meta in metas:
        for alvo in meta.get("remete_a") or []:
            if alvo in existentes:
                continue
            # subdivisão (par/inc/ali) resolve para o artigo que a contém
            artigo = alvo.split("!")[0] + "!" + alvo.split("!")[1].split("_")[0]
            if artigo in existentes:
                continue
            if alvo.split("!")[0] in normas_ingeridas:
                erro(f"{meta['urn']}: remissao orfa para dispositivo inexistente: {alvo}")
            else:
                aviso(f"{meta['urn']}: remissao para norma nao ingerida: {alvo}")


def validar_hashes() -> None:
    if not MANIFEST.exists():
        aviso("fontes/manifest.json inexistente — nada ingerido ainda")
        return
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for chave, registro in manifest.get("documentos", {}).items():
        caminho = DIR_FONTES.parent / registro["arquivo"]
        if not caminho.exists():
            erro(f"manifest {chave}: arquivo arquivado ausente ({registro['arquivo']})")
            continue
        atual = sha256_arquivo(caminho)
        if atual != registro["sha256"]:
            erro(
                f"manifest {chave}: sha256 diverge do arquivo em disco "
                f"(declarado {registro['sha256'][:16]}..., real {atual[:16]}...)"
            )


def validar_interpretacoes() -> None:
    if not DIR_INTERPRETACOES.exists():
        return
    for caminho in sorted(DIR_INTERPRETACOES.rglob("*.md")):
        if caminho.name.upper().startswith("README"):
            continue
        try:
            meta, corpo = ler_frontmatter(caminho)
        except ValueError as exc:
            erro(str(exc))
            continue

        if meta.get("camada") != 3:
            erro(f"{rel(caminho)}: /interpretacoes/ exige camada 3")
        if not (meta.get("fundamenta_se_em") or []):
            erro(f"{rel(caminho)}: interpretacao sem citacao de dispositivo "
                 "(fundamenta_se_em vazio) — PREMISSAS.md §4.1")
        if not meta.get("autor"):
            erro(f"{rel(caminho)}: interpretacao sem autor")
        if meta.get("confianca") not in {"literal", "derivado", "controverso", "pendente"}:
            erro(f"{rel(caminho)}: grau de confianca invalido: {meta.get('confianca')!r}")


def relatar_pendencias(metas: list[dict]) -> None:
    pendentes = [m for m in metas if m.get("revisao_temporal_pendente")]
    if pendentes:
        aviso(
            f"{len(pendentes)} de {len(metas)} dispositivos com "
            "revisao_temporal_pendente: vigencia e eficacia ainda sao a data de "
            "publicacao. Revisar a clausula de vigencia antes de usar em producao."
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--estrito", action="store_true", help="avisos tambem falham")
    args = ap.parse_args()

    metas = validar_dispositivos()
    validar_remissoes(metas)
    validar_hashes()
    validar_interpretacoes()
    relatar_pendencias(metas)

    if not metas:
        aviso("nenhum dispositivo em /normas/ — base vazia")

    for msg in avisos:
        print(f"AVISO  {msg}")
    for msg in erros:
        print(f"ERRO   {msg}", file=sys.stderr)

    print(f"\n{len(metas)} dispositivo(s) validado(s) — "
          f"{len(erros)} erro(s), {len(avisos)} aviso(s)")

    if erros:
        return 1
    if args.estrito and avisos:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
