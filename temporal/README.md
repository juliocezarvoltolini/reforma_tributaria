# /temporal/ — camada 2

Cronograma da transição e parâmetros por exercício.

A transição é escalonada e há regimes coexistindo: a mesma pergunta tem
respostas diferentes conforme o ano. Todo dado aqui exige `fundamento` (URN do
dispositivo que o estabelece).

Não preencher por memória. Enquanto a norma não estiver ingerida, registre a
pendência em vez do valor.

## `propostas/` — revisão da vigência, antes de aplicar

`propostas/<slug>.yaml` é gerado por `pipeline/propor_vigencia.py`. Cada
dispositivo recebe a vigência que a **cláusula de vigência** da própria norma lhe
atribui (com a URN do inciso como `fundamento`), os marcos temporais **próprios**
do artigo em trecho literal (vigência não é eficácia) e campos `revisao` vazios.

- É uma **proposta**: nada em `normas/` é alterado por ela.
- O script só interpreta padrões exatos; o resto sai `nao_interpretado`, com o
  motivo. Se um inciso não é interpretado, "demais dispositivos" não é resolvido.
- Os trechos citados vêm de `normas/`, nunca digitados.
- O gerador **recusa sobrescrever** um arquivo que já tenha decisão **humana** em
  `revisao.decisao`. Decisão de regra (`revisado_por: regra:...`) não impede: ela
  é refeita por `revisar_por_regra.py`.
- `decisoes_necessarias` lista o que o modelo de dados ainda não responde, e
  `pendencias_gerais` o que vale para a norma inteira: publicação não confirmada
  no DOU, republicação citada no rodapé e não confirmada, republicação confirmada
  que não traz artigo (`republicacao_sem_artigo`, enquanto a regra
  `republicacao-sem-artigo` não for aprovada) ou que traz
  (`republicacao_de_artigos`), outro ato anexado ao compilado (com os artigos que
  ele traz, lidos no próprio bloco), regra derivada não aprovada (com o resultado
  que ela daria).
- Cada dispositivo traz `marcas_de_outro_ato`: as anotações oficiais do
  compilado (incluído, redação dada, revogado, vetado, promulgação de partes
  vetadas, vide) que mostram texto vindo de outro ato.

## Quem decide: regra, pessoa ou IA (PREMISSAS.md §3.4)

```
python pipeline/propor_vigencia.py --slug <slug>    # proposta
python pipeline/revisar_por_regra.py --slug <slug>  # decide o que é literal
python pipeline/fatiar.py --slug <slug>             # aplica a normas/
```

`revisar_por_regra.py` preenche `revisao` só onde não há o que decidir, eixo por
eixo, com `revisado_por: regra:clausula-literal/v1` (mais `+<regra derivada>`
quando usa uma). Não decide nada quando a publicação não está confirmada no DOU,
nem no artigo que:

- tem texto de outro ato (`redacao_de_outro_ato`) ou foi trazido por outro ato do
  compilado (`parte_de_outro_ato`): a cláusula desta norma não é a desse texto;
- diz no próprio texto quando algo entra em vigor ou produz efeitos
  (`clausula_temporal_propria`), ou é citado por um artigo que faz isso
  (`alcancado_por_clausula_temporal`).

Com a publicação em aberto (`rodape_cita_publicacao_nao_confirmada` ou
`republicacao_sem_artigo`), nada que dependa da data de publicação é decidido; a
data escrita no inciso, sim. Republicação que traz artigo
(`republicacao_de_artigos`) bloqueia a norma toda. Na forma
`vigencia_por_inciso` os efeitos nunca são decididos por regra. Pendência geral
que a regra não conhece bloqueia a norma toda.

As regras derivadas ficam em [`regras.yaml`](regras.yaml), cada uma com a leitura
que faz, um exemplo e a aprovação (`aprovada`, `aprovada_por`, `aprovada_em`).
Sem aprovação, a proposta mostra `resultado_se_aprovada` e não propõe data.
Revogada uma aprovação, o fatiamento recusa as decisões que dependiam dela até
`revisar_por_regra.py` ser rodado de novo.

