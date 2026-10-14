"""Etapa 2 — fatia o texto oficial em dispositivos (um arquivo por artigo).

Granularidade deliberada: o artigo é a fronteira semântica que já existe no
documento (ver docs/MODELO-DADOS.md). Fatiar por número de tokens corta no meio
de um inciso e produz citação falsa.

O parser extrai TEXTO e ESTRUTURA. Não infere vigência nem eficácia: essas datas
vêm da cláusula de vigência da norma e exigem revisão humana. Todo dispositivo
sai marcado com `revisao_temporal_pendente: true`.

Uso:
    python pipeline/fatiar.py --slug lc-214-2025
    python pipeline/fatiar.py --todas
    python pipeline/fatiar.py --todas --relatorio     # não escreve nada
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from typing import NamedTuple

import yaml

from comum import (
    DIR_NORMAS,
    DIR_TEMPORAL,
    MANIFEST,
    caminho_fonte,
    escrever_frontmatter,
    hoje,
    status_em,
    urn_dispositivo,
    urn_norma,
)
import datetime as _dt

from revisao_temporal import aplicar_revisao, carregar_revisoes, ordenar_meta

CATALOGO = Path(__file__).resolve().parent / "fontes.yaml"

# ---------------------------------------------------------------------------
# HTML -> texto
# ---------------------------------------------------------------------------

# Só estas tags terminam uma linha. A quebra de linha do CÓDIGO-FONTE do HTML não
# é quebra de parágrafo: o portal quebra o código no meio da frase, e tratá-la
# como quebra deixava "arts. 156-A e 195, V" ou "art. 195, I, ..." no início de
# uma linha, onde o parser os lia como início de artigo.
_QUEBRA = {"p", "br", "div", "tr", "li", "blockquote", "h1", "h2", "h3", "h4", "h5", "h6"}
_CELULA = {"td", "th"}
_IGNORAR = {"script", "style", "head"}
_VAZIAS = {"br", "img", "hr", "meta", "link", "input"}
# O portal marca texto superado de duas formas, as duas presentes no mesmo
# documento (LC 214): <span style="...text-decoration:line-through"> e <strike>.
_TAGS_RISCO = {"s", "strike", "del"}

_RE_ESPACOS = re.compile(r"\s+")
_ZERO_LARGURA = dict.fromkeys(map(ord, "​﻿"), None)

MARCA_RISCADO = "~~"


class Linha(NamedTuple):
    """Uma linha lógica do documento (um parágrafo), em três leituras.

    completa    tudo que o portal publicou, inclusive o texto riscado. Serve ao
                reconhecimento de estrutura: cabeçalho de artigo, aspas.
    vigente     sem os trechos riscados (texto superado ou revogado). É a base de
                todos os metadados: remissões, conceitos, subdivisões, anotações.
    marcada     o texto riscado entre `~~ ~~`. É o que vai para o corpo do
                arquivo: nada que o portal mostra se perde, e a anotação
                "(Revogado pela ...)" continua colada ao trecho que ela revoga.
                Descartar o riscado a deixaria solta no corpo do artigo, que
                passaria a parecer revogado por inteiro.
    blockquote  o parágrafo está dentro de <blockquote>? None = não se sabe.
    """

    completa: str
    vigente: str
    marcada: str
    blockquote: bool | None = None


def _normalizar(texto: str) -> str:
    return _RE_ESPACOS.sub(" ", texto).strip()


def _riscado(tag: str, attrs) -> bool:
    if tag in _TAGS_RISCO:
        return True
    estilo = dict(attrs).get("style") or ""
    return "line-through" in _RE_ESPACOS.sub("", estilo).lower()


def _marcar(segmentos: list[tuple[str, bool]]) -> str:
    """Junta os segmentos envolvendo cada trecho riscado em `~~ ~~`.

    Espaço em branco não tem estado: vai para o trecho em curso, de modo que dois
    pedaços riscados separados só por espaço formam um trecho só.
    """
    trechos: list[list] = []  # [texto, riscado]
    for texto, riscado in segmentos:
        if trechos and (trechos[-1][1] == riscado or not texto.strip()):
            trechos[-1][0] += texto
        else:
            trechos.append([texto, riscado])

    saida: list[str] = []
    for texto, riscado in trechos:
        miolo = texto.strip()
        if riscado and miolo:
            ini = texto[: len(texto) - len(texto.lstrip())]
            fim = texto[len(texto.rstrip()):]
            saida.append(f"{ini}{MARCA_RISCADO}{miolo}{MARCA_RISCADO}{fim}")
        else:
            saida.append(texto)
    return "".join(saida)


class _Extrator(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.linhas: list[Linha] = []
        self._pilha: list[tuple[str, bool]] = []
        self._pular = 0
        self._blockquote = 0
        self._segmentos: list[tuple[str, bool]] = []
        self._bq_na_linha = False

    def handle_starttag(self, tag, attrs):
        if tag in _IGNORAR:
            self._pular += 1
            return
        if self._pular:
            return
        if tag in _QUEBRA:
            self._fechar_linha()
        if tag == "blockquote":
            self._blockquote += 1
        if tag not in _VAZIAS:
            self._pilha.append((tag, _riscado(tag, attrs)))

    def handle_endtag(self, tag):
        if tag in _IGNORAR:
            if self._pular:
                self._pular -= 1
            return
        if self._pular:
            return
        if tag in _QUEBRA:
            self._fechar_linha()
        if tag == "blockquote" and self._blockquote:
            self._blockquote -= 1
        if tag in _CELULA:
            self._segmentos.append((" ", False))
        # HTML do Word deixa tags sem fechar: fecha tudo que estava aberto dentro
        # da tag que se fecha, para que um riscado esquecido não vaze adiante.
        for i in range(len(self._pilha) - 1, -1, -1):
            if self._pilha[i][0] == tag:
                del self._pilha[i:]
                break

    def handle_data(self, dados):
        if self._pular:
            return
        dados = dados.replace("\xa0", " ").translate(_ZERO_LARGURA)
        if not dados:
            return
        if not self._segmentos:
            self._bq_na_linha = self._blockquote > 0
        self._segmentos.append((dados, any(r for _, r in self._pilha)))

    def _fechar_linha(self) -> None:
        segmentos, self._segmentos = self._segmentos, []
        completa = _normalizar("".join(t for t, _ in segmentos))
        if not completa:
            return
        vigente = _normalizar("".join(t for t, r in segmentos if not r))
        self.linhas.append(
            Linha(completa, vigente, _normalizar(_marcar(segmentos)), self._bq_na_linha)
        )

    def concluir(self) -> list[Linha]:
        self.close()
        self._fechar_linha()
        return self.linhas


def detectar_encoding(dados: bytes) -> str:
    cabeca = dados[:4096].lower()
    m = re.search(rb'charset=["\']?\s*([a-z0-9\-_]+)', cabeca)
    if m:
        return m.group(1).decode("ascii", "ignore")
    return "utf-8"


def _decodificar(dados: bytes) -> str:
    """O charset declarado não é confiável: a LC 214 não declara nenhum, os bytes
    são windows-1252, e o padrão utf-8 falha no decode estrito."""
    enc = detectar_encoding(dados)
    for tentativa in (enc, "utf-8", "cp1252", "latin-1"):
        try:
            return dados.decode(tentativa)
        except (UnicodeDecodeError, LookupError):
            continue
    return dados.decode("latin-1", "replace")  # pragma: no cover - latin-1 nunca falha


def html_para_linhas(dados: bytes) -> list[Linha]:
    ex = _Extrator()
    ex.feed(_decodificar(dados))
    return ex.concluir()


def html_para_texto(dados: bytes) -> str:
    """Texto corrido, inclusive o trecho riscado (a leitura `completa`)."""
    return "\n".join(ln.completa for ln in html_para_linhas(dados))


# ---------------------------------------------------------------------------
# Datas de referência, lidas do original
# ---------------------------------------------------------------------------

def _sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if not unicodedata.combining(c))


_NUM_MES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto",
     "setembro", "outubro", "novembro", "dezembro"], 1)}

RE_TITULO = re.compile(
    r"^(?:EMENDA CONSTITUCIONAL|LEI COMPLEMENTAR|LEI|DECRETO)\b.*?\bDE (\d{1,2})[ºO°]? DE "
    r"([A-ZÇÃÉÊ]+) DE (\d{4})\s*$"
)
RE_ASSINATURA = re.compile(r"^Bras[ií]lia,\s+(?:em\s+)?(\d{1,2})\s*[ºo°]?\s+de\s+(\w+)\s+de\s+(\d{4})")
RE_DOU = re.compile(r"publicado\s+no\s+DOU\s+(?:de\s+)?(\d{1,2})\.(\d{1,2})\.(\d{4})")


def _iso(dia: str, mes: str | int, ano: str) -> str | None:
    if isinstance(mes, str):
        mes = int(mes) if mes.isdigit() else _NUM_MES.get(_sem_acento(mes).lower())
    if not mes:
        return None
    return f"{int(ano):04d}-{int(mes):02d}-{int(dia):02d}"


def extrair_referencias(linhas_fonte: list[str]) -> dict:
    """Data do ato (título e linha de assinatura) e publicação no DOU (rodapé do
    compilado), cada uma com o trecho literal. O que não se acha fica nulo."""
    fontes = []
    for linha in linhas_fonte[:40]:
        if m := RE_TITULO.match(linha):
            if iso := _iso(m.group(1), m.group(2), m.group(3)):
                fontes.append({"origem": "titulo", "valor": iso, "trecho": linha})
                break
    for linha in linhas_fonte:
        if m := RE_ASSINATURA.match(linha):
            if iso := _iso(m.group(1), m.group(2), m.group(3)):
                fontes.append({"origem": "assinatura", "valor": iso, "trecho": linha})
                break
    valores = {f["valor"] for f in fontes}
    ato = {
        "valor": fontes[0]["valor"] if fontes else None,
        "fontes": fontes,
        "concordam": (len(valores) == 1) if len(fontes) > 1 else None,
    }

    # A publicação da norma é a do PRIMEIRO rodapé. O compilado pode trazer, depois
    # dos anexos, outro ato com assinatura e rodapé próprios (LC 214: "Brasília,
    # 1º de julho de 2025" e "DOU de 2.7.2025"). Esse rodapé não é a publicação da
    # norma, mas também não pode sumir: o outro ato pode ter vigência própria.
    rodapes, assinatura = [], None
    for linha in linhas_fonte:
        if RE_ASSINATURA.match(linha):
            assinatura = linha
        achados = [a for a in (_iso(d, mes, ano) for d, mes, ano in RE_DOU.findall(linha)) if a]
        if achados:
            rodapes.append({"assinatura": assinatura, "trecho": linha, "valores": achados})
    principal = rodapes[0] if rodapes else None
    return {
        "data_do_ato": ato,
        "publicacao_dou": {"valores": principal["valores"] if principal else [],
                           "trechos": [principal["trecho"]] if principal else []},
        "rodapes_adicionais": rodapes[1:],
    }



# ---------------------------------------------------------------------------
# Reconhecimento de estrutura
# ---------------------------------------------------------------------------

# "Art. 4º-A": o marcador ordinal vem ANTES do sufixo alfabético. Casar o
# sufixo direto após o número faria "4º-A" virar "4", colidindo com o art. 4º.
#
# Sem IGNORECASE: o portal publica todo cabeçalho como "Art." maiúsculo, e uma
# remissão em minúscula que cai no início de linha ("art. 195, I, ...") não é
# cabeçalho. Defesa em profundidade além da extração, que já não quebra linha
# no meio do parágrafo.
RE_ARTIGO = re.compile(r"^Art\.?\s*(\d+)\s*[ºo°]?\s*(-\s*[A-Z])?")
RE_ESTRUTURA = re.compile(
    r"^(LIVRO|PARTE|T[ÍI]TULO|CAP[ÍI]TULO|SE[ÇC][ÃA]O|SUBSE[ÇC][ÃA]O)\b.*", re.IGNORECASE
)
RE_ANOTACAO = re.compile(
    r"\((Reda[çc][ãa]o dada|Revogad[oa]|Inclu[íi]d[oa]|Vide|Vig[êe]ncia|"
    r"Produ[çc][ãa]o de efeito|Vetad[oa]|Promulga[çc][ãa]o)[^)]*\)",
    re.IGNORECASE,
)

# Fim do texto da norma. Depois do último artigo vêm o local e a data da
# assinatura ("Brasília, 16 de janeiro de 2025; ..."), os signatários, o rodapé e,
# na LC 214, os anexos. Nada disso é do último artigo; anexado a ele, o art. 544
# da LC 214 virava um arquivo de 97 KB. Os dois documentos reais terminam assim.
RE_FIM_DO_TEXTO = re.compile(r"^(?:Bras[ií]lia,\s|ANEXO\b)")
RE_ANEXO = re.compile(r"^ANEXO\s+[IVXLC]+\b")

RE_PARAGRAFO = re.compile(r"^§\s*(\d+)")
RE_PAR_UNICO = re.compile(r"^Par[áa]grafo\s+[úu]nico", re.IGNORECASE)
RE_INCISO = re.compile(r"^([IVXLC]+)\s*[-–]\s")
RE_ALINEA = re.compile(r"^([a-z])\)\s")

# Texto alterado vem entre aspas (técnica legislativa da LC 95/1998). O que o
# portal publica, medido nos HTML reais, NÃO é uniforme:
#   - a EC 132 usa aspas RETAS (&quot;), a LC 214 usa aspas CURVAS (“ ”);
#   - o bloco tem UM par de aspas, mesmo inserindo vários artigos: só o primeiro
#     abre aspas (o "Art. 156-B" seguinte vem sem aspa de abertura);
#   - o fechamento vem como `” (NR)` — a aspa NÃO está no fim da linha;
#   - há aspas internas ("a", "b") no meio do bloco, às vezes no fim da linha;
#   - a fonte tem erros: um ” sem abertura, e ’ onde devia haver ”.
# Por isso o sinal não é "a linha começa/termina com aspa" e sim o BALANÇO de
# aspas desde o início do documento.
ABRE_ASPAS = "“«"   # “ «
FECHA_ASPAS = "”»"  # ” »
ASPA_RETA = '"'


class _Aspas:
    """Balanço de aspas, linha a linha.

    Aspas curvas têm direção, então contam-se por profundidade. A aspa reta é a
    mesma para abrir e fechar, então conta-se por paridade: as internas ("a")
    vêm em par e não alteram a paridade do bloco que as contém.

    A aspa simples tipográfica (’) é ignorada: a fonte a usa por engano no lugar
    de ” (LC 214), e o bloco continua depois dela.
    """

    def __init__(self) -> None:
        self.profundidade = 0
        self.paridade = 0
        self.fechamentos_sem_abertura = 0

    @property
    def dentro(self) -> bool:
        return self.profundidade > 0 or self.paridade == 1

    @property
    def residuo(self) -> int:
        """0 = balanceado. Diferente de 0 ao fim do documento = bloco que nunca fechou."""
        return self.profundidade + self.paridade

    def abre_bloco(self, texto: str) -> bool:
        """A linha ABRE bloco: começa por aspa de abertura. A aspa reta só abre
        quando a paridade diz que se está fora; dentro de bloco ela é interna."""
        if not texto:
            return False
        return texto[0] in ABRE_ASPAS or (texto[0] == ASPA_RETA and self.paridade == 0)

    def consumir(self, texto: str) -> None:
        for c in texto:
            if c in ABRE_ASPAS:
                self.profundidade += 1
            elif c in FECHA_ASPAS:
                # Piso em zero: um ” solto não pode tornar a profundidade negativa
                # e contaminar os artigos seguintes. Fica contado, para reporte.
                if self.profundidade:
                    self.profundidade -= 1
                else:
                    self.fechamentos_sem_abertura += 1
            elif c == ASPA_RETA:
                self.paridade ^= 1


def chave_ordem(numero: str) -> tuple[int, str]:
    """Ordena 'Art. 4º' antes de 'Art. 4º-A' antes de 'Art. 5º'.

    Os artigos próprios de uma norma são estritamente crescentes. Isso é uma
    VALIDAÇÃO do fatiamento, não um critério de classificação: usada como
    critério, um único falso positivo alto fixava o piso lá em cima e todo o
    resto do documento passava a ser lido como "citado", em silêncio.
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

