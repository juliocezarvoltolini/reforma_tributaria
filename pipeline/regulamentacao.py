"""Remissões a lei futura: onde a base localiza a regulamentação, e onde não.

"Lei complementar definirá...", "Até que lei complementar disponha..." — o
dispositivo que remete a lei futura, lido sozinho, não diz se a lei já veio. Se a
base cala, quem consulta conclui "não regulamentado" (PREMISSAS.md §5.1); se a lei
veio e está indexada, a conclusão é falsa. Dois registros respondem:

- `/interpretacoes/` com `tipo: regulamentacao` (camada 3): liga cada remissão
  (`remissoes`) aos dispositivos que a regulam (`regulado_por`), com o trecho
  literal de cada lado. `confianca: literal` só quando o próprio regulador cita o
  artigo que remete ("criada nos termos do art. 8º da Emenda Constitucional nº
  132"); senão `derivado` (ou `controverso`), com o raciocínio no corpo.
- `/lacunas/` (camada 2): a remissão cuja regulamentação NÃO foi localizada nas
  normas indexadas — `situacao: nao_localizado`, nunca "não regulamentado". Diz
  em que normas (`pesquisado_em`) e com que termos se buscou; uma norma ingerida
  depois da busca a torna desatualizada, e a validação falha até que se refaça.

Todo trecho ({urn, trecho}) é verificado contra o texto ATUAL (sem o riscado) da
subdivisão citada — não do artigo inteiro, nem da redação superada.

A ligação diz QUE o regulador trata da matéria remetida. Quando ele produz
efeitos é dado do próprio regulador (consultar.py mostra o estado na data).
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from comum import DIR_INTERPRETACOES, DIR_LACUNAS, RAIZ, arquivos_norma, ler_frontmatter

TIPO_REGULAMENTACAO = "regulamentacao"
CONFIANCAS = {"literal", "derivado", "controverso"}
SITUACOES_LACUNA = {"nao_localizado"}
RE_RISCADO = re.compile(r"~~.*?~~")


def _normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", texto)).strip()


def urn_do_artigo(urn: str) -> str:
    """'...;132!art9_par3_incII' -> '...;132!art9'."""
    base, _, fragmento = urn.partition("!")
    return f"{base}!{fragmento.split('_')[0]}"


def indice_de_normas() -> dict[str, tuple[dict, str]]:
    """{urn do artigo: (metadados, corpo)} de tudo que está em normas/."""
    indice = {}
    for caminho in arquivos_norma():
        meta, corpo = ler_frontmatter(caminho)
        indice[meta["urn"]] = (meta, corpo)
    return indice


def texto_atual(meta: dict, corpo: str, urn: str) -> str | None:
    """Texto atual (sem o riscado) da subdivisão `urn` do artigo, com as suas
    subdivisões; o artigo inteiro se `urn` é o do artigo. None se o artigo não tem
    essa subdivisão."""
    from fatiar import subdivisao_por_linha

    linhas = [RE_RISCADO.sub("", linha).strip() for linha in corpo.split("\n")]
    linhas = [linha for linha in linhas if linha]
    if urn == meta["urn"]:
        return _normalizar(" ".join(linhas))
    if urn not in (meta.get("subdivisoes") or []):
        return None
    base, _, fragmento = meta["urn"].partition("!")
    subs = subdivisao_por_linha(linhas, base, fragmento.removeprefix("art"))
    proprias = [linha for linha, sub in zip(linhas, subs) if sub == urn or sub.startswith(f"{urn}_")]
    return _normalizar(" ".join(proprias))


def problemas_do_trecho(citacao: dict, indice: dict) -> list[str]:
    urn, trecho = citacao.get("urn"), citacao.get("trecho")
    if not urn or not trecho or not str(trecho).strip():
        return [f"citação sem urn ou sem trecho: {citacao!r}"]
    if urn_do_artigo(urn) not in indice:
        return [f"{urn}: dispositivo não está em normas/"]
    meta, corpo = indice[urn_do_artigo(urn)]
    texto = texto_atual(meta, corpo, urn)
    if texto is None:
        return [f"{urn}: o artigo não tem essa subdivisão"]
    if _normalizar(str(trecho)) not in texto:
        return [f"{urn}: trecho não está no texto atual da subdivisão: {str(trecho)[:80]!r}"]
    return []


def _comuns(registro: dict) -> list[str]:
    problemas = []
    for campo in ("titulo", "autor", "data"):
        if not registro.get(campo):
            problemas.append(f"sem {campo}")
    remissoes = registro.get("remissoes") or []
    if not remissoes:
        problemas.append("sem remissoes (o dispositivo que remete a lei futura)")
    return problemas


def _cita_o_artigo(trecho: str, meta_remissor: dict) -> bool:
    """O trecho do regulador nomeia o artigo e a norma que remetem?"""
    norma = _normalizar(meta_remissor["norma"].split(", de ")[0])
    numero = meta_remissor["urn"].partition("!")[2].removeprefix("art")
    trecho = _normalizar(trecho)
    return norma in trecho and re.search(rf"\bart\.\s*{re.escape(numero)}[º°]?(?![\d-])", trecho) is not None


def problemas_de_regulamentacao(registro: dict, corpo: str, indice: dict) -> list[str]:
    """Por que a ligação remissão -> regulador não vale. Vazio se vale."""
    problemas = _comuns(registro)
    if registro.get("camada") != 3:
        problemas.append("regulamentação é interpretação: camada 3")
    confianca = registro.get("confianca")
    if confianca not in CONFIANCAS:
        problemas.append(f"confianca {confianca!r}: use literal, derivado ou controverso "
                         "(remissão sem regulamentação localizada é lacuna)")
    reguladores = registro.get("regulado_por") or []
    if not reguladores:
        problemas.append("sem regulado_por (o dispositivo que regula)")
    citacoes = (registro.get("remissoes") or []) + reguladores
    for citacao in citacoes:
        problemas += problemas_do_trecho(citacao, indice)
    faltam = [c.get("urn") for c in citacoes
              if c.get("urn") not in (registro.get("fundamenta_se_em") or [])]
    if faltam:
        problemas.append(f"fundamenta_se_em não lista: {', '.join(map(str, faltam))}")
    if confianca == "literal":
        for remissao in registro.get("remissoes") or []:
            meta = indice.get(urn_do_artigo(str(remissao.get("urn"))), (None,))[0]
            if meta and not any(_cita_o_artigo(str(r.get("trecho") or ""), meta) for r in reguladores):
                problemas.append(f"literal: nenhum trecho do regulador cita o {meta['dispositivo']} "
                                 f"da {meta['norma'].split(', de ')[0]} — a ligação é derivado")
    elif not corpo.strip():
        problemas.append(f"confianca {confianca}: exponha o raciocínio no corpo")
    return problemas


def problemas_de_lacuna(registro: dict, corpo: str, indice: dict) -> list[str]:
    """Por que a lacuna não vale. Vazio se vale."""
    problemas = _comuns(registro)
    if registro.get("camada") != 2:
        problemas.append("lacuna é camada 2")
    if registro.get("situacao") not in SITUACOES_LACUNA:
        problemas.append(f"situacao {registro.get('situacao')!r}: a base só afirma "
                         "'nao_localizado' nas fontes indexadas")
    if not registro.get("termos_buscados"):
        problemas.append("sem termos_buscados")
    for citacao in (registro.get("remissoes") or []) + (registro.get("contexto") or []):
        problemas += problemas_do_trecho(citacao, indice)
    proprias = {indice[urn_do_artigo(str(c.get("urn")))][0].get("norma_slug")
                for c in registro.get("remissoes") or [] if urn_do_artigo(str(c.get("urn"))) in indice}
    indexadas = {meta.get("norma_slug") for meta, _ in indice.values()} - proprias
    nao_pesquisadas = sorted(indexadas - set(registro.get("pesquisado_em") or []))
    if nao_pesquisadas:
        problemas.append(f"busca desatualizada: norma(s) indexada(s) e não pesquisada(s): "
                         f"{', '.join(nao_pesquisadas)}")
    return problemas


def conflitos(regulamentacoes: list[tuple], lacunas: list[tuple]) -> list[str]:
    """A mesma remissão dada como regulada e como lacuna."""
    reguladas = {c.get("urn"): rel for rel, reg, _ in regulamentacoes
                 for c in reg.get("remissoes") or []}
    return [f"{rel}: {c.get('urn')} é lacuna e tem regulamentação em {reguladas[c.get('urn')]}"
            for rel, lac, _ in lacunas for c in lac.get("remissoes") or []
            if c.get("urn") in reguladas]


def carregar_registros(raiz: Path = RAIZ) -> dict[str, list[tuple[str, dict, str]]]:
    """{"regulamentacoes": [(caminho relativo, meta, corpo)], "lacunas": [...]}."""
    saida: dict[str, list] = {"regulamentacoes": [], "lacunas": []}
    pastas = ((raiz / DIR_INTERPRETACOES.name, "regulamentacoes"), (raiz / DIR_LACUNAS.name, "lacunas"))
    for pasta, chave in pastas:
        if not pasta.exists():
            continue
        for caminho in sorted(pasta.rglob("*.md")):
            if caminho.name.upper().startswith("README"):
                continue
            meta, corpo = ler_frontmatter(caminho)
            if chave == "lacunas" or meta.get("tipo") == TIPO_REGULAMENTACAO:
                saida[chave].append((caminho.relative_to(raiz).as_posix(), meta, corpo))
    return saida


def problemas_de_registros(registros: dict, indice: dict) -> list[str]:
    problemas = []
    for rel, meta, corpo in registros["regulamentacoes"]:
        problemas += [f"{rel}: {p}" for p in problemas_de_regulamentacao(meta, corpo, indice)]
    for rel, meta, corpo in registros["lacunas"]:
        problemas += [f"{rel}: {p}" for p in problemas_de_lacuna(meta, corpo, indice)]
    return problemas + conflitos(registros["regulamentacoes"], registros["lacunas"])

