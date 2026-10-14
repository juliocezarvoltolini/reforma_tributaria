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
    checar(stats["linhas_apos_o_fim"] == 3,
           f"3 linhas depois do fim reportadas, não anexadas (obteve {stats['linhas_apos_o_fim']})")


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
    """Quebra: interpretar 'arts. 3º a 5º' como 3 e 5, ou deixar 'demais
    dispositivos' cair no inciso III quando um inciso anterior tem alcance
    desconhecido. O artigo 3º seria datado errado, com aparência de certo."""
    clausula = [
        "Art. 9º Esta Lei fictícia entra em vigor:",
        "I - a partir de 1º de janeiro de 2030, em relação aos arts. 3º a 5º;",
        "II - em 2035, em relação ao art. 7º, exceto o § 1º; e",
        "III - na data de sua publicação, em relação aos demais dispositivos.",
    ]
    r = _pv().interpretar_clausula(clausula, URN_BASE, "9", EXISTENTES_FICT)
    checar([i["interpretado"] for i in r["incisos"]] == [False, False, True],
           "intervalo, data completa e 'exceto' não são interpretados")
    checar(all(m["inciso"] is None for m in r["mapa"].values()),
           "e então 'demais dispositivos' não pode ser resolvido para artigo nenhum")
    checar(all(m["motivo"] for m in r["mapa"].values()),
           "cada artigo indeterminado diz por quê")

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
        "II - em 2035, em relação aos arts. 6º a 7º.",
    ]
    r = _pv().interpretar_clausula(parcial, URN_BASE, "9", EXISTENTES_FICT)
    checar(r["mapa"]["3"]["inciso"] == "I" and r["mapa"]["3"]["ressalva"],
           "nomeado por inciso interpretado segue atribuído, mas com ressalva: o inciso "
           "não interpretado pode nomeá-lo também")


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