# Escopo da remissão. "art. 155, II, da Constituição Federal" NÃO é o art. 155
# desta norma — resolver para o namespace próprio cria ponteiro ERRADO, que é
# pior que ponteiro ausente: a IA seguiria a remissão para o dispositivo errado
# e responderia com confiança. Por isso a resolução é conservadora.
RE_ESCOPO_EXTERNO = re.compile(
    r"\bd[ao]s?\s+(?:Constitui[çc][ãa]o|Leis?|Decretos?|Emenda|"
    r"Medida\s+Provis[óo]ria|C[óo]digo|Ato|ADCT)\b",
    re.IGNORECASE,
)
# "desta Lei" / "deste Decreto" afirmam o contrário: a remissão é interna.
RE_ESCOPO_INTERNO = re.compile(
    r"\bdest[ae]\s+(?:Lei|Emenda|Decreto|Constitui[çc][ãa]o)\b", re.IGNORECASE
)

RE_CONCEITO = re.compile(
    r"considera[- ]se\s+(.{3,60}?)\s+(?:o |a |os |as |aquele|toda|todo)", re.IGNORECASE
)

# Normas citadas pelo nome, registradas como texto para resolução posterior.
RE_EXTERNA = re.compile(
    r"(Lei\s+Complementar|Emenda\s+Constitucional|Lei|Decreto|"
    r"Instru[çc][ãa]o\s+Normativa|Ajuste\s+SINIEF)\s+n[ºo°.]*\s*([\d.]+)",
    re.IGNORECASE,
)


