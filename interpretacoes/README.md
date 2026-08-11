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
