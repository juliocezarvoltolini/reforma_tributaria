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
hierarquia: ["LIVRO I — DO IBS E DA CBS", "TÍTULO II", "CAPÍTULO I — DO FATO GERADOR"]
                                  #     etiqueta — título (e a anotação do cabeçalho, se houver)
ordem: 12

# --- tempo (ver PREMISSAS.md §3) ---
data_ato: "2025-01-16"            # (*) data do ato (título); é a que compõe a URN
publicacao:                       # (*) entrada no mundo jurídico — NÃO é a data do ato
  datas: ["2025-01-16"]
  fonte: "dou"                    #     dou | rodape_compilado (o DOU prevalece, §1.4)
  trechos: ["Publicado em: 16/01/2025 | Edição: 11-B | Seção: 1 - Extra B | Página: 1"]
  dou: {edicao: "11-B", secao: "1 - Extra B", pagina: "1"}
  rodape_compilado:               #     o que o compilado diz, mantido à parte
    datas: ["2025-01-16", "2025-01-23"]   # 23/01 não confirmada no DOU → aviso
    trechos: ["Este texto não substitui o publicado no DOU de 16.1.2025 - ..."]
vigencia_inicio: "2026-01-01"     # (*) quando a norma vale
vigencia_fim: null                #     null = sem termo final conhecido
efeitos_inicio: "2027-01-01"      # (*) quando produz efeitos — pode diferir
efeitos_fim: null
precisao:                         #     só os campos SEM precisão de dia
  efeitos_inicio: "ano"           #     o texto diz "em 2027": grava-se 2027-01-01
excecoes_subdivisao:              #     subdivisões com datas próprias
  - urn: "urn:...!art12_par1"
    efeitos_inicio: "2029-01-01"  #     o que a exceção não diz herda do artigo
    fundamento: ["urn:...!art544_incIV"]
fundamento_temporal:              #     de onde vem cada data (só após revisão)
  vigencia: ["urn:...!art544"]
  efeitos: ["urn:...!art544_incIII"]
status: "futuro"                  # (*) vigente|vigente_sem_efeitos|sem_efeitos|futuro|
                                  #     revogado|pendente_regulamentacao

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
alterado_por:                     # anotação oficial ligada ao artigo que fez a alteração
  - anotacao: "(Incluído pela Lei Complementar nº 227, de 2026)"
    subdivisao: "urn:...;214!art26_par9"  # onde a anotação está; null se sozinha na linha
    link: "Lcp227.htm#art174"             # href do compilado, literal
    ato: "urn:...;227!art174"             # null se não leva a norma ingerida
tributos: ["IBS", "CBS"]
conceitos_definidos: ["operação onerosa"]

# --- controle ---
extracao: "automatica"            # automatica | revisada
eixos_revisados: [vigencia]       #     só com revisada: quais eixos foram decididos
revisao_temporal_pendente: true   # false só com os dois eixos revisados
revisado_por: null                #     pessoa | regra:<nome>/<versão>[+<derivada>] | ia:<modelo>
interpretacoes_ia: [...]          #     só com ia:<modelo>: ids em temporal/ia.yaml
revisado_em: null
---