def normalizar_artigo(numero: str, sufixo: str | None) -> str:
    """'4' + '- A' -> '4-A'. Sufixo sem espaço e em caixa alta."""
    if not sufixo:
        return numero
    return f"{numero}-{sufixo.lstrip('-').strip().upper()}"


def remissao_externa(texto: str, fim: int) -> bool:
    """A remissão que termina em `fim` aponta para outra norma?

    O qualificador de escopo liga-se à menção MAIS PRÓXIMA, então a janela
    termina na próxima menção de artigo. Sem esse corte, um "da Lei nº X" no
    fim da frase contamina todas as remissões internas que o precedem: em
    "o art. 12 e o art. 15 da Lei nº 9.430" só o art. 15 é externo.

    "desta Lei" vence "da Lei", porque afirma escopo interno explicitamente.
    """
    janela = _janela_da_mencao(texto, fim)
    if RE_ESCOPO_INTERNO.search(janela):
        return False
    return bool(RE_ESCOPO_EXTERNO.search(janela))


def _janela_da_mencao(texto: str, fim: int) -> str:
    janela = texto[fim:fim + 90]
    corte = re.search(r"[.;:]|\bart", janela, re.IGNORECASE)
    return janela[:corte.start()] if corte else janela


def escopo_interno_afirmado(texto: str, fim: int) -> bool:
    """A remissão que termina em `fim` diz expressamente "desta Lei/Emenda"?"""
    return bool(RE_ESCOPO_INTERNO.search(_janela_da_mencao(texto, fim)))


