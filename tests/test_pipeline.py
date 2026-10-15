"""Testes do pipeline, contra fixtures de MARCAÇÃO REAL com TEXTO inventado.

Os fixtures em tests/fixtures/ reproduzem a marcação que o portal do Planalto
de fato publica — observada nos HTML arquivados em fontes/ — com texto
INVENTADO. Norma real nunca entra em teste: texto normativo só existe na base
vindo de fonte oficial baixada, com hash (PREMISSAS.md §1.1).

Por que isto importa: o fixture anterior era sintético também na marcação. Ele
codificava a marcação que se supunha e passou verde em quatro rodadas em que a
ingestão real falhou. O que torna estes fixtures confiáveis é o cabeçalho de
cada um, que lista cada construção de marcação e onde ela foi observada.

Todo valor esperado aqui é um literal derivado à mão a partir do fixture — nunca
calculado pelo código sob teste.

Uso:
    python tests/test_pipeline.py
"""
from __future__ import annotations

import re
import sys
import traceback
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "pipeline"))

import fatiar as F  # noqa: E402
from comum import status_em, urn_dispositivo, urn_norma  # noqa: E402
from fatiar import (  # noqa: E402
    chave_ordem,
    detectar_encoding,
    extrair_externas,
    extrair_remissoes,
    nome_arquivo,
    subdivisoes_de,
)

FIXTURES = Path(__file__).parent / "fixtures"
URN_BASE = urn_norma("br:federal:lei.complementar", "1900-01-01", "999")

falhas: list[str] = []
CENARIOS: list[tuple[str, object]] = []


def checar(condicao: bool, descricao: str) -> None:
    if condicao:
        print(f"  ok   {descricao}")
    else:
        print(f"  FALHA {descricao}")
        falhas.append(descricao)


def cenario(titulo: str):
    """Registra um cenário. Uma exceção em um cenário é FALHA dele, não aborta os demais."""

    def registrar(fn):
        CENARIOS.append((titulo, fn))
        return fn

    return registrar


def fixture(nome: str) -> bytes:
    """Os fixtures ficam em UTF-8 para poderem ser editados; o portal publica em
    windows-1252, então os bytes entregues ao parser são recodificados."""
    return (FIXTURES / nome).read_text(encoding="utf-8").encode("cp1252")


def sem_erro(avisos: list[str]) -> bool:
    return not any(a.startswith("ERRO") for a in avisos)


def com_erro(avisos: list[str]) -> bool:
    return any(a.startswith("ERRO") for a in avisos)


def por_numero(artigos: list[dict], numero: str) -> dict:
    return next(a for a in artigos if a["numero"] == numero)


# ---------------------------------------------------------------------------
# Extração do HTML
# ---------------------------------------------------------------------------

@cenario("extração: quebra de linha do código-fonte não é quebra de parágrafo")
def extracao_hard_wrap():
    """Quebra: voltar a fatiar por '\\n' do código-fonte. O portal quebra o HTML
    no meio do parágrafo, e uma remissão ('arts. 156-A', 'art. 195, I') que cai
    no início de uma linha do código vira, para o parser, início de artigo."""
    linhas = F.html_para_linhas(fixture("planalto-ec.html"))
    completas = [ln.completa for ln in linhas]
    checar(
        "j) os conflitos fictícios relacionados aos tributos previstos nos "
        "arts. 156-A e 195, V;" in completas,
        "parágrafo quebrado em três linhas no código-fonte sai como UMA linha",
    )
    checar(
        not any(re.match(r"^arts?\.", c) for c in completas),
        "nenhuma linha extraída começa com remissão 'art(s).' em minúscula",
    )
    checar(
        'Art. 3º A revogação do art. 195, I, "b", não produzirá efeitos '
        "fictícios antes do prazo." in completas,
        "remissão 'art. 195' que abria linha no código-fonte volta ao seu parágrafo",
    )


@cenario("extração: charset")
def extracao_charset():
    """Quebra: confiar só no charset declarado. A EC declara windows-1252; a LC
    não declara nenhum (o padrão do detector é utf-8) e os bytes são cp1252, de
    modo que o decode estrito como UTF-8 falha e a reserva cp1252 tem de agir."""
    ec, lc = fixture("planalto-ec.html"), fixture("planalto-lc.html")
    checar(detectar_encoding(ec) == "windows-1252", "EC: charset declarado é lido")
    checar(detectar_encoding(lc) == "utf-8", "LC: sem declaração, o padrão é utf-8")
    texto_lc = F.html_para_texto(lc)
    checar("Redação dada pela Lei Complementar" in texto_lc,
           "LC: bytes cp1252 sob padrão utf-8 decodificam certo (reserva cp1252)")
    # 'Ã' sozinho existe em "REVOGAÇÃO"; o mojibake de ç/ã/é lidos como cp1252-sobre-UTF-8
    # é 'Ã§', 'Ã£', 'Ã©'.
    checar("�" not in texto_lc and not any(m in texto_lc for m in ("Ã§", "Ã£", "Ã©")),
           "LC: sem caractere de substituição nem mojibake")
    texto_ec = F.html_para_texto(ec)
    checar("Constituição fictícia" in texto_ec, "EC: windows-1252 decodifica certo")


@cenario("extração: <script>, <style> e <head> não vazam")
def extracao_ruido():
    html = (
        '<html><head><title>NAO DEVE APARECER</title><style>.x{color:red}</style></head>'
        '<body><p>Art. 1º Texto.</p><script>var ruido = "script nao aparece";</script>'
        "</body></html>"
    ).encode("utf-8")
    texto = F.html_para_texto(html)
    checar(texto == "Art. 1º Texto.", f"só o corpo sobrevive (obteve {texto!r})")


@cenario("extração: iso-8859-1 declarado")
def extracao_latin1():
    html_latin = (
        '<html><head><meta charset="iso-8859-1"></head><body>'
        "<p>Art. 1º Operação com acentuação.</p></body></html>"
    ).encode("latin-1")
    checar("Operação" in F.html_para_texto(html_latin), "decodifica iso-8859-1 corretamente")


# ---------------------------------------------------------------------------
# Classificação próprio x citado — marcação da EC (aspas retas)
# ---------------------------------------------------------------------------

@cenario("EC (aspas retas): artigo próprio x artigo de outra norma")
def ec_classificacao():
    """Quebras que este cenário captura, todas medidas no HTML real da EC 132:
      - fechamento '" (NR)' na mesma linha não era reconhecido
      - aspas interna ("b".) no fim de linha fechava o bloco inteiro
      - artigo seguinte do bloco (156-B) não tem aspa de abertura
      - fragmento 'art. 195, I' no início de linha virava artigo
    """
    artigos, avisos, stats = F.fatiar(F.html_para_linhas(fixture("planalto-ec.html")))
    numeros = [a["numero"] for a in artigos]
    checar(numeros == ["1", "2", "3", "4"], f"artigos próprios são 1, 2, 3, 4 (obteve {numeros})")
    checar(sem_erro(avisos), f"sem ERRO (obteve {avisos})")

    art1, art2, art3 = (por_numero(artigos, n) for n in ("1", "2", "3"))
    checar(
        art1["citados"] == ["43", "105", "150", "156-B"],
        f"art. 1 promove a inserção de 43, 105, 150 e 156-B (obteve {art1['citados']})",
    )
    checar(art2["citados"] == ["99"], f"art. 2 promove a inserção do 99 (obteve {art2['citados']})")
    checar(art3["citados"] == [], "art. 3 não cita nada")

    # 156-B: sem aspa de abertura, vem depois de uma aspa interna "b". no fim de linha
    checar(
        not any(a["numero"] == "156-B" for a in artigos),
        "156-B (bloco sem aspa de abertura, depois de '\"b\".') NÃO é artigo próprio",
    )
    checar(
        'Art. 156-B. Segundo artigo fictício do mesmo bloco, sem aspa de abertura." (NR)'
        in art1["linhas"],
        "o texto do 156-B fica, verbatim, no corpo do art. 1 que o insere",
    )
    checar(
        art1["linhas_proprias"]
        == ["Art. 1º A Constituição fictícia passa a vigorar com as seguintes alterações:"],
        "linhas_proprias do art. 1 exclui todo o texto inserido",
    )
    checar(
        art3["linhas"]
        == ['Art. 3º A revogação do art. 195, I, "b", não produzirá efeitos fictícios '
            "antes do prazo."],
        "fragmento 'art. 195, I' no início da linha do código-fonte não vira artigo",
    )

    checar(stats["aspas_estado_final"] == 0, "aspas balanceadas ao fim do documento")
    checar(stats["aspas_fechamento_sem_abertura"] == 0, "nenhum fechamento sem abertura")
    checar(stats["aspas_abertura_dentro_de_bloco"] == 0, "nenhuma abertura dentro de bloco")
    checar(stats["discordancia_blockquote"] == 0,
           "aspas e <blockquote> concordam em todo cabeçalho de artigo")

    # Depois do último artigo vêm local/data e assinaturas. Não são do artigo 4.
    art4 = por_numero(artigos, "4")
    checar(
        art4["linhas"]
        == ["Art. 4º Esta Emenda Constitucional fictícia entra em vigor na data de sua "
            "publicação."],
        "o último artigo termina onde o texto da norma termina",
    )
    # Brasília..., Mesa..., rodapé do DOU, "Art. 5º" depois do fim
    checar(stats["linhas_apos_o_fim"] == 4,
           f"4 linhas depois do fim reportadas, não anexadas (obteve {stats['linhas_apos_o_fim']})")


@cenario("remissões não vazam do texto citado")
def remissao_nao_vaza():
    artigos, _, _ = F.fatiar(F.html_para_linhas(fixture("planalto-ec.html")))
    art1 = por_numero(artigos, "1")
    alvo = urn_dispositivo(URN_BASE, "158")
    todas = extrair_remissoes("\n".join(art1["linhas"]), URN_BASE, "1")
    proprias = extrair_remissoes("\n".join(art1["linhas_proprias"]), URN_BASE, "1")
    checar(alvo in todas, "controle: o art. 158 aparece no texto inserido pelo art. 1")
    checar(alvo not in proprias, "mas não entra como remissão do art. 1")


# ---------------------------------------------------------------------------
# Classificação — marcação da LC (aspas curvas, texto superado)
# ---------------------------------------------------------------------------

def _lc():
    return F.fatiar(F.html_para_linhas(fixture("planalto-lc.html")))


@cenario("LC (aspas curvas): sequência e blocos citados")
def lc_classificacao():
    artigos, avisos, stats = _lc()
    numeros = [a["numero"] for a in artigos]
    checar(
        numeros == ["1", "2", "3", "4", "5", "6", "7", "7-A", "8", "9"],
        f"artigos próprios, sem repetição e sem perder os posteriores ao bloco (obteve {numeros})",
    )
    checar(sem_erro(avisos), f"sem ERRO (obteve {avisos})")
    art6 = por_numero(artigos, "6")
    checar(
        art6["citados"] == ["11", "16", "17"],
        f"art. 6 insere 11, 16 e 17; o 17 não tem aspa de abertura (obteve {art6['citados']})",
    )
    checar(
        urn_dispositivo(URN_BASE, "17") not in
        extrair_remissoes("\n".join(art6["linhas_proprias"]), URN_BASE, "6"),
        "nada do texto citado vira remissão do art. 6",
    )
    checar(
        "§ 3º Continuação fictícia do mesmo bloco, depois da aspa simples tipográfica."
        in art6["linhas"] and
        "§ 3º Continuação fictícia do mesmo bloco, depois da aspa simples tipográfica."
        not in art6["linhas_proprias"],
        "aspa simples tipográfica (’) não fecha o bloco: o § 3º seguinte continua citado",
    )
    checar(stats["aspas_estado_final"] == 0, "aspas balanceadas ao fim do documento")
    checar(stats["aspas_fechamento_sem_abertura"] == 1,
           "o ” solto do art. 7 é reportado como anomalia da fonte")
    checar(stats["aspas_abertura_dentro_de_bloco"] == 0, "nenhuma abertura dentro de bloco")
    checar(stats["discordancia_blockquote"] == 0, "aspas e <blockquote> concordam")


@cenario("LC: assinatura e anexos não são do último artigo")
def lc_fim_do_texto():
    """Quebra: anexar ao último artigo tudo que vem depois dele. Na LC 214 real o
    art. 544 ficava com 5.357 linhas (97 KB) — assinatura, rodapé e anexos (29
    linhas 'ANEXO <romano>') — e as remissões das tabelas viravam remissões do
    art. 544."""
    artigos, _, stats = _lc()
    art9 = por_numero(artigos, "9")
    checar(
        art9["linhas"][0] == "Art. 9º Último artigo fictício, que insere um bloco depois da "
                             "aspa solta:"
        and art9["linhas"][-1] == "Art. 31. Segundo artigo do segundo bloco, sem aspa de "
                                  "abertura. ” (NR)",
        "o art. 9 termina onde o texto da norma termina: a última linha é a do bloco citado",
    )
    checar([a["numero"] for a in artigos][-1] == "9",
           "'Art. 77' dentro do anexo não vira artigo")
    checar(stats["linhas_apos_o_fim"] == 7,
           f"7 linhas depois do fim reportadas (obteve {stats['linhas_apos_o_fim']})")
    checar(stats["anexos_nao_incorporados"] == 2,
           f"2 anexos reportados como não incorporados (obteve {stats['anexos_nao_incorporados']})")


@cenario("fim do texto: 'Brasília,' ou 'ANEXO' dentro de bloco citado não encerra a norma")
def fim_do_texto_nao_em_bloco():
    """Quebra: encerrar a norma em qualquer linha que comece com 'ANEXO'. Texto
    citado de outra norma pode conter um (a LC 214 altera leis que têm anexos)."""
    # A linha 'ANEXO I' vem DENTRO do bloco e sem aspa na frente: é ela que exercita
    # a defesa (uma linha que abre com aspa nunca casaria o marcador).
    texto = ('Art. 1º A Lei fictícia passa a vigorar com a alteração:\n'
             '\u201cArt. 9º Primeiro artigo fictício do bloco citado.\n'
             'ANEXO I\n'
             'Linha do anexo da lei alterada. \u201d (NR)\n'
             'Art. 2º Este artigo vem depois e continua sendo da norma.')
    arts, av, st = F.fatiar(texto)
    checar([a["numero"] for a in arts] == ["1", "2"] and st["linhas_apos_o_fim"] == 0,
           "o 'ANEXO I' citado não encerra a norma; o art. 2 é lido")


@cenario("LC: aspa solta não contamina os artigos seguintes")
def lc_aspa_solta():
    """Quebra: contador de profundidade sem piso. O ” sem abertura deixaria a
    profundidade em -1; o bloco aberto DEPOIS dele (art. 9) chegaria só a 0, e o
    '#31', que não tem aspa de abertura, seria lido como artigo próprio."""
    artigos, _, _ = _lc()
    numeros = [a["numero"] for a in artigos]
    checar("7-A" in numeros and "8" in numeros,
           "7-A e 8, posteriores ao ” solto, continuam artigos próprios")
    art9 = por_numero(artigos, "9")
    checar(art9["citados"] == ["30", "31"] and "31" not in numeros,
           f"o bloco aberto depois do ” solto é lido inteiro como citado (obteve {art9['citados']})")


@cenario("aspa reta: a que abre linha dentro de bloco é interna, não abertura")
def aspa_reta_interna():
    """Quebra: tratar toda aspa reta no início de linha como abertura de bloco. A
    mesma aspa abre e fecha, então só a paridade as distingue. Dentro do bloco,
    '"Art. 12"' (referência entre aspas) não é um bloco que abre dentro de outro."""
    texto = ('Art. 1º A emenda insere:\n'
             '"Art. 9º Texto do bloco, que remete a\n'
             '"Art. 12" da lei, entre aspas, em linha que começa com aspa.\n'
             'Fim do bloco." (NR)\n'
             'Art. 2º Próximo artigo da emenda.')
    arts, av, st = F.fatiar(texto)
    checar([a["numero"] for a in arts] == ["1", "2"], "só os arts. 1 e 2 são próprios")
    checar(st["aspas_abertura_dentro_de_bloco"] == 0,
           "a aspa reta interna não é contada como bloco aberto dentro de bloco")
    checar(st["aspas_estado_final"] == 0, "e a paridade fecha ao fim do bloco")


@cenario("anomalias de aspas são contadas, não escondidas")
def anomalias_de_aspas():
    """Quebra: contadores que ficam em zero qualquer que seja a entrada. Bloco que
    abre dentro de outro (fechamento perdido) e bloco que nunca fecha."""
    texto = ("Art. 1º A lei passa a vigorar assim:\n"
             "“Art. 9º Primeiro bloco, que nunca fecha.\n"
             "“Art. 10 Segundo bloco, aberto dentro do primeiro. ” (NR)\n"
             "Art. 2º Este vem depois e é lido como citado, porque o bloco ficou aberto.")
    arts, av, st = F.fatiar(texto)
    checar(st["aspas_abertura_dentro_de_bloco"] == 1, "a abertura dentro de bloco é contada")
    checar(st["aspas_estado_final"] == 1, "o saldo final diferente de zero é reportado")
    checar([a["numero"] for a in arts] == ["1"],
           "e o que veio depois do bloco aberto fica como citado (a anomalia é o aviso)")
    checar(any("ficou aberto" in a for a in av) and sem_erro(av),
           "com aviso, não com ERRO: o fatiamento é reportado, não abortado")


@cenario("LC: redação superada se funde ao dispositivo, sem colidir")
def lc_redacao_superada():
    """Quebra: tratar a redação riscada e a nova como dois artigos de mesmo número
    (colisão, que aborta a escrita) ou descartar a anterior sem registro."""
    artigos, _, stats = _lc()
    checar([a["numero"] for a in artigos].count("2") == 1, "o art. 2 existe uma única vez")
    art2 = por_numero(artigos, "2")
    checar(
        art2["linhas"][:2]
        == ["~~Art. 2º Redação antiga fictícia do segundo artigo, superada pela lei "
            "posterior:~~",
            "~~I - inciso antigo fictício;~~"],
        "a redação anterior fica no corpo, marcada ~~riscada~~, na ordem da fonte",
    )
    checar(
        art2["linhas"][2]
        == "Art. 2º Considera-se operação fictícia a que existir apenas em ambiente de "
           "teste. (Redação dada pela Lei Complementar nº 998, de 2030)",
        "depois vem a redação nova, sem marca",
    )
    checar(
        art2["linhas_proprias"][0]
        == "Art. 2º Considera-se operação fictícia a que existir apenas em ambiente de "
           "teste. (Redação dada pela Lei Complementar nº 998, de 2030)"
        and not any("antig" in ln for ln in art2["linhas_proprias"]),
        "linhas_proprias (base dos metadados) só tem a redação vigente",
    )
    subs = subdivisoes_de(art2["linhas_proprias"], URN_BASE, "2")
    checar(
        subs == [
            urn_dispositivo(URN_BASE, "2", inciso="I"),
            urn_dispositivo(URN_BASE, "2", inciso="II"),
            urn_dispositivo(URN_BASE, "2", paragrafo="U"),
        ],
        f"subdivisões só da redação vigente: um inciso I, não dois (obteve {subs})",
    )
    rem = extrair_remissoes("\n".join(art2["linhas_proprias"]), URN_BASE, "2")
    checar(
        urn_dispositivo(URN_BASE, "1", paragrafo="1") in rem,
        "captura '§ 1º do art. 1º' como parágrafo",
    )
    checar(stats["redacoes_anteriores_mescladas"] == 1, "uma redação anterior foi mesclada")


@cenario("LC: <strike> vale como line-through; anotação não perde o referente")
def lc_strike_e_anotacao():
    """Quebra: descartar o § 9º riscado deixaria a anotação '(Revogado ...)' solta no
    corpo do art. 3, que passaria a parecer revogado por inteiro."""
    artigos, _, _ = _lc()
    art3 = por_numero(artigos, "3")
    checar(
        art3["linhas"]
        == ["Art. 3º Artigo fictício que contém um parágrafo revogado.",
            "~~§ 9º Parágrafo antigo fictício, com termo em itálico.~~ "
            "(Revogado pela Lei Complementar nº 998, de 2030)"],
        "o § 9º riscado por <strike> fica marcado, com a anotação colada a ele",
    )
    checar(
        art3["linhas_proprias"]
        == ["Art. 3º Artigo fictício que contém um parágrafo revogado.",
            "(Revogado pela Lei Complementar nº 998, de 2030)"],
        "a base dos metadados não inclui o texto do § 9º revogado",
    )
    checar(
        subdivisoes_de(art3["linhas_proprias"], URN_BASE, "3") == [],
        "o § 9º revogado não é subdivisão vigente do art. 3",
    )


