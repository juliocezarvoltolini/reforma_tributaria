"""Consulta com filtro temporal — a forma correta de ler esta base.

Busca textual crua ignora vigência e devolve dispositivo que ainda não vale.
Este script aplica o filtro temporal ANTES de retornar (PREMISSAS.md §3.2) e
mostra as remissões a seguir antes de concluir (CLAUDE.md, passo 3).

Uso:
    python3 pipeline/consultar.py --data 2027-01-01 --termo "credito"
    python3 pipeline/consultar.py --urn "urn:lex:...!art12" --seguir
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
import unicodedata

from comum import arquivos_norma, ler_frontmatter, para_data, status_em

ROTULO = {
    "vigente": "vigente e produzindo efeitos",
    "vigente_sem_efeitos": "vigente, mas AINDA NAO produz efeitos",
    "futuro": "ainda NAO vigente",
    "revogado": "REVOGADO",
    "sem_efeitos": "vigente, mas ja NAO produz efeitos",
}


def normalizar(texto: str) -> str:
    norm = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in norm if not unicodedata.combining(c))


def carregar() -> list[tuple[dict, str]]:
    itens = []
    for caminho in arquivos_norma():
        try:
            itens.append(ler_frontmatter(caminho))
        except ValueError as exc:
            print(f"aviso: {exc}", file=sys.stderr)
    return itens


def imprimir(meta: dict, corpo: str, referencia: _dt.date, trecho: str | None) -> None:
    estado = status_em(meta, referencia)
    print(f"\n{'=' * 72}")
    print(f"{meta['norma']} — {meta['dispositivo']}")
    print(f"URN: {meta['urn']}")
    print(f"Estado em {referencia}: {ROTULO.get(estado, estado)}")
    print(f"  vigencia: {meta.get('vigencia_inicio')} -> {meta.get('vigencia_fim') or 'sem termo'}")
    print(f"  efeitos:  {meta.get('efeitos_inicio')} -> {meta.get('efeitos_fim') or 'sem termo'}")
    if meta.get("revisao_temporal_pendente"):
        print("  ATENCAO: revisao_temporal_pendente — datas provisorias, "
              "iguais a publicacao. Nao usar para decisao sem revisar a fonte.")
    if meta.get("hierarquia"):
        print(f"  contexto: {' > '.join(meta['hierarquia'])}")
    print(f"  fonte: {meta['fonte']['url']} (acesso {meta['fonte']['acesso']})")

    remissoes = meta.get("remete_a") or []
    if remissoes:
        print(f"\n  SEGUIR ANTES DE CONCLUIR ({len(remissoes)} remissao/oes):")
        for alvo in remissoes:
            print(f"    - {alvo}")

    print()
    print(trecho if trecho else corpo)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", help="data de referencia (AAAA-MM-DD)")
    ap.add_argument("--termo", help="busca textual no corpo do dispositivo")
    ap.add_argument("--urn", help="dispositivo especifico")
    ap.add_argument("--seguir", action="store_true",
                    help="exibe tambem os dispositivos referidos por remissao")
    ap.add_argument("--incluir-nao-vigentes", action="store_true",
                    help="nao filtra por estado na data de referencia")
    args = ap.parse_args()

    if not args.termo and not args.urn:
        ap.error("informe --termo ou --urn")

    if args.data:
        referencia = _dt.date.fromisoformat(args.data)
    else:
        referencia = _dt.date.today()
        print(f"AVISO: data de referencia nao informada. Assumindo hoje ({referencia}).\n"
              "A transicao da reforma e escalonada por exercicio — informe --data "
              "para perguntas sobre outro ano.", file=sys.stderr)

    itens = carregar()
    if not itens:
        print("Base vazia: nenhum dispositivo em /normas/.\n"
              "Nada a responder — rode o pipeline de ingestao.", file=sys.stderr)
        return 1

    indice = {m["urn"]: (m, c) for m, c in itens}
    resultados: list[tuple[dict, str, str | None]] = []

    if args.urn:
        if args.urn not in indice:
            print(f"URN nao localizada nas fontes indexadas: {args.urn}", file=sys.stderr)
            return 1
        meta, corpo = indice[args.urn]
        resultados.append((meta, corpo, None))
    else:
        alvo = normalizar(args.termo)
        for meta, corpo in itens:
            if alvo in normalizar(corpo):
                linhas = [ln for ln in corpo.split("\n") if alvo in normalizar(ln)]
                resultados.append((meta, corpo, "\n\n".join(linhas[:3])))

    if not args.incluir_nao_vigentes:
        antes = len(resultados)
        resultados = [
            r for r in resultados
            if status_em(r[0], referencia) not in {"futuro", "revogado", "sem_efeitos"}
        ]
        filtrados = antes - len(resultados)
        if filtrados:
            print(f"({filtrados} dispositivo(s) omitido(s) por nao estarem em vigor "
                  f"em {referencia} — use --incluir-nao-vigentes para ve-los)",
                  file=sys.stderr)

    if not resultados:
        print("Nao localizado nas fontes indexadas para a data de referencia.",
              file=sys.stderr)
        return 1

    for meta, corpo, trecho in resultados:
        imprimir(meta, corpo, referencia, trecho)
        if args.seguir:
            for alvo in meta.get("remete_a") or []:
                if alvo in indice:
                    m2, c2 = indice[alvo]
                    print(f"\n  --- remissao a partir de {meta['dispositivo']} ---")
                    imprimir(m2, c2, referencia, None)

    print(f"\n{'=' * 72}")
    print(f"{len(resultados)} dispositivo(s). Data de referencia: {referencia}.")
    print("Cite a URN de todo dispositivo usado e rotule literal/derivado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