def exige_escopo_interno(fonte: dict) -> bool:
    """Numa emenda constitucional, "art. N" sem qualificador é, quase sempre, da
    Constituição que ela altera — não da própria emenda. Medido na EC 132: das
    remissões que o padrão "interno salvo qualificador externo" resolvia, 8 de 20
    apontavam para artigos que a emenda não tem, todas referências à
    Constituição. Nessas normas, só se resolve o que é afirmado interno.

    Nas leis, o padrão continua "interno salvo qualificador externo". Essa é uma
    decisão de política em aberto (ver docs/ESTADO.md): mais de metade das
    menções na LC 214 não têm qualificador algum.
    """
    return fonte.get("tipo") == "emenda.constitucional"


def extrair_remissoes(
    texto: str,
    urn_base: str,
    artigo_atual: str,
    exigir_escopo_interno: bool = False,
) -> list[str]:
    """Remissões INTERNAS resolvidas em URN. É o índice de maior retorno: um
    artigo lido isoladamente frequentemente diz o oposto do aplicável.

    Recebe apenas o texto próprio do artigo — nunca o texto citado de outra
    norma que ele altere, cujas remissões pertencem àquela norma.

    Com `exigir_escopo_interno`, só resolve a remissão que afirma "desta Emenda"
    e semelhantes; a sem qualificador fica sem ponteiro. Ponteiro ausente falha
    seguro; ponteiro errado leva ao dispositivo equivocado.
    """
    achados: list[str] = []
    consumido = texto

    for tipo, regex in RE_REMISSOES:
        for m in regex.finditer(consumido):
            if remissao_externa(consumido, m.end()):
                continue
            if exigir_escopo_interno and not escopo_interno_afirmado(consumido, m.end()):
                continue
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

    # Auto-remissão é o próprio artigo ou uma subdivisão dele ("art1", "art1_par2").
    # Comparar por prefixo de texto descartava também "art10", "art158": o art. 1
    # perdia toda remissão aos artigos 10-19, 100-199 etc.
    proprio = urn_dispositivo(urn_base, artigo_atual)
    return [a for a in achados if a != proprio and not a.startswith(f"{proprio}_")]


def extrair_externas(texto: str) -> list[str]:
    vistos: list[str] = []
    for m in RE_EXTERNA.finditer(texto):
        ref = f"{m.group(1)} nº {m.group(2)}"
        ref = re.sub(r"\s+", " ", ref)
        if ref not in vistos:
            vistos.append(ref)
    return vistos


def _subdivisao_aberta_por_linha(
    linhas: list[str], urn_base: str, artigo: str
) -> list[str | None]:
    """URN da subdivisão que cada linha ABRE; None se a linha não tem rótulo."""
    saida: list[str | None] = []
    par_atual: str | None = None
    inc_atual: str | None = None

    for linha in linhas:
        urn: str | None = None
        if m := RE_PARAGRAFO.match(linha):
            par_atual, inc_atual = m.group(1), None
            urn = urn_dispositivo(urn_base, artigo, paragrafo=par_atual)
        elif RE_PAR_UNICO.match(linha):
            par_atual, inc_atual = "U", None
            urn = urn_dispositivo(urn_base, artigo, paragrafo="U")
        elif m := RE_INCISO.match(linha):
            inc_atual = m.group(1)
            urn = urn_dispositivo(urn_base, artigo, paragrafo=par_atual, inciso=inc_atual)
        elif m := RE_ALINEA.match(linha):
            urn = urn_dispositivo(
                urn_base, artigo, paragrafo=par_atual, inciso=inc_atual, alinea=m.group(1)
            )
        saida.append(urn)
    return saida


def subdivisoes_de(linhas: list[str], urn_base: str, artigo: str) -> list[str]:
    """URNs das subdivisões presentes no artigo, para citação granular."""
    return [u for u in _subdivisao_aberta_por_linha(linhas, urn_base, artigo) if u]


def subdivisao_por_linha(linhas: list[str], urn_base: str, artigo: str) -> list[str]:
    """URN da subdivisão a que cada linha pertence: a da última linha rotulada, ou
    a do próprio artigo enquanto não houver rótulo. É o `fundamento` de um trecho."""
    atual = urn_dispositivo(urn_base, artigo)
    saida: list[str] = []
    for urn in _subdivisao_aberta_por_linha(linhas, urn_base, artigo):
        atual = urn or atual
        saida.append(atual)
    return saida