@cenario("LC: artigo revogado")
def lc_artigo_revogado():
    artigos, _, _ = _lc()
    art4 = por_numero(artigos, "4")
    checar(
        art4["linhas"]
        == ["~~Art. 4º Texto fictício do artigo revogado, mantido riscado:~~ "
            "(Revogado pela Lei Complementar nº 998, de 2030)",
            "~~I - inciso fictício do artigo revogado;~~"],
        "artigo revogado mantém o texto marcado e a anotação",
    )
    checar(
        art4["linhas_proprias"] == ["(Revogado pela Lei Complementar nº 998, de 2030)"],
        "do artigo revogado só a anotação é texto vigente",
    )


@cenario("LC: riscado no meio de parágrafo vivo e rótulo duplicado")
def lc_riscado_parcial():
    artigos, _, _ = _lc()
    art5, art6 = por_numero(artigos, "5"), por_numero(artigos, "6")
    checar(
        art5["linhas"]
        == ["Art. 5º Texto vivo fictício ~~palavras antigas fictícias~~ palavras novas "
            "fictícias do artigo quinto."],
        "trecho riscado dentro do parágrafo é marcado só no trecho",
    )
    checar(
        art5["linhas_proprias"]
        == ["Art. 5º Texto vivo fictício palavras novas fictícias do artigo quinto."],
        "e sai por inteiro da base dos metadados, sem espaço duplo",
    )
    checar(
        art6["linhas"][0]
        == "Art. 6º A Lei fictícia nº 997 passa a vigorar com as seguintes alterações: "
           "~~Produção de efeitos~~ Produção de efeitos",
        "rótulo 'Produção de efeitos' riscado + cópia sem riscar",
    )


@cenario("LC: estrutura hierárquica")
def lc_hierarquia():
    artigos, _, _ = _lc()
    checar(
        por_numero(artigos, "1")["hierarquia"] == ["LIVRO I", "TÍTULO I", "CAPÍTULO I"],
        "hierarquia do art. 1",
    )
    checar(
        por_numero(artigos, "3")["hierarquia"] == ["LIVRO I", "TÍTULO I", "CAPÍTULO II"],
        "CAPÍTULO II substitui CAPÍTULO I no mesmo nível",
    )
    checar(
        por_numero(artigos, "2")["hierarquia"] == ["LIVRO I", "TÍTULO I", "CAPÍTULO I"],
        "a redação mesclada mantém a hierarquia do primeiro cabeçalho",
    )


@cenario("LC: contagem de trechos riscados")
def lc_estatisticas():
    _, _, stats = _lc()
    # Art. 2 antigo (2 linhas) + art. 3 § 9º + art. 4 (2 linhas) + art. 5 + art. 6
    checar(stats["linhas_com_riscado"] == 7,
           f"7 linhas com texto riscado (obteve {stats['linhas_com_riscado']})")


@cenario("remissões e subdivisões no art. 1")
def lc_remissoes_art1():
    artigos, _, _ = _lc()
    art1 = por_numero(artigos, "1")
    corpo1 = "\n".join(art1["linhas_proprias"])
    rem1 = extrair_remissoes(corpo1, URN_BASE, "1")
    checar(urn_dispositivo(URN_BASE, "4") in rem1, "art. 1 remete ao art. 4")
    checar(urn_dispositivo(URN_BASE, "2", inciso="II") in rem1,
           "captura 'inciso II do art. 2' como subdivisão")
    checar(not any(r.split("!")[1].split("_")[0] == "art1" for r in rem1),
           "não registra auto-remissão")
    subs = subdivisoes_de(art1["linhas_proprias"], URN_BASE, "1")
    checar(urn_dispositivo(URN_BASE, "1", paragrafo="1") in subs, "captura § 1º")
    checar(urn_dispositivo(URN_BASE, "1", paragrafo="2", inciso="I") in subs,
           "inciso herda o parágrafo corrente")
    checar(urn_dispositivo(URN_BASE, "1", paragrafo="2", inciso="I", alinea="a") in subs,
           "alínea herda parágrafo e inciso")


# ---------------------------------------------------------------------------
# Regras de abortar
# ---------------------------------------------------------------------------

@cenario("fatiar aborta em vez de classificar em silêncio")
def abortos():
    """Antes, artigo fora de ordem e sem aspas virava 'citado' em silêncio, e um
    único falso positivo alto fazia todo o resto do documento virar 'citado'. Agora
    a numeração é VALIDAÇÃO: o que a violar interrompe a escrita."""
    _, av = F.fatiar("Art. 1º a\nArt. 2º b\nArt. 2º c")[:2]
    checar(com_erro(av), "dois artigos próprios de mesmo número: ERRO (sobrescreveria arquivo)")
    _, av = F.fatiar("Art. 1º a\nArt. 3º b\nArt. 2º c")[:2]
    checar(com_erro(av), "artigo próprio fora de ordem, sem aspas: ERRO (não vira 'citado')")
    arts, av, _ = F.fatiar("Art. 1º a\nArt. 2º b\nArt. 3º c")
    checar(sem_erro(av) and len(arts) == 3, "sequência regular não gera ERRO")


@cenario("fatiar: 'Art.' minúsculo no início de linha não abre artigo")
def cabecalho_exige_maiuscula():
    """Quebra: voltar RE_ARTIGO para IGNORECASE. Defesa em profundidade além da
    extração: o portal publica cabeçalho sempre com 'Art.' maiúsculo."""
    arts, _, _ = F.fatiar('Art. 1º a\nart. 195, I, "b", não produzirá efeitos')
    checar([a["numero"] for a in arts] == ["1"], "só o 'Art. 1º' abre artigo")
    checar(arts[0]["linhas"][-1] == 'art. 195, I, "b", não produzirá efeitos',
           "a linha com a remissão continua no corpo do art. 1")


@cenario("verificação cruzada: aspas x <blockquote>")
def blockquote_cruzado():
    """O portal marca texto citado de duas formas independentes. Se discordarem, a
    discordância é reportada — não resolvida em silêncio por um dos sinais."""
    html = (
        "<html><body><p>Art. 1º A lei passa a vigorar assim:</p>"
        "<p>“Art. 9º Texto citado sem <i>blockquote</i>.” (NR)</p>"
        "<p>Art. 2º Segundo artigo.</p></body></html>"
    ).encode("utf-8")
    artigos, avisos, stats = F.fatiar(F.html_para_linhas(html))
    checar([a["numero"] for a in artigos] == ["1", "2"],
           "a classificação segue as aspas (9 é citado)")
    checar(stats["discordancia_blockquote"] == 1,
           "e a discordância com o <blockquote> ausente é contada")


@cenario("aspa de abertura ausente: <blockquote> e link para a norma alterada concordam")
def abertura_implicita():
    """Markup medido na LC 227 (compilado do Planalto): dentro do <blockquote>, o
    cabeçalho '<a href="Lcp214.htm#art493a">Art. 493-A.</a> É instituída...' vem
    SEM a aspa de abertura, e o '”' que fecha o trecho está no fim do § 15.
    Quebra: ler o 493-A como artigo próprio (a escrita aborta por ordem) ou, pior,
    reclassificar com UM sinal só."""
    def html(link: bool, bq: bool, alvo: str = "Lfict.htm#art7a") -> bytes:
        cab = f'<a href="{alvo}">Art. 7º-A.</a>' if link else "Art. 7º-A."
        abre, fecha = ("<blockquote>", "</blockquote>") if bq else ("", "")
        return (
            "<html><body><p>Art. 1º A Lei fictícia passa a vigorar com as seguintes "
            f"alterações:</p>{abre}"
            '<p>“<a href="Lfict.htm#art5">Art. 5º</a> Texto citado.” (NR)</p>'
            f"<p>{cab} Texto inserido, sem a aspa de abertura.</p>"
            "<p>§ 1º Parágrafo inserido.”</p>"
            f"{fecha}<p>Art. 2º Esta Lei entra em vigor na data de sua publicação.</p>"
            "</body></html>"
        ).encode("utf-8")

    artigos, avisos, stats = F.fatiar(F.html_para_linhas(html(link=True, bq=True)))
    checar([a["numero"] for a in artigos] == ["1", "2"],
           f"7-A é citado: os dois sinais concordam (obteve {[a['numero'] for a in artigos]})")
    checar(artigos[0]["citados"] == ["5", "7-A"], "e fica com o artigo que o insere")
    checar(stats["aspas_fechamento_sem_abertura"] == 0 and stats["discordancia_blockquote"] == 0,
           "o '”' do § 1º fecha o bloco aberto: nada órfão, nada discordante")
    checar(any("7-A" in a and "abertura" in a for a in avisos),
           f"a correção é reportada, não silenciosa (avisos: {avisos})")

    for link, bq in ((False, True), (True, False)):
        artigos, avisos, _ = F.fatiar(F.html_para_linhas(html(link=link, bq=bq)))
        checar("7-A" in [a["numero"] for a in artigos]
               and any(a.startswith("ERRO") for a in avisos),
               f"um sinal só (link={link}, blockquote={bq}): nada é reclassificado, e a "
               "ordem acusa o erro")
    artigos, _, _ = F.fatiar(F.html_para_linhas(html(link=True, bq=True, alvo="#art7a")))
    checar("7-A" in [a["numero"] for a in artigos],
           "link para âncora do MESMO arquivo não é sinal de outra norma")


URN_999 = "urn:lex:br:federal:lei.complementar:1900-01-03;999"


@cenario("anotação ligada ao artigo que fez a alteração")
def alteracoes_ligadas():
    """Markup medido no compilado da LC 214: '<a href="Lcp227.htm#art174">(Incluído
    pela Lei Complementar nº 227, de 2026)</a>' — a anotação é um link para o artigo
    da lei alteradora. Quebra: perder o link (o artigo alterado fica sem saber de
    quem vem a vigência do texto novo), ligar a um artigo inventado a partir de
    âncora irregular, ou tomar link de remissão comum por alteração."""
    import alteracoes as A

    html = ('<p>§ 1º Texto. <a href="Lcp999.htm#art7">(Incluído pela Lei Complementar nº '
            '999, de 1900)</a></p><p>Art. 2º Ver o <a href="#art1">art. 1º</a>.</p>').encode("utf-8")
    linhas = F.html_para_linhas(html)
    checar(linhas[0].links == (("Lcp999.htm#art7",
                                "(Incluído pela Lei Complementar nº 999, de 1900)"),)
           and linhas[1].links == (("#art1", "art. 1º"),),
           f"cada linha guarda seus links (obteve {[l.links for l in linhas]})")

    mapa = {"lcp999.htm": URN_999}
    checar(A.resolver_link("Lcp999.htm#art7", mapa) == URN_999 + "!art7"
           and A.resolver_link("../lcp/LCP999.htm#art7a", mapa) == URN_999 + "!art7-A",
           "arquivo de norma ingerida + âncora 'artN': URN do artigo")
    checar(A.resolver_link("Lcp999.htm#art181-4-a", mapa) is None
           and A.resolver_link("outra.htm#art7", mapa) is None
           and A.resolver_link("#art7", mapa) is None and A.resolver_link("Lcp999.htm", mapa) is None,
           "âncora irregular, norma não ingerida, mesmo arquivo ou sem âncora: não resolve")

    corpo = ["Art. 3º Caput.",
             "§ 1º Texto. (Incluído pela Lei Complementar nº 999, de 1900)",
             "~~§ 2º Antigo.~~ (Revogado pela Lei Complementar nº 999, de 1900)",
             "§ 3º Ver o art. 1º."]
    links = [(), (("Lcp999.htm#art7", "(Incluído pela Lei Complementar nº 999, de 1900)"),),
             (("Lcp999.htm#art9", "(Revogado pela Lei Complementar nº 999, de 1900)"),),
             (("#art1", "art. 1º"),)]
    r = A.alteracoes_do_artigo(corpo, links, URN_BASE, "3", mapa)
    checar(r == [
        {"anotacao": "(Incluído pela Lei Complementar nº 999, de 1900)",
         "subdivisao": urn_dispositivo(URN_BASE, "3", paragrafo="1"),
         "link": "Lcp999.htm#art7", "ato": URN_999 + "!art7"},
        {"anotacao": "(Revogado pela Lei Complementar nº 999, de 1900)",
         "subdivisao": urn_dispositivo(URN_BASE, "3", paragrafo="2"),
         "link": "Lcp999.htm#art9", "ato": URN_999 + "!art9"},
    ], f"só links de anotação, com a subdivisão onde estão (obteve {r})")
    isolada = A.alteracoes_do_artigo(
        ["Art. 3º Caput.", "(Incluído pela Lei Complementar nº 999, de 1900)"],
        [(), (("Lcp999.htm#art7", "(Incluído pela Lei Complementar nº 999, de 1900)"),)],
        URN_BASE, "3", mapa)
    checar(isolada == [{"anotacao": "(Incluído pela Lei Complementar nº 999, de 1900)",
                        "subdivisao": None, "isolada": True, "link": "Lcp999.htm#art7",
                        "ato": URN_999 + "!art7"}],
           "anotação sozinha na linha (LC 214: a do título inserido, que caiu no artigo "
           "anterior): sem subdivisão, marcada como isolada")

    nome = "Lei Complementar nº 214"
    alteradora = ({"dispositivos_citados": ["3", "5"]},
                  "Art. 7º A Lei Complementar nº 214, de 1º de janeiro de 1900, passa a vigorar "
                  "com as seguintes alterações:\n\n“Art. 3º ...”")
    checar(A.conferir("3", nome, *alteradora) == "citacao"
           and A.conferir("4", nome, *alteradora) is None,
           "artigo de alteração: confirma só o que ele cita, se o caput nomeia a norma")
    outra = ({"dispositivos_citados": ["3"]},
             "Art. 7º A Lei nº 1, de 1900, passa a vigorar com as seguintes alterações:")
    prefixo = ({"dispositivos_citados": ["3"]},
               "Art. 7º A Lei Complementar nº 2140, de 1900, passa a vigorar com as seguintes "
               "alterações:")
    checar(A.conferir("3", nome, *outra) is None and A.conferir("3", nome, *prefixo) is None,
           "cita o art. 3º, mas de outra norma (ou 'nº 2140', não 'nº 214'): não confirma")
    revogadora = ({"dispositivos_citados": []},
                  "Art. 9º Revogam-se:\n\nI - os seguintes dispositivos da Lei nº 1, de 1900:\n\n"
                  "a) o art. 4º;\n\nII - os seguintes dispositivos da Lei Complementar nº 214, "
                  "de 1º de janeiro de 1900:\n\na) o § 8º do art. 3º;\n\nb) os arts. 6º e 8º.")
    checar(A.conferir("3", nome, *revogadora) == "lista_de_revogacao"
           and A.conferir("8", nome, *revogadora) == "lista_de_revogacao",
           "artigo de revogação: confirma o que está no inciso que nomeia a norma")
    checar(A.conferir("4", nome, *revogadora) is None,
           "o art. 4º revogado é de OUTRA lei (inciso I): não confirma")


@cenario("validação: a ligação da anotação é conferida no artigo alterador")
def validar_alteracoes():
    """Quebra: aceitar link de anotação que o artigo alterador não confirma, ou
    calar quando o alterador não está na base."""
    import validar as V

    base = URN_BASE
    alterado = ({"urn": base + "!art3", "norma": "Lei Complementar nº 214, de 1º de janeiro de 1900",
                 "alterado_por": [
                     {"anotacao": "(Incluído pela ...)", "subdivisao": base + "!art3_par1",
                      "link": "Lcp999.htm#art7", "ato": URN_999 + "!art7"},
                     {"anotacao": "(Incluído pela ...)", "subdivisao": base + "!art3_par2",
                      "link": "Lcp999.htm#art8", "ato": URN_999 + "!art8"},
                     {"anotacao": "(Vide ADI 1)", "subdivisao": base + "!art3",
                      "link": "https://stf/x", "ato": None},
                     {"anotacao": "(Incluído pela ...)", "subdivisao": base + "!art3_par3",
                      "link": "Lcp999.htm#art50", "ato": URN_999 + "!art50"},
                     {"anotacao": "(Incluído pela ...)", "subdivisao": None, "isolada": True,
                      "link": "Lcp999.htm#art8", "ato": URN_999 + "!art8"}]}, "Art. 3º ...")
    art7 = ({"urn": URN_999 + "!art7", "dispositivos_citados": ["3"]},
            "Art. 7º A Lei Complementar nº 214, de 1º de janeiro de 1900, passa a vigorar com "
            "as seguintes alterações:")
    art8 = ({"urn": URN_999 + "!art8", "dispositivos_citados": ["4"]},
            "Art. 8º A Lei Complementar nº 214, de 1º de janeiro de 1900, passa a vigorar com "
            "as seguintes alterações:")
    r = V.conferir_alteracoes([alterado, art7, art8])
    checar(r["confirmadas"] == 1 and r["sem_ato"] == 1
           and [x.split("!")[-1] for x in r["nao_confirmadas"]] == ["art8"]
           and [x.split("!")[-1] for x in r["alterador_ausente"]] == ["art50"]
           and [x.split("!")[-1] for x in r["isoladas_nao_confirmadas"]] == ["art8"],
           f"uma confirmada, uma que o alterador não cita, uma sem alterador na base, uma "
           f"sem ato, e a isolada não confirmada contada à parte (obteve {r})")


@cenario("normas/ reais: LC 214 ligada às leis que a alteraram (pulado se ausentes)")
def alteracoes_reais():
    """Contrato com o compilado da LC 214: anotações do art. 26 e do art. 482-A
    apontam para 'Lcp227.htm#art174' (lido no HTML)."""
    if not (RAIZ / "normas" / "lc-214-2025").exists():
        print("  pulado: normas/lc-214-2025 ausente")
        return
    from comum import ler_frontmatter

    art174 = urn_norma("br:federal:lei.complementar", "2026-01-13", "227") + "!art174"
    meta, _ = ler_frontmatter(RAIZ / "normas" / "lc-214-2025" / "art-0482-A.md")
    da_227 = [a for a in meta.get("alterado_por") or [] if "227" in a["anotacao"]]
    checar(da_227 and all(a["ato"] == art174 for a in da_227),
           f"482-A: as anotações da LC 227 ligadas ao art. 174 dela (obteve {da_227[:2]})")
    meta, _ = ler_frontmatter(RAIZ / "normas" / "lc-214-2025" / "art-0026.md")
    checar(any(a["ato"] == art174 for a in meta.get("alterado_por") or []),
           "art. 26: ligado ao art. 174 da LC 227")


# ---------------------------------------------------------------------------
# Escopo da remissão — operam sobre texto, sem depender do HTML
# ---------------------------------------------------------------------------

@cenario("escopo da remissão (ponteiro errado é pior que ausente)")
def escopo_remissao():
    texto = ("Aplica-se o disposto no art. 155 da Constituição Federal e no art. 90 "
             "da Lei nº 995, de 1896, sem prejuízo do art. 3º desta Lei.")
    rem = extrair_remissoes(texto, URN_BASE, "7")
    checar(urn_dispositivo(URN_BASE, "155") not in rem,
           "'art. 155 da Constituição' NÃO resolve no namespace próprio")
    checar(urn_dispositivo(URN_BASE, "90") not in rem,
           "'art. 90 da Lei nº 995' NÃO resolve no namespace próprio")
    checar(urn_dispositivo(URN_BASE, "3") in rem,
           "'art. 3º desta Lei' resolve, porque o escopo interno é afirmado")


