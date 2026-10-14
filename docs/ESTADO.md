# Estado do projeto

Documento de trabalho. Registra o que está pronto, o que está aberto e o que já
foi tentado sem sucesso. Atualize ao fechar cada frente.

**Última atualização:** 2026-10-14

---

## 1. Como usar este documento

Leia nesta ordem antes de mexer no pipeline:

1. [`PREMISSAS.md`](../PREMISSAS.md) — regras vinculantes de confiabilidade
2. [`CLAUDE.md`](../CLAUDE.md) — protocolo de consulta
3. este arquivo — onde o trabalho parou e por quê

A seção [§6 Armadilhas já pagas](#6-armadilhas-já-pagas) é a mais importante
para quem chega agora: cada item custou uma rodada de ingestão real.

---

## 2. Estado do repositório

| Item | Situação |
|---|---|
| `main` | `6aa41f5` — PRs #1 a #3 mergeados |
| Branch de trabalho | `claude/using-superpowers-wn348h` |
| PR aberto | #4 |

Continue nessa branch — o push atualiza o PR #4. Não abra PR novo. O histórico
do PR #4 tem, em ordem: portabilidade Windows e acesso aos portais; perda de
dados em norma que altera outra; remissão resolvida para o dispositivo errado;
janela de escopo; e, desta frente, a correção do fatiamento sobre o HTML real
(código e testes) seguida da reingestão (dados).

### Pendências administrativas

- `main` ainda **não** é a branch padrão do repositório no GitHub; a padrão é a
  branch de trabalho, resquício do primeiro push num repositório vazio.
- O GitHub Actions nunca executou: todas as execuções falharam em segundos, sem
  runner atribuído, com logs em 404. O repositório é **público**, onde Actions é
  gratuito e ilimitado, então não é cota nem plano. Verificar em
  Settings → Actions → General. Enquanto isso, o hook de pre-commit cobre a
  verificação (`git config core.hooksPath .githooks`).
- **Deriva do HTML do Planalto, não revisada.** O `baixar.py` detectou que o
  portal serviu, num segundo download, um HTML diferente do arquivado (EC 132:
  arquivado `f8d721…`, visto depois `cb2740…`; a LC 214 também). Os eventos
  estão em `eventos/` **no checkout principal, ainda não commitados**. Tudo
  neste documento foi medido sobre o arquivo registrado no manifest. Se o texto
  novo for homologado (`--aceitar-deriva`), refaça `fatiar.py --todas
  --relatorio` e compare com os números do §5: a marcação pode ter mudado.

---

## 3. O que funciona

- **Download das fontes oficiais**, com `sha256` registrado em
  `fontes/manifest.json`, e `--de-arquivo` como reserva.
- **Detecção de deriva** de texto oficial, que gera evento em `/eventos/` em vez
  de sobrescrever.
- **Fatiamento sobre o HTML real** (§4): artigos próprios x texto de outra
  norma, texto riscado, fim da norma.
- **Verificação mecânica das premissas**, pelo hook e pela CI, a partir do mesmo
  `pipeline/verificar.sh`.
- **Determinismo dos índices e dos arquivos gerados** entre plataformas: LF em
  qualquer sistema, caminhos do manifest com `/`.
- **Testes com marcação real**: `tests/fixtures/planalto-ec.html` e
  `planalto-lc.html` reproduzem a marcação do portal (listada no cabeçalho de
  cada um) com texto inventado, e `test_pipeline.py` roda ainda contra os HTML
  arquivados em `fontes/` quando presentes, verificando propriedades (numeração
  consecutiva, ordem estrita, aspas balanceadas), nunca contagens.

---

## 4. Classificação própria x citada — fechada

Normas que alteram outras reproduzem o texto alterado no próprio corpo. Esse
texto pertence ao artigo que promove a alteração; não é artigo da norma
ingerida.

### Causa-raiz: não era um dos dois sinais, eram três defeitos

A hipótese anterior ("aspas ou ordem não corresponde ao que o portal publica")
estava certa só em parte. Lido o HTML real:

1. **O código-fonte do HTML quebra linha no meio do parágrafo**, e o extrator
   tratava essa quebra como quebra de parágrafo. Uma remissão como `art. 195, I`
   que caía no início de uma linha do código era lida como início de artigo.
   Era a origem dos "artigos" `158`, `159`, `195` (EC) e `156-A`, `473`, `486`
   (LC). Isto, e não a classificação, explicava `art156-A` próprio.
2. **O sinal de aspas estava errado nos detalhes**, todos medidos:
   - a EC usa aspas **retas** (`&quot;`), a LC usa aspas **curvas**;
   - o fechamento é `" (NR)` — a aspa **não** está no fim da linha;
   - há aspas internas (`"a"`, `"b"`) e uma delas termina linha (`…, IV, "b".`),
     o que parecia fechar o bloco inteiro;
   - um bloco que insere vários artigos tem **um** par de aspas: o `Art. 156-B`
     seguinte não tem aspa de abertura.

   O sinal certo é o **balanço** de aspas desde o início do documento (curvas por
   profundidade, retas por paridade).
3. **A ordem estritamente crescente, usada como critério, transformava um erro
   isolado em cascata**: um único falso positivo alto fixava o piso lá em cima e
   todo o resto virava "citado", em silêncio. Por isso a EC dava 5 artigos
   próprios e a LC 6, não os 63 e 752 da primeira ingestão. Agora a ordem é
   **validação**: o que a violar aborta a escrita.

Corroboração independente: o portal também envolve o texto citado em
`<blockquote>`. Aspas e `<blockquote>` concordam em todos os cabeçalhos de
artigo da EC, e em todos menos um no documento inteiro da LC (um `Art. 26`
citado, no trecho dos anexos, que o portal não envolveu). O fatiador reporta a
discordância em vez de escolher em silêncio.

### Resultado, medido (`fatiar.py --todas --relatorio`)

| | EC 132 | LC 214 |
|---|---|---|
| artigos próprios | 23 (1..23, sem lacunas) | 580 (1..544 sem lacunas + 36 com sufixo) |
| artigos de outras normas (texto citado) | 59 | 87 |
| remissões internas resolvidas | 8 (0 órfãs) | 775 (10 órfãs, 1%) |
| linhas com texto riscado no corpo | 0 | 265 |
| redações anteriores fundidas ao dispositivo | 0 | 21 |
| aspas | balanceadas | balanceadas; 1 `”` sem abertura **na fonte** |
| fora de `/normas/` (assinatura, anexos) | 33 linhas | 5.352 linhas (29 linhas `ANEXO`) |

Antes: 100% das remissões da LC eram órfãs (73/73).

---

## 5. O que o HTML real mostra

Medido nos arquivos de `fontes/`; é a evidência que faltou nas tentativas
anteriores.

- **Charset.** A EC declara `windows-1252`. A LC **não declara nenhum**: o
  padrão `utf-8` falha no decode estrito e o pipeline cai para `cp1252`. Não
  confie no cabeçalho.
- **Texto superado.** O portal mantém no compilado a redação anterior e a
  marca de **duas** formas, no mesmo documento (LC 214): `<span
  style="…text-decoration:line-through">` e `<strike>`. A redação nova vem logo
  depois, com o mesmo número e `(Redação dada pela …)`. Dispositivo revogado:
  texto riscado + `(Revogado pela …)` sem riscar, no mesmo parágrafo. Há ainda
  riscado no meio de parágrafo vivo e rótulo duplicado ("Produção de efeitos").
  A EC não tem texto riscado.
- **A maior parte do texto riscado está nos anexos** da LC (1.685 das 1.950
  linhas riscadas do documento), não nos artigos.
- **Fim da norma.** Nos dois documentos o texto do último artigo termina numa
  linha `Brasília, …` (local e data), seguida de signatários, do rodapé "Este
  texto não substitui o publicado no DOU" e, na LC, dos anexos.
- **Fonte com erros**, ambos na LC: um `”` sem abertura no `Parágrafo único` do
  `Art. 471-C` (`normas/lc-214-2025/art-0471-c.md`), e `’` no lugar de `”`
  num fechamento dentro do texto citado do `Art. 517`
  (`normas/lc-214-2025/art-0517.md`). São reportados, não corrigidos.

---

## 6. Armadilhas já pagas

Cada linha custou uma rodada. A coluna da direita é a lição.

| # | Defeito | Lição |
|---|---|---|
| 1 | `Art. 4º-A` lido como artigo `4` | O marcador ordinal vem **antes** do sufixo alfabético |
| 2 | `python3` inexistente no Windows | O atalho da Microsoft Store está no PATH e não executa nada: teste o candidato, não a presença |
| 3 | `UnicodeEncodeError` sob cp1252 | `§`, `—` e `→` aparecem sobretudo nas **mensagens de erro**: a falha só surgia quando algo já tinha dado errado |
| 4 | Portal derrubava a conexão | `ConnectionReset` idêntico em todas as URLs é filtro anti-bot, não erro de rede |
| 5 | 214 artigos perdidos por sobrescrita | Colisão de numeração tem de **abortar** a escrita, nunca avisar e sobrescrever |
| 6 | Remissão resolvida no namespace errado | Ponteiro errado é pior que ausente: o ausente falha seguro, o errado leva a IA ao dispositivo equivocado |
| 7 | Quebra de linha do código-fonte tratada como quebra de parágrafo | `art. 195, I` no início de uma linha virava artigo. **Só tags de bloco quebram linha** |
| 8 | Aspas lidas por "linha começa/termina com aspa" | Aspas retas x curvas, `" (NR)`, aspa interna, bloco de vários artigos: **conte o balanço**, não olhe a linha |
| 9 | Ordem crescente como critério de classificação | Um falso positivo alto virava cascata silenciosa. Critério frágil serve para **validar**, não para decidir |
| 10 | Texto riscado ignorado | Redação antiga e nova viravam dois artigos de mesmo número (colisão) e o corpo misturava as duas. Formatação **é** informação |
| 11 | Auto-remissão filtrada por `startswith` | `…!art1` casa com `…!art158`: o art. 1 perdia toda remissão aos arts. 10–19, 100–199… Compare identificador, não prefixo de texto |
| 12 | Padrão "interno salvo qualificador externo" numa emenda | 8 de 20 remissões da EC eram órfãs: `art. N` sem qualificador é, numa emenda, da Constituição |
| 13 | Último artigo engolia tudo que vem depois | O `Art. 544` da LC virou 97 KB (assinatura e anexos) e herdou as remissões das tabelas |
| 14 | `Path.write_text` grava CRLF no Windows | A base commitada daqui diferiria byte a byte da gerada no Linux/CI. Escrita com `newline="\n"` |
| 15 | `arquivo` do manifest com `\` | No Linux é um único nome de arquivo inexistente. Leitores normalizam, o escritor grava `/` |
| 16 | `verificar.sh` reprovava todo commit que muda os índices | A condição `git diff --cached` exigia o staged igual ao HEAD; a correção sugerida nunca passaria |
| 17 | Todos os rodapés "publicado no DOU" tomados como publicação da norma | A LC 214 traz, depois dos anexos, outro ato com assinatura e rodapé próprios (2.7.2025). A publicação é a do **primeiro** rodapé; os demais são outro ato |
| 18 | `--de-arquivo` registrava o arquivo como a primeira URL da norma | Um PDF do DOU viraria "texto compilado" com a URL do Planalto. O documento é escolhido por `--tipo`; sem ele, norma com mais de um documento é recusada |
| 19 | PDF "do DOU" que não era do DOU | Os metadados mostravam Word de terceiro com o cabeçalho da página copiado. Leia os metadados antes de aceitar um arquivo como fonte |

### O fixture de teste não é referência de formato

O fixture anterior era **sintético também na marcação**: codificava a marcação
que se supunha, e um teste afirmava como correta a heurística de ordem que
causava a cascata. Passou verde nas rodadas em que a ingestão real falhou. Os
novos reproduzem a marcação real e listam, no cabeçalho, cada construção e onde
foi observada. **Ao tocar o parser, leia o HTML real antes** e acrescente ao
fixture a construção que faltou.

---

## 7. Como diagnosticar

Windows: o comando é `python`, não `python3`.

```bash
git config core.hooksPath .githooks     # uma vez por clone
python pipeline/fatiar.py --todas --relatorio
```

`--relatorio` não escreve nada. O que ler na saída:

| Linha | O que revela |
|---|---|
| faixa de artigos próprios e lacunas | se a numeração é consecutiva (sinal de classificação certa) |
| artigos com sufixo alfabético | texto citado que escapou, ou acréscimo legítimo — confira a anotação |
| linhas com texto riscado / redações fundidas | o quanto da norma tem redação anterior |
| aspas: fechamento sem abertura, abertura dentro de bloco, saldo final | erros da fonte ou desincronia do balanço |
| aspas x `<blockquote>` | discordância entre os dois sinais independentes |
| depois do fim do texto | o que **não** foi incorporado (assinatura, anexos) |
| remissões órfãs | se a extração está sã (muito abaixo de 25%) |

Depois de corrigir:

```bash
python pipeline/fatiar.py --todas
python pipeline/indexar.py
pipeline/verificar.sh
```

O `fatiar.py` apaga o resultado da ingestão anterior antes de escrever. É
deliberado: sem isso, um fatiamento corrigido convive com os arquivos espúrios
do antigo.

---

## 8. Regras que não podem ser quebradas

- Nunca escrever texto normativo à mão. Camada 1 entra só pelo pipeline, de
  fonte baixada e com `sha256`.
- Nunca editar `/normas/` para "corrigir" texto, nem `/indices/` (derivados;
  regenerar com `indexar.py`).
- Nunca resolver remissão no namespace da norma ingerida quando o escopo não for
  internamente afirmado.
- Colisão de numeração própria **aborta** a escrita. Não relaxar para "fazer
  funcionar". Artigo fora de ordem também aborta.
- Todo dispositivo sai com `revisao_temporal_pendente: true`. O parser não
  infere vigência nem eficácia.

---

## 9. Decisões em aberto (para um humano)

Estas foram tomadas, ou deixadas como estavam, sem que o usuário as tenha
escolhido. Estão aqui para serem revistas.

1. **Texto riscado no corpo, entre `~~ ~~`, e fora dos metadados.** Alternativas:
   descartá-lo do corpo (perde a redação anterior e deixa a anotação
   `(Revogado …)` sem referente, o que faria o artigo inteiro parecer
   revogado) ou guardá-lo em front-matter. A redação anterior é o que responde
   a fato gerador anterior à mudança, então o tratamento definitivo faz parte
   da revisão temporal. Convenção documentada em `normas/README.md`.
2. **Política de escopo das remissões em leis.** A regra do repositório é não
   resolver quando o escopo não é afirmado internamente. Em **emenda** isso foi
   aplicado à risca (`exige_escopo_interno`). Em **lei** o padrão continua
   "interno salvo qualificador externo": 55% das menções na LC 214 não têm
   qualificador algum (1.786 ocorrências, contadas por padrão de remissão e
   portanto com sobreposição: 975 sem qualificador, 600 afirmadas internas, 211
   externas). A taxa de 1% de órfãs diz que o padrão acerta quase
   sempre, mas **não mede o ponteiro errado que por acaso existe** (ex.: `art. 16`
   de outra lei resolvido para o `art. 16` da LC). As 10 órfãs restantes se
   concentram nos arts. 26, 542 e 543, onde o qualificador ("os seguintes
   dispositivos da Lei nº …") vem **antes** de uma enumeração. Aplicar a regra
   literal à LC derrubaria a maioria das remissões; é decisão de precisão x
   cobertura.
3. **Anexos e assinatura ficam fora de `/normas/`.** Antes ficavam colados ao
   último artigo. Os anexos da LC são parte da lei e precisam de modelo próprio
   (URN, arquivo, validação). Lembrete: a maior parte do texto riscado está
   neles.
4. **`anotacoes_oficiais` é uma lista plana por artigo.** `(Revogado …)` de um §
   aparece na lista do artigo. Quem lê deve ir ao corpo, onde a anotação está
   colada ao trecho riscado. Ainda: 6 anotações `(Incluído pela …)` que seguem
   um cabeçalho de capítulo são atribuídas ao artigo **anterior**.

5. **Resolvidas em 2026-10-14, seguindo a recomendação aceita:** `data_ato`
   separado de `publicacao` (que pode ter várias datas e declara a `fonte`),
   `precisao: ano` para "em 2027", e `excecoes_subdivisao` para datas de § e
   inciso. Ver `docs/MODELO-DADOS.md`. O `temporal.json` deixou de gravar a
   string `"None"`.

---

## 10. Revisão da vigência — em andamento

A revisão tem duas partes: o que a **cláusula de vigência** diz de cada artigo
(mecânico) e o que o **próprio texto** do artigo diz sobre quando produz efeitos
(leitura humana). `pipeline/propor_vigencia.py` prepara as duas e não decide
nenhuma. Ver [`temporal/README.md`](../temporal/README.md).

```bash
python pipeline/propor_vigencia.py --slug emc-132-2023
```

- **O modelo e a aplicação estão prontos.** A revisão é preenchida no YAML da
  proposta e aplicada por `fatiar.py` (ver `temporal/README.md`), com três
  travas: deriva do `sha256` invalida a revisão; revisão inválida aborta antes de
  apagar arquivo; `validar.py` acusa decisão não aplicada. Verificado ponta a
  ponta numa cópia do repositório, com decisões de teste que não foram gravadas
  aqui.
- **EC 132: proposta aguardando revisão** em `temporal/propostas/emc-132-2023.yaml`.
  Dos 23 artigos, 19 caem no inciso III do `Art. 23` ("na data de sua
  publicação"), dois no I ("em 2027": arts. 3º e 11) e dois no II ("em 2033":
  arts. 4º e 5º). 16 têm marcos temporais próprios ou dependem de lei futura, e
  5 inserem texto na Constituição/ADCT, que não estão ingeridas. Nenhuma decisão
  foi preenchida: é trabalho humano.
- **Vigência não é eficácia.** Para todo artigo com marco próprio, ou que insere
  texto em outra norma, **não há proposta de efeitos**: o `Art. 22` revoga "em
  2027" e "em 2033" artigos da Constituição e do ADCT, o `Art. 7º` compensa "a
  partir de 2027", e os `Arts. 12` e `13` fixam valores por exercício.
- **Publicação da LC 214 confirmada no DOU.** A página do ato no portal da
  Imprensa Nacional está arquivada em `fontes/lc-214-2025/texto_publicado.html`
  (baixada por `baixar.py --tipo texto_publicado`): "Publicado em: 16/01/2025 |
  Edição: 11-B | Seção: 1 - Extra B | Página: 1". Os 580 dispositivos têm
  `publicacao.fonte: dou`. O rodapé do compilado cita também 23/01/2025
  ("republicado"), que esta página **não** confirma; uma busca indicou que a
  edição de 23/01/2025 republica só o Anexo XXIII, mas isso só vale depois de
  arquivar aquela edição. Fica como aviso.
- **Publicação da EC 132 confirmada no DOU**: "Publicado em: 21/12/2023 |
  Edição: 242 | Seção: 1 | Página: 1", arquivada em
  `fontes/emc-132-2023/texto_publicado.html`. Coincide com o rodapé do compilado.
  Os 603 dispositivos da base têm agora `publicacao.fonte: dou`.
- **A LC 214 traz outro ato no fim do compilado.** Depois dos anexos há um bloco
  citado, uma segunda assinatura ("Brasília, 1º de julho de 2025") e um rodapé
  próprio ("DOU de 2.7.2025"). Não é a publicação da LC; é outro ato, e os
  dispositivos que ele trouxe podem ter vigência própria. Identificar quais são
  é pré-requisito da revisão da LC.
- **LC 214: proposta ainda não.** A cláusula dela (`Art. 544`) tem forma diferente
  da EC: "entra em vigor na data de sua publicação, produzindo efeitos: I - ...",
  isto é, a vigência vem do caput e os incisos dão os EFEITOS. Usa ainda data
  completa, intervalos ("arts. 537 a 540"), subdivisões ("58, caput", "60, § 3º")
  e exceções ("exceto os §§ 1º e 5º"), e o próprio inciso III tem redação
  anterior riscada. Estender o gerador é o próximo passo.

---

## 11. Fora de escopo agora

- Revisão das cláusulas de vigência — trabalho humano, depois que o fatiamento
  estiver correto. É o que separa a base de ser útil ou perigosa, dada a
  transição escalonada por exercício.
- Busca vetorial. O filtro temporal é determinístico e vem antes da busca;
  embedding ignora tempo.
- Jurisprudência e legislação estadual ou municipal.
- Normas listadas em `pipeline/fontes.yaml` sob `pendentes:` — precisam de URL
  oficial confirmada antes de entrar.