def linhas_citadas(linhas: list[str]) -> list[bool]:
    """Para as linhas do CORPO de um dispositivo, quais são texto de outra norma.

    Mesmo balanço de aspas do fatiamento. O corpo guarda o texto riscado entre
    `~~ ~~`, então a marca precisa sair antes de olhar o primeiro caractere: um
    bloco citado riscado começa com `~~“`.
    """
    aspas = _Aspas()
    saida: list[bool] = []
    for linha in linhas:
        nua = linha.lstrip("~")
        saida.append(aspas.dentro or aspas.abre_bloco(nua))
        aspas.consumir(nua)
    return saida


# ---------------------------------------------------------------------------
# Fatiamento
# ---------------------------------------------------------------------------

_NIVEIS = ["LIVRO", "PARTE", "TITULO", "TÍTULO", "CAPITULO", "CAPÍTULO",
           "SECAO", "SEÇÃO", "SUBSECAO", "SUBSEÇÃO"]


def _atualizar_hierarquia(hierarquia: list[str], linha: str) -> list[str]:
    marcador = linha.upper().split()[0]
    nivel = next((i for i, o in enumerate(_NIVEIS) if marcador.startswith(o[:5])), len(_NIVEIS))
    mantidos = [h for h in hierarquia
                if next((i for i, o in enumerate(_NIVEIS)
                         if h.upper().startswith(o[:5])), len(_NIVEIS)) < nivel]
    mantidos.append(linha)
    return mantidos


def _como_linhas(entrada: str | list[Linha]) -> list[Linha]:
    if isinstance(entrada, str):
        return [Linha(ln, ln, ln) for ln in entrada.split("\n") if ln.strip()]
    return entrada


def _so_riscado(linha: Linha) -> bool:
    """Tudo na linha está riscado, salvo as anotações oficiais."""
    return linha.vigente != linha.completa and not RE_ANOTACAO.sub("", linha.vigente).strip()


def _novo_artigo(numero: str, hierarquia: list[str]) -> dict:
    return {
        "numero": numero,
        "hierarquia": list(hierarquia),
        # Corpo do arquivo: tudo que o portal mostra, o riscado entre ~~ ~~.
        "linhas": [],
        # Sem o riscado, incluindo o texto citado. Base das anotações oficiais e
        # das normas externas mencionadas.
        "linhas_vigentes": [],
        # Sem o riscado e sem o texto citado de outra norma. Base das remissões,
        # dos conceitos e das subdivisões: as que aparecem no texto citado
        # pertencem à norma alterada, e as do texto riscado não valem mais.
        "linhas_proprias": [],
        "citados": [],
        # O cabeçalho mais recente está riscado: é redação superada, e um
        # cabeçalho de mesmo número logo a seguir é a redação que a substitui.
        "cabecalho_riscado": False,
    }


def _anexar(artigo: dict, linha: Linha, proprio: bool) -> None:
    artigo["linhas"].append(linha.marcada)
    if linha.vigente:
        artigo["linhas_vigentes"].append(linha.vigente)
        if proprio:
            artigo["linhas_proprias"].append(linha.vigente)


