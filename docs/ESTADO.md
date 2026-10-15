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
   colada ao trecho riscado. ~~As anotações `(Incluído pela …)` que seguem um
   cabeçalho de capítulo eram atribuídas ao artigo anterior~~ — corrigido em
   2026-10-15: o título do cabeçalho (a linha depois da etiqueta "CAPÍTULO II")
   caía no fim do corpo do artigo anterior em 194 artigos da LC 214 e 69 da LC
   227. Agora o título, e a anotação que vem entre etiqueta e título, vão para a
   `hierarquia` ("CAPÍTULO II — DA REVOGAÇÃO"). 323 linhas saíram do fim de corpos
   e estão todas na hierarquia; nenhum outro texto mudou.

5. **Resolvidas em 2026-10-14, seguindo a recomendação aceita:** `data_ato`
   separado de `publicacao` (que pode ter várias datas e declara a `fonte`),
   `precisao: ano` para "em 2027", e `excecoes_subdivisao` para datas de § e
   inciso. Ver `docs/MODELO-DADOS.md`. O `temporal.json` deixou de gravar a
   string `"None"`.

---

## 10. Revisão da vigência — em andamento

A revisão tem duas partes: o que a **cláusula de vigência** diz de cada artigo
(mecânico) e o que o **próprio texto** do artigo diz sobre quando produz efeitos
(leitura). `pipeline/propor_vigencia.py` prepara as duas e não decide nenhuma;
`pipeline/revisar_por_regra.py` decide o que é literal (PREMISSAS.md §3.4) e
deixa o resto pendente. Ver [`temporal/README.md`](../temporal/README.md).

```bash
python pipeline/propor_vigencia.py --slug emc-132-2023
python pipeline/revisar_por_regra.py --slug emc-132-2023
python pipeline/fatiar.py --slug emc-132-2023
```

**Estado em 2026-10-15 (decisões por regra aplicadas a `normas/`):**

| Norma | Vigência e efeitos por regra | Só vigência por regra | Sem decisão | Por quê |
|---|---|---|---|---|
| EC 132 | — | 19 (arts. 3º e 4º com precisão de ano) | 4 | art. 5º tem partes revogadas; arts. 10, 11 e 21 dizem no próprio texto quando algo entra em vigor ou produz efeitos |
| LC 214 | 419 (arts. 537 a 540 com efeitos em 1º/05/2025) | 10 | 151 | só vigência: alcance do inciso mudado pela LC 227. Sem decisão: 146 com texto de outro ato (LC 227/2026, LC 235/2026, vetos, ADI), 4 com cláusula própria (19, 165, 373, 374), o art. 26 (promulgação de partes vetadas) |

Nenhuma decisão humana foi tomada: as 448 são de regra. Os efeitos na EC 132
nunca são decididos por regra (a cláusula só dá a vigência).

**Regras derivadas aprovadas pelo usuário em 2026-10-15** (`temporal/regras.yaml`),
com a PREMISSAS.md §3.4:

- `ano-primeiro-dia` (confirmada): "em 2027" -> 2027-01-01, precisão de ano.
- `primeiro-dia-do-mes-subsequente`: LC 214, art. 544, I -> 1º/05/2025.
- `republicacao-sem-artigo`: a republicação de 23/01/2025, arquivada (PDF da
  página 1 do DOU, `fontes/lc-214-2025/texto_republicado.pdf`) e lida por
  `pipeline/dou_pdf.py`, traz só o Anexo XXIII ("(\*) Republicação do Anexo
  XXIII a Lei Complementar nº 214..."), nenhum artigo; a publicação dos artigos
  continua 16/01/2025.

**LC 227/2026 e LC 235/2026 ingeridas em 2026-10-15** (compilado do Planalto e
página do DOU de cada uma; números, datas e URLs informados pelo usuário):

| Norma | Artigos | Publicação no DOU | Decidido por regra | Pendente |
|---|---|---|---|---|
| LC 227 | 182 próprios, 159 citados | 14/01/2026, Ed. 9, Seção 1, p. 1 | nada | o rodapé cita republicação (15/01/2026) e retificação (23/01/2026) não arquivadas. O art. 182 já é lido: 181 artigos no inciso III (a partir da publicação), o art. 169 no I (1º/01/2027), a alínea c do inciso II do art. 76 no I, e os §§ 4º e 5º do art. 52 no II, sem data (termo de evento) |
| LC 235 | 17 próprios, 5 citados | 28/08/2026, Ed. 163, Seção 1, p. 1 | vigência dos 17 (art. 17, cláusula única) | efeitos: a cláusula não diz |

Na LC 227, o cabeçalho "Art. 493-A." (texto inserido na LC 214) vem sem a aspa
de abertura no compilado. É lido como citado porque o `<blockquote>` e o link
para `Lcp214.htm#art493a` concordam, e isso fica em aviso. As duas leis têm
`remissoes: so_escopo_afirmado` no catálogo: são leis de alteração, e "art. N"
sem qualificador nelas é, quase sempre, da norma alterada.

**Item vetado (nível C, 2026-10-15).** Terceira interpretação de IA,
`item-vetado-sem-texto`: item "(VETADO)" não tem texto e não muda as datas do
resto do artigo. Não vale para caput vetado (LC 214, arts. 334, 494, 495 e 536:
o artigo inteiro sem texto fica sem datas), nem com promulgação de partes
vetadas (art. 26); item vetado incluído pela lei alteradora não vira exceção.
Mais 17 decisões de IA; pendentes: 89 de 802.

**Controverso, não decidido: LC 214, art. 544, III (redação dada pela LC
227).** Os arts. 168–171, 309–315, 444 e 462 só estão na redação nova do inciso
III (efeitos em 1º/01/2027). Pela redação anterior, os que já existiam caíam em
"demais dispositivos" (1º/01/2026), e a LC 227 é de 14/01/2026. Entre 1º e
14/01/2026 eles podem ter produzido efeitos pela redação anterior, e o modelo
guarda uma data só de início de efeitos. Gravar 1º/01/2027 esconderia essa
janela; por isso os efeitos ficam pendentes, só com a vigência decidida.

**Nível C aplicado em 2026-10-15** (autorizado pelo usuário, que declarou não
poder aprovar as regras derivadas). Duas interpretações de IA em
`temporal/ia.yaml`, com 13 citações literais conferidas:
- `lc227-republicacao-e-retificacao`: a republicação (só um item vetado do art.
  174) e a retificação (um título no art. 172) não mudam a publicação de
  14/01/2026 dos artigos da LC 227;
- `texto-alterado-pela-lc-227`: a regra `texto-alterado-por-ato-posterior`,
  aplicada só nas decisões de IA.
Resultado: 280 decisões de IA — 178 na LC 227 (177 com vigência e efeitos, o
art. 52 só com vigência) e 102 na LC 214 (`alterar`, com os trechos da LC 227
como exceção) —, além das 465 de regra, que não mudaram. Pendentes: 104 de
802. As decisões de IA aparecem na consulta como "NÃO equivale a revisão
humana"; uma decisão humana, quando houver, prevalece.

**Republicação e retificação da LC 227, lidas em 2026-10-15** (atos no
Planalto, `fontes/lc-227-2026/texto_republicado.doc` e `texto_retificado.doc`;
o DOU recusa acesso deste ambiente):
- republicação parcial "por ter constado inexatidão material": o trecho
  republicado é só "“Art. 293. … § 4º … I - (VETADO);”", texto que o art. 174
  da LC 227 insere na LC 214 — toca o art. 174;
- retificação: "onde se lê / leia-se" no art. 172 (a Parte Quinta que ele
  insere na Lei nº 1.079/1950).
O alcance é conhecido; a data da edição da republicação (15/01/2026) continua
só no rodapé. Se esses atos mudam a publicação dos artigos é interpretação: a
LC 227 continua sem decisão por regra.

**Próximo bloco:** os 146 artigos da LC 214 com texto de outro ato dependem da
cláusula de vigência da LC 227 (art. 182), que espera:
1. arquivar a republicação (DOU de 15/01/2026) e a retificação (23/01/2026);
2. ~~ligar cada anotação "(Incluído pela Lei Complementar nº 227...)" da LC 214
   ao artigo da LC 227 que fez a alteração~~ — feito: `alterado_por`, a partir
   dos links do compilado. Das anotações ligadas a artigo da base, 775 são
   confirmadas no texto do alterador (o art. 174 da LC 227 cita o artigo; o
   art. 181 o revoga no inciso da LC 214), 0 não confirmadas e 4 isoladas não
   confirmadas (arts. 98, 341, 470 e 471: a anotação do título inserido que
   caiu no artigo anterior, ver item 4 das decisões em aberto);
3. ~~usar `alterado_por` na proposta~~ — feito: a proposta da LC 214 mostra,
   por anotação, o ato, a conferência e as datas do ato (art. 182 da LC 227), e a
   combinação pela regra `texto-alterado-por-ato-posterior` (não aprovada): 770
   combináveis em 126 artigos, com resultado 14/01/2026 ou 1º/01/2027;
4. ~~levar a combinação à revisão por regra~~ — feito: `revisar_por_regra.py`
   decide esses artigos como `alterar`, com exceções por subdivisão. Espera duas
   coisas: a aprovação da regra `texto-alterado-por-ato-posterior` e a LC 227 sem
   pendência geral (a republicação toca o art. 174, a retificação o 172). Em
   simulação, com as duas, a LC 214 passaria de 419 para 521 artigos com
   vigência e efeitos decididos (102 com os trechos da LC 227 como exceção), e as
   531 decisões passam pela revisão temporal sem erro.

- **O modelo e a aplicação estão prontos.** A revisão é preenchida no YAML da
  proposta e aplicada por `fatiar.py` (ver `temporal/README.md`), com três
  travas: deriva do `sha256` invalida a revisão; revisão inválida aborta antes de
  apagar arquivo; `validar.py` acusa decisão não aplicada. Verificado ponta a
  ponta numa cópia do repositório, com decisões de teste que não foram gravadas
  aqui.
- **EC 132: proposta** em `temporal/propostas/emc-132-2023.yaml`.
  Dos 23 artigos, 19 caem no inciso III do `Art. 23` ("na data de sua
  publicação"), dois no I ("em 2027": arts. 3º e 11) e dois no II ("em 2033":
  arts. 4º e 5º). 16 têm marcos temporais próprios ou dependem de lei futura, e
  5 inserem texto na Constituição/ADCT, que não estão ingeridas.
- **Vigência não é eficácia.** Para todo artigo com marco próprio, ou que insere
  texto em outra norma, **não há proposta de efeitos**: o `Art. 22` revoga "em
  2027" e "em 2033" artigos da Constituição e do ADCT, o `Art. 7º` compensa "a
  partir de 2027", e os `Arts. 12` e `13` fixam valores por exercício.
- **Publicação da LC 214 confirmada no DOU.** A página do ato no portal da
  Imprensa Nacional está arquivada em `fontes/lc-214-2025/texto_publicado.html`
  (baixada por `baixar.py --tipo texto_publicado`): "Publicado em: 16/01/2025 |
  Edição: 11-B | Seção: 1 - Extra B | Página: 1". Os 580 dispositivos têm
  `publicacao.fonte: dou`. O rodapé do compilado cita também 23/01/2025
  ("republicado"): é a republicação do Anexo XXIII, confirmada pela página 1 do
  DOU de 23/01/2025 arquivada em PDF (código de autenticidade
  05152025012300001) e registrada em `publicacao.republicacoes`.
- **Promulgação das partes vetadas confirmada no DOU**: "Publicado em: 02/07/2025
  | Edição: 122 | Seção: 1 | Página: 3", arquivada em
  `fontes/lc-214-2025/texto_publicado_partes_vetadas.html`: os incisos V e X do
  art. 26.
- **Publicação da EC 132 confirmada no DOU**: "Publicado em: 21/12/2023 |
  Edição: 242 | Seção: 1 | Página: 1", arquivada em
  `fontes/emc-132-2023/texto_publicado.html`. Coincide com o rodapé do compilado.
  Os 603 dispositivos da base têm agora `publicacao.fonte: dou`.
- **A LC 214 traz outro ato no fim do compilado.** Depois dos anexos há um bloco
  citado, uma segunda assinatura ("Brasília, 1º de julho de 2025") e um rodapé
  próprio ("DOU de 2.7.2025"). Não é a publicação da LC; é outro ato, e os
  dispositivos que ele trouxe podem ter vigência própria. Pelo próprio bloco
  (preâmbulo "promulgo ... as seguintes partes vetadas" e artigos citados entre
  aspas), ele traz os incisos V e X do art. 26, que ficam fora da regra.
- **LC 214: proposta** em `temporal/propostas/lc-214-2025.yaml`.
  A cláusula (`Art. 544`) tem a forma "entra em vigor na data de sua publicação,
  produzindo efeitos: I - ...": a vigência de todos os 580 artigos é a publicação
  no DOU (16/01/2025), e os incisos dão os **efeitos**. Por inciso: I, 4 (arts.
  537 a 540, termo relativo, sem data proposta); II, 12 (1º/1/2025); III, 48
  (1º/1/2027); IV, 6 (1º/1/2029); V, 2 (1º/1/2033); VI, 507 ("demais
  dispositivos", 1º/1/2026). Exceções por subdivisão: caput do art. 58 e § 3º do
  art. 60 em 1º/1/2025 (o resto do artigo em VI); §§ 1º e 5º do art. 450 em
  1º/1/2029 (o resto em III).
- **Pontos que a proposta deixa para o revisor na LC 214:**
  - o termo do inciso I ("primeiro dia do quarto mês subsequente ao da sua
    publicação") é lido, mas só vira data pela regra derivada, não aprovada;
  - o art. 482-A (incluído depois) fica dentro de "480 a 484": se o intervalo o
    abrange é interpretação;
  - o inciso III tem redação dada pela LC 227/2026, que acrescentou os arts.
    168–171, 309–315, 444 e 462; antes dela, esses caíam em "demais
    dispositivos". A data em que a nova redação passou a valer depende da LC 227,
    que não está ingerida;
  - o compilado traz outro ato anexado (2.7.2025), cujos dispositivos podem ter
    vigência própria.

---

## 11. Fora de escopo agora

- Propostas de interpretação por IA (o terceiro caminho da PREMISSAS.md §3.4),
  com citação literal verificada mecanicamente e `revisado_por: ia:<modelo>`. O
  que a regra não decide continua pendente até lá, ou até uma decisão humana.
- Busca vetorial. O filtro temporal é determinístico e vem antes da busca;
  embedding ignora tempo.
- Jurisprudência e legislação estadual ou municipal.
- Normas listadas em `pipeline/fontes.yaml` sob `pendentes:` — precisam de URL
  oficial confirmada antes de entrar.