@cenario("'do ADCT' é qualificador externo")
def escopo_adct():
    """Quebra: o detector de escopo externo não conhecia a sigla. Medido na LC 214
    real: 'art. 92-A do ADCT' (arts. 388, 439 e 458) virava remissão para o
    art. 92-A da própria LC, que não existe."""
    rem = extrair_remissoes(
        "aplicam-se até a data estabelecida pelo art. 92-A do ADCT, e o art. 3º.",
        URN_BASE, "439",
    )
    checar(urn_dispositivo(URN_BASE, "92-A") not in rem, "'art. 92-A do ADCT' não resolve")
    checar(urn_dispositivo(URN_BASE, "3") in rem, "o 'art. 3º' seguinte continua interno")


@cenario("o qualificador liga-se à menção mais próxima")
def qualificador_proximo():
    """Regressão: a janela ia longe demais e um 'da Lei' no fim da frase descartava
    as remissões internas anteriores. Derrubou as remissões da base real de
    milhares para 82."""
    frase = "observado o art. 12 e o art. 15 da Lei nº 9.430, de 1996"
    rem = extrair_remissoes(frase, URN_BASE, "99")
    checar(urn_dispositivo(URN_BASE, "12") in rem,
           "art. 12 (interno) sobrevive ao 'da Lei' que qualifica o art. 15")
    checar(urn_dispositivo(URN_BASE, "15") not in rem, "art. 15 (externo) continua descartado")


@cenario("auto-remissão: só o próprio artigo é descartado, não os de numeração parecida")
def auto_remissao_exata():
    """Quebra: filtrar auto-remissão por `startswith('...!art1')`. O prefixo de
    texto de 'art1' é também o de 'art10', 'art158'..., e o art. 1 perdia em
    silêncio toda remissão a artigos 10-19, 100-199 etc. Ponteiro ausente falha
    seguro, mas aqui a ausência era sistemática."""
    texto = ("Observado o art. 158 e o art. 12, o disposto no art. 1º, § 2º, "
             "e no inciso II do art. 1º não se aplica ao art. 100.")
    rem = extrair_remissoes(texto, URN_BASE, "1")
    for vizinho in ("158", "12", "100"):
        checar(urn_dispositivo(URN_BASE, vizinho) in rem,
               f"art. 1 continua remetendo ao art. {vizinho}")
    checar(
        not any(r.split("!")[1].split("_")[0] == "art1" for r in rem),
        "mas a remissão ao próprio art. 1 (caput, §, inciso) é descartada",
    )
    rem2 = extrair_remissoes("conforme o art. 20 e o art. 2º", URN_BASE, "2")
    checar(urn_dispositivo(URN_BASE, "20") in rem2, "idem art. 2 → art. 20")


@cenario("emenda constitucional: remissão só resolve com escopo interno AFIRMADO")
def remissao_em_emenda():
    """Quebra: tratar 'art. N' sem qualificador como interno também numa emenda.
    Numa EC, 'o imposto previsto no art. 153, IV' é a Constituição; resolvê-lo no
    namespace da emenda cria ponteiro para artigo que a emenda não tem (ou, pior,
    tem com outro assunto). Medido na EC 132 real: 8 de 20 remissões órfãs, todas
    referências à Constituição sem o qualificador."""
    texto = ("A contribuição prevista no art. 195, V, observará o art. 1º desta "
             "Emenda Constitucional, sem prejuízo do art. 159, I.")
    rem = extrair_remissoes(texto, URN_BASE, "7", exigir_escopo_interno=True)
    checar(urn_dispositivo(URN_BASE, "1") in rem,
           "'art. 1º desta Emenda' resolve: o escopo interno é afirmado")
    checar(urn_dispositivo(URN_BASE, "195") not in rem,
           "'art. 195, V' sem qualificador NÃO resolve na emenda")
    checar(urn_dispositivo(URN_BASE, "159") not in rem,
           "'art. 159, I' sem qualificador NÃO resolve na emenda")
    checar(F.exige_escopo_interno({"tipo": "emenda.constitucional"}),
           "norma do tipo emenda.constitucional exige escopo afirmado")
    checar(not F.exige_escopo_interno({"tipo": "lei.complementar"}),
           "lei complementar mantém o padrão")
    checar(F.exige_escopo_interno({"tipo": "lei.complementar",
                                   "remissoes": "so_escopo_afirmado"}),
           "lei de alteração marcada no catálogo: só o escopo afirmado resolve")


@cenario("corpo de um dispositivo: quais linhas são texto de outra norma")
def linhas_citadas_do_corpo():
    """Quebra: reconhecer o início de bloco só no primeiro caractere. No corpo, a
    linha riscada começa com '~~', e um bloco citado riscado ('~~“Art. 7º ...”~~')
    seria lido como texto próprio."""
    corpo = [
        "Art. 1º A lei passa a vigorar assim:",
        "“Art. 9º Primeiro artigo do bloco.",
        "Art. 10. Segundo, sem aspa de abertura.",
        "§ 1º continua. ” (NR)",
        "Art. 2º Próprio de novo.",
        "~~“Art. 7º Bloco citado riscado.” (NR)~~",
    ]
    checar(
        F.linhas_citadas(corpo) == [False, True, True, True, False, True],
        "só o texto entre as aspas é marcado como citado, riscado inclusive",
    )


@cenario("subdivisão de cada linha do corpo")
def subdivisao_por_linha():
    """Cada linha herda a subdivisão da última linha rotulada; sem rótulo ainda, o
    artigo. Dá à proposta temporal o `fundamento` (URN) de cada trecho."""
    corpo = [
        "Art. 5º Texto do caput:",
        "§ 1º Um parágrafo:",
        "I - um inciso:",
        "a) uma alínea;",
        "continuação da alínea, sem rótulo",
        "Parágrafo único. Outro.",
    ]
    u = lambda **kw: urn_dispositivo(URN_BASE, "5", **kw)  # noqa: E731
    checar(
        F.subdivisao_por_linha(corpo, URN_BASE, "5") == [
            u(),
            u(paragrafo="1"),
            u(paragrafo="1", inciso="I"),
            u(paragrafo="1", inciso="I", alinea="a"),
            u(paragrafo="1", inciso="I", alinea="a"),
            u(paragrafo="U"),
        ],
        "uma URN por linha, herdada quando a linha não tem rótulo",
    )


@cenario("normas externas e parágrafo único")
def externas_e_paragrafo():
    ext = extrair_externas("A Lei nº 998, de 1899, passa a vigorar com a seguinte redação.")
    checar(any("998" in e for e in ext), f"captura norma alteradora: {ext}")
    rem = extrair_remissoes("o disposto no § 1º do art. 1º", URN_BASE, "2")
    checar(urn_dispositivo(URN_BASE, "1", paragrafo="1") in rem,
           "captura '§ 1º do art. 1º' como parágrafo")


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

@cenario("ordenação e nomes de arquivo")
def ordenacao_e_nomes():
    checar(chave_ordem("4") < chave_ordem("4-A") < chave_ordem("5"), "ordenação: 4 < 4-A < 5")
    checar(nome_arquivo("1") == "art-0001", "zero à esquerda")
    checar(nome_arquivo("12") == "art-0012", "dois dígitos")
    checar(nome_arquivo("4-A") == "art-0004-a", "sufixo alfabético")
    m = F.RE_ARTIGO.match("Art. 4º-A Texto")
    checar(m is not None and F.normalizar_artigo(m.group(1), m.group(2)) == "4-A",
           "'Art. 4º-A' é o artigo 4-A, não o 4")


@cenario("status_em (vigência x eficácia — PREMISSAS.md §3.1)")
def status():
    import datetime as dt

    meta = {
        "vigencia_inicio": "2026-01-01",
        "vigencia_fim": None,
        "efeitos_inicio": "2027-01-01",
        "efeitos_fim": None,
    }
    checar(status_em(meta, dt.date(2025, 6, 1)) == "futuro", "antes da vigência")
    checar(status_em(meta, dt.date(2026, 6, 1)) == "vigente_sem_efeitos",
           "vigente mas sem efeitos — distinção central do projeto")
    checar(status_em(meta, dt.date(2027, 6, 1)) == "vigente", "vigente com efeitos")
    revogado = dict(meta, vigencia_fim="2033-01-01")
    checar(status_em(revogado, dt.date(2033, 6, 1)) == "revogado", "após vigencia_fim")


# ---------------------------------------------------------------------------
# Contrato com as fontes reais arquivadas
# ---------------------------------------------------------------------------

@cenario("fontes reais arquivadas em fontes/ (pulado se ausentes)")
def fontes_reais():
    """Os fixtures provam o mecanismo; só o documento real prova o resultado. Todos
    os defeitos anteriores foram achados rodando contra o documento real e nenhum
    pelos testes. Verifica PROPRIEDADES — numeração consecutiva, estritamente
    crescente, aspas balanceadas — nunca contagens copiadas da saída do parser."""
    for slug in ("emc-132-2023", "lc-214-2025"):
        caminho = RAIZ / "fontes" / slug / "texto_compilado.html"
        if not caminho.exists():
            print(f"  pulado: {slug} (fontes/ não contém o original)")
            continue
        artigos, avisos, stats = F.fatiar(F.html_para_linhas(caminho.read_bytes()))
        checar(sem_erro(avisos), f"{slug}: fatiamento sem ERRO ({[a for a in avisos if a.startswith('ERRO')]})")
        bases = sorted({int(re.match(r"\d+", a["numero"]).group()) for a in artigos})
        checar(bases == list(range(1, bases[-1] + 1)) if bases else False,
               f"{slug}: numeração consecutiva de 1 a {bases[-1] if bases else '?'}")
        chaves = [chave_ordem(a["numero"]) for a in artigos]
        checar(chaves == sorted(set(chaves)), f"{slug}: artigos próprios estritamente crescentes")
        checar(stats["aspas_estado_final"] == 0, f"{slug}: aspas balanceadas ao fim")
        checar(stats["aspas_abertura_dentro_de_bloco"] == 0,
               f"{slug}: nenhuma abertura de bloco dentro de outro")
        checar(all(a["linhas_proprias"] or any(ln.startswith("~~") for ln in a["linhas"])
                   for a in artigos),
               f"{slug}: nenhum artigo sem texto vigente que não seja integralmente riscado")
        checar(not any(re.match(r"^(Bras[ií]lia,|ANEXO\b)", ln)
                       for a in artigos for ln in a["linhas_proprias"]),
               f"{slug}: nenhum artigo engloba a assinatura ou anexos da norma")


# ---------------------------------------------------------------------------
# Proposta de revisão da vigência (pipeline/propor_vigencia.py)
# ---------------------------------------------------------------------------

def _pv():
    import propor_vigencia

    return propor_vigencia


EXISTENTES_FICT = ["1", "2", "3", "4", "4-A", "5", "6", "7", "8", "9", "11"]


