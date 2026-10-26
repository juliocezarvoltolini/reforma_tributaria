---
id: nfs-e-nfs-e-via-esquemas-xsd-versao-1-01-atualizado
titulo: Esquemas XSD versão 1.01 - atualizado
tipo: schema
versao: '1.01'
documento_fiscal: NFS-e (NFS-e Via)
url: https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica/arquivos-dos-esquemas-xsd/schemas_v1-01_atualizado.zip
arquivo_original: fontes/acervo/nfs-e-nfs-e-via-esquemas-xsd-versao-1-01-atualizado.zip
sha256_original: e17ffb5eb05ecd7e7affe770fc6c88feb4e921adc7efd9ee58b4e40865f0a296
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: c8ea97df685f7f2a7221d4e0348a2a76ba5333d21804b642cc1f0513b71b5b26
---

## Arquivos do pacote

- xmldsig-core-schema_v1.00.xsd
- EventoVia_v1.01.xsd
- NFSeVia_v1.01.xsd
- ProcEventoVia_v1.01.xsd
- ProcNFSeVia_v1.01.xsd
- tiposComplexos_v1.01.xsd
- tiposEventos_v1.01.xsd
- tiposSimples_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| NFSeVia/infNFSeVia/valores/trib/ibscbs | TCIBSCBS | 0-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/CST | TSCodCST | 1-1 |  |  | 000 |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/cClassTrib | TSCodClassTrib | 1-1 |  |  | 000002 |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/cIndOp | TSIndOperacao | 1-1 |  |  | 080101 |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/vBC | TSBCIBSCBSDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/vLiq | TSLiqIBSCBSDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/vTotNF | TSTotNFIBSCBSDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS | TCGIBS | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/vIBSTot | TSIBSTotDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf | TCIBSUF | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/pAliqEfetUF | TSAliqEfetUFDesc2V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/vIBSUF | TSValorIBSUFDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun | TCIBSMun | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/pAliqEfetMun | TSAliqEfetMunDesc2V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/vIBSMun | TSValorIBSMunDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS | TCCBS | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/pAliq | TSPercCBSDesc2V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
| NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/vCBS | TSValorCBSDesc15V2 | 1-1 |  |  |  |  | tiposComplexos_v1.01.xsd |
