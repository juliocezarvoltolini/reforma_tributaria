# /lacunas/ — camada 2

Pendências de regulamentação, registradas como **dado positivo**.

Motivo (PREMISSAS.md §5.1): se a base fica silenciosa sobre um ponto não
regulamentado, a IA preenche o vazio com plausibilidade — e a resposta *parece
boa*, que é o que a torna perigosa.

Cada arquivo aponta o dispositivo que exige o regulamento. "Não localizado nas
fontes indexadas" é uma resposta completa.

## O que a base afirma: "não localizado nas fontes indexadas"

A base só sabe o que ingeriu. Uma lacuna diz que a regulamentação **não foi
localizada nas normas indexadas** — nunca que ela não existe no mundo. Por isso
o registro diz onde e com que termos se buscou, e a validação falha quando uma
norma é ingerida depois da busca: a base responderia "não localizado" com a
regulamentação dentro dela.

Onde a regulamentação foi localizada, o registro não é lacuna: é a ligação em
`/interpretacoes/regulamentacao/` (camada 3). A mesma remissão nos dois lugares
é erro de validação.

```yaml
---
camada: 2
tipo: lacuna
titulo: "..."
autor: "ia:claude-opus-5-5"        # ou o nome de quem buscou
data: "2026-10-15"
situacao: nao_localizado           # o único valor aceito
remissoes:                         # o dispositivo que remete a lei futura
  - urn: "urn:lex:...!art20"
    trecho: "Até que lei disponha sobre a matéria"
pesquisado_em: [lc-214-2025, lc-227-2026, lc-235-2026]   # todas as normas indexadas
termos_buscados: ["...", "..."]
contexto:                          # opcional: dispositivos próximos, sem conclusão
  - urn: "urn:lex:...!art542_incIX"
    trecho: "..."
---
```

Todo `trecho` é verificado (`pipeline/validar.py`) contra o texto **atual** —
sem a redação riscada — da subdivisão citada pela URN.
