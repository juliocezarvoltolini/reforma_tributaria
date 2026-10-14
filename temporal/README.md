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
- `decisoes_necessarias` lista o que o modelo de dados ainda não responde e que o
  revisor precisa decidir antes de aplicar.
