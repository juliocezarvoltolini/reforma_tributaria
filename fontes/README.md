# /fontes/ — originais imutáveis (camada 1)

Documentos oficiais baixados, com `sha256` registrado em `manifest.json`.

- **Não editar nada aqui.** O conteúdo é byte-a-byte o que a fonte oficial serviu.
- Arquivos entram exclusivamente por `pipeline/baixar.py`.
- Mudança no texto oficial gera evento em `/eventos/` e exige revisão humana
  antes de sobrescrever (PREMISSAS.md §6.1). Nunca sobrescreva à mão.

## `acervo/`

Originais dos atos de `pipeline/acervo.yaml` (decretos, atos da RFB e do CGIBS,
Ajustes SINIEF, Notas Técnicas, schemas e leiautes dos documentos fiscais), um
arquivo por id, chave `acervo/<id>` no manifest. Entram por
`python pipeline/baixar.py --acervo`; não são fatiados em `/normas/`.
