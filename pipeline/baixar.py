"""Etapa 1 — baixa fontes oficiais, arquiva o original e registra procedência.

Implementa PREMISSAS.md §1.1 (procedência verificável) e §6.1 (detecção de
deriva: mudança no texto oficial é evento que exige revisão, nunca sobrescrita
silenciosa).

Uso:
    python3 pipeline/baixar.py                 # baixa tudo que falta
    python3 pipeline/baixar.py --id lcp-214-2025
    python3 pipeline/baixar.py --aceitar-deriva  # homologa texto alterado
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests
import yaml

from comum import (
    DIR_EVENTOS,
    DIR_FONTES,
    MANIFEST,
    hoje,
    sha256_bytes,
)

CATALOGO = Path(__file__).resolve().parent / "fontes.yaml"
TIMEOUT = 60
UA = "reforma-tributaria-base/1.0 (ingestao de normas oficiais)"


def carregar_catalogo() -> dict:
    return yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))


def carregar_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"documentos": {}}


def salvar_manifest(manifest: dict) -> None:
    DIR_FONTES.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def extensao_de(url: str, content_type: str) -> str:
    if url.lower().endswith(".pdf") or "pdf" in content_type:
        return "pdf"
    return "html"


def registrar_deriva(chave: str, antigo: str, novo: str, url: str) -> Path:
    """Grava um evento de deriva de texto oficial para revisão humana."""
    DIR_EVENTOS.mkdir(parents=True, exist_ok=True)
    destino = DIR_EVENTOS / f"deriva-{chave.replace('/', '-')}-{hoje()}.md"
    destino.write_text(
        "---\n"
        f"tipo: deriva_fonte\n"
        f"documento: {chave}\n"
        f"detectado_em: {hoje()}\n"
        f"sha256_anterior: {antigo}\n"
        f"sha256_atual: {novo}\n"
        f"url: {url}\n"
        "status: aguardando_revisao\n"
        "---\n\n"
        "O texto oficial mudou desde a última ingestão.\n\n"
        "Revisar o que mudou e por quê (consolidação editorial, alteração\n"
        "legislativa, correção de erro material) antes de homologar. Após a\n"
        "análise, reingerir com `--aceitar-deriva` e registrar a conclusão\n"
        "aqui, alterando `status`.\n",
        encoding="utf-8",
    )
    return destino


def baixar_um(fonte: dict, entrada: dict, manifest: dict, aceitar_deriva: bool) -> int:
    slug = fonte["slug"]
    url = entrada["url"]
    chave = f"{slug}/{entrada['tipo']}"

    print(f"  -> {url}")
    try:
        resp = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": UA})
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"     FALHA: {exc}", file=sys.stderr)
        print(
            "     Se for bloqueio de rede, execute onde o dominio esteja liberado.\n"
            "     Se for 404, corrija a URL em pipeline/fontes.yaml — nao contorne.",
            file=sys.stderr,
        )
        return 1

    dados = resp.content
    digest = sha256_bytes(dados)
    anterior = manifest["documentos"].get(chave)

    if anterior and anterior["sha256"] != digest and not aceitar_deriva:
        caminho_evento = registrar_deriva(chave, anterior["sha256"], digest, url)
        print(
            f"     DERIVA DETECTADA em {chave}\n"
            f"     anterior: {anterior['sha256'][:16]}...\n"
            f"     atual:    {digest[:16]}...\n"
            f"     evento registrado em {caminho_evento.relative_to(DIR_FONTES.parent)}\n"
            f"     arquivo NAO sobrescrito. Revise e use --aceitar-deriva.",
            file=sys.stderr,
        )
        return 1

    ext = extensao_de(url, resp.headers.get("Content-Type", ""))
    destino = DIR_FONTES / slug / f"{entrada['tipo']}.{ext}"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(dados)

    manifest["documentos"][chave] = {
        "id": fonte["id"],
        "slug": slug,
        "titulo": fonte["titulo"],
        "tipo_documento": entrada["tipo"],
        "url": url,
        "arquivo": str(destino.relative_to(DIR_FONTES.parent)),
        "sha256": digest,
        "bytes": len(dados),
        "acesso": hoje(),
        "content_type": resp.headers.get("Content-Type", ""),
    }
    print(f"     ok  {len(dados)} bytes  sha256={digest[:16]}...")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", help="baixar apenas esta fonte")
    ap.add_argument(
        "--aceitar-deriva",
        action="store_true",
        help="homologa mudanca no texto oficial e sobrescreve o arquivado",
    )
    args = ap.parse_args()

    catalogo = carregar_catalogo()
    manifest = carregar_manifest()
    falhas = 0

    fontes = catalogo.get("fontes") or []
    if args.id:
        fontes = [f for f in fontes if f["id"] == args.id]
        if not fontes:
            print(f"fonte '{args.id}' nao esta em fontes.yaml", file=sys.stderr)
            return 2

    for fonte in sorted(fontes, key=lambda f: f.get("prioridade", 99)):
        print(f"[{fonte['id']}] {fonte['titulo']}")
        for entrada in fonte["urls"]:
            if not entrada.get("url_verificada", False):
                print("     aviso: URL ainda nao verificada (fontes.yaml)")
            falhas += baixar_um(fonte, entrada, manifest, args.aceitar_deriva)

    salvar_manifest(manifest)

    pendentes = catalogo.get("pendentes") or []
    if pendentes:
        print(f"\n{len(pendentes)} fonte(s) pendente(s) de identificacao — ver fontes.yaml")

    if falhas:
        print(f"\n{falhas} falha(s) na ingestao.", file=sys.stderr)
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())
