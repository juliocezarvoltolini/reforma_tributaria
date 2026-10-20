"""Acervo: decretos, atos infralegais, Ajustes SINIEF e Notas Técnicas, arquivados
com procedência e conferidos — sem fatiamento.

`/normas/` é texto articulado de EC e LC, fatiado por dispositivo. Os atos abaixo
dela na hierarquia (PREMISSAS.md §2.1) vêm em formatos que o fatiamento não lê
(Nota Técnica em PDF com tabelas de leiaute, pacote de schemas, resolução em
página de portal). Eles entram aqui: catálogo em `pipeline/acervo.yaml`, original
em `fontes/acervo/<id>.<ext>` com sha256 em `fontes/manifest.json` (chave
`acervo/<id>`), índice em `indices/acervo.json`.

O que torna o registro conferível, e não só uma lista: `conferir` traz trechos
LITERAIS do original (o cabeçalho com número e data, a ementa) e a validação
confere cada um contra o texto extraído do arquivo arquivado. O registro não pode
dizer o que a fonte não diz. Só o espaço é normalizado — caixa e acento, não.

Canal oficial recusado é `bloqueio` (pendência declarada, como em fontes.yaml),
nunca original obtido de terceiro (PREMISSAS.md §1.3).
"""
from __future__ import annotations

import io
import re
import unicodedata
import zipfile
from pathlib import Path
from typing import Callable
from urllib.parse import urlparse

import yaml

ARQUIVO = Path(__file__).resolve().parent / "acervo.yaml"

# Ordem de prevalência (PREMISSAS.md §2.1), continuando a `prioridade` de
# fontes.yaml (EC 1, LC 2): menor prevalece.
NIVEIS = {
    "lei.ordinaria": 3,
    "decreto": 4,
    "portaria": 5,
    "instrucao.normativa": 5,
    "ato.declaratorio": 5,
    "ato.conjunto": 5,
    "ato.tecnico.conjunto": 5,
    "retificacao": 5,
    "edital": 5,
    "resolucao": 5,
    "ato": 5,
    "ajuste.sinief": 6,
    "convenio": 6,
    "ato.cotepe": 6,
    "nota.tecnica": 6,
    "informe.tecnico": 6,
    "schema": 6,
    "leiaute": 6,
    # Comunicado oficial: orientação do órgão, não ato normativo — abaixo de tudo.
    "comunicado": 7,
    "nota": 7,
    "recomendacao": 7,
}

# Canais oficiais por tipo (PREMISSAS.md §1.2): (host, prefixo do caminho).
DOU = ("www.in.gov.br", "")
PLANALTO = ("www.planalto.gov.br", "")
RFB = ("normas.receita.fazenda.gov.br", "")
# A API do Sijut2, onde o texto dos atos da RFB é servido (a página link.action é
# uma casca idêntica para todos os atos — medido em 2026-10-20).
SIJUT2 = ("normasinternet2.receita.fazenda.gov.br", "/api/consulta-externa/")
CGIBS = ("www.cgibs.gov.br", "")
CONFAZ = ("www.confaz.fazenda.gov.br", "")
PORTAIS_DFE = (
    ("www.nfe.fazenda.gov.br", ""),
    ("www.cte.fazenda.gov.br", ""),
    ("dfe-portal.svrs.rs.gov.br", ""),
    ("mdfe-portal.sefaz.rs.gov.br", ""),
    ("www.gov.br", "/nfse"),
)
CANAIS = {
    "lei.ordinaria": (PLANALTO, DOU),
    "decreto": (PLANALTO, DOU),
    "portaria": (DOU, RFB, SIJUT2, CGIBS),
    "instrucao.normativa": (RFB, SIJUT2, DOU),
    "ato.declaratorio": (RFB, SIJUT2, DOU),
    "ato.conjunto": (RFB, CGIBS, DOU),
    "ato.tecnico.conjunto": (RFB, CGIBS, DOU),
    "retificacao": (DOU, CONFAZ, RFB, CGIBS),
    "comunicado": (CGIBS, RFB, DOU),
    "nota": (RFB, SIJUT2, DOU),
    "recomendacao": (RFB, SIJUT2, DOU),
    "edital": (RFB, SIJUT2, DOU),
    "resolucao": (CGIBS, RFB, SIJUT2, DOU),
    "ato": (CGIBS, DOU),
    "ajuste.sinief": (CONFAZ, DOU),
    "convenio": (CONFAZ, DOU),
    "ato.cotepe": (CONFAZ, DOU),
    "nota.tecnica": PORTAIS_DFE,
    "informe.tecnico": PORTAIS_DFE,
    "schema": PORTAIS_DFE,
    "leiaute": PORTAIS_DFE,
}

