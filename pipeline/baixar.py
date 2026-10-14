"""Etapa 1 — baixa fontes oficiais, arquiva o original e registra procedência.

Implementa PREMISSAS.md §1.1 (procedência verificável) e §6.1 (detecção de
deriva: mudança no texto oficial é evento que exige revisão, nunca sobrescrita
silenciosa).

Uso:
    python3 pipeline/baixar.py                 # baixa tudo que falta
    python3 pipeline/baixar.py --id lcp-214-2025
    python3 pipeline/baixar.py --aceitar-deriva  # homologa texto alterado

    # Quando o portal recusa acesso por script (reset de conexão, 403):
    python3 pipeline/baixar.py --id lcp-214-2025 --de-arquivo ~/Downloads/lcp214.htm

No Windows o comando é `python` ou `py`, não `python3`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests
import yaml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from comum import (
    DIR_EVENTOS,
    DIR_FONTES,
    MANIFEST,
    gravar_texto,
    hoje,
    sha256_bytes,
)

CATALOGO = Path(__file__).resolve().parent / "fontes.yaml"
TIMEOUT = 60

# Portais oficiais costumam derrubar a conexão de clientes que não se parecem
# com navegador — o sintoma é ConnectionResetError no handshake, igual para
# todas as URLs. Enviar cabeçalhos de navegador é a diferença entre funcionar e
# tomar reset. Não é contornar controle de acesso: o conteúdo é público e a
# procedência continua registrada com URL, data e hash.
CABECALHOS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
}


def sessao() -> requests.Session:
    s = requests.Session()
    s.headers.update(CABECALHOS)
    tentativas = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=2,  # 0s, 2s, 4s, 8s
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET"]),
    )
    adaptador = HTTPAdapter(max_retries=tentativas)
    s.mount("https://", adaptador)
    s.mount("http://", adaptador)
    return s


def carregar_catalogo() -> dict:
    return yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))


def carregar_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"documentos": {}}


def salvar_manifest(manifest: dict) -> None:
    DIR_FONTES.mkdir(parents=True, exist_ok=True)
    gravar_texto(
        MANIFEST,
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )


def extensao_de(url: str, content_type: str) -> str:
    if url.lower().endswith(".pdf") or "pdf" in content_type:
        return "pdf"
    return "html"


def registrar_deriva(chave: str, antigo: str, novo: str, url: str) -> Path:
    """Grava um evento de deriva de texto oficial para revisão humana."""
    DIR_EVENTOS.mkdir(parents=True, exist_ok=True)
    destino = DIR_EVENTOS / f"deriva-{chave.replace('/', '-')}-{hoje()}.md"
    gravar_texto(
        destino,
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
    )
    return destino


def gravar(
    fonte: dict,
    entrada: dict,
    dados: bytes,
    manifest: dict,
    aceitar_deriva: bool,
    content_type: str,
    obtencao: str,
) -> int:
    """Arquiva os bytes, confere deriva e registra procedência."""
    slug = fonte["slug"]
    chave = f"{slug}/{entrada['tipo']}"
    url = entrada["url"]

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

    ext = extensao_de(url, content_type)
    destino = DIR_FONTES / slug / f"{entrada['tipo']}.{ext}"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(dados)

    manifest["documentos"][chave] = {
        "id": fonte["id"],
        "slug": slug,
        "titulo": fonte["titulo"],
        "tipo_documento": entrada["tipo"],
        "url": url,
        "arquivo": destino.relative_to(DIR_FONTES.parent).as_posix(),
        "sha256": digest,
        "bytes": len(dados),
        "acesso": hoje(),
        "content_type": content_type,
        "obtencao": obtencao,  # "download" | "manual"
    }
    print(f"     ok  {len(dados)} bytes  sha256={digest[:16]}...  ({obtencao})")
    return 0


def diagnosticar(exc: Exception) -> None:
    texto = str(exc)
    print(f"     FALHA: {exc}", file=sys.stderr)

    if "ConnectionReset" in texto or "Connection aborted" in texto:
        print(
            "     O servidor derrubou a conexao. Causa tipica: o portal recusa\n"
            "     cliente que nao parece navegador, ou bloqueia o seu IP.\n"
            "     Este script ja envia cabecalhos de navegador e tenta 4 vezes.\n"
            "     Se persistir, baixe o arquivo no navegador e ingira com:\n"
            "       python pipeline/baixar.py --id <id> --de-arquivo <caminho>\n"
            "     A procedencia continua registrada (URL, data e hash).",
            file=sys.stderr,
        )
    elif "404" in texto:
        print(
            "     404: a URL mudou. Corrija em pipeline/fontes.yaml — nao contorne.",
            file=sys.stderr,
        )
    elif "SSL" in texto or "certificate" in texto.lower():
        print(
            "     Falha de TLS. Nao desabilite a verificacao: isso quebraria a\n"
            "     cadeia de procedencia. Investigue o certificado do portal.",
            file=sys.stderr,
        )
    else:
        print(
            "     Se for bloqueio de rede, execute onde o dominio esteja liberado.",
            file=sys.stderr,
        )


def baixar_um(
    fonte: dict, entrada: dict, manifest: dict, aceitar_deriva: bool, s: requests.Session
) -> int:
    url = entrada["url"]
    print(f"  -> {url}")
    try:
        resp = s.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as exc:
        diagnosticar(exc)
        return 1

    return gravar(
        fonte,
        entrada,
        resp.content,
        manifest,
        aceitar_deriva,
        resp.headers.get("Content-Type", ""),
        "download",
    )


def entrada_por_tipo(fonte: dict, tipo: str | None) -> dict:
    """A entrada do catálogo a que um arquivo corresponde.

    Sem `tipo`, só vale se a norma tiver uma única URL. Antes, `--de-arquivo` usava
    sempre a primeira: um PDF do DOU seria registrado como texto compilado, com a
    URL do Planalto como procedência.
    """
    entradas = fonte["urls"]
    tipos = ", ".join(e["tipo"] for e in entradas)
    if tipo is None:
        if len(entradas) == 1:
            return entradas[0]
        raise ValueError(f"'{fonte['id']}' tem mais de um documento ({tipos}): informe --tipo")
    for entrada in entradas:
        if entrada["tipo"] == tipo:
            return entrada
    raise ValueError(f"'{fonte['id']}' nao tem documento do tipo '{tipo}' (tem: {tipos})")


def entradas_para_baixar(fonte: dict, tipo: str | None) -> list[dict]:
    """Sem `tipo`, todas as URLs da norma; com `tipo`, só aquela."""
    if tipo is None:
        return list(fonte["urls"])
    return [entrada_por_tipo(fonte, tipo)]


def ingerir_arquivo_local(
    fonte: dict, caminho: Path, manifest: dict, aceitar_deriva: bool, tipo: str | None = None
) -> int:
    """Ingere um original que o usuário baixou pelo navegador.

    Mantém PREMISSAS.md §1.1 intacta: a URL oficial vem do catálogo, o hash é
    dos bytes reais e a data de acesso é registrada. O campo `obtencao`
    distingue isto de um download automatizado, para auditoria.
    """
    try:
        entrada = entrada_por_tipo(fonte, tipo)
    except ValueError as exc:
        print(f"     {exc}", file=sys.stderr)
        return 1

    if not caminho.exists():
        print(f"     arquivo nao encontrado: {caminho}", file=sys.stderr)
        return 1

    dados = caminho.read_bytes()
    if not dados:
        print(f"     arquivo vazio: {caminho}", file=sys.stderr)
        return 1

    print(f"  -> arquivo local: {caminho}")
    print(f"     procedencia declarada: {entrada['url']}")

    tipo = "application/pdf" if caminho.suffix.lower() == ".pdf" else "text/html"
    return gravar(fonte, entrada, dados, manifest, aceitar_deriva, tipo, "manual")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", help="processar apenas esta fonte")
    ap.add_argument(
        "--de-arquivo",
        metavar="CAMINHO",
        help="ingere um original baixado manualmente, em vez de buscar na rede "
        "(exige --id)",
    )
    ap.add_argument(
        "--tipo",
        help="documento da norma (texto_compilado, texto_publicado...). Obrigatorio com "
        "--de-arquivo quando a norma tem mais de um documento",
    )
    ap.add_argument(
        "--aceitar-deriva",
        action="store_true",
        help="homologa mudanca no texto oficial e sobrescreve o arquivado",
    )
    args = ap.parse_args()

    if args.de_arquivo and not args.id:
        ap.error("--de-arquivo exige --id, para saber a que norma o arquivo corresponde")

    catalogo = carregar_catalogo()
    manifest = carregar_manifest()
    falhas = 0

    fontes = catalogo.get("fontes") or []
    if args.id:
        fontes = [f for f in fontes if f["id"] == args.id]
        if not fontes:
            disponiveis = ", ".join(f["id"] for f in catalogo.get("fontes") or [])
            print(f"fonte '{args.id}' nao esta em fontes.yaml", file=sys.stderr)
            print(f"disponiveis: {disponiveis}", file=sys.stderr)
            return 2

    s = sessao()
    for fonte in sorted(fontes, key=lambda f: f.get("prioridade", 99)):
        print(f"[{fonte['id']}] {fonte['titulo']}")

        if args.de_arquivo:
            falhas += ingerir_arquivo_local(
                fonte, Path(args.de_arquivo).expanduser(), manifest, args.aceitar_deriva,
                args.tipo,
            )
            continue

        try:
            entradas = entradas_para_baixar(fonte, args.tipo)
        except ValueError as exc:
            print(f"     {exc}", file=sys.stderr)
            falhas += 1
            continue
        for entrada in entradas:
            if not entrada.get("url_verificada", False):
                print("     aviso: URL ainda nao verificada (fontes.yaml)")
            falhas += baixar_um(fonte, entrada, manifest, args.aceitar_deriva, s)

    salvar_manifest(manifest)

    pendentes = catalogo.get("pendentes") or []
    if pendentes:
        print(f"\n{len(pendentes)} fonte(s) pendente(s) de identificacao — ver fontes.yaml")

    if falhas:
        print(f"\n{falhas} falha(s) na ingestao.", file=sys.stderr)
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())
