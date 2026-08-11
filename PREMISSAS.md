# Premissas do Repositório

Documento normativo do projeto. Toda regra aqui é vinculante para qualquer
contribuição — humana ou gerada por IA. Alterações neste arquivo exigem commit
próprio, com justificativa.

**Escopo do repositório:** tributos sobre o consumo instituídos ou alterados pela
Reforma Tributária — IBS, CBS e Imposto Seletivo.

**Profundidade normativa:** da Constituição até o infralegal federal (atos da
RFB, atos do Comitê Gestor do IBS, Ajustes SINIEF e Notas Técnicas de documentos
fiscais). Jurisprudência e legislação estadual/municipal estão **fora** do escopo
atual.

---

## 1. Fonte

### P1.1 — Nada entra sem procedência verificável

Todo conteúdo da camada 1 (texto normativo) exige, obrigatoriamente:

- URL oficial de origem
- data de acesso
- `sha256` do arquivo baixado
- cópia do original arquivada em `/fontes/`

Ausência de qualquer um destes itens é **erro de build**, não pendência.

### P1.2 — Fontes admissíveis

| Tipo de norma | Canal oficial |
|---|---|
| Emenda Constitucional, Lei Complementar, Lei ordinária | `planalto.gov.br` (compilado) + `in.gov.br` (DOU, publicado) |
| Decreto e atos federais | `in.gov.br` |
| Instrução Normativa, Portaria, Ato Declaratório (RFB) | `normas.receita.fazenda.gov.br` |
| Atos do Comitê Gestor do IBS | portal oficial do CGIBS |
| Convênios e Ajustes SINIEF | `confaz.fazenda.gov.br` |
| Notas Técnicas de documentos fiscais | Portal Nacional da NF-e |

O catálogo operacional com as URLs canônicas está em `pipeline/fontes.yaml`.

### P1.3 — Fontes inadmissíveis

Não são fonte, em nenhuma hipótese:

- material de escritório de advocacia, consultoria ou auditoria
- notícia, blog, newsletter, post em rede social, webinar
- planilha ou apostila de terceiro
- **memória de modelo de linguagem**

A última merece ênfase. Um LLM reproduz números de artigo, alíquotas e datas com
fluência e sem sinal de erro. Se a afirmação não aponta para um dispositivo
arquivado em `/fontes/`, ela não existe neste repositório.

### P1.4 — Texto publicado prevalece sobre texto compilado

O texto publicado no DOU é o que tem autoridade. O compilado do Planalto é
consolidação editorial e pode conter erro. Ambos são arquivados; em divergência,
prevalece o publicado, e a divergência é registrada em `/eventos/`.

---

## 2. Hierarquia e conflito normativo

### P2.1 — Ordem de prevalência

`CF/EC` → `Lei Complementar` → `Lei ordinária` → `Decreto` → `ato infralegal`
→ `Ajuste SINIEF / Nota Técnica`

### P2.2 — Tipo de alteração é registrado, não inferido

Cada relação entre dispositivos declara seu tipo, porque a confiabilidade de
cada um é diferente:

| Tipo | Natureza |
|---|---|
| `revogacao_expressa` | fato objetivo — a norma nova declara a revogação |
| `alteracao_redacao` | fato objetivo |
| `acrescimo` | fato objetivo |
| `renumeracao` | fato objetivo |
| `revogacao_tacita` | **interpretação** (LINDB art. 2º, §1º) |

`revogacao_tacita` é camada 3. Nunca pode ser registrada como fato, e sempre
exige fundamentação escrita.

---

## 3. Tempo

Esta é a área de maior risco do projeto. A Reforma Tributária tem transição
escalonada por vários exercícios, com regimes coexistindo. Uma resposta correta
para um ano é uma resposta errada para outro.

### P3.1 — Quatro eixos temporais distintos

Colapsar estes eixos num único campo "vigente: sim/não" é o erro mais provável
e mais caro do projeto.

