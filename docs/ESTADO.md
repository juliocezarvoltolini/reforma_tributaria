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
| PR aberto | #4, com 4 commits ainda não mergeados |

Commits do PR #4, do mais recente para o mais antigo:

```
7a8ae88  janela de escopo que descartava remissões internas
0b3fca8  remissão resolvida para o dispositivo errado
1b8b633  perda de dados no fatiamento de norma que altera outra norma
efbbabb  portabilidade Windows e acesso recusado pelos portais
```

Continue nessa branch — o push atualiza o PR #4. Não abra PR novo.

### Pendências administrativas

- `main` ainda **não** é a branch padrão do repositório no GitHub; a padrão é a
  branch de trabalho, resquício do primeiro push num repositório vazio.
- O GitHub Actions nunca executou: todas as execuções falharam em segundos, sem
  runner atribuído, com logs em 404. O repositório é **público**, onde Actions é
  gratuito e ilimitado, então não é cota nem plano. Verificar em
  Settings → Actions → General. Enquanto isso, o hook de pre-commit cobre a
  verificação (`git config core.hooksPath .githooks`).

---

## 3. O que funciona

- **Download das fontes oficiais.** Cabeçalhos de navegador resolveram a recusa
  do portal. Medido: 510 KB (EC 132) e 5,4 MB (LC 214), com `sha256` registrado
  em `fontes/manifest.json`.
- **`--de-arquivo`** como reserva, para ingerir original baixado pelo navegador
  sem afrouxar a procedência.
- **Detecção de deriva** de texto oficial, que gera evento em `/eventos/` em vez
  de sobrescrever.
- **Verificação mecânica das premissas**, pelo hook e pela CI, a partir do mesmo
  `pipeline/verificar.sh`.
- **Determinismo dos índices** derivados.
- **Portabilidade Windows**: detecção de interpretador e saída em UTF-8.

---

## 4. O que está aberto

### Classificação própria x citada no fatiamento

É a única frente bloqueante. O resto do pipeline depende dela.

Normas que alteram outras normas reproduzem o texto alterado no próprio corpo.
A EC 132 insere artigos na Constituição; a LC 214 altera outras leis nas
disposições finais. Esse texto pertence ao artigo que promove a alteração — não
é artigo da norma ingerida.

`pipeline/fatiar.py` classifica por dois sinais:

1. **Aspas** — a técnica legislativa da LC 95/1998 exige que o texto alterado
   venha entre aspas.
2. **Ordem** — artigos próprios são estritamente crescentes, com `4-A` entre
   `4` e `5`.

Pelo menos um dos dois não corresponde ao que o portal realmente publica.

---

## 5. Evidência coletada

Medições de execuções reais, não suposições.

### Primeira ingestão, antes das correções

| Norma | Artigos escritos |
|---|---|
| EC 132/2023 | 63 |
| LC 214/2025 | 752 |
| **Total em `/normas/` depois** | **601** |

815 escritos e 601 presentes: cerca de **214 artigos foram sobrescritos e
perdidos**, em silêncio. Causa: artigos citados colidiam com artigos próprios de
mesmo número (`Art. 195` da Constituição contra o art. 195 da própria LC).

Duplicatas relatadas na EC 132: `153, 156-A, 156-B, 158, 159, 159-A, 19, 195, 2,
239, 3, 6` — todos números de artigos da Constituição, não da EC.

### Segunda medição, após o filtro de escopo

```
79 de 82 remissoes (96%) apontam para dispositivo inexistente
em norma ja ingerida, a partir de 6 artigo(s).
Concentracao: art473: 49; art156-A: 13; art486: 9; art159: 4; art195: 3
```

Duas leituras:

- **82 remissões em toda a base é implausível** para centenas de artigos. Era o
  filtro de escopo descartando remissões internas legítimas. Corrigido em
  `7a8ae88`; a janela de análise agora termina na próxima menção de artigo.
- **`art156-A` como artigo próprio** permanece sem explicação. É o fio a puxar.

> **Cuidado ao interpretar esta medição:** não está confirmado se `/normas/`
> havia sido reingerido com o fatiamento corrigido quando ela foi tomada. Pode
> refletir a ingestão antiga. **Refaça a medição antes de concluir qualquer
> coisa a partir dela.**

### Hipótese sobre a contagem da EC 132