@cenario("proposta: a cláusula de vigência atribui cada artigo ao seu inciso")
def proposta_clausula_mapeia_artigos():
    """Quebra: errar a atribuição de um artigo a um inciso, ou resolver 'demais
    dispositivos' sobre o conjunto errado. O resultado vira data de vigência."""
    clausula = [
        "Art. 9º Esta Emenda Constitucional fictícia entra em vigor:",
        "I - em 2030, em relação aos arts. 3º e 11;",
        "II - em 2035, em relação aos arts. 4º-A, 5º e 6º; e",
        "III - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(clausula, URN_BASE, "9", EXISTENTES_FICT)
    atribuido = {n: m["inciso"] for n, m in r["mapa"].items()}
    checar(
        atribuido == {"1": "III", "2": "III", "3": "I", "4": "III", "4-A": "II", "5": "II",
                      "6": "II", "7": "III", "8": "III", "9": "III", "11": "I"},
        f"cada artigo no seu inciso (obteve {atribuido})",
    )
    checar(r["mapa"]["3"]["termo"] == {"tipo": "ano", "ano": 2030},
           "inciso I: 'em 2030' vira termo de ano")
    checar(r["mapa"]["7"]["termo"] == {"tipo": "publicacao"},
           "inciso III: 'na data de sua publicação' vira termo de evento")
    checar(r["urn"] == urn_dispositivo(URN_BASE, "9"), "a cláusula é identificada pela URN")
    checar(
        [i["urn"] for i in r["incisos"]]
        == [urn_dispositivo(URN_BASE, "9", inciso=x) for x in ("I", "II", "III")],
        "cada inciso carrega a URN que será o `fundamento` da proposta",
    )


@cenario("proposta: o que não casa com o padrão exato não é interpretado")
def proposta_clausula_nao_interpreta():
    """Quebra: dar data a um termo fora do padrão, ou deixar 'demais dispositivos'
    cair no inciso III quando um inciso anterior tem ALCANCE desconhecido. O
    artigo seria datado errado, com aparência de certo.

    Termo e alcance são lidos separadamente: o termo fora do padrão do inciso I
    não impede saber que ele nomeia os arts. 3º e 5º; a sobra 'o Anexo I' no II
    impede saber o que ele nomeia."""
    clausula = [
        "Art. 9º Esta Lei fictícia entra em vigor:",
        "I - noventa dias após a data de sua publicação, em relação aos arts. 3º e 5º;",
        "II - em 2035, em relação aos arts. 6º e o Anexo I; e",
        "III - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(clausula, URN_BASE, "9", EXISTENTES_FICT)
    checar([i["interpretado"] for i in r["incisos"]] == [False, False, True],
           "termo fora do padrão e alcance com sobra não são interpretados")
    checar([i["alcance_interpretado"] for i in r["incisos"]] == [True, False, True],
           "mas o alcance do inciso I é lido")
    checar(r["mapa"]["3"]["inciso"] == "I" and r["mapa"]["3"]["termo"] is None
           and r["mapa"]["3"]["motivo"] and r["mapa"]["3"]["ressalva"],
           "art. 3: no inciso I, sem data (termo fora do padrão), com ressalva do inciso II")
    nao_nomeados = [n for n in EXISTENTES_FICT if n not in ("3", "5")]
    checar(all(r["mapa"][n]["inciso"] is None and r["mapa"][n]["motivo"] for n in nao_nomeados),
           "o alcance do II é desconhecido: 'demais dispositivos' não é resolvido")

    prazo = [
        "Art. 9º Esta Lei fictícia entra em vigor:",
        "I - em 90 dias, em relação aos arts. 3º e 5º; e",
        "II - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(prazo, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["incisos"][0]["interpretado"] is False and r["incisos"][0]["termo"] is None,
           "'em 90 dias' é prazo, não ano: não vira 'ano 90'")
    r = _pv().interpretar_clausula(
        ["Art. 9º Esta Lei fictícia entra em vigor:",
         "I - em 300, em relação aos arts. 3º e 5º."], URN_BASE, "9", EXISTENTES_FICT)
    checar(r["incisos"][0]["interpretado"] is False,
           "número que não é ano (fora de 1900-2099) não é aceito como ano")

    dois_demais = [
        "Art. 9º Esta Lei fictícia entra em vigor:",
        "I - em 2030, em relação aos demais dispositivos; e",
        "II - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(dois_demais, URN_BASE, "9", EXISTENTES_FICT)
    checar(all(m["inciso"] is None and m["motivo"] for m in r["mapa"].values()),
           "dois incisos 'demais dispositivos': ambíguo, nenhum artigo é atribuído")

    parcial = [
        "Art. 9º Esta Lei fictícia entra em vigor:",
        "I - em 2030, em relação aos arts. 3º e 5º;",
        "II - em 2035, em relação aos arts. 6º e o Anexo I.",
    ]
    r = _pv().interpretar_clausula(parcial, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["mapa"]["3"]["inciso"] == "I" and r["mapa"]["3"]["ressalva"],
           "nomeado por inciso interpretado segue atribuído, mas com ressalva: o inciso "
           "não interpretado pode nomeá-lo também")


@cenario("proposta: leitura do alcance de um inciso")
def proposta_ler_alcance():
    """Quebra: separar a lista por ' e ' antes de reconhecer as subdivisões.
    '450, §§ 1º e 5º' viraria os artigos 450 e 5; '58, caput' viraria o art. 58
    inteiro; '480 a 484' viraria 480 e 484."""
    ler = _pv().ler_alcance

    def resumo(itens):
        return None if itens is None else [
            (i["artigos"], i["somente"], i["exceto"]) for i in itens]

    checar(resumo(ler("6º, §§ 1º e 5º, 13 e 15"))
           == [(["6"], ["par1", "par5"], None), (["13"], None, None), (["15"], None, None)],
           "'§§ 1º e 5º' são parágrafos do art. 6, não o art. 5")
    checar(resumo(ler("3º, 4º, caput, 5º, § 3º, 9º a 11 e 20"))
           == [(["3"], None, None), (["4"], ["par0"], None), (["5"], ["par3"], None),
               (["9", "10", "11"], None, None), (["20"], None, None)],
           "caput, parágrafo (§ 3º) e intervalo")
    checar(resumo(ler("6º, exceto os §§ 1º e 5º, 12 e 14"))
           == [(["6"], None, ["par1", "par5"]), (["12"], None, None), (["14"], None, None)],
           "'exceto os §§' fica com o artigo que o precede")
    checar(ler("6º e o Anexo I") is None, "qualquer sobra: a lista inteira não é interpretada")
    checar(ler("6º; 7º") is None and ler("6º, 7º,") is None,
           "separador desconhecido ou vírgula final: nada é descartado em silêncio")
    checar(ler("4º-A a 4º-C") is None, "intervalo entre artigos com sufixo não é interpretado")
    checar(ler("9º a 11, § 2º") is None, "subdivisão aplicada a um intervalo não é interpretada")


CL_LC = [
    "Art. 90. Esta Lei Complementar fictícia entra em vigor na data de sua publicação, "
    "produzindo efeitos: Produção de efeitos",
    "I - a partir do primeiro dia do quarto mês subsequente ao da sua publicação, "
    "em relação aos arts. 7º a 8º;",
    "II - a partir de 1º de janeiro de 2030, em relação aos arts. 3º, 4º, caput, 5º, § 3º, "
    "9º a 11 e 20;",
    "~~III - a partir de 1º de janeiro de 2031, em relação aos arts. 6º, exceto os §§ 1º e 5º, "
    "12 e 14;~~",
    "III - a partir de 1º de janeiro de 2031, em relação aos arts. 2º, 6º, exceto os §§ 1º e 5º, "
    "12 e 14; (Redação dada pela Lei Complementar nº 998, de 2030)",
    "IV - a partir de 1º de janeiro de 2032, em relação aos arts. 6º, §§ 1º e 5º, 13 e 15; e",
    "V - a partir de 1º de janeiro de 2029, em relação aos demais dispositivos.",
]
EXISTENTES_LC = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10-A", "11", "12", "13",
                 "14", "15", "20", "90"]


@cenario("proposta: cláusula que dá a vigência no caput e os efeitos nos incisos")
def proposta_clausula_efeitos():
    """A forma da LC 214: 'entra em vigor na data de sua publicação, produzindo
    efeitos: I - ...'. Quebra: tratar os incisos como vigência (como na EC), ou
    perder as subdivisões, a redação anterior e o sufixo dentro de intervalo."""
    r = _pv().interpretar_clausula(CL_LC, URN_BASE, "90", EXISTENTES_LC)
    u = lambda n, **kw: urn_dispositivo(URN_BASE, n, **kw)  # noqa: E731
    checar(r["forma"] == "efeitos_por_inciso", "forma reconhecida pelo caput")
    checar(r["vigencia"] == {"termo": {"tipo": "publicacao"}, "fundamento": u("90")},
           "a vigência de todos vem do caput, na publicação")
    atribuido = {n: m["inciso"] for n, m in r["mapa"].items()}
    checar(atribuido == {"1": "V", "2": "III", "3": "II", "4": "V", "5": "V", "6": "III",
                         "7": "I", "8": "I", "9": "II", "10": "II", "10-A": None, "11": "II",
                         "12": "III", "13": "IV", "14": "III", "15": "IV", "20": "II",
                         "90": "V"},
           f"efeitos de cada artigo no seu inciso (obteve {atribuido})")
    checar(r["mapa"]["3"]["termo"] == {"tipo": "data", "data": "2030-01-01"},
           "'a partir de 1º de janeiro de 2030' vira data")
    checar(r["mapa"]["7"]["termo"] == {"tipo": "relativo_publicacao",
                                       "regra": "primeiro-dia-do-mes-subsequente", "meses": 4}
           and r["mapa"]["7"]["motivo"] is None,
           "termo relativo ('quarto mês subsequente'): lido, com o nome da regra que o converte")
    checar(r["mapa"]["10-A"]["motivo"],
           "10-A dentro do intervalo '9º a 11': indeterminado, com motivo")
    exc = {n: [(e["urn"], e["inciso"]) for e in r["mapa"][n]["excecoes"]]
           for n in ("4", "5", "6")}
    checar(exc == {"4": [(u("4", paragrafo="0"), "II")], "5": [(u("5", paragrafo="3"), "II")],
                   "6": [(u("6", paragrafo="1"), "IV"), (u("6", paragrafo="5"), "IV")]},
           f"subdivisões com inciso próprio viram exceções (obteve {exc})")
    checar([n for n, m in r["mapa"].items() if m["alterado_pela_redacao_posterior"]] == ["2"],
           "o art. 2, que só a redação nova do III nomeia, é sinalizado")

    # Inteiro num inciso e em parte noutro, SEM 'exceto': qual prevalece no § 1º é
    # interpretação, não leitura.
    ambiguo = [
        "Art. 90. Esta Lei Complementar fictícia entra em vigor na data de sua publicação, "
        "produzindo efeitos:",
        "I - a partir de 1º de janeiro de 2030, em relação aos arts. 3º e 6º;",
        "II - a partir de 1º de janeiro de 2031, em relação aos arts. 6º, § 1º; e",
        "III - a partir de 1º de janeiro de 2029, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(ambiguo, URN_BASE, "90", EXISTENTES_LC)
    checar(r["mapa"]["6"]["inciso"] is None and r["mapa"]["6"]["motivo"]
           and r["mapa"]["3"]["inciso"] == "I",
           "art. 6 inteiro no I e § 1º no II, sem 'exceto': indeterminado")


@cenario("proposta: conflito, artigo inexistente e ausência de 'demais'")
def proposta_clausula_anomalias():
    conflito = [
        "Art. 9º Esta Emenda fictícia entra em vigor:",
        "I - em 2030, em relação aos arts. 3º e 5º;",
        "II - em 2035, em relação aos arts. 5º e 6º; e",
        "III - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(conflito, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["mapa"]["5"]["inciso"] is None and r["mapa"]["5"]["motivo"],
           "artigo nomeado em dois incisos fica indeterminado, não vai para o primeiro")
    checar(r["mapa"]["3"]["inciso"] == "I" and r["mapa"]["6"]["inciso"] == "II",
           "os não conflitantes seguem atribuídos")

    inexistente = [
        "Art. 9º Esta Emenda fictícia entra em vigor:",
        "I - em 2030, em relação aos arts. 3º e 99; e",
        "II - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(inexistente, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["artigos_inexistentes"] == ["99"], "artigo nomeado que a norma não tem é reportado")

    sem_demais = [
        "Art. 9º Esta Emenda fictícia entra em vigor:",
        "I - em 2030, em relação aos arts. 3º e 5º.",
    ]
    r = _pv().interpretar_clausula(sem_demais, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["mapa"]["3"]["inciso"] == "I" and r["mapa"]["1"]["inciso"] is None
           and r["mapa"]["1"]["motivo"],
           "sem 'demais dispositivos', o artigo não nomeado fica sem vigência proposta")


@cenario("proposta: localizar o artigo que contém a cláusula")
def proposta_localiza_clausula():
    p = _pv()
    corpos = {
        "8": ["Art. 8º Fica criado o fundo; vigora a lei desde a entrada em vigor do regime."],
        "9": ["Art. 9º Esta Emenda fictícia entra em vigor:", "I - em 2030, em relação ao art. 3º."],
    }
    checar(p.localizar_clausula(corpos) == ["9"],
           "só o caput 'entra em vigor' é cláusula; menção no meio do texto não é")
    corpos["10"] = ["Art. 10. Esta outra parte entra em vigor:"]
    checar(sorted(p.localizar_clausula(corpos)) == ["10", "9"],
           "mais de um candidato é devolvido como tal, para o gerador recusar")


@cenario("proposta: marcos temporais próprios, em trecho literal e sem interpretação")
def proposta_marcos_proprios():
    """Quebra: tratar a data de OUTRA lei citada como marco desta norma; deixar o
    texto riscado entrar; contar texto citado como próprio."""
    corpo = [
        "Art. 5º Fica criado fundo, nos termos da Lei nº 9.999, de 1º de janeiro de 1999.",
        "§ 1º A partir de 2040, o valor será revisto.",
        "§ 2º Até que lei complementar disponha, vale o regime atual.",
        "§ 3º Vale para o que existir na data de publicação desta Emenda.",
        "§ 4º Em até 90 (noventa) dias após a promulgação desta Emenda, o Executivo enviará projeto.",
        "§ 5º A redução é de até 100% (cem por cento).",
        "§ 6º Com a redação vigente em 31 de maio de 2023, aplica-se o disposto.",
        "§ 7º ~~Texto antigo de 2020, riscado~~ Texto novo sem marco.",
        "§ 8º Lei complementar definirá os produtos beneficiados.",
        "§ 9º O crédito será concedido nos termos de lei complementar.",
        "§ 10. A lei complementar que instituir o imposto poderá prever regimes.",
        "“Art. 9º Texto citado de outra norma, em 2045.” (NR)",
    ]
    r = _pv().marcos_proprios(corpo, URN_BASE, "5")
    achado = {" ".join(m["trecho"].split(" ")[:2]): set(m["tipos"]) for m in r["marcos"]}
    checar(
        achado == {
            "§ 1º": {"ano", "a_partir_de_ate"},
            "§ 2º": {"condicao_ate_que"},
            "§ 3º": {"evento_publicacao"},
            "§ 4º": {"evento_promulgacao", "prazo_relativo"},
            "§ 6º": {"ano", "data_explicita"},
            "§ 8º": {"depende_de_lei_futura"},
            "§ 9º": {"depende_de_lei_futura"},
            "§ 10.": {"depende_de_lei_futura"},
        },
        f"só os parágrafos com marco próprio, com os tipos certos (obteve {achado})",
    )
    checar(r["marcos"][0]["urn"] == urn_dispositivo(URN_BASE, "5", paragrafo="1"),
           "cada marco traz a URN da subdivisão em que está")
    checar(r["citado_com_marcos"] == 1,
           "o ano do texto citado é contado à parte, não como marco desta norma")


@cenario("proposta: data do ato e publicação no DOU, lidas do original")
def proposta_referencias():
    fonte = [
        "EMENDA CONSTITUCIONAL FICTÍCIA Nº 999, DE 5 DE MARÇO DE 1900",
        "Art. 1º Texto.",
        "Brasília, em 5 de março de 1900",
        "Este texto não substitui o publicado no DOU 6.3.1900",
    ]
    r = _pv().extrair_referencias(fonte)
    checar(r["data_do_ato"]["valor"] == "1900-03-05", "data do ato lida do título")
    checar(r["publicacao_dou"]["valores"] == ["1900-03-06"], "publicação lida do rodapé")
    checar(r["publicacao_dou"]["trechos"] == ["Este texto não substitui o publicado no DOU 6.3.1900"],
           "e o trecho literal acompanha o valor")

    duas = fonte[:3] + [
        "Este texto não substitui o publicado no DOU de 6.3.1900 - Edição extra e "
        "republicado no DOU de 13.3.1900"]
    checar(_pv().extrair_referencias(duas)["publicacao_dou"]["valores"]
           == ["1900-03-06", "1900-03-13"],
           "duas publicações (original e republicação) são ambas devolvidas")

    r = _pv().extrair_referencias(["Art. 1º Sem rodapé algum."])
    checar(r["data_do_ato"]["valor"] is None and r["publicacao_dou"]["valores"] == [],
           "o que não se encontra é nulo, não é suposto")

    # Medido na LC 214 real: depois dos anexos, o compilado traz OUTRO ato, com
    # assinatura e rodapé próprios. A publicação da norma é a do primeiro rodapé.
    com_outro_ato = fonte + [
        "ANEXO I",
        "Brasília, 1º de julho de 1901",
        "Este texto não substitui o publicado no DOU de 2.7.1901.",
    ]
    r = _pv().extrair_referencias(com_outro_ato)
    checar(r["publicacao_dou"]["valores"] == ["1900-03-06"],
           "a publicação é a do rodapé que segue a primeira assinatura")
    checar([x["valores"] for x in r["rodapes_adicionais"]] == [["1901-07-02"]]
           and r["rodapes_adicionais"][0]["assinatura"] == "Brasília, 1º de julho de 1901",
           "o rodapé de outro ato é devolvido à parte, com a assinatura que o precede")


@cenario("proposta: YAML legível para quem revisa (sem âncoras)")
def proposta_sem_ancoras():
    """Quebra: reaproveitar o mesmo objeto em dois lugares. O YAML grava '&id001' num
    e '*id001' no outro, e quem edita o arquivo à mão não vê a proposta de efeitos."""
    import tempfile

    if not (RAIZ / "normas" / "emc-132-2023").exists():
        print("  pulado: normas/ da EC 132 ausente")
        return
    with tempfile.TemporaryDirectory() as tmp:
        alvo = Path(tmp) / "p.yaml"
        _pv().gravar_proposta(alvo, _pv().construir("emc-132-2023"))
        texto = alvo.read_text(encoding="utf-8")
    checar("&id0" not in texto and "*id0" not in texto, "nenhuma âncora/alias no arquivo gerado")


@cenario("proposta: nunca sobrescreve revisão humana")
def proposta_nao_sobrescreve_revisao():
    """Quebra: regenerar a proposta apagaria a decisão que um humano já tomou."""
    import tempfile

    import yaml

    p = _pv()
    with tempfile.TemporaryDirectory() as tmp:
        alvo = Path(tmp) / "proposta.yaml"
        novo = {"dispositivos": [{"artigo": "1", "revisao": {"decisao": None}}]}
        checar(p.gravar_proposta(alvo, novo) is True, "arquivo novo é gravado")
        checar(p.gravar_proposta(alvo, novo) is True, "proposta sem decisão pode ser regenerada")

        revisado = {"dispositivos": [{"artigo": "1", "revisao": {"decisao": "aceitar"}}]}
        alvo.write_text(yaml.safe_dump(revisado), encoding="utf-8")
        antes = alvo.read_bytes()
        checar(p.gravar_proposta(alvo, novo) is False, "com decisão humana, recusa")
        checar(alvo.read_bytes() == antes, "e o arquivo revisado permanece intacto")


@cenario("proposta: EC 132 real (pulado se normas/ ou fontes/ ausentes)")
def proposta_ec_real():
    """Contrato com o documento real. Valores lidos à mão no `Art. 23` (incisos I a
    III) e no rodapé do compilado; não vêm da saída do gerador."""
    if not (RAIZ / "normas" / "emc-132-2023").exists() or \
            not (RAIZ / "fontes" / "emc-132-2023" / "texto_compilado.html").exists():
        print("  pulado: normas/ ou fontes/ da EC 132 ausentes")
        return
    prop = _pv().construir("emc-132-2023")
    atribuido = {d["artigo"]: d["vigencia"]["inciso"] for d in prop["dispositivos"]}
    esperado = {str(n): "III" for n in range(1, 24)}
    esperado.update({"3": "I", "11": "I", "4": "II", "5": "II"})
    checar(atribuido == esperado, f"Art. 23 aplicado aos 23 artigos (obteve {atribuido})")
    checar(prop["clausula_de_vigencia"]["urn"].endswith("!art23"),
           "a cláusula é o art. 23")
    checar(prop["referencias"]["data_do_ato"]["valor"] == "2023-12-20", "data do ato")
    checar(prop["referencias"]["publicacao_dou"]["valores"] == ["2023-12-21"],
           "publicação no DOU, como diz o rodapé")
    por_artigo = {d["artigo"]: d for d in prop["dispositivos"]}
    checar("revogacao_expressa" in por_artigo["22"]["pendencias"],
           "o art. 22 ('Revogam-se: ... em 2027 ... em 2033') é sinalizado")
    checar("texto_inserido_em_outra_norma" in por_artigo["1"]["pendencias"],
           "o art. 1 insere texto na Constituição, que não está ingerida")
    # Art. 8, parágrafo único: "Lei complementar definirá os produtos ..." (lido no texto)
    checar("depende_de_lei_futura" in por_artigo["8"]["pendencias"]
           and por_artigo["8"]["efeitos"]["proposta"] is None,
           "o art. 8 depende de lei complementar futura: sem proposta de efeitos")
    checar(all(d["revisao"]["decisao"] is None for d in prop["dispositivos"]),
           "nenhuma decisão vem preenchida: a proposta não decide")


# ---------------------------------------------------------------------------
# Revisão temporal: do YAML revisado ao front-matter (pipeline/revisao_temporal.py)
# ---------------------------------------------------------------------------

def _rt():
    import revisao_temporal

    return revisao_temporal


SHA_FICT = "a" * 64
URN_EC = urn_norma("br:federal:emenda.constitucional", "1900-01-01", "999")


def _entrada(artigo: str, revisao: dict, efeitos_proposta: bool = True,
             termo: str = "ano") -> dict:
    """Uma entrada de proposta no formato que propor_vigencia.py grava."""
    if termo == "ano":
        vig = {"tipo": "ano", "ano": 2030, "data_candidata": "2030-01-01", "precisao": "ano"}
    else:
        vig = {"tipo": "evento", "evento": "publicacao", "data_candidata": "1900-01-02",
               "precisao": "dia"}
    base = {"decisao": None, "vigencia_inicio": None, "vigencia_fim": None,
            "efeitos_inicio": None, "efeitos_fim": None, "precisao": {},
            "fundamento_vigencia": [], "fundamento_efeitos": [],
            "excecoes_subdivisao": [], "revisado_por": None, "revisado_em": None,
            "observacao": None}
    base.update(revisao)
    return {
        "urn": urn_dispositivo(URN_EC, artigo),
        "artigo": artigo,
        "vigencia": {"inciso": "I", "fundamento": urn_dispositivo(URN_EC, "23", inciso="I"),
                     "proposta": vig},
        "efeitos": {"proposta": dict(vig) if efeitos_proposta else None},
        "revisao": base,
    }


def _carregar(entradas: list[dict], sha: str = SHA_FICT, urns: set | None = None,
              regras: dict | None = None):
    import tempfile

    import yaml

    with tempfile.TemporaryDirectory() as tmp:
        caminho = Path(tmp) / "p.yaml"
        caminho.write_text(yaml.safe_dump({"fonte_sha256": SHA_FICT, "dispositivos": entradas},
                                          allow_unicode=True), encoding="utf-8")
        if urns is None:
            urns = {e["urn"] for e in entradas}
        return _rt().carregar_revisoes(caminho, sha, urns, regras={} if regras is None else regras)


REVISOR = {"revisado_por": "Revisora Fictícia", "revisado_em": "1900-02-01"}


@cenario("revisão: 'aceitar' adota a proposta, com precisão e fundamento")
def revisao_aceitar():
    revs, erros = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR})])
    r = revs.get(urn_dispositivo(URN_EC, "3"))
    checar(not erros and r is not None, f"aceita sem erro (erros: {erros})")
    checar(r["vigencia_inicio"] == "2030-01-01" and r["efeitos_inicio"] == "2030-01-01",
           "as datas vêm da proposta")
    checar(r["precisao"] == {"vigencia_inicio": "ano", "efeitos_inicio": "ano"},
           "'em 2030' fica registrado como precisão de ano, não como 1º de janeiro")
    checar(r["fundamento_temporal"]
           == {"vigencia": [urn_dispositivo(URN_EC, "23", inciso="I")],
               "efeitos": [urn_dispositivo(URN_EC, "23", inciso="I")]},
           "e cada data cita o inciso da cláusula que a estabelece")


@cenario("revisão: o que não pode ser aplicado é erro, não silêncio")
def revisao_erros():
    """Quebra: aplicar data sem fundamento, sem revisor, ou aceitar efeitos que o
    gerador não propôs. Cada caso precisa barrar a escrita, não ser ignorado."""
    _, erros = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR},
                                   efeitos_proposta=False)])
    checar(len(erros) == 1, "'aceitar' sem proposta de efeitos: erro (use 'alterar')")

    _, erros = _carregar([_entrada("3", {"decisao": "aceitar"})])
    checar(len(erros) == 1, "decisão sem revisado_por/revisado_em: erro")

    _, erros = _carregar([_entrada("3", {
        "decisao": "alterar", **REVISOR, "vigencia_inicio": "1900-01-02",
        "efeitos_inicio": "1901-01-01", "fundamento_vigencia": [urn_dispositivo(URN_EC, "23")],
        "fundamento_efeitos": []})])
    checar(len(erros) == 1, "'alterar' sem fundamento dos efeitos: erro")

    _, erros = _carregar([_entrada("3", {
        "decisao": "alterar", **REVISOR, "vigencia_inicio": "1900-01-02",
        "efeitos_inicio": "1901-03-01", "precisao": {"efeitos_inicio": "ano"},
        "fundamento_vigencia": [urn_dispositivo(URN_EC, "23")],
        "fundamento_efeitos": [urn_dispositivo(URN_EC, "7")]})])
    checar(len(erros) == 1, "precisão de ano exige a convenção 1º de janeiro (AAAA-01-01)")

    _, erros = _carregar([_entrada("3", {"decisao": "talvez", **REVISOR})])
    checar(len(erros) == 1, "decisão fora de aceitar/alterar/rejeitar: erro")

    _, erros = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR})], urns=set())
    checar(len(erros) == 1, "revisão para dispositivo que a norma não tem: erro")


@cenario("revisão: 'aceitar' com efeitos de outro inciso e exceções propostas")
def revisao_aceitar_efeitos_e_excecoes():
    """Quebra: fundamentar os efeitos no dispositivo da vigência, ou descartar as
    exceções por subdivisão que a cláusula estabelece (LC 214, art. 450)."""
    entrada = _entrada("6", {"decisao": "aceitar", **REVISOR}, termo="publicacao")
    entrada["vigencia"]["fundamento"] = urn_dispositivo(URN_EC, "90")
    exc = {"urn": urn_dispositivo(URN_EC, "6", paragrafo="1"), "efeitos_inicio": "2032-01-01",
           "fundamento": [urn_dispositivo(URN_EC, "90", inciso="IV")]}
    entrada["efeitos"] = {
        "inciso": "III", "fundamento": urn_dispositivo(URN_EC, "90", inciso="III"),
        "proposta": {"tipo": "data", "data_candidata": "2031-01-01", "precisao": "dia"},
        "excecoes": [exc],
    }
    revs, erros = _carregar([entrada])
    r = revs.get(urn_dispositivo(URN_EC, "6"))
    checar(not erros and r is not None, f"aceita sem erro (erros: {erros})")
    checar(r and r["fundamento_temporal"] == {
        "vigencia": [urn_dispositivo(URN_EC, "90")],
        "efeitos": [urn_dispositivo(URN_EC, "90", inciso="III")]},
        "vigência fundamentada no caput, efeitos no inciso III")
    checar(r and r["efeitos_inicio"] == "2031-01-01" and r["excecoes_subdivisao"] == [exc],
           "e o § 1º com a própria data, do inciso IV")


