---
id: nfe-schema-evento-211110-nt2025-002-v1-40
titulo: Evento 211110 - NT 2025.002 v1.40
tipo: schema
versao: '1.40'
data: '2026-07-23'
documento_fiscal: NF-e/NFC-e
url: https://dfe-portal.svrs.rs.gov.br/NFE/DownloadArquivoEstatico/?sistema=NFE&tipoArquivo=2&nomeArquivo=Schema_Evento_211110_NT2025.002%20v1.40.zip
arquivo_original: fontes/acervo/nfe-schema-evento-211110-nt2025-002-v1-40.zip
sha256_original: f07354d4c273d5bac6ebf541d5cfde4ba03aee51e48be7b585de615d2e204401
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 1bf017c293d59e47b24b826a0a1d4dbd43af10bb309f0679ecf5c935824fa229
---

## Arquivos do pacote

- e211110_v1.00.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo | escolha |
|---|---|---|---|---|---|---|---|---|
| detEvento/gCredPresOper/gIBSCredPres | (grupo) | 0-1 |  |  |  |  | e211110_v1.00.xsd |  |
| detEvento/gCredPresOper/gIBSCredPres/pCredPres | TDec_0302_04 | 1-1 |  |  |  | Percentual do Crédito Presumido | e211110_v1.00.xsd |  |
| detEvento/gCredPresOper/gIBSCredPres/vCredPres | TDec1302 | 1-1 |  |  |  | Valor do Crédito Presumido | e211110_v1.00.xsd |  |
| detEvento/gCredPresOper/gCBSCredPres | (grupo) | 0-1 |  |  |  |  | e211110_v1.00.xsd |  |
| detEvento/gCredPresOper/gCBSCredPres/pCredPres | TDec_0302_04 | 1-1 |  |  |  | Percentual do Crédito Presumido | e211110_v1.00.xsd |  |
| detEvento/gCredPresOper/gCBSCredPres/vCredPres | TDec1302 | 1-1 |  |  |  | Valor do Crédito Presumido | e211110_v1.00.xsd |  |
