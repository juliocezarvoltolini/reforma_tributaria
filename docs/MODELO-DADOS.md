# Modelo de dados

## Identificador canônico: URN LexML

Chave primária de todo dispositivo. Padrão brasileiro oficial (LexML), o que
permite interoperar com bases públicas sem tradução.

```
urn:lex:br:federal:lei.complementar:2025-01-16;214!art12_par1_inc2_ali-a
└──────── identificação da norma ────────────┘ └──── subdivisão ────┘
```

Subdivisões, na ordem: `art` → `par` (§) → `inc` (inciso) → `ali` (alínea).
`par0` designa o caput. `parU` designa parágrafo único.

Autoridades usadas neste repositório:

| Norma | Fragmento |
|---|---|
| Emenda Constitucional | `br:federal:emenda.constitucional` |
| Lei Complementar | `br:federal:lei.complementar` |
| Lei ordinária | `br:federal:lei` |
| Decreto | `br:federal:decreto` |
| Instrução Normativa RFB | `br:federal:instrucao.normativa` |
| Ajuste SINIEF | `br:federal:ajuste.sinief` |

## Granularidade: um arquivo por artigo

Decisão deliberada:

- **Lei inteira num arquivo** — estoura contexto e impede citação precisa.
- **Um arquivo por inciso** — milhares de arquivos, e o inciso perde sentido sem
  o caput.
- **Artigo** — caput, parágrafos, incisos e alíneas formam a unidade natural de
  leitura e de citação jurídica. É a fronteira semântica que já existe no
  documento; basta respeitá-la.

Isso também resolve o problema clássico de RAG jurídico: fatiar por número de
tokens corta no meio de um inciso e produz citação falsa.

Caminho: `normas/<slug-da-norma>/art-NNNN.md` (NNNN com zero à esquerda, para
ordenação lexicográfica correta).

## Front-matter

Campos obrigatórios marcados com **(*)**.

```yaml
---
urn: "urn:lex:br:federal:lei.complementar:2025-01-16;214!art12"   # (*)
norma: "LC 214/2025"                                              # (*)
norma_slug: "lc-214-2025"                                         # (*)
dispositivo: "art. 12"                                            # (*)
camada: 1                                                         # (*)

# --- estrutura ---
hierarquia: ["LIVRO I", "TÍTULO II", "CAPÍTULO I"]
ordem: 12

# --- tempo (ver PREMISSAS.md §3) ---
publicacao: "2025-01-16"          # (*) entrada no mundo jurídico
vigencia_inicio: "2026-01-01"     # (*) quando a norma vale
vigencia_fim: null                #     null = sem termo final conhecido
efeitos_inicio: "2027-01-01"      # (*) quando produz efeitos — pode diferir
efeitos_fim: null
status: "futuro"                  # (*) vigente|futuro|revogado|pendente_regulamentacao

# --- procedência (ver PREMISSAS.md §1) ---
fonte:                            # (*)
  url: "https://www.planalto.gov.br/..."
  tipo: "texto_compilado"         # texto_publicado | texto_compilado
  acesso: "2026-08-11"
  sha256: "e3b0c44298fc1c14..."
ingerido_em: "2026-08-11"         # (*) tempo de conhecimento (bitemporal)

# --- relações ---
remete_a: ["urn:...!art9", "urn:...!art57_par2"]
altera: []
alterado_por: []
tributos: ["IBS", "CBS"]
conceitos_definidos: ["operação onerosa"]

# --- controle ---
extracao: "automatica"            # automatica | revisada
revisado_por: null
revisado_em: null
---

Art. 12. [texto verbatim, sem edição, sem paráfrase]
```

### Regras de preenchimento

- `vigencia_*` e `efeitos_*` **nunca** são inferidos pelo parser. O parser
  extrai texto e estrutura; datas de eficácia vêm da cláusula de vigência da
  própria norma e exigem revisão humana (`extracao: revisada`).
- `status` é derivado dos campos temporais mais a data de consulta — o valor
  gravado é o estado na data de ingestão, e a consulta recalcula.
- `sha256` é o do arquivo em `/fontes/`, não do arquivo Markdown.

## Camadas e diretórios

| Diretório | Camada | Editável à mão | Conteúdo |
|---|---|---|---|
| `/fontes/` | 1 | não | originais imutáveis + `manifest.json` |
| `/normas/` | 1+2 | não (só pipeline) | dispositivos fatiados |
| `/eventos/` | 2 | sim | alterações, revogações, divergências de texto |
| `/temporal/` | 2 | sim | cronograma da transição, parâmetros por exercício |
| `/lacunas/` | 2 | sim | pendências de regulamentação |
| `/interpretacoes/` | 3 | sim | análise, com citação obrigatória |
| `/indices/` | derivado | **não** | regenerável via `pipeline/indexar.py` |

## Índices derivados

Em ordem de retorno sobre o custo:

| Arquivo | Função |
|---|---|
| `remissoes.json` | grafo `dispositivo → dispositivos citados`. Maior ganho isolado: permite puxar dependências antes de responder |
| `temporal.json` | `dispositivo × início × fim`, para resolver "estado em D" por filtro determinístico, não por semântica |
| `conceitos.json` | termos com definição legal e o dispositivo que os define — evita uso do sentido coloquial |
| `alteracoes.json` | quem alterou ou revogou o quê, e quando |
| `vocabulario.json` | mapa antigo → novo (PIS/COFINS → CBS, ICMS/ISS → IBS); as perguntas reais chegam no vocabulário antigo |
| `cobertura.json` | o que está efetivamente ingerido — evita presumir cobertura inexistente |

## Sobre busca vetorial

Não é usada, por decisão. O volume do escopo cabe em busca lexical com filtro
temporal, que dá citação exata. Embedding erra sistematicamente em pergunta
normativa porque ignora tempo: "alíquota em 2027" recupera com prazer um trecho
que só vale a partir de 2033 — os vetores são quase idênticos.

Se for adicionada no futuro, deve servir apenas para **encontrar candidatos**.
A citação vem sempre da camada 1.