@cenario("revisão parcial: só a vigência")
def revisao_parcial():
    """Quebra: exigir os dois eixos juntos. Na EC 132 a regra fixa a vigência dos 23
    artigos, mas os efeitos da maioria precisam de leitura; sem revisão parcial, a
    base continuaria dando o art. 3º como vigente desde 2023, contra o art. 23."""
    entrada = _entrada("3", {"decisao": "aceitar", "escopo": ["vigencia"], **REVISOR},
                       efeitos_proposta=False)
    revs, erros = _carregar([entrada])
    r = revs.get(urn_dispositivo(URN_EC, "3"))
    checar(not erros and r is not None and r["eixos"] == ["vigencia"],
           f"aceita só a vigência, sem proposta de efeitos (erros: {erros})")
    meta = {"urn": urn_dispositivo(URN_EC, "3"), "vigencia_inicio": "1900-01-02",
            "efeitos_inicio": "1900-01-02", "vigencia_fim": None, "efeitos_fim": None,
            "extracao": "automatica", "revisao_temporal_pendente": True}
    novo = _rt().aplicar_revisao(meta, r)
    checar(novo["vigencia_inicio"] == "2030-01-01" and novo["efeitos_inicio"] == "1900-01-02",
           "a vigência muda; os efeitos ficam como estavam")
    checar(novo["revisao_temporal_pendente"] is True and novo["eixos_revisados"] == ["vigencia"]
           and novo["precisao"] == {"vigencia_inicio": "ano"},
           "e o dispositivo continua pendente, dizendo qual eixo foi revisado")
    erros_v, _ = _rt().problemas_no_dispositivo(novo)
    checar(not erros_v, f"o resultado passa na validação (erros: {erros_v})")
    erros_v, _ = _rt().problemas_no_dispositivo(dict(novo, revisao_temporal_pendente=False))
    checar(erros_v, "só a vigência revisada e pendência false: incoerente, erro")
    checar(_rt().revisoes_nao_aplicadas(revs, [novo]) == [],
           "a comparação de 'decisão não aplicada' olha só o eixo revisado")
    _, erros = _carregar([_entrada("3", {"decisao": "aceitar", "escopo": ["prazo"], **REVISOR})])
    checar(len(erros) == 1, "escopo fora de vigencia/efeitos: erro")


@cenario("regras derivadas: só valem aprovadas")
def regras_derivadas():
    """Quebra: aplicar uma regra que ninguém aprovou, ou calcular o mês errado."""
    import regras_temporais as R

    checar(R.primeiro_dia_do_mes_subsequente("1900-01-16", 4) == "1900-05-01",
           "publicação em janeiro, quarto mês subsequente: 1º de maio")
    checar(R.primeiro_dia_do_mes_subsequente("1900-12-05", 2) == "1901-02-01",
           "atravessa o ano")
    regras = {"x": {"aprovada": True, "aprovada_por": "Fulana", "aprovada_em": "1900-01-01"},
              "y": {"aprovada": True, "aprovada_por": None, "aprovada_em": "1900-01-01"},
              "z": {"aprovada": False, "aprovada_por": "Fulana", "aprovada_em": "1900-01-01"}}
    checar(R.aprovada(regras, "x") and not R.aprovada(regras, "y")
           and not R.aprovada(regras, "z") and not R.aprovada(regras, "w"),
           "aprovada exige aprovada: true, aprovada_por e aprovada_em")


def _proposta_para_regra(forma: str, entradas: list[dict]) -> dict:
    return {"fonte_sha256": SHA_FICT, "resumo": {"forma_da_clausula": forma},
            "dispositivos": entradas}


def _entrada_lc(artigo: str, efeitos_data: str | None, **extra) -> dict:
    caput = urn_dispositivo(URN_EC, "90")
    e = {
        "urn": urn_dispositivo(URN_EC, artigo), "artigo": artigo,
        "vigencia": {"inciso": None, "fundamento": caput, "motivo": None, "ressalva": None,
                     "proposta": {"tipo": "evento", "evento": "publicacao",
                                  "data_candidata": "1900-01-02", "precisao": "dia"}},
        "efeitos": {"inciso": "II", "fundamento": urn_dispositivo(URN_EC, "90", inciso="II"),
                    "motivo": None, "ressalva": None, "excecoes": [],
                    "proposta": ({"tipo": "data", "data_candidata": efeitos_data,
                                  "precisao": "dia"} if efeitos_data else None)},
        "atual_no_pipeline": {"publicacao": {"datas": ["1900-01-02"], "fonte": "dou"}},
        "pendencias": [],
        "revisao": {"decisao": None, "revisado_por": None, "revisado_em": None},
    }
    for chave, valor in extra.items():
        if chave in ("vigencia", "efeitos"):
            e[chave].update(valor)
        else:
            e[chave] = valor
    return e


@cenario("revisão por regra: o que é literal decide; o resto fica pendente")
def revisao_por_regra():
    import revisar_por_regra as RR

    regras = {"ano-primeiro-dia": {"aprovada": True, "aprovada_por": "F", "aprovada_em": "1900-01-01"}}
    humano = _entrada_lc("9", "1930-01-01")
    humano["revisao"] = {"decisao": "rejeitar", "revisado_por": "Revisora", "revisado_em": "1900-01-05"}
    prop = _proposta_para_regra("efeitos_por_inciso", [
        _entrada_lc("1", "1930-01-01"),
        _entrada_lc("2", None),
        _entrada_lc("3", "1930-01-01", pendencias=["alcance_alterado_pela_redacao_posterior"]),
        _entrada_lc("4", "1930-01-01", efeitos={"ressalva": "inciso II pode nomeá-lo"}),
        _entrada_lc("5", "1930-01-01", atual_no_pipeline={"publicacao": {"datas": ["1900-01-02"],
                                                                          "fonte": "rodape_compilado"}}),
        humano,
    ])
    novo, resumo = RR.decidir_por_regra(prop, regras, "1900-02-01")
    rev = {d["artigo"]: d["revisao"] for d in novo["dispositivos"]}
    checar(rev["1"]["decisao"] == "aceitar" and rev["1"]["escopo"] == ["vigencia", "efeitos"]
           and rev["1"]["revisado_por"] == "regra:clausula-literal/v1",
           "data escrita no inciso, publicação no DOU: vigência e efeitos, por regra")
    checar(rev["2"]["escopo"] == ["vigencia"], "sem data de efeitos: só a vigência")
    checar(rev["3"]["escopo"] == ["vigencia"] and rev["4"]["escopo"] == ["vigencia"],
           "alcance mudado pela redação nova, ou ressalva: efeitos ficam para leitura")
    checar(rev["5"]["decisao"] is None,
           "publicação só pelo rodapé (sem DOU): nada por regra")
    checar(rev["9"] == humano["revisao"], "decisão humana nunca é tocada")
    checar(resumo == {"vigencia_e_efeitos": 1, "so_vigencia": 3, "so_efeitos": 0, "nada": 1,
                      "humanas": 1},
           f"resumo da execução (obteve {resumo})")

    ec = _entrada_lc("3", "1930-01-01")
    ec["vigencia"]["proposta"] = {"tipo": "ano", "ano": 1930, "data_candidata": "1930-01-01",
                                  "precisao": "ano"}
    novo, _ = RR.decidir_por_regra(_proposta_para_regra("vigencia_por_inciso", [ec]), regras, "1900-02-01")
    r = novo["dispositivos"][0]["revisao"]
    checar(r["escopo"] == ["vigencia"] and r["revisado_por"] == "regra:clausula-literal/v1+ano-primeiro-dia",
           "forma da EC: só a vigência, e a regra do ano registrada")
    novo, _ = RR.decidir_por_regra(_proposta_para_regra("vigencia_por_inciso", [ec]), {}, "1900-02-01")
    checar(novo["dispositivos"][0]["revisao"]["decisao"] is None,
           "'em 1930' sem a regra do ano aprovada: nada")

    # Reexecução em outro dia: a decisão de regra não muda, então a data também não.
    prop2 = _proposta_para_regra("efeitos_por_inciso", [_entrada_lc("1", "1930-01-01")])
    uma, _ = RR.decidir_por_regra(prop2, regras, "1900-02-01")
    outra, _ = RR.decidir_por_regra(uma, regras, "1900-03-01")
    checar(outra["dispositivos"][0]["revisao"]["revisado_em"] == "1900-02-01",
           "reexecutar sem mudança não altera revisado_em (nada de diff a cada dia)")

    # Proposta regenerada (sem decisões): a memória é o que normas/ já tem aplicado.
    urn = prop2["dispositivos"][0]["urn"]
    aplicada = {"urn": urn, "extracao": "revisada", "eixos_revisados": ["vigencia", "efeitos"],
                "revisado_por": "regra:clausula-literal/v1", "revisado_em": "1900-02-01",
                "vigencia_inicio": "1900-01-02", "efeitos_inicio": "1930-01-01"}
    nova, _ = RR.decidir_por_regra(prop2, regras, "1900-03-01", {urn: aplicada})
    checar(nova["dispositivos"][0]["revisao"]["revisado_em"] == "1900-02-01",
           "proposta regenerada, decisão igual à aplicada em normas/: revisado_em original")
    mudou = {**aplicada, "efeitos_inicio": "1929-01-01"}
    nova, _ = RR.decidir_por_regra(prop2, regras, "1900-03-01", {urn: mudou})
    checar(nova["dispositivos"][0]["revisao"]["revisado_em"] == "1900-03-01",
           "a data adotada mudou: é outra decisão, revisado_em novo")


# Estrutura medida na LC 227, art. 182: alcance em alíneas ("em relação:"),
# subdivisão nomeada de trás para a frente ("à alínea “c” do inciso II do art. 76"),
# termo de evento e "a partir da sua publicação". Conteúdo fictício.
CL_ALINEAS = [
    "Art. 90. Esta Lei Complementar fictícia entra em vigor na data de sua publicação, "
    "produzindo efeitos:",
    "I - a partir de 1º de janeiro de 2030, em relação:",
    "a) à alínea “c” do inciso II do art. 6º;",
    "b) ao art. 7º;",
    "II - a partir da data da eleição de alguém, prevista no art. 1º da Lei fictícia nº 2, "
    "em relação aos §§ 4º e 5º do art. 5º desta Lei Complementar; e",
    "III - a partir da sua publicação, em relação aos demais dispositivos.",
]
EXISTENTES_ALINEAS = ["1", "2", "3", "4", "5", "6", "7", "90"]


@cenario("proposta: alcance em alíneas e subdivisão nomeada de trás para a frente")
def proposta_clausula_alineas():
    """Quebra: perder o alcance que vem nas alíneas (e com ele 'demais
    dispositivos'), ler 'alínea “c” do inciso II do art. 6º' como o art. 6º
    inteiro, ou dar data ao termo de evento."""
    pv = _pv()
    u = lambda n, sub=None: urn_dispositivo(URN_BASE, n) + (f"_{sub}" if sub else "")  # noqa: E731
    r = pv.interpretar_clausula(CL_ALINEAS, URN_BASE, "90", EXISTENTES_ALINEAS)
    checar(r["forma"] == "efeitos_por_inciso", "forma da LC")
    checar([(i["rotulo"], i["interpretado"], i["alcance_interpretado"]) for i in r["incisos"]]
           == [("I", True, True), ("II", False, True), ("III", True, True)],
           f"I com alcance nas alíneas; II com termo de evento, alcance lido; III lido "
           f"(obteve {[(i['rotulo'], i['interpretado'], i['alcance_interpretado']) for i in r['incisos']]})")
    checar(r["incisos"][2]["termo"] == {"tipo": "publicacao"},
           "'a partir da sua publicação' é a publicação")
    m = r["mapa"]
    checar(m["7"]["inciso"] == "I" and m["7"]["termo"] == {"tipo": "data", "data": "2030-01-01"},
           "art. 7º, alínea b: inteiro no inciso I")
    checar(m["6"]["inciso"] == "III"
           and [(e["urn"], e["inciso"]) for e in m["6"]["excecoes"]] == [(u("6", "incII_ali-c"), "I")],
           f"art. 6º: o resto em 'demais'; a alínea c do inciso II do caput no I "
           f"(obteve {[(e['urn'], e['inciso']) for e in m['6']['excecoes']]})")
    checar([(e["urn"], e["inciso"], e["termo"]) for e in m["5"]["excecoes"]]
           == [(u("5", "par4"), "II", None), (u("5", "par5"), "II", None)],
           "§§ 4º e 5º do art. 5º no inciso II, sem data (termo de evento)")
    checar(m["1"]["inciso"] == "III" and m["1"]["termo"] == {"tipo": "publicacao"}
           and m["1"]["motivo"] is None, "os demais: a partir da publicação")

    subs = [u("6", "incII"), u("6", "incII_ali-c")]
    checar(pv.subdivisao_existe(u("6", "incII_ali-c"), subs)
           and pv.subdivisao_existe(u("6", "par0"), [])
           and not pv.subdivisao_existe(u("6", "incII_ali-d"), subs),
           "subdivisão nomeada tem de existir no artigo (o caput sempre existe)")

    pub = {"datas": ["1900-01-02"], "fonte": "dou"}
    clausula_exc = [{"urn": u("6", "incII_ali-c"), "termo": {"tipo": "data", "data": "1930-01-01"},
                     "fundamento": u("90") + "_incI"},
                    {"urn": u("6", "incII_ali-d"), "termo": {"tipo": "data", "data": "1930-01-01"},
                     "fundamento": u("90") + "_incI"}]
    exc, tipos, sem_data, inexistentes = pv.excecoes_de_efeitos(clausula_exc, subs, pub, {})
    checar([e["urn"] for e in exc] == [u("6", "incII_ali-c")] and tipos == ["data"]
           and inexistentes == ["art6_incII_ali-d"] and sem_data == [],
           f"exceção para subdivisão inexistente não entra, e é apontada (obteve {inexistentes})")
    checar(pv.ler_item_preposicionado("à alínea “c” do art. 6º") is None,
           "alínea sem o inciso a que pertence: não é lida")
    proposta = {"tipo": "data", "data_candidata": "1930-01-01"}
    inicio, motivo = pv.efeitos_apos_excecoes(proposta, None, [], ["art6_incII_ali-d"])
    checar(inicio is None and "art6_incII_ali-d" in motivo,
           "subdivisão inexistente: os efeitos do artigo ficam sem data, com o motivo")
    checar(pv.efeitos_apos_excecoes(proposta, None, [], []) == (proposta, None),
           "todas as exceções lidas e existentes: a proposta fica")

    sobra = CL_ALINEAS[:3] + ["b) ao Anexo I;"] + CL_ALINEAS[4:]
    r = pv.interpretar_clausula(sobra, URN_BASE, "90", EXISTENTES_ALINEAS)
    checar(r["incisos"][0]["alcance_interpretado"] is False and m["1"]["inciso"] == "III"
           and pv.interpretar_clausula(sobra, URN_BASE, "90", EXISTENTES_ALINEAS)["mapa"]["1"]["inciso"] is None,
           "uma alínea fora do padrão: o alcance do inciso não é lido, e 'demais' não se resolve")
    externo = pv._ler_inciso("II - em 2030, em relação aos §§ 4º e 5º do art. 52 da Lei nº 1, "
                             "de 1900.", URN_BASE, "90")
    checar(externo["alcance"] is None,
           "subdivisão de artigo de OUTRA norma no alcance: não interpretado")


@cenario("proposta: texto alterado por ato posterior — o literal e a combinação")
def proposta_texto_alterado():
    """Quebra: dar ao texto que a LC 227 incluiu na LC 214 a vigência da LC 214
    (anterior à existência do texto); combinar datas sem a regra aprovada; ou
    combinar uma ligação que o ato alterador não confirma."""
    pv = _pv()
    checar([pv.tipo_da_anotacao(a) for a in (
        "(Incluído pela Lei Complementar nº 999, de 1900)", "(Incluída pela ...)",
        "(Redação dada pela ...)", "(Revogado pela ...)", "(revogada pela ...)", "(Vide ADI 1)")]
           == ["incluido", "incluido", "redacao_dada", "revogado", "revogado", None],
           "tipo lido da anotação")
    aprov = {"texto-alterado-por-ato-posterior": {"aprovada": True, "aprovada_por": "F",
                                                  "aprovada_em": "1900-01-01"}}
    r = pv.combinar_alteracao("incluido", True, "1926-01-14", "1926-01-14",
                              "1925-01-16", "1926-01-01", {})
    checar(r["resultado_se_aprovada"] == {"vigencia_inicio": "1926-01-14",
                                          "efeitos_inicio": "1926-01-14"}
           and r["proposta"] is None,
           f"incluído depois: vale da data mais tardia; sem a regra, só o resultado (obteve {r})")
    r = pv.combinar_alteracao("redacao_dada", True, "1926-01-14", "1926-01-14",
                              "1925-01-16", "1927-01-01", aprov)
    checar(r["proposta"] == {"vigencia_inicio": "1926-01-14", "efeitos_inicio": "1927-01-01"},
           "efeitos que a norma alterada dá ao artigo, se mais tardios, prevalecem; com a regra, "
           "a proposta")
    r = pv.combinar_alteracao("revogado", True, "1926-01-14", "1926-03-01",
                              "1925-01-16", "1926-01-01", aprov)
    checar(r["proposta"] == {"vigencia_fim": "1926-03-01"},
           "revogado: deixa de valer quando o revogador produz EFEITOS (não quando entra em vigor)")
    for args, msg in (((False, "1926-01-14", "1926-01-14", "1925-01-16", "1926-01-01"),
                       "ligação não confirmada"),
                      ((True, "1926-01-14", None, "1925-01-16", "1926-01-01"),
                       "efeitos do ato alterador sem data"),
                      ((True, "1926-01-14", "1926-01-14", "1925-01-16", None),
                       "efeitos do artigo alterado sem data")):
        r = pv.combinar_alteracao("incluido", *args, aprov)
        checar(r["resultado_se_aprovada"] is None and r["proposta"] is None and r["motivo"],
               f"{msg}: nada a combinar, com motivo")

    if not (RAIZ / "normas" / "lc-227-2026").exists():
        print("  pulado (real): normas/lc-227-2026 ausente")
        return
    prop = pv.construir("lc-214-2025", regras={})
    base227 = urn_norma("br:federal:lei.complementar", "2026-01-13", "227")
    por = {d["artigo"]: d for d in prop["dispositivos"]}
    alt = [a for a in por["482-A"]["alteracoes"] if a["ato"] == base227 + "!art174"]
    checar(alt and all(a["tipo"] == "incluido" and a["conferida"]
                       and a["ato_vigencia"] == {"data": "2026-01-14", "fundamento": base227 + "!art182"}
                       and a["ato_efeitos"] == {"data": "2026-01-14",
                                                "fundamento": base227 + "!art182_incIII"}
                       for a in alt),
           f"482-A: incluído pelo art. 174 da LC 227, conferido, com as datas do art. 182 dela "
           f"(obteve {alt[:1]})")
    isolada = [a for a in por["98"]["alteracoes"] if a["subdivisao"] is None]
    checar(isolada and all(not a["conferida"] and a["resultado_se_aprovada"] is None
                           for a in isolada),
           "art. 98: a anotação isolada (do título inserido) não é conferida, nada a combinar")
    ids = {(g["id"], g.get("regra")) for g in prop["pendencias_gerais"]}
    checar(("regra_derivada_nao_aprovada", "texto-alterado-por-ato-posterior") in ids,
           "a combinação aparece como regra derivada não aprovada")
    atos = {a["slug"]: a for a in prop["atos_alteradores"]}
    checar("retificacao_citada_no_rodape" in atos["lc-227-2026"]["pendencias_gerais"],
           "e as pendências do ato alterador ficam à vista")