RE_ID = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
RE_DATA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def carregar() -> list[dict]:
    if not ARQUIVO.exists():
        return []
    return (yaml.safe_load(ARQUIVO.read_text(encoding="utf-8")) or {}).get("atos") or []


# Ligaduras tipográficas que o extrator de PDF devolve como um caractere só.
LIGADURAS = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"})


def normalizar(texto: str) -> str:
    """Forma comparável: sem NENHUM espaço, ligaduras desfeitas, composição NFC.

    O espaço todo sai porque o extrator de PDF parte palavras ("d o Comitê", "a
    provação" — medido nos PDFs do CGIBS em 2026-10-20). Caixa, acento e a ordem
    dos caracteres continuam exigidos."""
    return re.sub(r"\s+", "", unicodedata.normalize("NFC", texto).translate(LIGADURAS))


def texto_do_original(dados: bytes, ext: str) -> str:
    if ext == "pdf":
        from pypdf import PdfReader

        return normalizar("\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(dados)).pages))
    from fatiar import html_para_texto

    if ext in ("zip", "xlsx"):
        # Pacote de schemas: nomes e conteúdo dos XSD/XML (o grupo de IBS/CBS está
        # dentro deles). Planilha: os textos das células (sharedStrings) e os nomes.
        # ZIP dentro de ZIP (pacote de eventos da NF-e) é lido também, com o caminho
        # "externo.zip/interno.xsd".
        partes = []

        def ler_zip(conteudo_zip: bytes, prefixo: str) -> None:
            with zipfile.ZipFile(io.BytesIO(conteudo_zip)) as z:
                for nome in z.namelist():
                    partes.append(prefixo + nome)
                    if nome.lower().endswith(".zip"):
                        ler_zip(z.read(nome), f"{prefixo}{nome}/")
                    elif nome.lower().endswith((".xsd", ".xml")):
                        conteudo = z.read(nome).decode("utf-8", "replace")
                        partes.append(re.sub(r"<[^>]+>", " ", conteudo) if ext == "xlsx" else conteudo)

        ler_zip(dados, "")
        return normalizar("\n".join(partes))
    if ext == "json":
        # Atos da RFB: a API do Sijut2 serve o texto em segmentos de HTML.
        import json

        textos: list[str] = []

        def colher(obj) -> None:
            if isinstance(obj, dict):
                for valor in obj.values():
                    colher(valor)
            elif isinstance(obj, list):
                for valor in obj:
                    colher(valor)
            elif isinstance(obj, str):
                textos.append(html_para_texto(obj.encode("utf-8")) if "<" in obj else obj)

        colher(json.loads(dados.decode("utf-8")))
        return normalizar("\n".join(textos))
    return normalizar(html_para_texto(dados))


def no_canal(tipo: str, url: str) -> bool:
    partes = urlparse(url)
    return partes.scheme == "https" and any(
        partes.hostname == host and partes.path.startswith(prefixo)
        for host, prefixo in CANAIS.get(tipo, ()))


def problemas_do_registro(reg: dict, docs: dict, ler: Callable[[str], bytes]) -> list[str]:
    """Erros de um registro do acervo (o bloqueio declarado é tratado em
    `problemas_do_acervo`)."""
    probs = []
    if not RE_ID.match(str(reg.get("id", ""))):
        probs.append(f"id {reg.get('id')!r} fora do formato (minúsculas, dígitos, '.' e '-')")
    tipo = reg.get("tipo")
    if tipo not in NIVEIS:
        probs.append(f"tipo {tipo!r} desconhecido")
    for campo in ("titulo", "orgao", "url"):
        if not str(reg.get(campo) or "").strip():
            probs.append(f"{campo} ausente")
    if reg.get("url") and tipo in NIVEIS and not no_canal(tipo, reg["url"]):
        probs.append(f"url fora do canal oficial de {tipo} (PREMISSAS.md §1.2): {reg['url']}")
    if reg.get("data") is not None and not RE_DATA.match(str(reg["data"])):
        probs.append(f"data {reg['data']!r} fora do formato AAAA-MM-DD")
    if "bloqueio" in reg:
        return probs

    conferir = reg.get("conferir") or []
    if not conferir or not all(isinstance(t, str) and t.strip() for t in conferir):
        probs.append("conferir: ao menos um trecho literal do original, nenhum vazio")
    registro = docs.get(f"acervo/{reg.get('id')}")
    if registro is None:
        probs.append("sem original no manifest (rode pipeline/baixar.py --acervo)")
        return probs
    if registro.get("url") != reg.get("url"):
        probs.append(f"url diverge da baixada (manifest: {registro.get('url')})")
    try:
        texto = texto_do_original(ler(registro["arquivo"]), Path(registro["arquivo"]).suffix[1:])
    except Exception as exc:  # original ilegível é erro do registro, não da validação
        probs.append(f"original ilegível ({registro['arquivo']}): {type(exc).__name__}: {exc}")
        return probs
    for trecho in conferir:
        if isinstance(trecho, str) and trecho.strip() and normalizar(trecho) not in texto:
            probs.append(f"conferir: trecho ausente do original: {trecho!r}")
    if reg.get("numero") and normalizar(str(reg["numero"])) not in texto:
        probs.append(f"numero {reg['numero']!r} ausente do original")
    return probs


def problemas_do_acervo(regs: list[dict], docs: dict,
                        ler: Callable[[str], bytes]) -> tuple[list[str], list[str]]:
    erros, avisos = [], []
    vistos: set = set()
    for reg in regs:
        rid = reg.get("id")
        if rid in vistos:
            erros.append(f"acervo {rid}: id duplicado")
        vistos.add(rid)
        erros += [f"acervo {rid}: {p}" for p in problemas_do_registro(reg, docs, ler)]
        if "bloqueio" in reg:
            if not str(reg["bloqueio"] or "").strip():
                erros.append(f"acervo {rid}: bloqueio sem motivo")
            elif f"acervo/{rid}" in docs:
                erros.append(f"acervo {rid}: bloqueio declarado, mas há original arquivado")
            else:
                avisos.append(f"acervo {rid}: canal oficial recusou — {reg['bloqueio']}")
    return erros, avisos


CAMPOS_DO_INDICE = ("id", "tipo", "orgao", "titulo", "numero", "data", "versao", "ementa",
                    "documento_fiscal", "situacao", "url", "bloqueio")


def indice(regs: list[dict], docs: dict) -> dict:
    atos, por_tipo = [], {}
    for reg in sorted(regs, key=lambda r: (NIVEIS.get(r.get("tipo"), 99), str(r.get("id")))):
        item = {c: reg[c] for c in CAMPOS_DO_INDICE if reg.get(c) is not None}
        item["nivel"] = NIVEIS.get(reg.get("tipo"))
        registro = docs.get(f"acervo/{reg.get('id')}")
        if registro and "bloqueio" not in reg:
            item.update(arquivo=registro["arquivo"], sha256=registro["sha256"],
                        acesso=registro.get("acesso"))
        atos.append(item)
        por_tipo[reg.get("tipo")] = por_tipo.get(reg.get("tipo"), 0) + 1
    return {"atos": atos,
            "totais": {"arquivados": sum("sha256" in a for a in atos),
                       "bloqueados": sum("bloqueio" in a for a in atos),
                       "por_tipo": dict(sorted(por_tipo.items()))}}
