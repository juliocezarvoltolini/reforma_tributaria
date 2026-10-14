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
| [`docs/ESTADO.md`](docs/ESTADO.md) | onde o trabalho parou, evidência medida e armadilhas já pagas |

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

# Linux/macOS use python3; no Windows o comando é python (ou py).
python3 pipeline/baixar.py                     # baixa, arquiva e registra hash
python3 pipeline/fatiar.py --todas             # fatia em dispositivos
python3 pipeline/indexar.py                    # gera índices derivados
python3 pipeline/validar.py                    # verifica as premissas
```

> **Windows:** não existe `python3` — o atalho com esse nome é o instalador da
> Microsoft Store e não executa nada. Use `python` ou `py`. O
> `pipeline/verificar.sh` detecta o interpretador sozinho; os scripts avulsos
> não, então ajuste o comando.

### Quando o portal recusa acesso por script

Portais oficiais derrubam a conexão de clientes que não parecem navegador. O
sintoma é `ConnectionResetError` igual em todas as URLs. O `baixar.py` já envia
cabeçalhos de navegador e tenta quatro vezes com espera crescente; se ainda
assim o portal recusar, baixe o arquivo no navegador e ingira a partir dele:

```bash
python pipeline/baixar.py --id lcp-214-2025 --de-arquivo caminho/do/lcp214.htm
```

Isso **não** afrouxa a premissa de procedência: a URL oficial vem do catálogo, o
`sha256` é dos bytes reais e a data de acesso é registrada. O manifest grava
`obtencao: manual` para distinguir de um download automatizado, e a detecção de
deriva continua valendo nas reingestões.

### Audite o fatiamento antes de confiar nele

```bash
python pipeline/fatiar.py --todas --relatorio
```

Mostra, sem escrever nada, quantos artigos são **próprios** da norma e quantos
são artigos de **outras normas** citados porque esta as altera. A EC 132 insere
artigos na Constituição e a LC 214 altera outras leis nas disposições finais —
esse texto pertence ao artigo que promove a alteração, e tratá-lo como artigo
próprio sobrescreve arquivos e destrói dados.

A classificação usa dois sinais: aspas (técnica da LC 95/1998) e ordem crescente
da numeração própria. Confira a faixa de artigos próprios contra a norma real
antes de considerar a ingestão boa.

Três advertências para a primeira execução:

1. As URLs em `pipeline/fontes.yaml` estão marcadas `url_verificada: false` —
   seguem o padrão conhecido dos portais, mas não foram confirmadas por acesso
   real. Se der 404, **corrija a URL no catálogo**; não contorne.
2. Todo dispositivo sai com `revisao_temporal_pendente: true`. O parser extrai
   texto e estrutura, mas **não infere vigência nem eficácia** — essas datas vêm
   da cláusula de vigência da norma e exigem revisão humana. Sem essa revisão a
   base responde com datas provisórias.
3. O `fatiar.py` **apaga o resultado da ingestão anterior** antes de escrever.
   Isso é deliberado: sem apagar, um fatiamento corrigido deixa para trás os
   arquivos espúrios do fatiamento antigo, e a base passa a conter dispositivos
   que a norma não tem.

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

Ative o hook uma vez, ao clonar:

```bash
git config core.hooksPath .githooks
```

A partir daí todo `git commit` roda a verificação e **recusa o commit** se
alguma premissa for violada. Para rodar à mão:

```bash
pipeline/verificar.sh
pipeline/verificar.sh --corrigir-indices   # regenera indices/ e inclui no commit
```

O hook e a CI chamam o **mesmo** `pipeline/verificar.sh`, então não podem
divergir — e a base segue verificável mesmo sem o GitHub Actions disponível.

O que a verificação faz valer:

| Regra | Premissa |
|---|---|
| Nada na camada 1 sem `sha256` de fonte | §1.1 |
| Nenhum texto de teste em `/normas/` ou `/fontes/` | §1.3 |
| Nenhum intervalo de vigência ou eficácia incoerente | §3.1 |
| Nenhuma interpretação sem citação, autor e grau de confiança | §4.1 |
| Nenhuma remissão órfã dentro de norma ingerida | §7 |
| `/indices/` como função pura de `/normas/` | §6.3 |
