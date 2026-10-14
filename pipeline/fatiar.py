"""Etapa 2 — fatia o texto oficial em dispositivos (um arquivo por artigo).

Granularidade deliberada: o artigo é a fronteira semântica que já existe no
documento (ver docs/MODELO-DADOS.md). Fatiar por número de tokens corta no meio
de um inciso e produz citação falsa.

O parser extrai TEXTO e ESTRUTURA. Não infere vigência nem eficácia: essas datas
vêm da cláusula de vigência da norma e exigem revisão humana. Todo dispositivo
sai marcado com `revisao_temporal_pendente: true`.

Uso:
    python3 pipeline/fatiar.py --slug lc-214-2025
    python3 pipeline/fatiar.py --todas
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml

from comum import (
    DIR_FONTES,
    DIR_NORMAS,
    MANIFEST,
    escrever_frontmatter,
    hoje,
    status_em,
    urn_dispositivo,
    urn_norma,
)
import datetime as _dt

CATALOGO = Path(__file__).resolve().parent / "fontes.yaml"

# ---------------------------------------------------------------------------
# HTML -> texto
# ---------------------------------------------------------------------------

_QUEBRA = {"p", "br", "div", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6"}
_IGNORAR = {"script", "style", "head"}


class _Extrator(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.partes: list[str] = []
        self._pular = 0

    def handle_starttag(self, tag, attrs):
        if tag in _IGNORAR:
            self._pular += 1
        elif tag in _QUEBRA:
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in _IGNORAR and self._pular:
            self._pular -= 1
        elif tag in _QUEBRA:
            self.partes.append("\n")

    def handle_data(self, dados):
        if not self._pular:
            self.partes.append(dados)

    def texto(self) -> str:
        return "".join(self.partes)


def detectar_encoding(dados: bytes) -> str:
    cabeca = dados[:4096].lower()
    m = re.search(rb'charset=["\']?\s*([a-z0-9\-_]+)', cabeca)
    if m:
        return m.group(1).decode("ascii", "ignore")
    return "utf-8"


def html_para_texto(dados: bytes) -> str:
    enc = detectar_encoding(dados)
    for tentativa in (enc, "utf-8", "cp1252", "latin-1"):
        try:
            bruto = dados.decode(tentativa)
            break
        except (UnicodeDecodeError, LookupError):
            continue
    else:  # pragma: no cover - latin-1 nunca falha
        bruto = dados.decode("latin-1", "replace")

    ex = _Extrator()
    ex.feed(bruto)
    texto = ex.texto().replace("\xa0", " ").replace("​", "")
    linhas = [re.sub(r"[ \t]+", " ", ln).strip() for ln in texto.split("\n")]
    return "\n".join(ln for ln in linhas if ln)


# ---------------------------------------------------------------------------
# Reconhecimento de estrutura
# ---------------------------------------------------------------------------

# "Art. 4º-A": o marcador ordinal vem ANTES do sufixo alfabético. Casar o
# sufixo direto após o número faria "4º-A" virar "4", colidindo com o art. 4º.
RE_ARTIGO = re.compile(r"^Art\.?\s*(\d+)\s*[ºo°]?\s*(-\s*[A-Z])?", re.IGNORECASE)
RE_ESTRUTURA = re.compile(
    r"^(LIVRO|PARTE|T[ÍI]TULO|CAP[ÍI]TULO|SE[ÇC][ÃA]O|SUBSE[ÇC][ÃA]O)\b.*", re.IGNORECASE
)
RE_ANOTACAO = re.compile(
    r"\((Reda[çc][ãa]o dada|Revogad[oa]|Inclu[íi]d[oa]|Vide|Vig[êe]ncia|"
    r"Produ[çc][ãa]o de efeito|Vetado)[^)]*\)",
    re.IGNORECASE,
)

RE_PARAGRAFO = re.compile(r"^§\s*(\d+)")
RE_PAR_UNICO = re.compile(r"^Par[áa]grafo\s+[úu]nico", re.IGNORECASE)
RE_INCISO = re.compile(r"^([IVXLC]+)\s*[-–]\s")
RE_ALINEA = re.compile(r"^([a-z])\)\s")

# Texto alterado vem entre aspas (técnica legislativa da LC 95/1998). O Planalto
# usa aspas curvas; aceitamos as retas e as angulares por segurança.
RE_ABRE_CITACAO = re.compile(r'^\s*[“"«]')
RE_FECHA_CITACAO = re.compile(r'[”"»]\s*\.?\s*$')


def chave_ordem(numero: str) -> tuple[int, str]:
    """Ordena 'Art. 4º' antes de 'Art. 4º-A' antes de 'Art. 5º'.

    Permite exigir que os artigos próprios de uma norma sejam estritamente
    crescentes, o que distingue artigo próprio de artigo citado.
    """
    base = re.match(r"\d+", numero)
    ordinal = int(base.group()) if base else 0
    sufixo = numero[numero.index("-") + 1:].upper() if "-" in numero else ""
    return (ordinal, sufixo)


# Remissões, do mais específico para o mais genérico.
RE_REMISSOES = [
    (
        "par",
        re.compile(r"§\s*(\d+)\s*[ºo°]?\s*d[oe]\s*art\.?\s*(\d+)(-[A-Z])?", re.IGNORECASE),
    ),
    (
        "inc",
        re.compile(
            r"inciso\s+([IVXLC]+)\s*d[oe]\s*art\.?\s*(\d+)(-[A-Z])?", re.IGNORECASE
        ),
    ),
    ("art", re.compile(r"\bart(?:s|igos?)?\.?\s*(\d+)(-[A-Z])?", re.IGNORECASE)),
]

RE_EXTERNA = re.compile(
    r"(Lei\s+Complementar|Emenda\s+Constitucional|Lei|Decreto|"
    r"Instru[çc][ãa]o\s+Normativa|Ajuste\s+SINIEF)\s+n[ºo°.]*\s*([\d.]+)",
    re.IGNORECASE,
)

RE_CONCEITO = re.compile(
    r"considera[- ]se\s+(.{3,60}?)\s+(?:o |a |os |as |aquele|toda|todo)", re.IGNORECASE
)


def normalizar_artigo(numero: str, sufixo: str | None) -> str:
    """'4' + '- A' -> '4-A'. Sufixo sem espaço e em caixa alta."""
    if not sufixo:
        return numero
    return f"{numero}-{sufixo.lstrip('-').strip().upper()}"


def extrair_remissoes(texto: str, urn_base: str, artigo_atual: str) -> list[str]:
    """Remissões internas resolvidas em URN. É o índice de maior retorno:
    um artigo lido isoladamente frequentemente diz o oposto do aplicável."""
    achados: list[str] = []
    consumido = texto

    for tipo, regex in RE_REMISSOES:
        for m in regex.finditer(consumido):
            if tipo == "par":
                alvo = urn_dispositivo(
                    urn_base, normalizar_artigo(m.group(2), m.group(3)), paragrafo=m.group(1)
                )
            elif tipo == "inc":
                alvo = urn_dispositivo(
                    urn_base, normalizar_artigo(m.group(2), m.group(3)), inciso=m.group(1)
                )
            else:
                alvo = urn_dispositivo(urn_base, normalizar_artigo(m.group(1), m.group(2)))
            if alvo not in achados:
                achados.append(alvo)

    proprio = urn_dispositivo(urn_base, artigo_atual)
    return [a for a in achados if not a.startswith(proprio)]


def extrair_externas(texto: str) -> list[str]:
    vistos: list[str] = []
    for m in RE_EXTERNA.finditer(texto):
        ref = f"{m.group(1)} nº {m.group(2)}"
        ref = re.sub(r"\s+", " ", ref)
        if ref not in vistos:
            vistos.append(ref)
    return vistos


def subdivisoes_de(linhas: list[str], urn_base: str, artigo: str) -> list[str]:
    """URNs das subdivisões presentes no artigo, para citação granular."""
    urns: list[str] = []
    par_atual: str | None = None
    inc_atual: str | None = None

    for linha in linhas:
        if m := RE_PARAGRAFO.match(linha):
            par_atual, inc_atual = m.group(1), None
            urns.append(urn_dispositivo(urn_base, artigo, paragrafo=par_atual))
        elif RE_PAR_UNICO.match(linha):
            par_atual, inc_atual = "U", None
            urns.append(urn_dispositivo(urn_base, artigo, paragrafo="U"))
        elif m := RE_INCISO.match(linha):
            inc_atual = m.group(1)
            urns.append(
                urn_dispositivo(urn_base, artigo, paragrafo=par_atual, inciso=inc_atual)
            )
        elif m := RE_ALINEA.match(linha):
            urns.append(
                urn_dispositivo(
                    urn_base, artigo, paragrafo=par_atual, inciso=inc_atual,
                    alinea=m.group(1),
                )
            )
    return urns


# ---------------------------------------------------------------------------
# Fatiamento
# ---------------------------------------------------------------------------

def fatiar(texto: str) -> tuple[list[dict], list[str]]:
    """Devolve (artigos, avisos). Cada artigo traz linhas e hierarquia.

    Classifica cada linha "Art. N" em duas categorias, porque tratar as duas
    como artigo próprio destrói dados:

    `proprio`  — artigo da norma sendo ingerida.
    `citado`   — artigo de OUTRA norma, reproduzido porque esta a está
                 alterando. A EC 132 insere "Art. 156-A" na Constituição; a
                 LC 214 altera artigos de outras leis nas disposições finais.
                 Esse texto pertence ao artigo que promove a alteração, não é
                 artigo da norma ingerida.

    Dois sinais distinguem, em ordem:

    1. Aspas. A técnica legislativa (LC 95/1998) exige que o texto alterado
       venha entre aspas. É o sinal mais confiável.
    2. Ordem. Os artigos próprios de uma norma são estritamente crescentes.
       "Art. 195" depois de "Art. 3º" não é o artigo 195 desta norma.
    """
    hierarquia: list[str] = []
    artigos: list[dict] = []
    avisos: list[str] = []
    atual: dict | None = None
    em_citacao = False
    ultima_chave: tuple[int, str] = (0, "")
    citados_orfaos = 0

    for linha in texto.split("\n"):
        if RE_ESTRUTURA.match(linha) and len(linha) < 200 and not em_citacao:
            marcador = linha.upper().split()[0]
            ordem = ["LIVRO", "PARTE", "TITULO", "TÍTULO", "CAPITULO", "CAPÍTULO",
                     "SECAO", "SEÇÃO", "SUBSECAO", "SUBSEÇÃO"]
            nivel = next((i for i, o in enumerate(ordem) if marcador.startswith(o[:5])), len(ordem))
            hierarquia = [h for h in hierarquia
                          if next((i for i, o in enumerate(ordem)
                                   if h.upper().startswith(o[:5])), len(ordem)) < nivel]
            hierarquia.append(linha)
            continue

        abre_citacao = bool(RE_ABRE_CITACAO.match(linha))
        dentro_de_citacao = em_citacao or abre_citacao
        if abre_citacao and not RE_FECHA_CITACAO.search(linha):
            em_citacao = True
        elif em_citacao and RE_FECHA_CITACAO.search(linha):
            em_citacao = False

        # A aspas de abertura precede o "Art.", então o reconhecimento tem de
        # ignorá-la. O texto apensado ao artigo continua sendo a linha original,
        # verbatim.
        linha_nua = linha.lstrip("“\"«' ")
        if m := RE_ARTIGO.match(linha_nua):
            numero = normalizar_artigo(m.group(1), m.group(2))
            chave = chave_ordem(numero)

            if dentro_de_citacao or chave <= ultima_chave:
                # Artigo citado: texto de outra norma, alterado por este artigo.
                if atual is not None:
                    atual["linhas"].append(linha)
                    if numero not in atual["citados"]:
                        atual["citados"].append(numero)
                else:
                    citados_orfaos += 1
                continue

            atual = {
                "numero": numero,
                "rotulo": linha.split(".")[0].strip(),
                "hierarquia": list(hierarquia),
                "linhas": [linha],
                "citados": [],
            }
            artigos.append(atual)
            ultima_chave = chave
            continue

        if atual is not None:
            atual["linhas"].append(linha)

    if not artigos:
        avisos.append(
            "nenhum artigo reconhecido — verifique se o HTML baixado e o texto "
            "da norma e nao uma pagina de erro ou indice"
        )

    if citados_orfaos:
        avisos.append(
            f"{citados_orfaos} linha(s) 'Art.' antes do primeiro artigo proprio "
            "foram descartadas (provavel cabecalho, ementa ou indice)"
        )

    # Colisão aqui significa perda de dados na escrita. É erro, não aviso.
    numeros = [a["numero"] for a in artigos]
    if len(numeros) != len(set(numeros)):
        repetidos = sorted({n for n in numeros if numeros.count(n) > 1}, key=chave_ordem)
        avisos.append(
            "ERRO artigos proprios duplicados, o que sobrescreveria arquivos: "
            + ", ".join(repetidos)
        )

    return artigos, avisos


def nome_arquivo(numero: str) -> str:
    """art-0012 / art-0012-a — zero à esquerda garante ordenação lexicográfica."""
    base = re.match(r"\d+", numero).group()
    nome = f"art-{int(base):04d}"
    if "-" in numero:
        nome += numero[numero.index("-"):].lower()
    return nome


def processar_norma(fonte: dict, manifest: dict, relatorio: bool = False) -> int:
    slug = fonte["slug"]
    chave = f"{slug}/texto_compilado"
    registro = manifest["documentos"].get(chave)
    if not registro:
        print(f"[{slug}] sem documento em fontes/manifest.json — rode baixar.py antes",
              file=sys.stderr)
        return 1

    caminho = DIR_FONTES.parent / registro["arquivo"]
    if not caminho.exists():
        print(f"[{slug}] arquivo ausente: {caminho}", file=sys.stderr)
        return 1

    texto = html_para_texto(caminho.read_bytes())
    artigos, avisos = fatiar(texto)

    erros = [a for a in avisos if a.startswith("ERRO")]
    for aviso in avisos:
        print(f"[{slug}] {'ERRO' if aviso.startswith('ERRO') else 'AVISO'}: "
              f"{aviso.removeprefix('ERRO ')}", file=sys.stderr)
    if not artigos:
        return 1
    if erros:
        # Escrever com números repetidos sobrescreveria arquivos silenciosamente.
        # Abortar preserva o dado e expõe o problema para correção.
        print(f"[{slug}] nada foi escrito — corrija o fatiamento antes de ingerir",
              file=sys.stderr)
        return 1

    proprios = len(artigos)
    citados = sum(len(a["citados"]) for a in artigos)
    if relatorio:
        faixa = f"{artigos[0]['numero']}..{artigos[-1]['numero']}"
        print(f"[{slug}] RELATORIO (nada escrito)")
        print(f"  artigos proprios: {proprios}  (faixa {faixa})")
        print(f"  artigos citados de outras normas: {citados}")
        com_citacao = [a for a in artigos if a["citados"]]
        print(f"  artigos que alteram outras normas: {len(com_citacao)}")
        for a in com_citacao[:12]:
            amostra = ", ".join(a["citados"][:8])
            extra = f" (+{len(a['citados']) - 8})" if len(a["citados"]) > 8 else ""
            print(f"    art. {a['numero']} cita: {amostra}{extra}")
        return 0

    base = urn_norma(fonte["autoridade"], fonte["data"], fonte["numero"])
    publicacao = fonte["data"]
    referencia = _dt.date.today()
    destino_dir = DIR_NORMAS / slug

    # Remove o resultado de execuções anteriores. Sem isso, um fatiamento que
    # antes produzia artigos espúrios deixa esses arquivos para trás, e a base
    # passa a conter dispositivos que a norma não tem.
    if destino_dir.exists():
        antigos = list(destino_dir.glob("art-*.md"))
        for arquivo in antigos:
            arquivo.unlink()
        if antigos:
            print(f"[{slug}] {len(antigos)} arquivo(s) da ingestao anterior removidos")
    destino_dir.mkdir(parents=True, exist_ok=True)

    for artigo in artigos:
        corpo_linhas = artigo["linhas"]
        corpo = "\n\n".join(corpo_linhas)
        # group(0): a anotação inteira. findall() devolveria só o grupo de
        # captura ("Redação dada"), perdendo a norma que promoveu a alteração.
        anotacoes = [re.sub(r"\s+", " ", m.group(0)) for m in RE_ANOTACAO.finditer(corpo)]
        conceitos = [c.strip() for c in RE_CONCEITO.findall(corpo)]

        meta = {
            "urn": urn_dispositivo(base, artigo["numero"]),
            "norma": fonte["titulo"],
            "norma_slug": slug,
            "dispositivo": f"art. {artigo['numero']}",
            "camada": 1,
            "hierarquia": artigo["hierarquia"],
            "publicacao": publicacao,
            # Datas provisórias — iguais à publicação até revisão humana da
            # cláusula de vigência. Ver revisao_temporal_pendente.
            "vigencia_inicio": publicacao,
            "vigencia_fim": None,
            "efeitos_inicio": publicacao,
            "efeitos_fim": None,
            "status": None,
            "fonte": {
                "url": registro["url"],
                "tipo": registro["tipo_documento"],
                "acesso": registro["acesso"],
                "sha256": registro["sha256"],
            },
            "ingerido_em": hoje(),
            "remete_a": extrair_remissoes(corpo, base, artigo["numero"]),
            "remete_a_externo": extrair_externas(corpo),
            "subdivisoes": subdivisoes_de(corpo_linhas, base, artigo["numero"]),
            "anotacoes_oficiais": anotacoes,
            "conceitos_definidos": conceitos,
            # Artigos de OUTRAS normas reproduzidos aqui porque este artigo as
            # altera. Não são dispositivos desta norma.
            "dispositivos_citados": artigo["citados"],
            "altera": [],
            "alterado_por": [],
            "extracao": "automatica",
            "revisao_temporal_pendente": True,
            "revisado_por": None,
            "revisado_em": None,
        }
        meta["status"] = status_em(meta, referencia)

        escrever_frontmatter(destino_dir / f"{nome_arquivo(artigo['numero'])}.md", meta, corpo)

    print(f"[{slug}] {proprios} artigos proprios escritos em "
          f"{destino_dir.relative_to(DIR_NORMAS.parent)} "
          f"(faixa {artigos[0]['numero']}..{artigos[-1]['numero']})")
    print(f"[{slug}] {citados} artigo(s) de outras normas tratados como texto "
          "alterado, nao como dispositivo proprio")
    print(f"[{slug}] ATENCAO: {proprios} dispositivos com revisao_temporal_pendente")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", help="fatiar apenas esta norma")
    ap.add_argument("--todas", action="store_true", help="fatiar tudo que foi baixado")
    ap.add_argument(
        "--relatorio",
        action="store_true",
        help="mostra a classificacao proprio/citado sem escrever nada — use para "
        "auditar o fatiamento antes de confiar nele",
    )
    args = ap.parse_args()

    if not args.slug and not args.todas:
        ap.error("informe --slug ou --todas")

    if not MANIFEST.exists():
        print("fontes/manifest.json inexistente — rode pipeline/baixar.py antes",
              file=sys.stderr)
        return 2

    catalogo = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    fontes = catalogo.get("fontes") or []
    if args.slug:
        fontes = [f for f in fontes if f["slug"] == args.slug]
        if not fontes:
            print(f"slug '{args.slug}' nao esta em fontes.yaml", file=sys.stderr)
            return 2

    return min(1, sum(processar_norma(f, manifest, args.relatorio) for f in fontes))


if __name__ == "__main__":
    raise SystemExit(main())
