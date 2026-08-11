"""Utilidades compartilhadas do pipeline.

Regras de projeto que este módulo faz valer (ver PREMISSAS.md):
  - identificador canônico é a URN LexML;
  - texto normativo nunca é editado, apenas reescrito a partir da fonte;
  - todo dispositivo carrega procedência com sha256.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import re
import unicodedata
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent

DIR_FONTES = RAIZ / "fontes"
DIR_NORMAS = RAIZ / "normas"
DIR_EVENTOS = RAIZ / "eventos"
DIR_TEMPORAL = RAIZ / "temporal"
DIR_LACUNAS = RAIZ / "lacunas"
DIR_INTERPRETACOES = RAIZ / "interpretacoes"
DIR_INDICES = RAIZ / "indices"

MANIFEST = DIR_FONTES / "manifest.json"

CAMPOS_OBRIGATORIOS = (
    "urn",
    "norma",
    "norma_slug",
    "dispositivo",
    "camada",
    "publicacao",
    "vigencia_inicio",
    "efeitos_inicio",
    "status",
    "fonte",
    "ingerido_em",
)

STATUS_VALIDOS = {"vigente", "futuro", "revogado", "pendente_regulamentacao"}

# Marca que impede a promoção acidental de conteúdo não verificado para a
# camada 1. A validação falha se encontrar isto em /normas/.
MARCA_NAO_VERIFICADO = "NAO_VERIFICADO"


# ---------------------------------------------------------------------------
# URN LexML
# ---------------------------------------------------------------------------

def urn_norma(autoridade: str, data: str, numero: str) -> str:
    """urn:lex:br:federal:lei.complementar:2025-01-16;214"""
    return f"urn:lex:{autoridade}:{data};{numero}"


def urn_dispositivo(
    base: str,
    artigo: int | str,
    paragrafo: str | None = None,
    inciso: str | None = None,
    alinea: str | None = None,
) -> str:
    """Monta a URN de um dispositivo a partir da URN da norma.

    Subdivisões na ordem art -> par -> inc -> ali. `par0` designa o caput;
    `parU`, o parágrafo único.
    """
    partes = [f"art{artigo}"]
    if paragrafo is not None:
        partes.append(f"par{paragrafo}")
    if inciso is not None:
        partes.append(f"inc{inciso}")
    if alinea is not None:
        partes.append(f"ali-{alinea}")
    return f"{base}!{'_'.join(partes)}"


# ---------------------------------------------------------------------------
# Arquivos com front-matter
# ---------------------------------------------------------------------------

_SEP = re.compile(r"^---\s*$", re.MULTILINE)


def ler_frontmatter(caminho: Path) -> tuple[dict, str]:
    """Devolve (metadados, corpo). Levanta ValueError se o formato quebrar."""
    texto = caminho.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        raise ValueError(f"{caminho}: sem front-matter")
    partes = _SEP.split(texto, maxsplit=2)
    if len(partes) < 3:
        raise ValueError(f"{caminho}: front-matter malformado")
    meta = yaml.safe_load(partes[1]) or {}
    return meta, partes[2].lstrip("\n")


def escrever_frontmatter(caminho: Path, meta: dict, corpo: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    bloco = yaml.safe_dump(
        meta, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    caminho.write_text(f"---\n{bloco}---\n\n{corpo.rstrip()}\n", encoding="utf-8")


def arquivos_norma(slug: str | None = None):
    """Itera sobre os dispositivos de /normas/ (opcionalmente de uma norma)."""
    alvo = DIR_NORMAS / slug if slug else DIR_NORMAS
    if not alvo.exists():
        return
    yield from sorted(alvo.rglob("art-*.md"))


# ---------------------------------------------------------------------------
# Integridade
# ---------------------------------------------------------------------------

def sha256_bytes(dados: bytes) -> str:
    return hashlib.sha256(dados).hexdigest()


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Tempo
# ---------------------------------------------------------------------------

def para_data(valor) -> _dt.date | None:
    if valor in (None, "", "null"):
        return None
    if isinstance(valor, _dt.datetime):
        return valor.date()
    if isinstance(valor, _dt.date):
        return valor
    return _dt.date.fromisoformat(str(valor).strip())


def status_em(meta: dict, referencia: _dt.date) -> str:
    """Estado do dispositivo numa data — recalculado, nunca lido do arquivo.

    Distingue vigência de produção de efeitos (PREMISSAS.md §3.1): um
    dispositivo pode estar vigente e ainda não produzir efeitos.
    """
    vi = para_data(meta.get("vigencia_inicio"))
    vf = para_data(meta.get("vigencia_fim"))
    ei = para_data(meta.get("efeitos_inicio"))
    ef = para_data(meta.get("efeitos_fim"))

    if vf is not None and referencia >= vf:
        return "revogado"
    if vi is not None and referencia < vi:
        return "futuro"
    if ef is not None and referencia >= ef:
        return "sem_efeitos"
    if ei is not None and referencia < ei:
        return "vigente_sem_efeitos"
    return "vigente"


def hoje() -> str:
    return _dt.date.today().isoformat()


# ---------------------------------------------------------------------------
# Texto
# ---------------------------------------------------------------------------

def slugificar(texto: str) -> str:
    norm = unicodedata.normalize("NFKD", texto)
    norm = "".join(c for c in norm if not unicodedata.combining(c))
    norm = re.sub(r"[^a-zA-Z0-9]+", "-", norm).strip("-").lower()
    return norm


ROMANOS = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
    "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
}
