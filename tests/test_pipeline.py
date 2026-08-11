"""Testes do pipeline, contra fixture sintético.

O fixture reproduz a MARCAÇÃO do portal do Planalto com texto INVENTADO. Norma
real nunca entra em teste: texto normativo só existe na base vindo de fonte
oficial baixada, com hash (PREMISSAS.md §1.1).

Uso:
    python3 tests/test_pipeline.py
"""
from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "pipeline"))

from comum import status_em, urn_dispositivo, urn_norma  # noqa: E402
from fatiar import (  # noqa: E402
    detectar_encoding,
    extrair_externas,
    extrair_remissoes,
    fatiar,
    html_para_texto,
    nome_arquivo,
    subdivisoes_de,
)

FIXTURE = Path(__file__).parent / "fixtures" / "planalto-sintetico.html"
URN_BASE = urn_norma("br:federal:lei.complementar", "1900-01-01", "999")

falhas: list[str] = []


def checar(condicao: bool, descricao: str) -> None:
    if condicao:
        print(f"  ok   {descricao}")
    else:
        print(f"  FALHA {descricao}")
        falhas.append(descricao)


def main() -> int:
    dados = FIXTURE.read_bytes()

    print("html_para_texto")
    checar(detectar_encoding(dados) == "utf-8", "detecta charset declarado")
    texto = html_para_texto(dados)
    checar("este texto nao pode aparecer" not in texto, "remove <script>")
    checar("color: red" not in texto, "remove <style>")
    checar("Art. 1º" in texto, "preserva texto dos dispositivos")

    print("\nfatiar")
    artigos, avisos = fatiar(texto)
    checar(len(artigos) == 5, f"5 artigos reconhecidos (achou {len(artigos)})")
    checar(not avisos, f"sem avisos (achou {avisos})")
    numeros = [a["numero"] for a in artigos]
    checar(numeros == ["1", "2", "3", "4", "4-A"], f"numeracao correta: {numeros}")

    art1, art2 = artigos[0], artigos[1]
    checar(
        art1["hierarquia"] == ["LIVRO I", "TÍTULO I", "CAPÍTULO I"],
        f"hierarquia do art. 1: {art1['hierarquia']}",
    )
    checar(
        artigos[2]["hierarquia"] == ["LIVRO I", "TÍTULO I", "CAPÍTULO II"],
        "CAPITULO II substitui CAPITULO I no mesmo nivel",
    )

    print("\nremissoes")
    corpo1 = "\n".join(art1["linhas"])
    rem1 = extrair_remissoes(corpo1, URN_BASE, "1")
    checar(urn_dispositivo(URN_BASE, "4") in rem1, "art. 1 remete ao art. 4")
    checar(
        urn_dispositivo(URN_BASE, "2", inciso="II") in rem1,
        "captura 'inciso II do art. 2' como subdivisao",
    )
    checar(
        not any(r.startswith(urn_dispositivo(URN_BASE, "1")) for r in rem1),
        "nao registra auto-remissao",
    )

    corpo2 = "\n".join(art2["linhas"])
    rem2 = extrair_remissoes(corpo2, URN_BASE, "2")
    checar(
        urn_dispositivo(URN_BASE, "1", paragrafo="1") in rem2,
        "captura '§ 1º do art. 1º' como paragrafo",
    )

    print("\nremissoes externas")
    ext = extrair_externas(corpo2)
    checar(any("998" in e for e in ext), f"captura norma alteradora: {ext}")

    print("\nsubdivisoes")
    subs = subdivisoes_de(art1["linhas"], URN_BASE, "1")
    checar(urn_dispositivo(URN_BASE, "1", paragrafo="1") in subs, "captura § 1º")
    checar(
        urn_dispositivo(URN_BASE, "1", paragrafo="2", inciso="I") in subs,
        "inciso herda o paragrafo corrente",
    )
    checar(
        urn_dispositivo(URN_BASE, "1", paragrafo="2", inciso="I", alinea="a") in subs,
        "alinea herda paragrafo e inciso",
    )
    subs2 = subdivisoes_de(art2["linhas"], URN_BASE, "2")
    checar(urn_dispositivo(URN_BASE, "2", paragrafo="U") in subs2, "paragrafo unico -> parU")

    print("\nnome_arquivo")
    checar(nome_arquivo("1") == "art-0001", "zero a esquerda")
    checar(nome_arquivo("12") == "art-0012", "dois digitos")
    checar(nome_arquivo("4-A") == "art-0004-a", "sufixo alfabetico")

    print("\nstatus_em (vigencia x eficacia — PREMISSAS.md §3.1)")
    import datetime as dt

    meta = {
        "vigencia_inicio": "2026-01-01",
        "vigencia_fim": None,
        "efeitos_inicio": "2027-01-01",
        "efeitos_fim": None,
    }
    checar(status_em(meta, dt.date(2025, 6, 1)) == "futuro", "antes da vigencia")
    checar(
        status_em(meta, dt.date(2026, 6, 1)) == "vigente_sem_efeitos",
        "vigente mas sem efeitos — distincao central do projeto",
    )
    checar(status_em(meta, dt.date(2027, 6, 1)) == "vigente", "vigente com efeitos")

    revogado = dict(meta, vigencia_fim="2033-01-01")
    checar(status_em(revogado, dt.date(2033, 6, 1)) == "revogado", "apos vigencia_fim")

    print("\nencoding latin-1 (padrao do Planalto)")
    html_latin = (
        '<html><head><meta charset="iso-8859-1"></head><body>'
        "<p>Art. 1º Operação com acentuação.</p></body></html>"
    ).encode("latin-1")
    texto_latin = html_para_texto(html_latin)
    checar("Operação" in texto_latin, "decodifica iso-8859-1 corretamente")

    print()
    if falhas:
        print(f"{len(falhas)} FALHA(S)")
        return 1
    print("todos os testes passaram")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