| Eixo | Campo | Significado |
|---|---|---|
| Publicação | `publicacao` | entrada no mundo jurídico |
| Vigência | `vigencia_inicio` / `vigencia_fim` | quando a norma passa a valer, após *vacatio legis* |
| Produção de efeitos | `efeitos_inicio` / `efeitos_fim` | anterioridade e eficácia diferida — **frequentemente distinta da vigência** |
| Aplicação | (derivado) | a norma aplicável é a vigente na data do **fato gerador**, não na data da consulta |

### P3.2 — Toda consulta exige data de referência

Uma pergunta sem data de referência é malformada. A base responde "estado do
dispositivo na data D", nunca "o que vale" em abstrato.

Quando a data não for informada, ela deve ser **explicitada como assumida** na
resposta — jamais assumida em silêncio.

### P3.3 — Modelo bitemporal

Além do tempo de vigência, registra-se o **tempo de conhecimento** (`ingerido_em`
— quando o dado entrou nesta base). Isso permite auditar decisões passadas:
"em março a base dizia X porque o ato Y ainda não havia sido publicado".

Sem isso, a base reescreve o próprio passado a cada atualização e nenhuma
decisão anterior é auditável.

---

## 4. Camadas

Três camadas, com dependência estritamente unidirecional.

### Camada 1 — Texto normativo (`/normas/`)

Verbatim, imutável, com hash. Nunca editado in loco; correção só por novo commit
com justificativa. Não contém comentário, resumo ou paráfrase.

### Camada 2 — Metadados objetivos (front-matter e `/indices/`)

Numeração, datas, remissões, revogações expressas, hierarquia estrutural.
Verificável mecanicamente contra a camada 1.

### Camada 3 — Interpretação (`/interpretacoes/`)

Análise e síntese. Sempre com autor, data e **citação obrigatória** dos
dispositivos que a fundamentam.

### P4.1 — Regra de dependência

> A camada 3 nunca sobrescreve a camada 1.
> Nenhuma resposta se apoia na camada 3 sem ancorar na camada 1.

### P4.2 — Grau de confiança

Toda afirmação da camada 3 declara seu grau:

| Grau | Significado |
|---|---|
| `literal` | está escrito no dispositivo citado |
| `derivado` | decorre logicamente da combinação dos dispositivos citados |
| `controverso` | há divergência ou lacuna de sentido documentada |
| `pendente` | depende de regulamentação ainda não editada |

### P4.3 — Interpretação não é oficial

Há uma tensão real entre "apenas canais oficiais" e "interpretar a legislação":
interpretação, por definição, não é oficial. A separação em camadas é o que
resolve isso. Este repositório entrega **fundamentação rastreável**, não parecer
jurídico com autoridade própria.

---

## 5. Lacuna como dado positivo

### P5.1 — Silêncio é o pior modo de falha

Boa parte da reforma remete a regulamentação futura. Se a base fica silenciosa
sobre esses pontos, a IA preenche o vazio com plausibilidade — e a resposta
*parece boa*, que é exatamente o que a torna perigosa.

Toda pendência conhecida é registrada em `/lacunas/`, apontando o dispositivo que
exige o regulamento. **"Não regulamentado" é uma resposta que a base sabe dar.**

---

## 6. Integridade ao longo do tempo

### P6.1 — Detecção de deriva

Reingestão periódica compara o `sha256` da fonte. Se o texto oficial mudar, isso
é um **evento que gera alerta e revisão** — nunca sobrescrita silenciosa.

### P6.2 — Histórico imutável

Sem `git push --force` no histórico da base normativa. O histórico do Git é parte
do registro de auditoria.

### P6.3 — Índices são derivados

Tudo em `/indices/` é gerado por script e regenerável a partir de `/normas/`.
Nunca editado à mão. A fonte da verdade é única.

---

## 7. Garantias mecânicas

Premissa que não é verificada por máquina é intenção, não garantia. A CI falha
quando:

- falta front-matter obrigatório ou hash de fonte
- uma remissão aponta para dispositivo inexistente
- há sobreposição ou buraco em intervalos de vigência do mesmo dispositivo
- o hash arquivado diverge do declarado
- uma interpretação (camada 3) não cita nenhum dispositivo
- um arquivo de `/normas/` contém marca de conteúdo não verificado

Executar localmente: `python3 pipeline/validar.py`