def fatiar(entrada: str | list[Linha]) -> tuple[list[dict], list[str], dict]:
    """Devolve (artigos, avisos, estatisticas). Cada artigo traz linhas e hierarquia.

    Classifica cada linha "Art. N" em duas categorias, porque tratar as duas
    como artigo próprio destrói dados:

    `proprio`  — artigo da norma sendo ingerida.
    `citado`   — artigo de OUTRA norma, reproduzido porque esta a está
                 alterando. A EC 132 insere "Art. 156-A" na Constituição; a
                 LC 214 altera artigos de outras leis nas disposições finais.
                 Esse texto pertence ao artigo que promove a alteração, não é
                 artigo da norma ingerida.

    O critério é o BALANÇO de aspas (ver `_Aspas`): o artigo é citado se, ao
    início da linha, há bloco aberto, ou se a própria linha o abre. Dois
    portais, dois formatos de aspas, e um bloco que insere vários artigos tem um
    par só — por isso nem "a linha começa com aspa" nem "termina com aspa"
    servem de critério.

    A numeração estritamente crescente dos artigos próprios é VALIDAÇÃO, não
    critério: o que a violar vira ERRO e a escrita é abortada. Como critério,
    um falso positivo alto fixava o piso lá em cima e todo o resto do documento
    virava "citado" em silêncio.

    Texto riscado (superado) é mantido no corpo, marcado, e excluído dos
    metadados. Um cabeçalho riscado seguido de cabeçalho de mesmo número é a
    redação anterior do mesmo dispositivo: os dois se fundem num artigo só, em
    vez de colidir. Dois cabeçalhos de mesmo número SEM riscado continuam sendo
    colisão, e aborta.

    `estatisticas` são contagens para o relatório, não critério de nada.
    """
    linhas = _como_linhas(entrada)
    hierarquia: list[str] = []
    artigos: list[dict] = []
    avisos: list[str] = []
    atual: dict | None = None
    aspas = _Aspas()
    citados_orfaos = 0
    discordantes: list[str] = []
    stats = {
        "aspas_fechamento_sem_abertura": 0,
        "aspas_abertura_dentro_de_bloco": 0,
        "aspas_estado_final": 0,
        "discordancia_blockquote": 0,
        "linhas_com_riscado": 0,
        "redacoes_anteriores_mescladas": 0,
        "linhas_apos_o_fim": 0,
        "anexos_nao_incorporados": 0,
    }
    fim_do_texto = False

    for linha in linhas:
        completa = linha.completa
        if fim_do_texto:
            stats["linhas_apos_o_fim"] += 1
            if RE_ANEXO.match(completa):
                stats["anexos_nao_incorporados"] += 1
            continue
        if linha.vigente != completa:
            stats["linhas_com_riscado"] += 1

        dentro_antes = aspas.dentro
        abre = aspas.abre_bloco(completa)
        dentro = dentro_antes or abre
        aspas.consumir(completa)

        # Só encerra fora de bloco citado: as leis que esta norma altera também
        # podem ter anexos.
        if atual is not None and not dentro and RE_FIM_DO_TEXTO.match(completa):
            fim_do_texto = True
            stats["linhas_apos_o_fim"] += 1
            if RE_ANEXO.match(completa):
                stats["anexos_nao_incorporados"] += 1
            continue

        if RE_ESTRUTURA.match(completa) and len(completa) < 200 and not dentro_antes:
            if linha.vigente:  # estrutura inteiramente riscada foi superada pelo portal
                hierarquia = _atualizar_hierarquia(hierarquia, linha.vigente)
            continue

        # A aspa de abertura precede o "Art.", então o reconhecimento tem de
        # ignorá-la. O texto apensado ao artigo continua sendo a linha original,
        # verbatim.
        m = RE_ARTIGO.match(completa.lstrip(ABRE_ASPAS + ASPA_RETA + "' "))
        if m:
            numero = normalizar_artigo(m.group(1), m.group(2))

            if abre and dentro_antes:
                stats["aspas_abertura_dentro_de_bloco"] += 1
            # Verificação cruzada: o portal marca texto citado também por
            # <blockquote>. Os dois sinais são independentes; se discordam, é dado
            # a reportar, e não motivo para escolher um deles em silêncio.
            if linha.blockquote is not None and linha.blockquote != dentro:
                stats["discordancia_blockquote"] += 1
                discordantes.append(numero)

            if dentro:
                # Artigo citado: texto de outra norma, alterado por este artigo.
                if atual is not None:
                    _anexar(atual, linha, proprio=False)
                    if numero not in atual["citados"]:
                        atual["citados"].append(numero)
                else:
                    citados_orfaos += 1
                continue

            if atual is not None and atual["numero"] == numero and atual["cabecalho_riscado"]:
                stats["redacoes_anteriores_mescladas"] += 1
            else:
                atual = _novo_artigo(numero, hierarquia)
                artigos.append(atual)
            atual["cabecalho_riscado"] = _so_riscado(linha)
            _anexar(atual, linha, proprio=True)
            continue

        if atual is not None:
            _anexar(atual, linha, proprio=not dentro)

    stats["aspas_fechamento_sem_abertura"] = aspas.fechamentos_sem_abertura
    stats["aspas_estado_final"] = aspas.residuo

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

    # Anomalias do documento: reportadas, nunca corrigidas em silêncio.
    if aspas.residuo:
        avisos.append(
            "bloco de aspas ficou aberto ate o fim do documento — o que veio "
            "depois dele pode ter sido lido como texto citado"
        )
    if aspas.fechamentos_sem_abertura:
        avisos.append(
            f"{aspas.fechamentos_sem_abertura} aspa(s) de fechamento sem abertura "
            "na fonte — ignoradas"
        )
    if stats["aspas_abertura_dentro_de_bloco"]:
        avisos.append(
            f"{stats['aspas_abertura_dentro_de_bloco']} bloco(s) abrem dentro de outro "
            "bloco — possivel fechamento perdido"
        )
    if discordantes:
        avisos.append(
            f"aspas e <blockquote> discordam em {len(discordantes)} cabecalho(s): "
            + ", ".join(discordantes[:10])
            + " — a classificacao seguiu as aspas"
        )

    # Colisão aqui significa perda de dados na escrita. É erro, não aviso.
    numeros = [a["numero"] for a in artigos]
    if len(numeros) != len(set(numeros)):
        repetidos = sorted({n for n in numeros if numeros.count(n) > 1}, key=chave_ordem)
        avisos.append(
            "ERRO artigos proprios duplicados, o que sobrescreveria arquivos: "
            + ", ".join(repetidos)
        )

    chaves = [chave_ordem(n) for n in numeros]
    fora_de_ordem = [
        f"{numeros[i]} depois de {numeros[i - 1]}"
        for i in range(1, len(numeros))
        if chaves[i] < chaves[i - 1]
    ]
    if fora_de_ordem:
        avisos.append(
            "ERRO artigos proprios fora de ordem — provavel texto de outra norma "
            "lido como proprio, ou aspas desbalanceadas: " + "; ".join(fora_de_ordem[:10])
        )

    return artigos, avisos, stats


def nome_arquivo(numero: str) -> str:
    """art-0012 / art-0012-a — zero à esquerda garante ordenação lexicográfica."""
    base = re.match(r"\d+", numero).group()
    nome = f"art-{int(base):04d}"
    if "-" in numero:
        nome += numero[numero.index("-"):].lower()
    return nome


def _imprimir_estatisticas(stats: dict, prefixo: str = "  ") -> None:
    """O que o documento tinha de incomum, com números, para o humano conferir."""
    print(f"{prefixo}linhas com texto riscado: {stats['linhas_com_riscado']}  "
          f"(redacoes anteriores mescladas ao dispositivo: "
          f"{stats['redacoes_anteriores_mescladas']})")
    print(f"{prefixo}aspas: fechamento sem abertura={stats['aspas_fechamento_sem_abertura']}  "
          f"abertura dentro de bloco={stats['aspas_abertura_dentro_de_bloco']}  "
          f"saldo final={stats['aspas_estado_final']}")
    print(f"{prefixo}aspas x <blockquote>: {stats['discordancia_blockquote']} discordancia(s)")
    print(f"{prefixo}depois do fim do texto (assinatura, anexos): "
          f"{stats['linhas_apos_o_fim']} linha(s), {stats['anexos_nao_incorporados']} anexo(s) "
          "NAO incorporados a /normas/ — permanecem em fontes/")


# Cabeçalho da página de um ato no portal da Imprensa Nacional (in.gov.br),
# em campos marcados por classe dentro de <article id="materia">. O <span> da
# seção não é fechado no original; por isso cada campo é lido pela própria
# classe, e não pela estrutura de tags.
RE_DOU_DATA = re.compile(r'class="publicado-dou-data">\s*(\d{2})/(\d{2})/(\d{4})\s*<')
RE_DOU_EDICAO = re.compile(r'class="edicao-dou-data">\s*([^<]+?)\s*<')
RE_DOU_SECAO = re.compile(r'class="secao-dou">\s*Se[çc][ãa]o:\s*([^<]+?)\s*<')
RE_DOU_PAGINA = re.compile(r'class="secao-dou-data">\s*([^<]+?)\s*<')