@cenario("proposta: cláusula única, só vigência ('entra em vigor na data de sua publicação.')")
def proposta_clausula_unica():
    """Forma medida na LC 235, art. 17: 'Esta Lei Complementar entra em vigor na data
    de sua publicação.', sem incisos. Quebra: deixar todos os artigos indeterminados,
    ou tratar a cláusula como se dissesse quando produzem efeitos — ela não diz."""
    pv = _pv()
    r = pv.interpretar_clausula(["Art. 9º Esta Lei fictícia entra em vigor na data de sua "
                                 "publicação."], URN_BASE, "9", EXISTENTES_FICT)
    checar(r["forma"] == "vigencia_unica"
           and r["vigencia"] == {"termo": {"tipo": "publicacao"},
                                 "fundamento": urn_dispositivo(URN_BASE, "9")},
           f"forma reconhecida, vigência de todos no caput (obteve {r['forma']})")
    checar(all(m["motivo"] is None and m["inciso"] is None for m in r["mapa"].values()),
           "nenhum artigo indeterminado")
    com_inciso = pv.interpretar_clausula(
        ["Art. 9º Esta Lei fictícia entra em vigor na data de sua publicação.",
         "I - em 2030, em relação aos arts. 3º e 5º."], URN_BASE, "9", EXISTENTES_FICT)
    checar(com_inciso["forma"] is None, "caput fechado em ponto seguido de inciso: não é a forma")

    import revisar_por_regra as RR
    e = _entrada_lc("3", "1930-01-01")
    e["efeitos"].update(inciso=None)
    novo, _ = RR.decidir_por_regra(_proposta_para_regra("vigencia_unica", [e]), {}, "1900-02-01")
    checar(novo["dispositivos"][0]["revisao"]["escopo"] == ["vigencia"],
           "cláusula única: a regra decide só a vigência")

    if (RAIZ / "normas" / "lc-227-2026").exists():
        # Contrato com o art. 182 real da LC 227, lido em normas/lc-227-2026/art-0182.md.
        prop = pv.construir("lc-227-2026", regras={})
        base = urn_norma("br:federal:lei.complementar", "2026-01-13", "227")
        por = {d["artigo"]: d["efeitos"] for d in prop["dispositivos"]}
        checar(prop["clausula_de_vigencia"]["urn"] == urn_dispositivo(base, "182")
               and por["169"]["inciso"] == "I"
               and por["169"]["proposta"]["data_candidata"] == "2027-01-01",
               "LC 227: art. 169 no inciso I, 1º/01/2027")
        checar(por["76"]["inciso"] == "III" and [(e["urn"], e["efeitos_inicio"])
                                                 for e in por["76"]["excecoes"]]
               == [(urn_dispositivo(base, "76") + "_incII_ali-c", "2027-01-01")],
               f"LC 227: art. 76 nos demais, a alínea c do inciso II em 1º/01/2027 "
               f"(obteve {por['76']['excecoes']})")
        checar(por["52"]["proposta"] is None and por["52"]["motivo"],
               "LC 227: art. 52, §§ 4º e 5º com termo de evento: efeitos sem data, com motivo")
        checar(por["1"]["inciso"] == "III"
               and por["1"]["proposta"]["data_candidata"] == "2026-01-14",
               "LC 227: os demais a partir da publicação no DOU, 14/01/2026")

    if not (RAIZ / "normas" / "lc-235-2026").exists():
        print("  pulado (real): normas/lc-235-2026 ausente")
        return
    prop = pv.construir("lc-235-2026", regras={})
    base = urn_norma("br:federal:lei.complementar", "2026-08-27", "235")
    checar(prop["clausula_de_vigencia"]["urn"] == urn_dispositivo(base, "17")
           and prop["clausula_de_vigencia"]["forma"] == "vigencia_unica",
           "LC 235: cláusula no art. 17, forma única")
    checar(all(d["vigencia"]["proposta"]["data_candidata"] == "2026-08-28"
               for d in prop["dispositivos"]),
           "LC 235: vigência de todos na publicação no DOU, 28/08/2026")


@cenario("revisão por regra: ponto aberto bloqueia")
def revisao_por_regra_bloqueios():
    """Quebra: decidir por regra um artigo cuja redação veio de outro ato, que fixa
    o tempo de dispositivos no próprio texto, ou cuja data depende de uma
    publicação ainda em aberto. A data sairia certa na aparência e errada no fato."""
    import revisar_por_regra as RR

    aprov = {"aprovada": True, "aprovada_por": "F", "aprovada_em": "1900-01-01"}
    todas = {"ano-primeiro-dia": aprov, "primeiro-dia-do-mes-subsequente": aprov}

    def rodar(entradas, gerais=(), forma="efeitos_por_inciso", regras=todas):
        prop = _proposta_para_regra(forma, entradas)
        prop["pendencias_gerais"] = list(gerais)
        novo, resumo = RR.decidir_por_regra(prop, regras, "1900-02-01")
        return {d["artigo"]: d["revisao"] for d in novo["dispositivos"]}, resumo

    for p in ("redacao_de_outro_ato", "parte_de_outro_ato", "clausula_temporal_propria",
              "alcancado_por_clausula_temporal"):
        rev, _ = rodar([_entrada_lc("1", "1930-01-01", pendencias=[p])])
        checar(rev["1"]["decisao"] is None, f"pendência {p}: nada por regra")

    relativo = {"proposta": {"tipo": "relativo", "regra": "primeiro-dia-do-mes-subsequente",
                             "data_candidata": "1900-05-01", "precisao": "dia"}}
    republicacao = [{"id": "rodape_cita_publicacao_nao_confirmada"}]
    rev, resumo = rodar([_entrada_lc("1", "1930-01-01"), _entrada_lc("2", None),
                         _entrada_lc("3", None, efeitos=relativo)], republicacao)
    checar(rev["1"]["escopo"] == ["efeitos"] and resumo["so_efeitos"] == 1,
           "republicação em aberto: a vigência (na publicação) espera; a data escrita dos "
           "efeitos não depende dela")
    checar(rev["2"]["decisao"] is None and rev["3"]["decisao"] is None,
           "republicação em aberto: nada que dependa da data de publicação")
    rev, _ = rodar([_entrada_lc("1", "1930-01-01"), _entrada_lc("2", None)],
                   [{"id": "republicacao_sem_artigo"}])
    checar(rev["1"]["escopo"] == ["efeitos"] and rev["2"]["decisao"] is None,
           "republicação só de anexo com a regra não aprovada: igual à publicação em aberto")
    rev, _ = rodar([_entrada_lc("1", "1930-01-01")], [{"id": "republicacao_de_artigos"}])
    checar(rev["1"]["decisao"] is None, "republicação que traz artigo: nada por regra")

    rev, _ = rodar([_entrada_lc("1", "1930-01-01"), _entrada_lc("2", "1930-01-01")],
                   [{"id": "outro_ato_no_compilado", "artigos": ["1"]}])
    checar(rev["1"]["decisao"] is None and rev["2"]["decisao"] == "aceitar",
           "outro ato no compilado: só os artigos que ele trouxe saem da regra")
    rev, _ = rodar([_entrada_lc("2", "1930-01-01")],
                   [{"id": "outro_ato_no_compilado", "artigos": None}])
    checar(rev["2"]["decisao"] is None, "outro ato sem artigos identificados: nada por regra")
    rev, _ = rodar([_entrada_lc("2", "1930-01-01")], [{"id": "ponto_que_a_regra_nao_conhece"}])
    checar(rev["2"]["decisao"] is None, "pendência geral desconhecida: na dúvida, nada")

    rev, _ = rodar([_entrada_lc("3", None, efeitos=relativo)])
    checar(rev["3"]["escopo"] == ["vigencia", "efeitos"] and rev["3"]["revisado_por"]
           == "regra:clausula-literal/v1+primeiro-dia-do-mes-subsequente",
           "termo relativo com a regra aprovada: decide, e registra a regra")
    rev, _ = rodar([_entrada_lc("3", None, efeitos=relativo)],
                   regras={"ano-primeiro-dia": aprov})
    checar(rev["3"]["escopo"] == ["vigencia"], "regra do termo relativo não aprovada: efeitos ficam")

    exc = {"excecoes": [{"urn": urn_dispositivo(URN_EC, "1", paragrafo="1"),
                         "efeitos_inicio": "1931-01-01", "fundamento": ["x"]}]}
    rev, _ = rodar([_entrada_lc("1", "1930-01-01", efeitos=dict(exc))])
    checar(rev["1"]["escopo"] == ["vigencia"],
           "exceção por subdivisão sem o tipo do termo registrado: efeitos ficam")
    rev, _ = rodar([_entrada_lc("1", "1930-01-01",
                                efeitos={**exc, "termos_das_excecoes": ["data"]})])
    checar(rev["1"]["escopo"] == ["vigencia", "efeitos"], "exceção com data escrita: decide")
    rev, _ = rodar([_entrada_lc("1", "1930-01-01",
                                efeitos={**exc, "termos_das_excecoes": ["evento"]})],
                   republicacao)
    checar(rev["1"]["decisao"] is None,
           "exceção que depende da publicação em aberto: os efeitos ficam (e a vigência também)")

    ec = _entrada_lc("3", None, pendencias=["alcance_alterado_pela_redacao_posterior"])
    ec["vigencia"]["inciso"] = "I"
    rev, _ = rodar([ec], forma="vigencia_por_inciso")
    checar(rev["3"]["decisao"] is None,
           "forma da EC: o inciso que dá a vigência mudou de alcance, nada por regra")


@cenario("revisão: decisão de regra só vale com as regras que ela usa aprovadas")
def revisao_regra_revogada():
    """Quebra: revogar a aprovação de uma regra derivada e o fatiamento continuar
    aplicando as datas que dependiam dela, porque ninguém rodou revisar_por_regra.py;
    ou aceitar um `revisado_por: regra:...` que não é regra nenhuma do código."""
    rev = {"decisao": "aceitar", "escopo": ["vigencia"],
           "revisado_por": "regra:clausula-literal/v1+ano-primeiro-dia", "revisado_em": "1900-02-01"}
    aprov = {"ano-primeiro-dia": {"aprovada": True, "aprovada_por": "F", "aprovada_em": "1900-01-01"}}
    revs, erros = _carregar([_entrada("3", rev)], regras=aprov)
    checar(not erros and revs, f"regra aprovada: aplica (erros: {erros})")
    revs, erros = _carregar([_entrada("3", rev)], regras={})
    checar(not revs and len(erros) == 1 and "revisar_por_regra" in erros[0],
           f"regra que deixou de estar aprovada: erro, nada aplicado (obteve {erros})")
    literal = {**rev, "revisado_por": "regra:clausula-literal/v1"}
    revs, erros = _carregar([_entrada("3", literal)], regras={})
    checar(not erros and revs, "a regra literal é código, não depende de aprovação")
    inventada = {**rev, "revisado_por": "regra:inventada/v1"}
    revs, erros = _carregar([_entrada("3", inventada)], regras=aprov)
    checar(not revs and len(erros) == 1, "regra que o código não tem: erro")


@cenario("proposta: termo relativo à publicação só vira data com a regra aprovada")
def proposta_termo_relativo():
    """Quebra: converter 'quarto mês subsequente' em data sem a regra aprovada, ou
    aceitar uma forma sem ordinal, que o padrão não conhece."""
    pv = _pv()
    lido = pv._ler_termo("a partir do primeiro dia do quarto mês subsequente ao da sua publicação")
    checar(lido == {"tipo": "relativo_publicacao", "regra": "primeiro-dia-do-mes-subsequente",
                    "meses": 4}, f"ordinal por extenso vira número de meses (obteve {lido})")
    checar(pv._ler_termo("a partir do primeiro dia do mês subsequente ao da sua publicação")
           is None, "sem ordinal: fora do padrão, não interpretado")
    pub = {"datas": ["1900-01-16"], "fonte": "dou", "dou": {}}
    aprovada = {"primeiro-dia-do-mes-subsequente": {"aprovada": True, "aprovada_por": "F",
                                                    "aprovada_em": "1900-01-01"}}
    com = pv._inicio_proposto(lido, pub, aprovada)
    sem = pv._inicio_proposto(lido, pub, {})
    checar(com["tipo"] == "relativo" and com["regra"] == "primeiro-dia-do-mes-subsequente"
           and com["data_candidata"] == "1900-05-01", "regra aprovada: a data é calculada")
    checar(sem["data_candidata"] is None and sem["resultado_se_aprovada"] == "1900-05-01",
           "regra não aprovada: sem data, mas a proposta mostra o que ela daria")
    nada = pv._inicio_proposto(lido, {"datas": [], "fonte": None}, aprovada)
    checar(nada["data_candidata"] is None and nada["resultado_se_aprovada"] is None,
           "sem publicação localizada: nada a calcular")


@cenario("proposta: redação de outro ato, partes trazidas por outro ato, cláusula própria")
def proposta_outro_ato():
    """Quebra: tratar como texto original um artigo que lei posterior incluiu,
    alterou ou revogou em parte, ou que um ato de promulgação de partes vetadas
    trouxe — a cláusula de vigência desta norma não vale para esse texto; ou
    ignorar um artigo que fixa, no próprio texto, quando ele ou outro dispositivo
    entra em vigor ou produz efeitos."""
    pv = _pv()
    corpo = ["Art. 3º Texto original de R$ 10,00 (dez reais).",
             "§ 1º Outro. (Incluído pela Lei Complementar nº 998, de 2030)",
             "~~II - antigo. (Revogado)~~",
             "III - (VETADO)",
             "IV - item. (Promulgação partes vetadas)"]
    checar(pv.marcas_de_outro_ato(corpo) == [
        "(Incluído pela Lei Complementar nº 998, de 2030)", "(Revogado)", "(VETADO)",
        "(Promulgação partes vetadas)"], "anotações de outro ato, na ordem do texto")
    checar(pv.marcas_de_outro_ato(["Art. 4º Valor de R$ 10,00 (dez reais)."]) == [],
           "parêntese comum não é anotação")

    linhas = ["Art. 1º Texto.", "Art. 2º Texto.", "Brasília, 1º de janeiro de 1900.", "FULANO",
              "Este texto não substitui o publicado no DOU de 2.1.1900", "ANEXO I", "tabela",
              "O PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu "
              "promulgo as seguintes partes vetadas da Lei fictícia.",
              "“Art. 2º ..........", "..........", "X - item.", "“Art. 3º-A ..........",
              "Brasília, 1º de julho de 1900.", "FULANO",
              "Este texto não substitui o publicado no DOU de 2.7.1900."]
    checar(pv.artigos_de_outros_atos(linhas) == [
        {"assinatura": "Brasília, 1º de julho de 1900.", "artigos": ["2", "3-A"]}],
        "o bloco de promulgação cita, entre aspas, os arts. 2 e 3-A")
    sem_citacao = linhas[:8] + ["Art. 1º Fica revogado o que for."] + linhas[12:]
    checar(pv.artigos_de_outros_atos(sem_citacao)[0]["artigos"] is None,
           "bloco sem artigo citado entre aspas: não se sabe o que ele trouxe")
    sem_preambulo = linhas[:7] + linhas[8:]
    checar(pv.artigos_de_outros_atos(sem_preambulo)[0]["artigos"] is None,
           "sem o preâmbulo do outro ato, o bloco não é delimitado: não se sabe")

    marcos = [{"urn": "x", "tipos": ["produz_efeitos", "ano"],
               "trecho": "§ 2º O disposto no art. 7º desta Lei produzirá efeitos a partir de 1930."},
              {"urn": "y", "tipos": ["ano"], "trecho": "§ 3º Em 1931, aplica-se o art. 8º desta Lei."}]
    checar(pv.clausula_temporal_propria(marcos, URN_BASE, "3", False) == (True, ["7"]),
           "o artigo fixa o tempo de outro dispositivo: os dois ficam fora da regra")
    checar(pv.clausula_temporal_propria(marcos[1:], URN_BASE, "3", False) == (False, []),
           "marco de ano não é cláusula temporal")


@cenario("proposta: decisão de regra não impede regenerar; humana impede")
def proposta_guarda_regra():
    import tempfile

    import yaml

    p = _pv()
    with tempfile.TemporaryDirectory() as tmp:
        alvo = Path(tmp) / "proposta.yaml"
        so_regra = {"dispositivos": [{"artigo": "1", "revisao": {
            "decisao": "aceitar", "revisado_por": "regra:clausula-literal/v1"}}]}
        alvo.write_text(yaml.safe_dump(so_regra), encoding="utf-8")
        checar(p.gravar_proposta(alvo, {"dispositivos": []}) is True,
               "só decisões de regra: pode regenerar (elas são refeitas por revisar_por_regra)")
        humana = {"dispositivos": [{"artigo": "1", "revisao": {
            "decisao": "aceitar", "revisado_por": "Revisora"}}]}
        alvo.write_text(yaml.safe_dump(humana), encoding="utf-8")
        checar(p.gravar_proposta(alvo, {"dispositivos": []}) is False, "decisão humana: recusa")


@cenario("revisão: data sem aspas no YAML editado à mão")
def revisao_data_sem_aspas():
    """Quebra: tratar só texto como data. Quem revisa escreve `2027-01-01` sem
    aspas, e o YAML entrega um objeto `date`; a revisão seria rejeitada ou, pior,
    gravada num formato que a comparação depois não reconhece."""
    import datetime as dt

    revisao = {"decisao": "alterar", "revisado_por": "Revisora Fictícia",
               "revisado_em": dt.date(1900, 2, 1),
               "vigencia_inicio": dt.date(1900, 1, 2), "efeitos_inicio": dt.date(1901, 1, 1),
               "precisao": {"efeitos_inicio": "ano"},
               "fundamento_vigencia": [urn_dispositivo(URN_EC, "23", inciso="III")],
               "fundamento_efeitos": [urn_dispositivo(URN_EC, "7")]}
    revs, erros = _carregar([_entrada("3", revisao)])
    r = revs.get(urn_dispositivo(URN_EC, "3"))
    checar(not erros and r is not None, f"datas sem aspas são aceitas (erros: {erros})")
    checar(r and r["vigencia_inicio"] == "1900-01-02" and r["revisado_em"] == "1900-02-01",
           "e gravadas como texto AAAA-MM-DD")


@cenario("revisão: deriva da fonte invalida a revisão")
def revisao_deriva():
    """Quebra: aplicar uma revisão feita sobre outro texto. Se o sha256 do original
    mudou, a decisão humana pode não valer mais para o texto atual."""
    revs, erros = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR})], sha="b" * 64)
    checar(not revs and len(erros) == 1, "sha256 diferente: nada aplicado, um erro")
    revs, erros = _carregar([_entrada("3", {})], sha="b" * 64)
    checar(not revs and not erros, "sem decisão nenhuma, a deriva não é erro (nada a aplicar)")


@cenario("revisão: 'rejeitar' e 'alterar' com exceção por subdivisão")
def revisao_rejeitar_e_excecao():
    revs, erros = _carregar([_entrada("3", {"decisao": "rejeitar", **REVISOR})])
    checar(not revs and not erros, "'rejeitar' não aplica nada e não é erro")

    exc = {"urn": urn_dispositivo(URN_EC, "5", paragrafo="1"), "efeitos_inicio": "1905-01-01",
           "fundamento": [urn_dispositivo(URN_EC, "23", inciso="II")]}
    revisao = {"decisao": "alterar", **REVISOR, "vigencia_inicio": "1900-01-02",
               "efeitos_inicio": "1900-01-02",
               "fundamento_vigencia": [urn_dispositivo(URN_EC, "23", inciso="III")],
               "fundamento_efeitos": [urn_dispositivo(URN_EC, "23", inciso="III")],
               "excecoes_subdivisao": [exc]}
    revs, erros = _carregar([_entrada("5", revisao, termo="publicacao")])
    checar(not erros and revs[urn_dispositivo(URN_EC, "5")]["excecoes_subdivisao"] == [exc],
           f"exceção do § 1º é aceita (erros: {erros})")

    alheia = dict(exc, urn=urn_dispositivo(URN_EC, "6", paragrafo="1"))
    _, erros = _carregar([_entrada("5", dict(revisao, excecoes_subdivisao=[alheia]),
                                   termo="publicacao")])
    checar(len(erros) == 1, "exceção que não é subdivisão do próprio artigo: erro")


@cenario("revisão: aplicar ao front-matter")
def revisao_aplicar():
    meta = {"urn": urn_dispositivo(URN_EC, "3"), "vigencia_inicio": "1900-01-02",
            "efeitos_inicio": "1900-01-02", "vigencia_fim": None, "efeitos_fim": None,
            "extracao": "automatica", "revisao_temporal_pendente": True,
            "revisado_por": None, "revisado_em": None}
    revs, _ = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR})])
    novo = _rt().aplicar_revisao(meta, revs[urn_dispositivo(URN_EC, "3")])
    checar(novo["vigencia_inicio"] == "2030-01-01" and novo["extracao"] == "revisada"
           and novo["revisao_temporal_pendente"] is False
           and novo["revisado_por"] == "Revisora Fictícia",
           "datas, extracao, pendência e revisor atualizados")
    checar(meta["extracao"] == "automatica", "o meta original não é alterado")
    erros, _ = _rt().problemas_no_dispositivo(novo)
    checar(not erros, f"o resultado passa na validação (erros: {erros})")


