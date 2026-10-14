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
- O gerador **recusa sobrescrever** um arquivo que já tenha `revisao.decisao`
  preenchida. Quem revisa edita o arquivo; regenerar exige apagá-lo de propósito.
- `decisoes_necessarias` lista o que o modelo de dados ainda não responde, e
  `pendencias_gerais` o que vale para a norma inteira (publicação não confirmada
  no DOU, outro ato anexado ao compilado).

## Como revisar e aplicar

Em cada dispositivo, preencha o bloco `revisao`:

| `decisao` | O que acontece | Exige |
|---|---|---|
| `aceitar` | adota a proposta de vigência **e** a de efeitos | que exista proposta de efeitos (artigo sem marco temporal próprio) |
| `alterar` | grava as datas informadas | `vigencia_inicio`, `efeitos_inicio`, `fundamento_vigencia`, `fundamento_efeitos` (listas de URN) |
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
  proposta de efeitos) aborta o fatiamento antes de apagar qualquer arquivo.
- `validar.py` (e o hook de pre-commit) acusa decisão tomada e ainda não
  aplicada a `normas/`.
