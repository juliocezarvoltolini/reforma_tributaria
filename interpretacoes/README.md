# /interpretacoes/ — camada 3

Análise e síntese. **Nunca sobrescreve a camada 1.**

Front-matter obrigatório (a CI falha sem ele):

```yaml
---
camada: 3
titulo: "..."
autor: "nome"
data: "2026-08-11"
confianca: literal        # literal | derivado | controverso | pendente
fundamenta_se_em:         # obrigatório e não vazio
  - "urn:lex:...!art12"
---
```

Se `confianca: derivado`, exponha o raciocínio: o leitor precisa poder discordar
da inferência sem refazer a pesquisa.

Toda URN de `fundamenta_se_em` precisa existir em `/normas/` (artigo, subdivisão
listada ou caput `_par0`).

## Regulamentação de remissão a lei futura (`regulamentacao/`)

"Lei complementar definirá..." não diz se a lei veio. Quando a base tem a lei, o
registro `tipo: regulamentacao` liga a remissão ao dispositivo que a regula, e
`consultar.py` mostra a ligação — com o estado do regulador na data — no
dispositivo que remete e no regulador. Onde nada é localizado, o registro é uma
lacuna (`/lacunas/`), nunca os dois.

```yaml
---
camada: 3
tipo: regulamentacao
titulo: "..."
autor: "ia:claude-opus-5-5"     # ou o nome de quem leu
data: "2026-10-15"
confianca: literal              # literal | derivado | controverso
remissoes:                      # quem remete a lei futura
  - urn: "urn:lex:...;132!art8_parU"
    trecho: "Lei complementar definirá os produtos..."
regulado_por:                   # quem regula
  - urn: "urn:lex:...;214!art125"
    trecho: "criada nos termos do art. 8º da Emenda Constitucional nº 132"
fundamenta_se_em: [...]         # todas as URNs acima
---
```

- `literal` só quando algum trecho do regulador cita o artigo e a norma que
  remetem (como o art. 125 da LC 214 cita o art. 8º da EC 132). A validação
  confere; sem isso, a ligação é `derivado`, com o raciocínio no corpo.
- Todo `trecho` é verificado contra o texto **atual** (sem o riscado) da
  subdivisão citada pela URN.
- A ligação diz que o regulador trata da matéria remetida. Quando ele produz
  efeitos, e se uma regra transitória ("até que lei complementar...") deixou de
  valer, não é afirmado aqui: depende das datas do regulador.