@cenario("validação do front-matter temporal")
def revisao_validacao_front_matter():
    """Quebra: aceitar em normas/ um dispositivo 'revisado' sem fundamento, ou com
    precisão inventada. É o que a CI precisa recusar mesmo se alguém editar à mão."""
    ok = {"urn": urn_dispositivo(URN_EC, "3"), "data_ato": "1900-01-01",
          "publicacao": {"datas": ["1900-01-02"], "fonte": "rodape_compilado"},
          "vigencia_inicio": "1900-01-02", "efeitos_inicio": "1900-01-02",
          "extracao": "automatica", "revisao_temporal_pendente": True}
    erros, avisos = _rt().problemas_no_dispositivo(ok)
    checar(not erros, f"dispositivo automático coerente passa (erros: {erros})")

    erros, _ = _rt().problemas_no_dispositivo(dict(ok, extracao="revisada",
                                                   revisao_temporal_pendente=False))
    checar(erros, "'revisada' sem revisor nem fundamento: erro")
    erros, _ = _rt().problemas_no_dispositivo(dict(
        ok, extracao="revisada", revisao_temporal_pendente=False,
        revisado_por="Revisora Fictícia", revisado_em="1900-02-01"))
    checar(erros == ["extracao revisada sem fundamento_temporal de vigência e de efeitos"],
           "'revisada' com revisor mas sem fundamento: erro, e só esse")
    erros, _ = _rt().problemas_no_dispositivo(dict(ok, precisao={"vigencia_inicio": "mes"}))
    checar(erros, "precisão fora de ano/dia: erro")
    erros, _ = _rt().problemas_no_dispositivo(dict(ok, publicacao={"datas": ["21/12/2023"],
                                                                     "fonte": "dou"}))
    checar(erros, "data de publicação fora do formato ISO: erro")
    erros, avisos = _rt().problemas_no_dispositivo(dict(ok, publicacao={"datas": [],
                                                                          "fonte": None}))
    checar(not erros and avisos, "publicação não localizada: aviso, não erro")


@cenario("validação: decisão tomada e ainda não aplicada a normas/")
def revisao_nao_aplicada():
    revs, _ = _carregar([_entrada("3", {"decisao": "aceitar", **REVISOR})])
    urn = urn_dispositivo(URN_EC, "3")
    automatico = {"urn": urn, "vigencia_inicio": "1900-01-02", "efeitos_inicio": "1900-01-02",
                  "extracao": "automatica"}
    checar(len(_rt().revisoes_nao_aplicadas(revs, [automatico])) == 1,
           "revisão decidida com normas/ ainda automático: erro (rode fatiar.py)")
    aplicado = _rt().aplicar_revisao(automatico, revs[urn])
    checar(_rt().revisoes_nao_aplicadas(revs, [aplicado]) == [],
           "depois de aplicada, nada a acusar")


@cenario("front-matter: data do ato separada da publicação")
def front_matter_ato_e_publicacao():
    """Quebra: gravar a data do ato como `publicacao`. A EC diz 'entra em vigor na
    data de sua publicação', e a publicação no DOU é outro dia."""
    refs = F.extrair_referencias([ln.completa for ln in F.html_para_linhas(fixture("planalto-ec.html"))])
    pub = F.publicacao_de(refs)
    checar(pub == {"datas": ["1900-01-02"], "fonte": "rodape_compilado",
                   "trechos": ["Este texto não substitui o publicado no DOU 2.1.1900"]},
           f"publicação lida do rodapé do fixture, com a origem declarada (obteve {pub})")
    checar(F.publicacao_de({"publicacao_dou": {"valores": [], "trechos": []}})
           == {"datas": [], "fonte": None, "trechos": []},
           "sem rodapé: publicação vazia, não suposta")

    fonte = {"titulo": "Emenda fictícia", "slug": "emc-999-1900", "data": "1900-01-01"}
    registro = {"url": "https://exemplo.invalido", "tipo_documento": "texto_compilado",
                "acesso": "1900-03-01", "sha256": "a" * 64}
    artigo = {"numero": "3", "hierarquia": [], "linhas": ["Art. 3º Texto."],
              "linhas_vigentes": ["Art. 3º Texto."], "linhas_proprias": ["Art. 3º Texto."],
              "citados": []}
    meta, corpo = F.montar_meta(artigo, fonte, registro, URN_EC, pub, False)
    checar(meta["data_ato"] == "1900-01-01" and meta["publicacao"] == pub,
           "data_ato do catálogo e publicação do rodapé, em campos distintos")
    checar(meta["vigencia_inicio"] == "1900-01-02" and meta["efeitos_inicio"] == "1900-01-02",
           "provisórias: a primeira publicação, não a data do ato")
    checar(list(meta)[:8] == ["urn", "norma", "norma_slug", "dispositivo", "camada",
                              "hierarquia", "data_ato", "publicacao"],
           "ordem canônica do front-matter")
    meta2, _ = F.montar_meta(artigo, fonte, registro, URN_EC,
                             {"datas": [], "fonte": None, "trechos": []}, False)
    checar(meta2["vigencia_inicio"] == "1900-01-01",
           "sem publicação localizada, a provisória cai para a data do ato")


@cenario("proposta: LC 214 real (pulado se normas/ ou fontes/ ausentes)")
def proposta_lc_real():
    """Contrato com o art. 544 real, lido à mão em normas/lc-214-2025/art-0544.md:
    vigência na publicação; efeitos I (termo relativo) 537 a 540; II 1º/1/2025 com
    35, '58, caput', '60, § 3º', 480 a 484; III (redação dada pela LC 227/2026)
    1º/1/2027 com 168 a 171 e '450, exceto os §§ 1º e 5º'; IV 1º/1/2029 com 446 e
    '450, §§ 1º e 5º'; V 1º/1/2033 com 518; VI 1º/1/2026 os demais. Publicação no
    DOU em 16/01/2025."""
    if not (RAIZ / "normas" / "lc-214-2025").exists() or \
            not (RAIZ / "fontes" / "lc-214-2025" / "texto_compilado.html").exists():
        print("  pulado: normas/ ou fontes/ da LC 214 ausentes")
        return
    prop = _pv().construir("lc-214-2025", regras={})
    base = urn_norma("br:federal:lei.complementar", "2025-01-16", "214")
    u = lambda n, **kw: urn_dispositivo(base, n, **kw)  # noqa: E731
    por = {d["artigo"]: d for d in prop["dispositivos"]}
    checar(prop["clausula_de_vigencia"]["forma"] == "efeitos_por_inciso"
           and prop["clausula_de_vigencia"]["urn"] == u("544"), "cláusula: art. 544, forma da LC")
    checar(all(d["vigencia"]["proposta"]["data_candidata"] == "2025-01-16"
               and d["vigencia"]["fundamento"] == u("544") for d in prop["dispositivos"]),
           "vigência de todos: publicação no DOU, fundamentada no caput")
    esperado = {"35": ("II", "2025-01-01"), "1": ("VI", "2026-01-01"), "168": ("III", "2027-01-01"),
                "446": ("IV", "2029-01-01"), "518": ("V", "2033-01-01"), "482": ("II", "2025-01-01"),
                "537": ("I", None), "482-A": (None, None)}
    obtido = {n: (por[n]["efeitos"]["inciso"],
                  (por[n]["efeitos"]["proposta"] or {}).get("data_candidata"))
              for n in esperado}
    checar(obtido == esperado, f"efeitos por inciso (obteve {obtido})")
    exc = {n: [(e["urn"], e["efeitos_inicio"]) for e in por[n]["efeitos"]["excecoes"]]
           for n in ("58", "60", "450")}
    checar(exc == {"58": [(u("58", paragrafo="0"), "2025-01-01")],
                   "60": [(u("60", paragrafo="3"), "2025-01-01")],
                   "450": [(u("450", paragrafo="1"), "2029-01-01"),
                           (u("450", paragrafo="5"), "2029-01-01")]},
           f"subdivisões com efeitos próprios (obteve {exc})")
    checar(por["58"]["efeitos"]["termos_das_excecoes"] == ["data"]
           and por["450"]["efeitos"]["termos_das_excecoes"] == ["data", "data"],
           "o tipo do termo de cada exceção fica registrado, para a revisão por regra")
    checar(por["58"]["efeitos"]["inciso"] == "VI" and por["450"]["efeitos"]["inciso"] == "III",
           "o resto do art. 58 cai em 'demais'; o art. 450 fica no III")
    checar("alcance_alterado_pela_redacao_posterior" in por["168"]["pendencias"]
           and "alcance_alterado_pela_redacao_posterior" not in por["461"]["pendencias"],
           "168 só está na redação nova do III; 461 está nas duas")
    ids = {p["id"] for p in prop["pendencias_gerais"]}
    checar({"outro_ato_no_compilado", "republicacao_sem_artigo",
            "regra_derivada_nao_aprovada"} <= ids
           and "rodape_cita_publicacao_nao_confirmada" not in ids,
           f"pendências gerais: o outro ato anexado, a republicação de 23/01/2025 (só o Anexo "
           f"XXIII) e, sem regras aprovadas, a do inciso I (obteve {sorted(ids)})")
    checar(por["537"]["efeitos"]["proposta"]["resultado_se_aprovada"] == "2025-05-01",
           "inciso I: 'quarto mês subsequente' à publicação de 16/01/2025, se a regra for aprovada")
    outro = next(p for p in prop["pendencias_gerais"] if p["id"] == "outro_ato_no_compilado")
    checar(outro["artigos"] == ["26"], f"o ato de 1º/07/2025 trouxe partes do art. 26 (obteve "
                                       f"{outro['artigos']})")
    checar({"redacao_de_outro_ato", "parte_de_outro_ato"} <= set(por["26"]["pendencias"]),
           "art. 26: anotado e trazido em parte pelo outro ato")
    checar("redacao_de_outro_ato" in por["482-A"]["pendencias"]
           and "redacao_de_outro_ato" not in por["1"]["pendencias"],
           "482-A incluído por lei posterior; art. 1 sem anotação")
    checar("clausula_temporal_propria" in por["19"]["pendencias"]
           and "clausula_temporal_propria" not in por["544"]["pendencias"],
           "art. 19, II 'somente entrará em vigor com...': cláusula própria; a do 544 é a da norma")
    aprovada = {"primeiro-dia-do-mes-subsequente": {"aprovada": True, "aprovada_por": "F",
                                                    "aprovada_em": "1900-01-01"}}
    com = {d["artigo"]: d for d in _pv().construir("lc-214-2025", regras=aprovada)["dispositivos"]}
    checar(com["537"]["efeitos"]["proposta"]["data_candidata"] == "2025-05-01",
           "com a regra aprovada, a data é proposta")


@cenario("contrato: a proposta gerada é consumível pela revisão (EC 132 real)")
def contrato_proposta_revisao():
    """Quebra: o gerador e o consumidor divergirem no formato. A revisão humana seria
    feita num arquivo que o fatiamento depois rejeita, ou lê errado."""
    import json
    import tempfile

    import yaml

    if not (RAIZ / "normas" / "emc-132-2023").exists() or \
            not (RAIZ / "fontes" / "emc-132-2023" / "texto_compilado.html").exists():
        print("  pulado: normas/ ou fontes/ da EC 132 ausentes")
        return
    prop = _pv().construir("emc-132-2023")
    manifest = json.loads((RAIZ / "fontes" / "manifest.json").read_text(encoding="utf-8"))
    sha = manifest["documentos"]["emc-132-2023/texto_compilado"]["sha256"]
    checar(prop.get("fonte_sha256") == sha, "a proposta registra o sha256 do original")

    # Art. 14: inciso III do art. 23 e nenhum marco próprio (lido no texto).
    entrada = next(d for d in prop["dispositivos"] if d["artigo"] == "14")
    entrada["revisao"].update({"decisao": "aceitar", "revisado_por": "Teste",
                               "revisado_em": "2026-01-01"})
    with tempfile.TemporaryDirectory() as tmp:
        caminho = Path(tmp) / "emc-132-2023.yaml"
        caminho.write_text(yaml.safe_dump(prop, allow_unicode=True), encoding="utf-8")
        revs, erros = _rt().carregar_revisoes(
            caminho, sha, {d["urn"] for d in prop["dispositivos"]})
    r = revs.get(entrada["urn"])
    checar(not erros and r is not None, f"carregada sem erro (erros: {erros})")
    checar(r and r["vigencia_inicio"] == "2023-12-21" and r["efeitos_inicio"] == "2023-12-21"
           and r["fundamento_temporal"]["vigencia"] == [prop["clausula_de_vigencia"]["urn"] + "_incIII"],
           "art. 14: publicação no DOU segundo o rodapé, fundamentada no art. 23, III")


@cenario("consulta: precisão de ano e exceções por subdivisão")
def consulta_precisao_e_excecoes():
    """Quebra: omitir da consulta, como 'revogado', um dispositivo cuja revogação é
    'em 2033' quando a data consultada cai em 2033 (o dia não está no texto); ou
    omitir um artigo ainda futuro que tem um parágrafo já em vigor."""
    import datetime as dt

    import consultar as C

    revogado_em_ano = {
        "urn": urn_dispositivo(URN_EC, "22"), "vigencia_inicio": "1900-01-02",
        "vigencia_fim": "2033-01-01", "efeitos_inicio": "1900-01-02", "efeitos_fim": None,
        "precisao": {"vigencia_fim": "ano"},
    }
    checar(C.incertezas(revogado_em_ano, dt.date(2033, 6, 1)) != [],
           "em 2033 o estado é incerto: há aviso")
    checar(C.incertezas(revogado_em_ano, dt.date(2032, 6, 1)) == [], "em 2032, nenhum aviso")
    checar(status_em(revogado_em_ano, dt.date(2033, 6, 1)) == "revogado"
           and C.relevante_na_data(revogado_em_ano, dt.date(2033, 6, 1)),
           "'revogado' pela convenção de 1º de janeiro, mas NÃO omitido no ano incerto")
    checar(not C.relevante_na_data(revogado_em_ano, dt.date(2034, 6, 1)),
           "em 2034 a revogação é certa: omitido")

    par3 = urn_dispositivo(URN_EC, "9", paragrafo="3")
    futuro = {
        "urn": urn_dispositivo(URN_EC, "9"), "vigencia_inicio": "2030-01-01",
        "vigencia_fim": None, "efeitos_inicio": "2030-01-01", "efeitos_fim": None,
        "excecoes_subdivisao": [{"urn": par3, "vigencia_inicio": "1900-01-02",
                                 "efeitos_inicio": "1900-01-02",
                                 "fundamento": [urn_dispositivo(URN_EC, "23")]}],
    }
    ref = dt.date(1950, 1, 1)
    checar(status_em(futuro, ref) == "futuro" and C.relevante_na_data(futuro, ref),
           "artigo futuro com parágrafo já vigente aparece na consulta")
    checar(C.excecoes_na_data(futuro, ref) == [(par3, "vigente")],
           "e o parágrafo aparece com o próprio estado")


@cenario("status: todo estado que status_em produz está no vocabulário")
def status_no_vocabulario():
    """Quebra: a validação chamar de 'fora do vocabulário' um estado que o próprio
    código calcula — vigente e ainda sem efeitos é justamente o caso que separa
    vigência de eficácia (PREMISSAS.md §3.1)."""
    import datetime as dt

    from comum import STATUS_VALIDOS

    base = {"vigencia_inicio": "1900-01-01", "vigencia_fim": None,
            "efeitos_inicio": "1900-01-01", "efeitos_fim": None}
    casos = [base, {**base, "vigencia_fim": "1900-06-01"}, {**base, "vigencia_inicio": "1950-01-01"},
             {**base, "efeitos_fim": "1900-06-01"}, {**base, "efeitos_inicio": "1950-01-01"}]
    estados = {status_em(m, dt.date(1910, 1, 1)) for m in casos}
    checar(len(estados) == 5 and estados <= STATUS_VALIDOS,
           f"estados produzidos {sorted(estados)} cabem em {sorted(STATUS_VALIDOS)}")


@cenario("validação: o aviso de pendência separa o todo provisório do eixo que falta")
def validar_resumo_pendencias():
    """Quebra: dizer 'vigência e eficácia provisórias' de um dispositivo que já teve
    um dos eixos decidido, ou contar decisão de regra como revisão humana."""
    import validar as V

    auto = {"extracao": "automatica", "revisao_temporal_pendente": True}
    so_vig = {"extracao": "revisada", "eixos_revisados": ["vigencia"],
              "revisao_temporal_pendente": True, "revisado_por": "regra:clausula-literal/v1"}
    so_efe = {**so_vig, "eixos_revisados": ["efeitos"]}
    humano = {"extracao": "revisada", "eixos_revisados": ["vigencia", "efeitos"],
              "revisao_temporal_pendente": False, "revisado_por": "Revisora"}
    r = V.resumo_pendencias([auto, so_vig, so_efe, so_efe, humano])
    checar(r == {"total": 5, "tudo_provisorio": 1, "falta_efeitos": 1, "falta_vigencia": 2,
                 "por_regra": 3, "por_ia": 0, "por_pessoa": 1}, f"contagem (obteve {r})")


@cenario("consulta: diz quem fixou as datas e o que continua provisório")
def consulta_origem_das_datas():
    """Quebra: apresentar data fixada por regra ou por IA como se fosse revisão
    humana, ou calar que os efeitos continuam provisórios quando só a vigência
    foi decidida (PREMISSAS.md §3.4)."""
    import consultar as C

    auto = {"extracao": "automatica", "revisao_temporal_pendente": True}
    checar(any("PROVISORI" in linha for linha in C.origem_das_datas(auto)),
           "extração automática: tudo provisório")
    regra = {"extracao": "revisada", "eixos_revisados": ["vigencia"],
             "revisao_temporal_pendente": True, "revisado_por": "regra:clausula-literal/v1",
             "revisado_em": "1900-01-01"}
    linhas = C.origem_das_datas(regra)
    checar(any("vigencia" in linha and "regra" in linha and "sem leitura humana" in linha
               for linha in linhas), f"vigência fixada por regra, dito assim (obteve {linhas})")
    checar(any("efeitos" in linha and "PROVISORI" in linha for linha in linhas),
           "efeitos ainda provisórios, dito assim")
    ia = {**regra, "eixos_revisados": ["vigencia", "efeitos"], "revisao_temporal_pendente": False,
          "revisado_por": "ia:modelo-x"}
    checar(any("NAO equivale a revisao humana" in linha for linha in C.origem_das_datas(ia)),
           "registro de IA não passa por revisão humana")
    humano = {**ia, "revisado_por": "Revisora"}
    checar(C.origem_das_datas(humano) == ["vigencia e efeitos revisados por Revisora em 1900-01-01"],
           f"revisão humana (obteve {C.origem_das_datas(humano)})")


@cenario("DOU: cabeçalho de publicação lido da página do ato")
def dou_cabecalho():
    """Quebra: tomar a data de outro lugar da página (o título repetido na navegação,
    o rodapé do site) ou tropeçar no <span> sem fechar do original."""
    dados = (FIXTURES / "dou-materia.html").read_bytes()
    checar(
        F.publicacao_dou(dados) == {
            "data": "1900-01-02", "edicao": "99-B", "secao": "1 - Extra B", "pagina": "1",
            "trecho": "Publicado em: 02/01/1900 | Edição: 99-B | Seção: 1 - Extra B | Página: 1",
        },
        f"data, edição, seção e página do cabeçalho (obteve {F.publicacao_dou(dados)})",
    )
    checar(F.publicacao_dou(fixture("planalto-ec.html")) is None,
           "página sem cabeçalho do DOU: nada, não um palpite")
    texto = dados.decode("utf-8")
    com_vizinho = texto.replace(
        '<article id="materia">',
        '<aside><span class="publicado-dou-data">31/12/1899</span></aside> <article id="materia">', 1)
    checar(F.publicacao_dou(com_vizinho.encode("utf-8"))["data"] == "1900-01-02",
           "um campo de data fora de <article id=\"materia\"> (ato vizinho) é ignorado")