def publicacao_dou(dados: bytes) -> dict | None:
    """Data, edição, seção e página da publicação, lidas da página do ato no DOU.

    Só dentro de <article id="materia">: fora dele a página repete o título na
    navegação. None se o cabeçalho não está lá — nunca um palpite.
    """
    html = _decodificar(dados)
    inicio = html.find('<article id="materia"')
    if inicio < 0:
        return None
    materia = html[inicio:]
    m = RE_DOU_DATA.search(materia)
    if not m:
        return None
    try:
        data = _dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))).isoformat()
    except ValueError:
        return None
    campos = {}
    for nome, regex in (("edicao", RE_DOU_EDICAO), ("secao", RE_DOU_SECAO),
                        ("pagina", RE_DOU_PAGINA)):
        achado = regex.search(materia)
        campos[nome] = achado.group(1) if achado else None
    trecho = next((ln.completa for ln in html_para_linhas(dados)
                   if ln.completa.startswith("Publicado em:")), None)
    return {"data": data, **campos, "trecho": trecho}


def publicacao_de(refs: dict, dou: dict | None = None) -> dict:
    """`publicacao` do front-matter.

    Com a página do DOU arquivada, a publicação vem dela (`fonte: dou`): o texto
    publicado prevalece sobre o compilado (PREMISSAS.md §1.4). O rodapé do
    compilado continua registrado à parte, e a data que só ele cita fica visível
    como não confirmada — na LC 214, a "republicação" de 23/01/2025.

    Sem o DOU, a publicação é a do rodapé do compilado, declarada como tal.
    """
    rodape = refs.get("publicacao_dou") or {}
    rodape_datas = list(rodape.get("valores") or [])
    rodape_trechos = list(rodape.get("trechos") or []) if rodape_datas else []
    if dou:
        pub = {"datas": [dou["data"]], "fonte": "dou",
               "trechos": [dou["trecho"]] if dou.get("trecho") else [],
               "dou": {"edicao": dou.get("edicao"), "secao": dou.get("secao"),
                       "pagina": dou.get("pagina")}}
        if rodape_datas:
            pub["rodape_compilado"] = {"datas": rodape_datas, "trechos": rodape_trechos}
        return pub
    return {"datas": rodape_datas, "fonte": "rodape_compilado" if rodape_datas else None,
            "trechos": rodape_trechos}


