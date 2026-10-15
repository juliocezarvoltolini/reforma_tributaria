"""Republicação e retificação de uma norma, lidas do ato no Planalto (.doc).

O DOU recusa acesso automatizado; o Planalto publica cada ato em
`ccivil_03/<período>/<ano>/ret/<norma>-rep.doc` e `-ret.doc`. Padrões medidos nos
atos da LC 227, no texto que o antiword extrai:

  REPUBLICAÇÃO
  LEI COMPLEMENTAR Nº 227, DE 13 DE JANEIRO DE 2026 (*)
  <ementa>
  “Art. 293.  /  § 4º  /  I - (VETADO);”          (o trecho republicado)
  (*) Republicação parcial da Lei Complementar nº 227, ..., por ter constado
      inexatidão material.

  RETIFICAÇÃO
  Na LEI COMPLEMENTAR Nº 227, DE 13 DE JANEIRO DE 2026, publicada no DOU de
      14/1/2026, Seção 1, pág. 1, onde se lê:
  <trecho>
  Leia-se:
  <trecho>

O ato do Planalto não traz a data da edição do DOU em que saiu: a data continua
sendo a do rodapé do compilado, não confirmada. O que ele dá é o ALCANCE: quais
artigos foram republicados ou retificados.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from dou_pdf import _normalizar

RE_ARTIGO_PROPRIO = re.compile(r"^Art\.\s*(\d+)\s*[ºo°]?\s*(-[A-Z])?")
RE_ARTIGO_CITADO = re.compile(r"^[“\"]\s*Art\.\s*(\d+)\s*[ºo°]?\s*(-[A-Z])?")
_ANTIWORD_PADRAO = Path("C:/Program Files/Git/mingw64/bin/antiword.exe")


def linhas_do_doc(caminho: Path) -> list[str]:
    """Linhas de texto do .doc, pelo antiword (sem quebra de linha artificial)."""
    antiword = shutil.which("antiword") or (str(_ANTIWORD_PADRAO) if _ANTIWORD_PADRAO.exists()
                                            else None)
    if antiword is None:  # sem silêncio: o ato arquivado precisa ser lido
        raise SystemExit("antiword ausente: necessário para ler o .doc do Planalto")
    saida = subprocess.run([antiword, "-m", "UTF-8.txt", "-w", "0", str(caminho)],
                           capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return [linha.strip() for linha in saida.splitlines() if linha.strip()]


def _numeros(linhas: list[str], regex: re.Pattern) -> list[str]:
    achados = [m.group(1) + (m.group(2) or "") for linha in linhas if (m := regex.match(linha))]
    return list(dict.fromkeys(achados))


def ler_republicacao(linhas: list[str], titulo: str) -> dict | None:
    """O que a republicação traz: artigos desta norma e artigos citados (entre aspas)."""
    if not linhas or re.sub(r"\s+", "", linhas[0]).upper() != "REPUBLICAÇÃO":
        return None
    alvo = _normalizar(titulo)
    inicio = next((i for i, linha in enumerate(linhas) if _normalizar(linha) == alvo), None)
    if inicio is None:
        return None
    nota_ini = next((i for i in range(inicio + 1, len(linhas)) if linhas[i].startswith("(*)")),
                    None)
    if nota_ini is None:
        raise ValueError("republicação sem a nota '(*)' que diz o que foi republicado")
    bloco = linhas[inicio + 1:nota_ini]
    nota = " ".join(linhas[nota_ini:])
    return {"fonte": "planalto", "nota": nota,
            "parcial": re.search(r"\bparcial\b", nota, re.IGNORECASE) is not None,
            "artigos_proprios": _numeros(bloco, RE_ARTIGO_PROPRIO),
            "artigos_citados": _numeros(bloco, RE_ARTIGO_CITADO)}


def artigos_tocados(ato: dict, artigos: list[dict]) -> list[str]:
    """Artigos desta norma que o ato tocou: os que ele nomeia e os que inserem, em
    outra norma, o artigo que ele cita entre aspas (LC 227: o “Art. 293” republicado
    é texto que o art. 174 insere na LC 214). Na dúvida — o mesmo número citado por
    dois artigos — os dois contam."""
    citados = set(ato.get("artigos_citados") or [])
    tocados = set(ato.get("artigos_proprios") or [])
    tocados |= {a["numero"] for a in artigos if citados & set(a.get("citados") or [])}
    return sorted(tocados, key=lambda n: (int(re.match(r"\d+", n).group()), n))


def ler_retificacao(linhas: list[str], titulo: str) -> dict | None:
    """O que a retificação corrige: o trecho 'onde se lê' e o 'leia-se', e os
    artigos desta norma que eles nomeiam."""
    if len(linhas) < 2 or linhas[0].strip().upper() != "RETIFICAÇÃO":
        return None
    if _normalizar(titulo) not in _normalizar(linhas[1]) or "onde se lê" not in linhas[1].lower():
        return None
    leia = next((i for i, linha in enumerate(linhas) if linha.strip().lower() == "leia-se:"), None)
    if leia is None:
        return None
    onde_se_le, leia_se = linhas[2:leia], linhas[leia + 1:]
    return {"fonte": "planalto", "cabecalho": linhas[1],
            "artigos_proprios": _numeros(onde_se_le + leia_se, RE_ARTIGO_PROPRIO),
            "onde_se_le": onde_se_le, "leia_se": leia_se}