@cenario("DOU: a publicação confirmada prevalece; o rodapé fica registrado")
def dou_prevalece():
    """Quebra: descartar o que o rodapé do compilado diz, ou mantê-lo como se fosse
    confirmado. A data que só o rodapé cita (na LC 214, a republicação de 23/01/2025)
    precisa continuar visível, como não confirmada."""
    dou = F.publicacao_dou((FIXTURES / "dou-materia.html").read_bytes())
    refs = {"publicacao_dou": {"valores": ["1900-01-02", "1900-01-09"],
                               "trechos": ["... DOU de 2.1.1900 e republicado no DOU de 9.1.1900"]}}
    pub = F.publicacao_de(refs, dou)
    checar(pub["datas"] == ["1900-01-02"] and pub["fonte"] == "dou"
           and pub["trechos"] == [dou["trecho"]],
           "datas e trecho vêm do DOU")
    checar(pub["dou"] == {"edicao": "99-B", "secao": "1 - Extra B", "pagina": "1"},
           "edição, seção e página registradas")
    checar(pub["rodape_compilado"] == {"datas": ["1900-01-02", "1900-01-09"],
                                       "trechos": refs["publicacao_dou"]["trechos"]},
           "o rodapé do compilado continua registrado, à parte")
    meta = {"urn": urn_dispositivo(URN_EC, "1"), "publicacao": pub,
            "extracao": "automatica", "revisao_temporal_pendente": True}
    erros, avisos = _rt().problemas_no_dispositivo(meta)
    checar(not erros and any("1900-01-09" in a for a in avisos),
           "a data que só o rodapé cita vira aviso de não confirmada")
    checar(F.publicacao_de(refs) ["fonte"] == "rodape_compilado",
           "sem DOU arquivado, continua o rodapé")


# Estrutura das linhas que o pypdf extrai da página do DOU em PDF (LC 214, DOU de
# 23/01/2025, p. 1): cabeçalho com data e número, código de autenticidade,
# 'R E P U B L I C A Ç Ã O' antes do título, o bloco republicado, a nota '(*)' e,
# logo depois, o próximo ato da página. Conteúdo fictício.
LINHAS_REPUB = [
    "REPÚBLICA FEDERATIVA DO BRASIL • IMPRENSA NACIONAL",
    "Ano I Nº 7 Brasília - DF, terça-feira, 9 de janeiro de 1900",
    "ISSN 0000-0000",
    "1",
    "Documento assinado digitalmente conforme MP nº 0, de 1º/01/1900,",
    "http://www.in.gov.br/autenticidade.html, pelo código 05151900010900003",
    "Sumário",
    "Atos do Poder Legislativo",
    "R E P U B L I C A Ç Ã O",
    "LEI COMPLEMENTAR Nº 999, DE 2 DE JANEIRO DE 1900 (*)",
    "Ementa fictícia da lei.",
    '"ANEXO II',
    "Tabela fictícia",
    '"',
    "(*) Republicação do Anexo II a Lei Complementar nº 999, de 2 de janeiro de 1900, por",
    "ter sido constatada inexatidão material, quanto ao original, na edição de 2/1/1900.",
    "LEI Nº 1, DE 8 DE JANEIRO DE 1900",
    "Art. 1º Outra lei fictícia.",
]
TITULO_FICT = "Lei Complementar nº 999, de 2 de janeiro de 1900"


@cenario("DOU em PDF: republicação lida da página")
def dou_republicacao():
    """Quebra: tomar por republicação desta norma a de outro ato da mesma página,
    contar o 'Art. 1º' do ato seguinte como artigo republicado, ou aceitar página
    cujo código de autenticidade não bate com a data do cabeçalho."""
    import dou_pdf as D

    r = D.ler_republicacao(LINHAS_REPUB, TITULO_FICT)
    checar(r == {
        "data": "1900-01-09", "edicao": "7", "pagina": 3,
        "codigo_autenticidade": "05151900010900003",
        "trecho": "Ano I Nº 7 Brasília - DF, terça-feira, 9 de janeiro de 1900",
        "nota": "(*) Republicação do Anexo II a Lei Complementar nº 999, de 2 de janeiro de "
                "1900, por ter sido constatada inexatidão material, quanto ao original, na "
                "edição de 2/1/1900.",
        "artigos": [], "anexos": ["II"],
    }, f"data, página, nota literal e o que foi republicado (obteve {r})")
    com_artigo = LINHAS_REPUB[:12] + ["Art. 5º Texto republicado."] + LINHAS_REPUB[12:]
    checar(D.ler_republicacao(com_artigo, TITULO_FICT)["artigos"] == ["5"],
           "artigo dentro do bloco republicado é contado")
    checar(D.ler_republicacao(LINHAS_REPUB, "Lei Complementar nº 998, de 2 de janeiro de 1900")
           is None, "republicação de outra norma: nada")
    sem_marca = [linha for linha in LINHAS_REPUB if not linha.startswith("R E P")]
    checar(D.ler_republicacao(sem_marca, TITULO_FICT) is None,
           "título sem 'REPUBLICAÇÃO' antes: não é republicação")
    trocado = [linha.replace("05151900010900003", "05151900011000003") for linha in LINHAS_REPUB]
    try:
        D.ler_republicacao(trocado, TITULO_FICT)
        recusou = False
    except ValueError:
        recusou = True
    checar(recusou, "código de autenticidade com outra data: erro, não palpite")


@cenario("DOU em PDF: republicação real da LC 214 (pulado se ausente)")
def dou_republicacao_real():
    """Contrato com o PDF arquivado, lido à mão: página 1 do DOU de 23/01/2025
    (código 05152025012300001), nota '(*) Republicação do Anexo XXIII a Lei
    Complementar nº 214, de 16 de janeiro de 2025, por ter sido constada
    inexatidão material...', e nenhum artigo no bloco republicado."""
    arquivo = RAIZ / "fontes" / "lc-214-2025" / "texto_republicado.pdf"
    if not arquivo.exists():
        print("  pulado: fontes/lc-214-2025/texto_republicado.pdf ausente")
        return
    import dou_pdf as D

    r = D.ler_republicacao(D.linhas_do_pdf(arquivo.read_bytes()),
                           "Lei Complementar nº 214, de 16 de janeiro de 2025")
    checar(r is not None and r["data"] == "2025-01-23" and r["pagina"] == 1
           and r["codigo_autenticidade"] == "05152025012300001",
           f"DOU de 23/01/2025, página 1 (obteve {r and {k: r[k] for k in ('data', 'pagina')}})")
    checar(r and r["artigos"] == [] and r["anexos"] == ["XXIII"],
           f"só o Anexo XXIII, nenhum artigo (obteve {r and (r['artigos'], r['anexos'])})")
    checar(r and r["nota"].startswith("(*) Republicação do Anexo XXIII a Lei Complementar nº "
                                      "214, de 16 de janeiro de 2025, por ter sido constada"),
           "nota literal")


@cenario("DOU: republicação confirmada não fica como 'não confirmada'")
def dou_republicacao_confirmada():
    """Quebra: continuar chamando de 'não confirmada' a data que a página arquivada
    confirma como republicação; trocar a publicação pela republicação; ou deixar a
    regra decidir datas que dependem da publicação quando a republicação traz artigo."""
    dou = F.publicacao_dou((FIXTURES / "dou-materia.html").read_bytes())
    refs = {"publicacao_dou": {"valores": ["1900-01-02", "1900-01-09"],
                               "trechos": ["... DOU de 2.1.1900 e republicado no DOU de 9.1.1900"]},
            "rodapes_adicionais": []}
    rep = {"data": "1900-01-09", "edicao": "7", "pagina": 3,
           "codigo_autenticidade": "05151900010900003", "trecho": "Ano I Nº 7 ...",
           "nota": "(*) Republicação do Anexo II ...", "artigos": [], "anexos": ["II"]}
    pub = F.publicacao_de(refs, dou, [rep])
    checar(pub["datas"] == ["1900-01-02"] and pub["republicacoes"] == [rep],
           "a publicação continua a original; a republicação fica registrada à parte")
    meta = {"urn": urn_dispositivo(URN_EC, "1"), "publicacao": pub,
            "extracao": "automatica", "revisao_temporal_pendente": True}
    erros, avisos = _rt().problemas_no_dispositivo(meta)
    checar(not erros and not any("1900-01-09" in a for a in avisos),
           f"data do rodapé confirmada como republicação: sem aviso (avisos: {avisos})")

    pv = _pv()
    aprov = {"aprovada": True, "aprovada_por": "F", "aprovada_em": "1900-01-01"}

    def ids(publicacao, regras):
        return {p["id"] for p in pv._pendencias_gerais(refs, publicacao, [], regras)}

    checar(ids(pub, {}) == {"republicacao_sem_artigo"},
           "republicação só de anexo, regra não aprovada: pendência própria, que bloqueia o "
           "que depende da publicação")
    checar(ids(pub, {"republicacao-sem-artigo": aprov}) == set(),
           "regra aprovada: a publicação dos artigos é a original, sem pendência")
    com_artigo = F.publicacao_de(refs, dou, [{**rep, "artigos": ["5"]}])
    checar(ids(com_artigo, {"republicacao-sem-artigo": aprov}) == {"republicacao_de_artigos"},
           "republicação que traz artigo: a regra não se aplica")


@cenario("rodapé que cita retificação: pendência, não silêncio")
def rodape_retificacao():
    """Rodapé medido na LC 227: 'Este texto não substitui o publicado no DOU de
    14.1.2026, republicado no DOU de 15.1.2026 e retificado em 23.1.2026.' A data
    da retificação não vem como 'DOU de'. Quebra: ignorá-la — uma retificação pode
    mudar o texto e as datas, e a regra decidiria sobre um texto não confirmado."""
    trecho = ("Este texto não substitui o publicado no DOU de 2.1.1900, republicado no DOU "
              "de 3.1.1900 e retificado em 9.1.1900.")
    refs = {"publicacao_dou": {"valores": ["1900-01-02", "1900-01-03"], "trechos": [trecho]},
            "rodapes_adicionais": []}
    dou = F.publicacao_dou((FIXTURES / "dou-materia.html").read_bytes())
    pub = F.publicacao_de(refs, dou)
    ids = {p["id"] for p in _pv()._pendencias_gerais(refs, pub, [], {})}
    checar("retificacao_citada_no_rodape" in ids,
           f"retificação citada no rodapé vira pendência geral (obteve {sorted(ids)})")
    meta = {"urn": urn_dispositivo(URN_EC, "1"), "publicacao": pub,
            "extracao": "automatica", "revisao_temporal_pendente": True}
    _, avisos = _rt().problemas_no_dispositivo(meta)
    checar(any("retifica" in a for a in avisos), f"e aviso na validação (avisos: {avisos})")
    sem = {**refs, "publicacao_dou": {"valores": ["1900-01-02"],
                                      "trechos": ["... publicado no DOU de 2.1.1900"]}}
    checar("retificacao_citada_no_rodape" not in
           {p["id"] for p in _pv()._pendencias_gerais(sem, F.publicacao_de(sem, dou), [], {})},
           "rodapé sem retificação: nada")


@cenario("normas/ reais: data do ato e publicação (pulado se ausentes)")
def normas_reais_publicacao():
    """Contrato com a base gravada. Valores lidos à mão nos cabeçalhos das páginas
    do DOU arquivadas — EC: 'Publicado em: 21/12/2023 | Edição: 242 | Seção: 1 |
    Página: 1'; LC: 'Publicado em: 16/01/2025 | Edição: 11-B | Seção: 1 - Extra B |
    Página: 1' — e no rodapé do compilado da LC ('publicado no DOU de 16.1.2025 -
    Edição extra e republicado no DOU de 23.1.2025')."""
    from comum import ler_frontmatter

    casos = {
        "emc-132-2023": ("2023-12-20", ["2023-12-21"], "dou"),
        "lc-214-2025": ("2025-01-16", ["2025-01-16"], "dou"),
    }
    for slug, (ato, datas, fonte) in casos.items():
        arq = RAIZ / "normas" / slug / "art-0001.md"
        if not arq.exists():
            print(f"  pulado: {slug} (normas/ ausente)")
            continue
        meta, _ = ler_frontmatter(arq)
        checar(meta.get("data_ato") == ato, f"{slug}: data_ato {ato} (obteve {meta.get('data_ato')})")
        pub = meta.get("publicacao")
        checar(isinstance(pub, dict) and pub.get("datas") == datas and pub.get("fonte") == fonte,
               f"{slug}: publicação {datas}, fonte {fonte} (obteve {pub})")
    arq = RAIZ / "normas" / "lc-214-2025" / "art-0001.md"
    if arq.exists():
        pub = ler_frontmatter(arq)[0].get("publicacao") or {}
        checar((pub.get("dou") or {}).get("edicao") == "11-B"
               and (pub.get("rodape_compilado") or {}).get("datas") == ["2025-01-16", "2025-01-23"],
               "lc-214-2025: edição 11-B do DOU, e o rodapé (com 23/01) registrado à parte")


@cenario("baixar: o tipo do documento decide a entrada do catálogo")
def baixar_escolhe_por_tipo():
    """Quebra: `--de-arquivo` usava sempre a PRIMEIRA URL da norma. Um PDF do DOU
    seria registrado como texto compilado, com a URL do Planalto como origem, e
    com --aceitar-deriva substituiria o HTML de que saem as normas."""
    import baixar

    compilado = {"tipo": "texto_compilado", "url": "https://planalto.invalido/lcp999.htm"}
    publicado = {"tipo": "texto_publicado", "url": "https://dou.invalido/lcp-999"}
    duas = {"id": "lcp-999", "urls": [compilado, publicado]}
    checar(baixar.entrada_por_tipo(duas, "texto_publicado") is publicado,
           "--tipo texto_publicado escolhe a URL do DOU")
    checar(baixar.entrada_por_tipo({"id": "x", "urls": [compilado]}, None) is compilado,
           "norma com uma só URL dispensa --tipo")
    for tipo, descricao in ((None, "sem --tipo, numa norma com duas URLs"),
                            ("texto_inexistente", "com tipo que a norma não tem")):
        try:
            baixar.entrada_por_tipo(duas, tipo)
            checar(False, f"{descricao}: recusa")
        except ValueError as exc:
            checar("texto_compilado" in str(exc) and "texto_publicado" in str(exc),
                   f"{descricao}: recusa, listando os tipos disponíveis")
    checar(baixar.entradas_para_baixar(duas, "texto_publicado") == [publicado],
           "download com --tipo busca só aquela URL")
    checar(baixar.entradas_para_baixar(duas, None) == [compilado, publicado],
           "download sem --tipo busca todas, como antes")


@cenario("catálogo: a LC 214 tem a URL do DOU como texto publicado")
def catalogo_lc214_dou():
    import yaml

    from fatiar import CATALOGO

    fontes = yaml.safe_load(CATALOGO.read_text(encoding="utf-8"))["fontes"]
    lc = next(f for f in fontes if f["id"] == "lcp-214-2025")
    urls = {u["tipo"]: u["url"] for u in lc["urls"]}
    # URL informada pelo usuário em 2026-10-14, do portal oficial da Imprensa Nacional
    checar(urls.get("texto_publicado") ==
           "https://www.in.gov.br/en/web/dou/-/lei-complementar-n-214-de-16-de-janeiro-de-2025-607430757",
           "entrada texto_publicado com a URL do in.gov.br")
    checar(urls.get("texto_compilado") == "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm",
           "e o texto compilado continua o mesmo")

    ec = next(f for f in fontes if f["id"] == "emc-132-2023")
    urls = {u["tipo"]: u["url"] for u in ec["urls"]}
    # URL informada pelo usuário em 2026-10-14, do portal oficial da Imprensa Nacional
    checar(urls.get("texto_publicado") ==
           "https://www.in.gov.br/web/dou/-/emenda-constitucional-n-132-532314756",
           "EC 132: entrada texto_publicado com a URL do in.gov.br")
    checar(urls.get("texto_compilado") ==
           "https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm",
           "EC 132: o texto compilado continua o mesmo")


# ---------------------------------------------------------------------------
# Índices e portabilidade
# ---------------------------------------------------------------------------

def _snapshot_indices() -> dict[str, str]:
    return {
        p.name: p.read_text(encoding="utf-8")
        for p in sorted((RAIZ / "indices").glob("*.json"))
    }


@cenario("índices determinísticos")
def indices():
    """Os índices são derivados: gerar duas vezes tem de dar o mesmo byte. A CI
    verifica isso com `git diff --quiet -- indices/`. Qualquer valor que varie
    entre execuções — data, hora, ordem de dicionário — quebraria a CI sem que
    nada de real tivesse mudado."""
    import datetime as dt

    import indexar

    indexar.main()
    primeira = _snapshot_indices()
    indexar.main()
    checar(primeira == _snapshot_indices(), "gerar duas vezes produz bytes idênticos")

    # Regressão: str(None) gravava a string "None" onde o campo é nulo.
    import json

    temporal = json.loads((RAIZ / "indices" / "temporal.json").read_text(encoding="utf-8"))
    checar(all(v != "None" for d in temporal.values() for v in d.values()),
           "temporal.json grava null, não a string 'None'")

    # Regressão: `cobertura.json` carimbava a data de geração, o que fazia a CI
    # acusar diff em todo dia posterior ao commit.
    cobertura = (RAIZ / "indices" / "cobertura.json").read_text(encoding="utf-8")
    checar(dt.date.today().isoformat() not in cobertura,
           "nenhum índice embute a data da geração")


@cenario("arquivos gerados têm fim de linha LF em qualquer plataforma")
def fim_de_linha_lf():
    """Quebra: voltar a `Path.write_text`. No Windows ele grava CRLF, e a base
    commitada daqui passaria a diferir byte a byte da gerada no Linux/CI: o
    `git diff --quiet -- indices/` do verificar.sh falharia, e cada reingestão em
    outra plataforma reescreveria todos os arquivos de normas/."""
    import json
    import tempfile

    import comum
    from comum import escrever_frontmatter

    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "art-0001.md"
        escrever_frontmatter(md, {"urn": "u", "n": 1}, "linha 1\n\nlinha 2")
        checar(b"\r" not in md.read_bytes(), "dispositivo em normas/ sem CR")

        js = Path(tmp) / "indice.json"
        comum.gravar_texto(js, json.dumps({"a": [1, 2]}, indent=2) + "\n")
        checar(b"\r" not in js.read_bytes(), "gravar_texto (índices, manifest, eventos) sem CR")
        checar(js.read_bytes().endswith(b"]\n}\n"), "e preserva o fim de linha final")


@cenario("manifest portável: caminho registrado no Windows resolve em qualquer plataforma")
def manifest_portavel():
    """Quebra: ler `registro["arquivo"]` cru. O manifest gerado no Windows traz
    'fontes\\\\emc-132-2023\\\\texto_compilado.html'; no Linux isso é UM nome de
    arquivo inexistente, e validar.py acusaria 'arquivo arquivado ausente' na CI."""
    import comum

    checar(
        comum.arquivo_posix("fontes\\emc-132-2023\\texto_compilado.html")
        == "fontes/emc-132-2023/texto_compilado.html",
        "barras invertidas do Windows viram '/'",
    )
    checar(
        comum.arquivo_posix("fontes/lc-214-2025/texto_compilado.html")
        == "fontes/lc-214-2025/texto_compilado.html",
        "caminho que já está em '/' não muda",
    )


@cenario("portabilidade de saída")
def portabilidade():
    """Regressão: no Windows a saída redirecionada usa a codepage local (cp1252) e
    imprimir '§', '—' ou '→' levantava UnicodeEncodeError — e o texto legal é cheio
    desses caracteres. Pior: eles aparecem sobretudo nas MENSAGENS DE ERRO, então a
    falha só surgia quando algo já tinha dado errado."""
    import os
    import subprocess

    ambiente = dict(os.environ, PYTHONIOENCODING="cp1252")
    codigo = (
        "import sys; sys.path.insert(0, 'pipeline'); import comum; "
        "print('art. 12, § 1º — remete a → art. 57')"
    )
    resultado = subprocess.run(
        [sys.executable, "-c", codigo], cwd=RAIZ, env=ambiente, capture_output=True
    )
    checar(resultado.returncode == 0, "imprime §, — e → sob codepage legada (cp1252 do Windows)")


# ---------------------------------------------------------------------------

def main() -> int:
    for titulo, fn in CENARIOS:
        print(f"\n{titulo}")
        try:
            fn()
        except Exception as exc:  # um cenário quebrado é FALHA dele, não do conjunto
            ultima = traceback.extract_tb(exc.__traceback__)[-1]
            msg = f"{titulo}: {type(exc).__name__}: {exc} ({Path(ultima.filename).name}:{ultima.lineno})"
            print(f"  FALHA {msg}")
            falhas.append(msg)

    print()
    if falhas:
        print(f"{len(falhas)} FALHA(S)")
        return 1
    print("todos os testes passaram")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