Art. 12. [texto verbatim, sem edição, sem paráfrase]
```

### Regras de preenchimento

- `vigencia_*` e `efeitos_*` **nunca** são inferidos pelo parser. O parser
  extrai texto e estrutura; datas de eficácia vêm da cláusula de vigência da
  própria norma, por regra literal, regra derivada aprovada ou interpretação
  (PREMISSAS.md §3.4), e `revisado_por` diz qual (`extracao: revisada`).
- `eixos_revisados` diz quais eixos foram decididos. Com um só, o outro continua
  provisório e `revisao_temporal_pendente` continua `true`.
- Até a revisão, `vigencia_inicio` e `efeitos_inicio` são **provisórias**: a
  primeira data de `publicacao`, ou `data_ato` se a publicação não foi localizada.
  `revisao_temporal_pendente: true` marca isso.
- `data_ato` e `publicacao` são datas diferentes. "Entra em vigor na data de sua
  publicação" refere-se à publicação no DOU, não à data que dá nome ao ato.
- `publicacao.fonte: dou` diz que a data foi lida da página do ato no DOU,
  arquivada em `fontes/<slug>/texto_publicado.html` (`baixar.py --tipo
  texto_publicado`). O rodapé do compilado continua em `rodape_compilado`, e a
  data que só ele cita gera aviso de não confirmada.
- `publicacao.republicacoes` registra republicação confirmada por página do DOU
  arquivada (`texto_republicado`, PDF da versão certificada, lido por
  `pipeline/dou_pdf.py`): data, edição, página, código de autenticidade, a nota
  "(\*)" literal e o que foi republicado (`artigos`, `anexos`). Não substitui
  `datas`: se a republicação muda a publicação que vale para os artigos é decisão
  da revisão temporal (regra `republicacao-sem-artigo`, em `temporal/regras.yaml`).
  A data do rodapé confirmada como republicação deixa de gerar aviso.
- Quando o DOU não é acessível, o ato de republicação ou de retificação vem do
  Planalto (`ccivil_03/.../ret/*-rep.doc`, `*-ret.doc`, lido por
  `pipeline/atos_planalto.py`): `publicacao.republicacoes` e
  `publicacao.retificacoes` com `fonte: planalto`, a nota ou o "onde se lê / leia-se"
  literal e os `artigos_tocados` — os que o ato nomeia e os que inserem, em outra
  norma, o artigo que ele cita entre aspas. O ato do Planalto dá o ALCANCE, não a
  data da edição do DOU.
- `publicacao.fonte: rodape_compilado` diz que a data foi lida no rodapé do texto
  compilado ("publicado no DOU ..."), sem confirmação no DOU. Só o **primeiro**
  rodapé conta: o compilado pode trazer, depois dos anexos, outro ato com
  assinatura e rodapé próprios.
- `precisao: {campo: ano}` registra o que o texto diz de fato. A data gravada é
  AAAA-01-01 por convenção, e `consultar.py` avisa — e não omite o dispositivo —
  quando a data consultada cai naquele ano.
- `alterado_por` vem dos links das anotações no compilado do Planalto
  (`pipeline/alteracoes.py`). `ato` só é preenchido quando o arquivo é de norma
  do catálogo e a âncora é `artN`; âncora irregular, link para o próprio arquivo
  ou para fora (STF, decreto não ingerido) ficam com `ato: null`. `validar.py`
  confere cada ligação no texto do artigo alterador: ele cita o artigo anotado
  (alteração) ou o lista no inciso que nomeia a norma (revogação). Anotação
  sozinha na linha (`isolada: true`) fica sem subdivisão.
- `excecoes_subdivisao` cobre o que a cláusula diz de uma subdivisão ("exceto
  os §§ 1º e 5º"). A URN tem de ser de subdivisão do próprio artigo, e cada
  exceção tem `fundamento`.

### Revisão temporal

A revisão é preenchida em `temporal/propostas/<slug>.yaml`, gerado por
`pipeline/propor_vigencia.py`, e aplicada por `pipeline/fatiar.py` ao regravar
`normas/`. Tem de ser assim porque o fatiamento apaga e regrava a norma a cada
execução: um passo separado seria desfeito pela próxima reingestão. Ver
`temporal/README.md`.

- A revisão só é aplicada se o `sha256` do original for o mesmo sobre o qual ela
  foi feita. Deriva da fonte exige nova revisão.
- Revisão inválida aborta a escrita, antes de apagar qualquer arquivo.
- `validar.py` acusa decisão tomada e ainda não refletida em `normas/`.
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
| `/lacunas/` | 2 | sim | remissões a lei futura cuja regulamentação não foi localizada nas normas indexadas (`situacao: nao_localizado`, com onde e o que se buscou) |
| `/interpretacoes/` | 3 | sim | análise, com citação obrigatória; `regulamentacao/` liga cada remissão a lei futura ao dispositivo que a regula |
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