Decisão humana prevalece e nunca é tocada pela regra. Registro feito por IA leva
`revisado_por: ia:<modelo>` e aparece na consulta como não equivalente a revisão
humana.

## Formas de cláusula reconhecidas

| Forma | Exemplo real | O que os incisos dão |
|---|---|---|
| `vigencia_por_inciso` | EC 132, art. 23: "entra em vigor: I - em 2027, em relação aos arts. 3º e 11" | a vigência; os efeitos só são propostos iguais a ela quando o artigo não tem marco próprio |
| `efeitos_por_inciso` | LC 214, art. 544: "entra em vigor na data de sua publicação, produzindo efeitos: I - ..." | os efeitos; a vigência de todos vem do caput |

O alcance de cada inciso é lido por inteiro — artigos, intervalos ("480 a 484"),
`caput`, `§ 3º`, `§§ 1º e 5º`, `exceto os §§ 1º e 5º`, "demais dispositivos" — e
qualquer sobra invalida a lista. Termo e alcance são independentes: um termo fora
do padrão deixa aqueles artigos sem data, mas não impede resolver "demais
dispositivos". O termo "a partir do primeiro dia do <ordinal> mês subsequente ao
da sua publicação" é lido, e só vira data pela regra derivada
`primeiro-dia-do-mes-subsequente`, depois de aprovada. Subdivisões com inciso
próprio viram `efeitos.excecoes`, que `aceitar` aplica junto. Artigo com sufixo
dentro de um intervalo (482-A em "480 a 484") fica indeterminado: se o intervalo
o abrange é interpretação. A diferença entre a redação riscada de um inciso e a
vigente é sinalizada (`alcance_alterado_pela_redacao_posterior`).

## Como revisar e aplicar

Em cada dispositivo sem decisão, preencha o bloco `revisao`. `escopo` diz quais
eixos a decisão cobre: `[vigencia]`, `[efeitos]` ou os dois (o padrão). O eixo
de fora continua provisório, e o dispositivo pendente (`eixos_revisados`).

| `decisao` | O que acontece | Exige |
|---|---|---|
| `aceitar` | adota as propostas dos eixos do `escopo` | proposta com data em cada eixo do escopo |
| `alterar` | grava as datas informadas | para os eixos do escopo, `vigencia_inicio`/`efeitos_inicio` e `fundamento_vigencia`/`fundamento_efeitos` (listas de URN) |
| `rejeitar` | nada; o dispositivo continua pendente | — |

Toda decisão exige `revisado_por` e `revisado_em` (AAAA-MM-DD). Em `alterar`
valem ainda `vigencia_fim`, `efeitos_fim`, `precisao` (`{campo: ano}`, com a data
em AAAA-01-01) e `excecoes_subdivisao` (URN de § ou inciso do **próprio** artigo,
as datas que diferem do artigo e `fundamento`).

```yaml
revisao:
  decisao: alterar
  vigencia_inicio: 2023-12-21
  efeitos_inicio: 2027-01-01
  precisao: {efeitos_inicio: ano}
  fundamento_vigencia: ["urn:lex:...;132!art23_incIII"]
  fundamento_efeitos: ["urn:lex:...;132!art7"]
  revisado_por: Nome
  revisado_em: 2026-10-20
```

Depois, `python pipeline/fatiar.py --slug <slug>` aplica a revisão a `normas/`,
e `python pipeline/indexar.py` atualiza os índices. Travas:

- Se o `sha256` do original mudou desde a proposta (`fonte_sha256`), **nada** é
  aplicado e o fatiamento aborta: a decisão foi tomada sobre outro texto.
- Revisão inválida (data fora do formato, falta de fundamento, `aceitar` sem
  proposta de efeitos, decisão de regra com regra derivada não aprovada) aborta o
  fatiamento antes de apagar qualquer arquivo.
- `validar.py` (e o hook de pre-commit) acusa decisão tomada e ainda não
  aplicada a `normas/`.
