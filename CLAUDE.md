# Protocolo de consulta — obrigatório

Este repositório é uma base normativa sobre a Reforma Tributária do consumo
(IBS, CBS, Imposto Seletivo). As regras abaixo são vinculantes ao responder
qualquer pergunta usando este repositório.

As premissas completas estão em `PREMISSAS.md`. Este arquivo é o procedimento
operacional derivado delas.

---

## Regra zero

**Não use conhecimento próprio sobre legislação tributária brasileira.**

Você reproduz números de artigo, alíquotas, prazos e datas com fluência e sem
sinal de erro. Neste domínio isso é o modo de falha mais perigoso, porque a
resposta errada é indistinguível da certa para quem pergunta.

Se a informação não está em `/normas/`, a resposta correta é:

> Não localizado nas fontes indexadas neste repositório.

Nunca complete a lacuna por analogia, memória ou plausibilidade.

---

## Procedimento

### 1. Estabeleça a data de referência

Nenhuma resposta é válida sem ela. A transição da reforma é escalonada por
exercício: o mesmo dispositivo produz respostas diferentes conforme o ano.

- Se o usuário informou a data, use-a.
- Se não informou, **declare explicitamente a data assumida** na resposta.
- Se a pergunta é sobre uma operação concreta, a data relevante é a do **fato
  gerador**, não a de hoje.

Nunca assuma data em silêncio.

### 2. Localize o dispositivo

Busque em `/normas/`. Cada arquivo é um artigo, com front-matter YAML contendo
URN, vigência, efeitos e remissões.

```bash
grep -rl "termo" normas/
python3 pipeline/consultar.py --data 2027-01-01 --termo "termo"
```

Prefira `consultar.py`: ele aplica o filtro temporal antes de devolver resultado.
Busca textual crua ignora vigência e devolve dispositivo que ainda não vale.

### 3. Siga as remissões antes de responder

Este é o erro mais comum e mais silencioso.

O texto legal é denso em `"nos termos do art. X"` e `"ressalvado o disposto no
§ Y"`. **Um artigo lido isoladamente frequentemente diz o oposto do que se
aplica ao caso.**

O campo `remete_a` do front-matter e o índice `indices/remissoes.json` existem
para isso. Percorra as remissões do dispositivo encontrado antes de concluir.

### 4. Verifique vigência e efeitos separadamente

São campos distintos e frequentemente divergentes:

- `vigencia_inicio` / `vigencia_fim` — quando a norma vale
- `efeitos_inicio` / `efeitos_fim` — quando produz efeitos

Um dispositivo pode estar vigente há anos e só produzir efeitos no futuro.
Responder pela vigência quando a pergunta é sobre efeitos é erro material.

Verifique também `status`: `vigente`, `futuro`, `revogado`,
`pendente_regulamentacao`.

### 5. Consulte as lacunas

Se o ponto está registrado em `/lacunas/`, a resposta é que **não há
regulamentação**, indicando o dispositivo que a exige. Isso é uma resposta
completa, não uma falha.

### 6. Cite sempre

Toda afirmação carrega o dispositivo e a URN de origem:

> LC 214/2025, art. 12, § 1º
> `urn:lex:br:federal:lei.complementar:2025-01-16;214!art12_par1`

Afirmação sem citação é bug.

### 7. Rotule a natureza da afirmação

Distinga sempre, na própria resposta:

| Rótulo | Significado |
|---|---|
| `literal` | está escrito no dispositivo citado |
| `derivado` | decorre da combinação dos dispositivos citados — mostre a combinação |
| `controverso` | há divergência documentada |
| `pendente` | depende de regulamentação não editada |

Se a resposta é `derivado`, exponha o raciocínio. O usuário precisa poder
discordar da inferência sem precisar refazer a pesquisa.

---

## Formato de resposta

```
Data de referência: 2027-01-01 (assumida — não informada na pergunta)

[resposta]

Fundamento:
- LC 214/2025, art. 12 — urn:...!art12 — literal
- LC 214/2025, art. 57, § 2º — urn:...!art57_par2 — literal
  (remissão a partir do art. 12)

Natureza: derivado — a conclusão combina o art. 12 com a ressalva do art. 57.

Não coberto: a forma de apuração depende de ato conjunto ainda não editado
(ver lacunas/).
```

---

## Ao contribuir com o repositório

- **Nunca** escreva texto normativo manualmente. Texto de camada 1 entra
  exclusivamente pelo pipeline, a partir de fonte oficial baixada e com hash.
- **Nunca** edite arquivos em `/indices/`. São derivados; regenere com
  `python3 pipeline/indexar.py`.
- **Nunca** edite `/normas/` para "corrigir" texto. Reingira a fonte.
- Interpretação vai em `/interpretacoes/`, com autor, data, grau de confiança e
  citação obrigatória.
- Antes de commitar: `pipeline/verificar.sh`. Com
  `git config core.hooksPath .githooks` isso roda sozinho a cada commit e
  recusa o que violar as premissas.

---

## Estado atual da base

Consulte `indices/cobertura.json` para saber o que está efetivamente ingerido.
**Não presuma que uma norma está na base porque ela existe no mundo.**

Se `/normas/` está vazio ou não contém a norma da pergunta, diga isso — não
responda pelo conhecimento do modelo.
