"""Leitura de página do DOU em PDF (versão certificada da Imprensa Nacional).

Hoje lê uma coisa: a REPUBLICAÇÃO de uma norma na página. A LC 214 foi
republicada em parte no DOU de 23/01/2025 (o rodapé do compilado só diz
"republicado no DOU de 23.1.2025"), e saber O QUE foi republicado decide se a
data de publicação dos artigos muda.

Padrões medidos no PDF real (fontes/lc-214-2025/texto_republicado.pdf), no
texto que o pypdf extrai:

  Ano CLXIII Nº 16 Brasília - DF, quinta-feira, 23 de janeiro de 2025
  ... pelo código 05152025012300001          (jornal, AAAAMMDD, página)
  R E P U B L I C A Ç Ã O
  LEI COMPLEMENTAR Nº 214, DE 16 DE JANEIRO DE 2025 (*)
  <ementa e o trecho republicado>
  (*) Republicação do Anexo XXIII a Lei Complementar nº 214, ... página 64.
  LEI Nº 15.103, DE 22 DE JANEIRO DE 2025     (o próximo ato da página)

Conservador: só reconhece republicação com a marca "REPUBLICAÇÃO" antes do
título exato da norma. Código de autenticidade com data diferente do cabeçalho
é erro.
"""
from __future__ import annotations

import io
import re
import unicodedata

from fatiar import _iso

RE_CABECALHO = re.compile(
    r"Ano\s+[IVXLCDM]+\s+N[ºo°]\s*(\d+)\s+Bras[íi]lia\s*-\s*DF\s*,\s*[\w-]+\s*,\s*"
    r"(\d{1,2})\s*[ºo°]?\s+de\s+(\w+)\s+de\s+(\d{4})", re.IGNORECASE)
RE_CODIGO = re.compile(r"pelo\s+c[óo]digo\s+(\d{4})(\d{8})(\d{5})\b", re.IGNORECASE)
RE_TITULO_ATO = re.compile(
    r"^(?:LEI|DECRETO|MEDIDA PROVIS[ÓO]RIA|EMENDA CONSTITUCIONAL|RESOLU[ÇC][ÃA]O|PORTARIA|"
    r"MENSAGEM|ATO)\b[^a-z]*\bN[ºo°]", re.UNICODE)
RE_ARTIGO = re.compile(r"^[“\"]?\s*Art\.\s*(\d+)\s*[ºo°]?\s*(-[A-Z])?")
RE_ANEXO_NA_NOTA = re.compile(r"\bAnexos?\s+([IVXLC]+)\b")


def linhas_do_pdf(dados: bytes) -> list[str]:
    """Linhas de texto do PDF, na ordem do pypdf."""
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # sem silêncio: o PDF arquivado precisa ser lido
        raise SystemExit("pypdf ausente: instale com 'python -m pip install pypdf' "
                         "para ler a página do DOU em PDF") from exc
    leitor = PdfReader(io.BytesIO(dados))
    texto = "\n".join(p.extract_text() or "" for p in leitor.pages)
    return [linha.strip() for linha in texto.splitlines() if linha.strip()]


def _normalizar(texto: str) -> str:
    """Caixa e espaços fora; 'nº' e 'Nº' iguais. Só para comparar títulos."""
    texto = unicodedata.normalize("NFC", texto).upper().replace("(*)", "")
    return re.sub(r"\s+", " ", texto.replace("N°", "Nº")).strip()


def ler_republicacao(linhas: list[str], titulo: str) -> dict | None:
    """A republicação da norma `titulo` na página, ou None se ela não está lá.

    `artigos`: artigos desta norma no trecho republicado (cabeçalho 'Art. N' de
    linha). `anexos`: os que a nota '(*)' diz republicar. `nota`: literal.
    """
    alvo = _normalizar(titulo)
    inicio = next(
        (i for i, linha in enumerate(linhas)
         if _normalizar(linha) == alvo and i > 0
         and re.sub(r"\s+", "", linhas[i - 1]).upper().startswith("REPUBLICAÇÃO")),
        None)
    if inicio is None:
        return None

    cab = next((m for linha in linhas if (m := RE_CABECALHO.search(linha))), None)
    cod = next((m for linha in linhas if (m := RE_CODIGO.search(linha))), None)
    if cab is None or cod is None:
        raise ValueError("página sem cabeçalho do DOU ou sem código de autenticidade")
    data = _iso(cab.group(2), cab.group(3), cab.group(4))
    data_codigo = f"{cod.group(2)[:4]}-{cod.group(2)[4:6]}-{cod.group(2)[6:]}"
    if data is None or data != data_codigo:
        raise ValueError(f"data do cabeçalho ({data}) difere da do código de autenticidade "
                         f"({data_codigo})")

    nota_ini = next((i for i in range(inicio + 1, len(linhas))
                     if linhas[i].startswith("(*)")), None)
    if nota_ini is None:
        raise ValueError("republicação sem a nota '(*)' que diz o que foi republicado")
    nota_fim = next((i for i in range(nota_ini + 1, len(linhas))
                     if RE_TITULO_ATO.match(linhas[i])), len(linhas))
    bloco = linhas[inicio + 1:nota_ini]
    nota = " ".join(linhas[nota_ini:nota_fim])
    artigos = [m.group(1) + (m.group(2) or "") for linha in bloco if (m := RE_ARTIGO.match(linha))]
    return {
        "data": data,
        "edicao": cab.group(1),
        "pagina": int(cod.group(3)),
        "codigo_autenticidade": "".join(cod.groups()),
        "trecho": next(linha for linha in linhas if RE_CABECALHO.search(linha)),
        "nota": nota,
        "artigos": list(dict.fromkeys(artigos)),
        "anexos": list(dict.fromkeys(RE_ANEXO_NA_NOTA.findall(nota))),
    }