63 artigos próprios é implausível para uma emenda constitucional, porque a maior
parte do texto de uma EC é o texto que ela insere na Constituição, não artigos
próprios dela.

**Não confirme esse número de memória.** Conte os artigos próprios lendo o HTML
arquivado em `fontes/emc-132-2023/texto_compilado.html`. Afirmar um número de
artigos a partir do conhecimento do modelo viola
[`PREMISSAS.md §1.3`](../PREMISSAS.md).

---

## 6. Armadilhas já pagas

Seis defeitos, todos encontrados por execução real, **nenhum** pelos testes.
Cada linha custou uma rodada.

| # | Defeito | Lição |
|---|---|---|
| 1 | `Art. 4º-A` lido como artigo `4` | O marcador ordinal vem **antes** do sufixo alfabético |
| 2 | `python3` inexistente no Windows | O atalho da Microsoft Store está no PATH e não executa nada: teste o candidato, não a presença |
| 3 | `UnicodeEncodeError` sob cp1252 | `§`, `—` e `→` aparecem sobretudo nas **mensagens de erro**: a falha só surgia quando algo já tinha dado errado |
| 4 | Portal derrubava a conexão | `ConnectionReset` idêntico em todas as URLs é filtro anti-bot, não erro de rede |
| 5 | 214 artigos perdidos por sobrescrita | Colisão de numeração tem de **abortar** a escrita, nunca avisar e sobrescrever |
| 6 | Remissão resolvida no namespace errado | Ponteiro errado é pior que ausente: o ausente falha seguro, o errado leva a IA ao dispositivo equivocado |

### O fixture de teste não é referência de formato

`tests/fixtures/planalto-sintetico.html` é **sintético**. Passou verde em todas
as rodadas em que a ingestão real falhou, porque codifica a marcação que eu
supus, não a que o portal publica. Um teste que valida a suposição errada é pior
que nenhum teste: dá confiança sem cobertura.

**Derive o fixture da marcação real** — trecho reduzido do HTML arquivado,
preservando a estrutura de marcação original.

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
| faixa de artigos próprios | se a contagem é plausível para o tipo de norma |
| lacunas na sequência | artigos legítimos que foram classificados como citados |
| artigos com sufixo alfabético | texto citado que escapou da classificação |
| proporção de remissões órfãs | se a extração está sã (muito abaixo de 25%) |

### O passo que faltou em todas as tentativas anteriores

Abra `fontes/emc-132-2023/texto_compilado.html` e localize a região onde a
EC 132 insere o `Art. 156-A`. Veja **como o portal marca o texto inserido**:
aspas curvas, aspas retas, ausência de aspas, tag ou classe CSS, indentação.

Essa evidência nunca foi observada. Quatro correções foram feitas contra um
documento que não havia sido lido, e cada correção plausível produziu um defeito
novo. Leia o HTML antes de mexer em qualquer heurística.

### Depois de corrigir

```bash
python pipeline/fatiar.py --todas
python pipeline/indexar.py
pipeline/verificar.sh
```

O `fatiar.py` apaga o resultado da ingestão anterior antes de escrever. É
deliberado: sem isso, um fatiamento corrigido convive com os arquivos espúrios
do antigo, e a base passa a conter dispositivos que a norma não tem.

---

## 8. Regras que não podem ser quebradas

- Nunca escrever texto normativo à mão. Camada 1 entra só pelo pipeline, de
  fonte baixada e com `sha256`.
- Nunca editar `/normas/` para "corrigir" texto, nem `/indices/` (derivados;
  regenerar com `indexar.py`).
- Nunca resolver remissão no namespace da norma ingerida quando o escopo não for
  internamente afirmado.
- Colisão de numeração própria **aborta** a escrita. Não relaxar para "fazer
  funcionar".
- Todo dispositivo sai com `revisao_temporal_pendente: true`. O parser não
  infere vigência nem eficácia.

---

## 9. Fora de escopo agora

- Revisão das cláusulas de vigência — trabalho humano, depois que o fatiamento
  estiver correto. É o que separa a base de ser útil ou perigosa, dada a
  transição escalonada por exercício.
- Busca vetorial. O filtro temporal é determinístico e vem antes da busca;
  embedding ignora tempo.
- Jurisprudência e legislação estadual ou municipal.
- Normas listadas em `pipeline/fontes.yaml` sob `pendentes:` — precisam de URL
  oficial confirmada antes de entrar.
