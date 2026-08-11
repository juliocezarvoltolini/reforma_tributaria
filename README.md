# Base normativa — Reforma Tributária do consumo

Repositório de referência sobre **IBS, CBS e Imposto Seletivo**, estruturado para
ser consultado por IA sem produzir resposta plausível-porém-errada.

- **Escopo:** tributos sobre o consumo.
- **Profundidade:** da Constituição ao infralegal federal (RFB, CGIBS, Ajustes
  SINIEF, Notas Técnicas de documentos fiscais).
- **Fora de escopo por ora:** jurisprudência e legislação estadual/municipal.

Leia antes de usar ou contribuir:

| Documento | Conteúdo |
|---|---|
| [`PREMISSAS.md`](PREMISSAS.md) | regras de confiabilidade — vinculantes |
| [`CLAUDE.md`](CLAUDE.md) | protocolo obrigatório de consulta por IA |
| [`docs/MODELO-DADOS.md`](docs/MODELO-DADOS.md) | URN, front-matter, camadas, índices |

---

## Estado atual: infraestrutura pronta, base vazia

**Nenhuma norma foi ingerida ainda.** `/normas/` está vazio, e isso é
intencional, não um passo esquecido.

A sessão que montou este repositório estava em ambiente com egresso de rede
restrito: `planalto.gov.br`, `in.gov.br`, `normas.receita.fazenda.gov.br`,
`confaz.fazenda.gov.br` e `lexml.gov.br` estavam todos bloqueados.

Escrever o texto das normas de memória teria violado
[`PREMISSAS.md §1.3`](PREMISSAS.md) — a regra que proíbe memória de modelo de
linguagem como fonte — logo na fundação do projeto. A base vazia é a resposta
correta a essa restrição.

Para popular, execute em ambiente com acesso aos domínios oficiais:

```bash
pip install pyyaml requests

python3 pipeline/baixar.py                     # baixa, arquiva e registra hash
python3 pipeline/fatiar.py --todas             # fatia em dispositivos
python3 pipeline/indexar.py                    # gera índices derivados
python3 pipeline/validar.py                    # verifica as premissas
```

Duas advertências para a primeira execução:

1. As URLs em `pipeline/fontes.yaml` estão marcadas `url_verificada: false` —
   seguem o padrão conhecido dos portais, mas não foram confirmadas por acesso
   real. Se der 404, **corrija a URL no catálogo**; não contorne.
2. Todo dispositivo sai com `revisao_temporal_pendente: true`. O parser extrai
   texto e estrutura, mas **não infere vigência nem eficácia** — essas datas vêm
   da cláusula de vigência da norma e exigem revisão humana. Sem essa revisão a
   base responde com datas provisórias.

---

## Consultar

```bash
python3 pipeline/consultar.py --data 2027-01-01 --termo "credito"
python3 pipeline/consultar.py --urn "urn:lex:...!art12" --seguir
```

`--data` é o parâmetro central. A transição da reforma é escalonada por
exercício, com regimes coexistindo: **a mesma pergunta tem respostas diferentes
conforme o ano**. Sem data de referência a pergunta é malformada, e o script
avisa quando você omite.

`--seguir` exibe também os dispositivos referidos por remissão. Vale o hábito:
um artigo lido isoladamente frequentemente diz o oposto do que se aplica ao caso.

---

## Estrutura

```
fontes/          originais imutáveis + manifest.json com sha256   [não editar]
normas/          um arquivo por artigo, texto verbatim            [só pipeline]
eventos/         alterações, revogações, vetos, deriva de fonte
temporal/        cronograma da transição e parâmetros por exercício
lacunas/         pendências de regulamentação, como dado positivo
glossario/       vocabulário antigo → novo, termos de risco
interpretacoes/  camada 3 — análise, com citação obrigatória
indices/         derivados, regeneráveis                          [não editar]
pipeline/        baixar → fatiar → indexar → validar → consultar
```

Cada diretório tem um `README.md` com suas regras.

---

## As três decisões de projeto

**Um arquivo por artigo.** O artigo é a fronteira semântica que já existe no
documento e a unidade natural de citação jurídica. Fatiar por número de tokens —
o padrão em RAG — corta no meio de um inciso e produz citação falsa.

**Sem busca vetorial.** Embedding ignora tempo: "alíquota em 2027" recupera com
prazer um trecho que só vale a partir de 2033, porque os vetores são quase
idênticos. O filtro temporal é determinístico e vem antes da busca.

**Vigência e eficácia são campos separados.** Colapsar os dois em "vigente:
sim/não" é o erro mais provável e mais caro deste domínio: um dispositivo pode
estar vigente há anos e só produzir efeitos no futuro.

---

## Contribuir

```bash
python3 tests/test_pipeline.py    # testes do parser
python3 pipeline/validar.py       # premissas como falha de build
```

A CI roda os dois, verifica que `/indices/` não foi editado à mão e que conteúdo
sintético de teste não vazou para `/normas/` ou `/fontes/`.

Regras que a validação faz valer: nada na camada 1 sem `sha256` de fonte;
nenhuma remissão órfã; nenhuma interpretação sem citação, autor e grau de
confiança; nenhum intervalo de vigência incoerente.