def montar_meta(
    artigo: dict, fonte: dict, registro: dict, base: str, publicacao: dict,
    exigir_escopo: bool,
) -> tuple[dict, str]:
    """(front-matter, corpo) de um artigo, ainda sem revisão temporal."""
    # Corpo do arquivo: tudo que o portal mostra, o riscado entre ~~ ~~.
    corpo = "\n\n".join(artigo["linhas"])
    # Sem o texto riscado: a anotação "(Revogado ...)" e as normas mencionadas
    # valem para o que está em vigor, não para a redação superada.
    vigente = "\n\n".join(artigo["linhas_vigentes"])
    # Texto próprio vigente, sem o que foi citado de outras normas. As
    # remissões e os conceitos saem daqui: no texto citado eles pertencem à
    # norma alterada, e resolvê-los no namespace desta criaria ponteiro errado.
    corpo_proprio = "\n\n".join(artigo["linhas_proprias"])
    # group(0): a anotação inteira. findall() devolveria só o grupo de
    # captura ("Redação dada"), perdendo a norma que promoveu a alteração.
    anotacoes = [re.sub(r"\s+", " ", m.group(0)) for m in RE_ANOTACAO.finditer(vigente)]
    conceitos = [c.strip() for c in RE_CONCEITO.findall(corpo_proprio)]

    # Datas PROVISÓRIAS até a revisão humana da cláusula de vigência (ver
    # revisao_temporal_pendente): a primeira publicação, ou a data do ato se a
    # publicação não foi localizada no original.
    provisoria = publicacao["datas"][0] if publicacao["datas"] else fonte["data"]

    meta = {
        "urn": urn_dispositivo(base, artigo["numero"]),
        "norma": fonte["titulo"],
        "norma_slug": fonte["slug"],
        "dispositivo": f"art. {artigo['numero']}",
        "camada": 1,
        "hierarquia": artigo["hierarquia"],
        # Data do ato: a do título, que também compõe a URN. Não é a publicação.
        "data_ato": fonte["data"],
        "publicacao": publicacao,
        "vigencia_inicio": provisoria,
        "vigencia_fim": None,
        "efeitos_inicio": provisoria,
        "efeitos_fim": None,
        "status": None,
        "fonte": {
            "url": registro["url"],
            "tipo": registro["tipo_documento"],
            "acesso": registro["acesso"],
            "sha256": registro["sha256"],
        },
        "ingerido_em": hoje(),
        "remete_a": extrair_remissoes(corpo_proprio, base, artigo["numero"], exigir_escopo),
        "remete_a_externo": extrair_externas(vigente),
        # Subdivisões do próprio artigo; as do texto citado pertencem à
        # norma alterada.
        "subdivisoes": subdivisoes_de(artigo["linhas_proprias"], base, artigo["numero"]),
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
    meta["status"] = status_em(meta, _dt.date.today())
    return ordenar_meta(meta), corpo


def processar_norma(fonte: dict, manifest: dict, relatorio: bool = False) -> int:
    slug = fonte["slug"]
    chave = f"{slug}/texto_compilado"
    registro = manifest["documentos"].get(chave)
    if not registro:
        print(f"[{slug}] sem documento em fontes/manifest.json — rode baixar.py antes",
              file=sys.stderr)
        return 1

    caminho = caminho_fonte(registro)
    if not caminho.exists():
        print(f"[{slug}] arquivo ausente: {caminho}", file=sys.stderr)
        return 1

    linhas = html_para_linhas(caminho.read_bytes())
    artigos, avisos, stats = fatiar(linhas)

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

    refs = extrair_referencias([ln.completa for ln in linhas])
    ato_lido = refs["data_do_ato"]["valor"]
    if ato_lido and ato_lido != fonte["data"]:
        print(f"[{slug}] AVISO: data do ato no original ({ato_lido}) difere da do catalogo "
              f"({fonte['data']}), que compoe a URN — confira pipeline/fontes.yaml",
              file=sys.stderr)

    # A página do ato no DOU, se arquivada, dá a publicação (prevalece, §1.4).
    dou = None
    registro_dou = manifest["documentos"].get(f"{slug}/texto_publicado")
    if registro_dou:
        arquivo_dou = caminho_fonte(registro_dou)
        dou = publicacao_dou(arquivo_dou.read_bytes()) if arquivo_dou.exists() else None
        if dou is None:
            print(f"[{slug}] AVISO: texto publicado arquivado sem cabecalho de publicacao "
                  "reconhecivel — a publicacao continua lida do rodape do compilado",
                  file=sys.stderr)
    primeira_rodape = (refs["publicacao_dou"]["valores"] or [None])[0]
    if dou and primeira_rodape and dou["data"] != primeira_rodape:
        print(f"[{slug}] AVISO: publicacao no DOU ({dou['data']}) difere da do rodape do "
              f"compilado ({primeira_rodape}); prevalece o DOU (PREMISSAS.md §1.4)",
              file=sys.stderr)
    publicacao = publicacao_de(refs, dou)

    base = urn_norma(fonte["autoridade"], fonte["data"], fonte["numero"])
    exigir_escopo = exige_escopo_interno(fonte)
    gerados = [montar_meta(a, fonte, registro, base, publicacao, exigir_escopo)
               for a in artigos]

    # Revisão temporal humana, se houver. Erro aqui aborta ANTES de apagar
    # qualquer arquivo: aplicar parte de uma revisão, ou descartá-la em silêncio,
    # deixaria a base num estado que ninguém decidiu.
    revisoes, erros_rev = carregar_revisoes(
        DIR_TEMPORAL / "propostas" / f"{slug}.yaml", registro["sha256"],
        {m["urn"] for m, _ in gerados})
    for erro in erros_rev:
        print(f"[{slug}] ERRO revisao temporal: {erro}", file=sys.stderr)

    proprios = len(artigos)
    citados = sum(len(a["citados"]) for a in artigos)
    if relatorio:
        faixa = f"{artigos[0]['numero']}..{artigos[-1]['numero']}"
        print(f"[{slug}] RELATORIO (nada escrito)")
        print(f"  artigos proprios: {proprios}  (faixa {faixa})")
        print(f"  artigos citados de outras normas: {citados}")
        _imprimir_estatisticas(stats)
        print(f"  data do ato: {fonte['data']}   publicacao: {publicacao['datas'] or 'nao localizada'}"
              f" ({publicacao['fonte'] or '-'})")
        print(f"  revisoes temporais aplicaveis: {len(revisoes)}  (erros: {len(erros_rev)})")

        # Lacunas na sequência própria. Um artigo que a norma tem mas que a
        # classificação mandou para "citado" aparece aqui — é o diagnóstico
        # mais direto de classificação errada.
        numeros_base = {int(re.match(r"\d+", a["numero"]).group()) for a in artigos}
        if numeros_base:
            faltando = sorted(set(range(1, max(numeros_base) + 1)) - numeros_base)
            print(f"  lacunas na sequencia (1..{max(numeros_base)}): {len(faltando)}")
            if faltando:
                amostra = ", ".join(str(n) for n in faltando[:25])
                extra = f" (+{len(faltando) - 25})" if len(faltando) > 25 else ""
                print(f"    {amostra}{extra}")

        # Artigos com sufixo alfabético: na norma original são acréscimos
        # legítimos, mas em bloco de alteração denunciam texto citado que
        # escapou da classificação.
        sufixados = [a["numero"] for a in artigos if "-" in a["numero"]]
        print(f"  artigos com sufixo alfabetico: {len(sufixados)}")
        if sufixados:
            print(f"    {', '.join(sufixados[:25])}")

        # Remissões: quantas foram resolvidas e quantas apontam para artigo
        # que esta ingestão não produziu.
        proprias = {m["urn"] for m, _ in gerados}
        total_rem = orfas_rem = 0
        for meta, _ in gerados:
            for alvo in meta["remete_a"]:
                total_rem += 1
                artigo_alvo = alvo.split("!")[0] + "!" + alvo.split("!")[1].split("_")[0]
                if artigo_alvo not in proprias:
                    orfas_rem += 1
        pct = f"{orfas_rem / total_rem:.0%}" if total_rem else "-"
        print(f"  remissoes internas resolvidas: {total_rem}  (orfas: {orfas_rem} = {pct})")
        return 1 if erros_rev else 0

    if erros_rev:
        print(f"[{slug}] nada foi escrito — corrija a revisao em "
              f"temporal/propostas/{slug}.yaml antes de ingerir", file=sys.stderr)
        return 1

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

    referencia = _dt.date.today()
    pendentes = 0
    for (meta, corpo), artigo in zip(gerados, artigos):
        if meta["urn"] in revisoes:
            meta = aplicar_revisao(meta, revisoes[meta["urn"]])
            meta["status"] = status_em(meta, referencia)
        pendentes += bool(meta["revisao_temporal_pendente"])
        escrever_frontmatter(destino_dir / f"{nome_arquivo(artigo['numero'])}.md", meta, corpo)

    print(f"[{slug}] {proprios} artigos proprios escritos em "
          f"{destino_dir.relative_to(DIR_NORMAS.parent)} "
          f"(faixa {artigos[0]['numero']}..{artigos[-1]['numero']})")
    print(f"[{slug}] {citados} artigo(s) de outras normas tratados como texto "
          "alterado, nao como dispositivo proprio")
    _imprimir_estatisticas(stats, prefixo=f"[{slug}] ")
    print(f"[{slug}] publicacao: {publicacao['datas'] or 'nao localizada'} "
          f"({publicacao['fonte'] or '-'}); data do ato: {fonte['data']}")
    print(f"[{slug}] revisao temporal aplicada a {len(revisoes)} dispositivo(s)")
    print(f"[{slug}] ATENCAO: {pendentes} dispositivos com revisao_temporal_pendente")
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
