"""Etapa 4 — validação. Roda na CI e antes de qualquer commit.

Premissa que não é verificada por máquina é intenção, não garantia
(PREMISSAS.md §7). Este script transforma as premissas em falha de build.

Uso:
    python3 pipeline/validar.py
    python3 pipeline/validar.py --estrito   # avisos também falham
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from comum import (
    CAMPOS_OBRIGATORIOS,
    DIR_FONTES,
    DIR_INTERPRETACOES,
    DIR_NORMAS,
    MANIFEST,
    MARCA_NAO_VERIFICADO,
    DIR_TEMPORAL,
    STATUS_VALIDOS,
    arquivos_norma,
    caminho_fonte,
    ler_frontmatter,
    para_data,
    sha256_arquivo,
)
from revisao_temporal import carregar_revisoes, problemas_no_dispositivo, revisoes_nao_aplicadas

erros: list[str] = []
avisos: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def aviso(msg: str) -> None:
    avisos.append(msg)


def rel(caminho: Path) -> str:
    return str(caminho.relative_to(DIR_NORMAS.parent))


# ---------------------------------------------------------------------------

def validar_dispositivos() -> list[dict]:
    metas: list[dict] = []
    por_urn: dict[str, list[str]] = defaultdict(list)
    # O mesmo aviso em centenas de dispositivos da mesma norma vira uma linha só:
    # repetido, ele empurraria para fora da tela os avisos que importam.
    avisos_temporais: dict[str, list[str]] = defaultdict(list)

    for caminho in arquivos_norma():
        try:
            meta, corpo = ler_frontmatter(caminho)
        except ValueError as exc:
            erro(str(exc))
            continue

        for campo in CAMPOS_OBRIGATORIOS:
            if meta.get(campo) in (None, "", []):
                erro(f"{rel(caminho)}: campo obrigatorio ausente ou vazio: '{campo}'")

        if meta.get("camada") != 1:
            erro(f"{rel(caminho)}: /normas/ so aceita camada 1 (achado: {meta.get('camada')})")

        if meta.get("status") and meta["status"] not in STATUS_VALIDOS:
            aviso(f"{rel(caminho)}: status '{meta['status']}' fora do vocabulario padrao")

        fonte = meta.get("fonte") or {}
        for campo in ("url", "tipo", "acesso", "sha256"):
            if not fonte.get(campo):
                erro(f"{rel(caminho)}: fonte.{campo} ausente — sem procedencia verificavel")

        if MARCA_NAO_VERIFICADO in corpo:
            erro(f"{rel(caminho)}: contem marca {MARCA_NAO_VERIFICADO} — "
                 "conteudo nao verificado nao entra na camada 1")

        if not corpo.strip():
            erro(f"{rel(caminho)}: corpo vazio — dispositivo sem texto normativo")

        vi = para_data(meta.get("vigencia_inicio"))
        vf = para_data(meta.get("vigencia_fim"))
        if vi and vf and vf <= vi:
            erro(f"{rel(caminho)}: vigencia_fim ({vf}) nao e posterior a vigencia_inicio ({vi})")

        ei = para_data(meta.get("efeitos_inicio"))
        ef = para_data(meta.get("efeitos_fim"))
        if ei and ef and ef <= ei:
            erro(f"{rel(caminho)}: efeitos_fim ({ef}) nao e posterior a efeitos_inicio ({ei})")

        # data do ato x publicação, precisão de ano, exceções por subdivisão e
        # coerência de um dispositivo marcado como revisado
        erros_t, avisos_t = problemas_no_dispositivo(meta)
        for msg in erros_t:
            erro(f"{rel(caminho)}: {msg}")
        for msg in avisos_t:
            avisos_temporais[msg].append(rel(caminho))

        if meta.get("urn"):
            por_urn[meta["urn"]].append(rel(caminho))

        metas.append(meta)

    for urn, caminhos in por_urn.items():
        if len(caminhos) > 1:
            erro(f"URN duplicada em {len(caminhos)} arquivos: {urn} -> {', '.join(caminhos)}")

    for msg, caminhos in sorted(avisos_temporais.items()):
        exemplo = caminhos[0] if len(caminhos) == 1 else f"{caminhos[0]} e mais {len(caminhos) - 1}"
        aviso(f"{len(caminhos)} dispositivo(s): {msg} ({exemplo})")

    return metas


LIMITE_ORFAS = 0.25  # acima disto, a extração está quebrada, não é ruído


def validar_remissoes(metas: list[dict]) -> None:
    """Remissão órfã é sintoma, não necessariamente defeito.

    Um ponteiro quebrado falha seguro: quem o segue não encontra nada. O caso
    perigoso é o ponteiro ERRADO — apontar para um dispositivo que existe mas
    não é o referido — e esse é evitado na extração, que só resolve remissão
    quando o escopo é internamente afirmado (ver fatiar.remissao_externa).

    Por isso aqui o relato é agregado: órfãs viram aviso com contagem, e só
    viram erro quando a proporção indica que a extração deixou de funcionar.
    """
    existentes = {m["urn"] for m in metas if m.get("urn")}
    normas_ingeridas = {u.split("!")[0] for u in existentes}

    total = 0
    orfas: dict[str, list[str]] = defaultdict(list)
    fora_da_base = 0

    for meta in metas:
        for alvo in meta.get("remete_a") or []:
            total += 1
            if alvo in existentes:
                continue
            # subdivisão (par/inc/ali) resolve para o artigo que a contém
            partes = alvo.split("!")
            artigo = partes[0] + "!" + partes[1].split("_")[0] if len(partes) > 1 else alvo
            if artigo in existentes:
                continue
            if partes[0] in normas_ingeridas:
                orfas[meta["urn"]].append(alvo)
            else:
                fora_da_base += 1

    if fora_da_base:
        aviso(f"{fora_da_base} remissao(oes) para norma ainda nao ingerida")

    if not orfas:
        return

    quantidade = sum(len(v) for v in orfas.values())
    proporcao = quantidade / total if total else 0
    resumo = (
        f"{quantidade} de {total} remissoes ({proporcao:.0%}) apontam para "
        f"dispositivo inexistente em norma ja ingerida, a partir de "
        f"{len(orfas)} artigo(s)"
    )

    piores = sorted(orfas.items(), key=lambda kv: -len(kv[1]))[:5]
    detalhe = "; ".join(f"{urn.split('!')[-1]}: {len(alvos)}" for urn, alvos in piores)

    if proporcao > LIMITE_ORFAS:
        erro(
            f"{resumo}. Concentracao: {detalhe}. "
            "Proporcao alta indica fatiamento ou extracao quebrados — "
            "rode 'fatiar.py --relatorio' e confira a faixa de artigos proprios."
        )
    else:
        aviso(f"{resumo}. Concentracao: {detalhe}")


def validar_hashes() -> None:
    if not MANIFEST.exists():
        aviso("fontes/manifest.json inexistente — nada ingerido ainda")
        return
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for chave, registro in manifest.get("documentos", {}).items():
        caminho = caminho_fonte(registro)
        if not caminho.exists():
            erro(f"manifest {chave}: arquivo arquivado ausente ({registro['arquivo']})")
            continue
        atual = sha256_arquivo(caminho)
        if atual != registro["sha256"]:
            erro(
                f"manifest {chave}: sha256 diverge do arquivo em disco "
                f"(declarado {registro['sha256'][:16]}..., real {atual[:16]}...)"
            )


def validar_interpretacoes() -> None:
    if not DIR_INTERPRETACOES.exists():
        return
    for caminho in sorted(DIR_INTERPRETACOES.rglob("*.md")):
        if caminho.name.upper().startswith("README"):
            continue
        try:
            meta, corpo = ler_frontmatter(caminho)
        except ValueError as exc:
            erro(str(exc))
            continue

        if meta.get("camada") != 3:
            erro(f"{rel(caminho)}: /interpretacoes/ exige camada 3")
        if not (meta.get("fundamenta_se_em") or []):
            erro(f"{rel(caminho)}: interpretacao sem citacao de dispositivo "
                 "(fundamenta_se_em vazio) — PREMISSAS.md §4.1")
        if not meta.get("autor"):
            erro(f"{rel(caminho)}: interpretacao sem autor")
        if meta.get("confianca") not in {"literal", "derivado", "controverso", "pendente"}:
            erro(f"{rel(caminho)}: grau de confianca invalido: {meta.get('confianca')!r}")


def validar_revisoes_temporais(metas: list[dict]) -> None:
    """Revisão humana em temporal/propostas/ coerente, e já refletida em normas/.

    Decisão tomada e não aplicada é erro: a base responderia com a data
    provisória enquanto o revisor acredita que a correção está em vigor.
    """
    pasta = DIR_TEMPORAL / "propostas"
    if not pasta.exists():
        return
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    for caminho in sorted(pasta.glob("*.yaml")):
        slug = caminho.stem
        registro = (manifest.get("documentos") or {}).get(f"{slug}/texto_compilado")
        if not registro:
            aviso(f"temporal/propostas/{caminho.name}: norma sem fonte no manifest")
            continue
        da_norma = [m for m in metas if m.get("norma_slug") == slug]
        revisoes, erros_rev = carregar_revisoes(
            caminho, registro["sha256"], {m["urn"] for m in da_norma})
        for msg in erros_rev:
            erro(f"temporal/propostas/{caminho.name}: {msg}")
        for msg in revisoes_nao_aplicadas(revisoes, da_norma):
            erro(f"temporal/propostas/{caminho.name}: {msg}")


def relatar_pendencias(metas: list[dict]) -> None:
    pendentes = [m for m in metas if m.get("revisao_temporal_pendente")]
    if pendentes:
        aviso(
            f"{len(pendentes)} de {len(metas)} dispositivos com "
            "revisao_temporal_pendente: vigencia e eficacia ainda sao provisorias "
            "(primeira publicacao, ou data do ato). Revisar a clausula de vigencia "
            "antes de usar em producao."
        )
    nao_confirmadas = [m for m in metas
                       if isinstance(m.get("publicacao"), dict)
                       and m["publicacao"].get("fonte") == "rodape_compilado"]
    if nao_confirmadas:
        aviso(
            f"{len(nao_confirmadas)} de {len(metas)} dispositivos com a data de publicacao "
            "lida do rodape do texto compilado, nao confirmada no DOU (PREMISSAS.md §1.4)."
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--estrito", action="store_true", help="avisos tambem falham")
    args = ap.parse_args()

    metas = validar_dispositivos()
    validar_remissoes(metas)
    validar_hashes()
    validar_interpretacoes()
    validar_revisoes_temporais(metas)
    relatar_pendencias(metas)

    if not metas:
        aviso("nenhum dispositivo em /normas/ — base vazia")

    # Enxurrada de mensagens é inútil: esconde o que importa e não cabe na
    # tela. Mostra as primeiras e diz quantas sobraram.
    LIMITE = 25
    for msg in avisos[:LIMITE]:
        print(f"AVISO  {msg}")
    if len(avisos) > LIMITE:
        print(f"AVISO  ... e mais {len(avisos) - LIMITE} aviso(s)")

    for msg in erros[:LIMITE]:
        print(f"ERRO   {msg}", file=sys.stderr)
    if len(erros) > LIMITE:
        print(f"ERRO   ... e mais {len(erros) - LIMITE} erro(s)", file=sys.stderr)

    print(f"\n{len(metas)} dispositivo(s) validado(s) — "
          f"{len(erros)} erro(s), {len(avisos)} aviso(s)")

    if erros:
        return 1
    if args.estrito and avisos:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
