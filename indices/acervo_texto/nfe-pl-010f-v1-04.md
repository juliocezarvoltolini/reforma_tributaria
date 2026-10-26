---
id: nfe-pl-010f-v1-04
titulo: Schemas XML NF-e - Pacote de Liberação nº 010f - NT 2025.002 v.1.50 e NT 2026.007 v.1.00 (Publicado em 31/08/26)
tipo: schema
versao: '1.50'
data: '2026-08-31'
documento_fiscal: NF-e/NFC-e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=8ITFuBLltXs=
arquivo_original: fontes/acervo/nfe-pl-010f-v1-04.zip
sha256_original: b8589490a58a09a993a80e6ac4d7ed10f20892061ecfc56719337098d4b95998
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 825ae3f3208d24ca1d3c9b5744aaf2c90a5bef5b25f47c0aba20908bb9a6faed
---

## Arquivos do pacote

- PL_010f_v1.04/
- PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd
- PL_010f_v1.04/leiauteNFe_v4.00.xsd
- PL_010f_v1.04/nfe_v4.00.xsd
- PL_010f_v1.04/tiposBasico_v4.00.xsd
- PL_010f_v1.04/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo | escolha |
|---|---|---|---|---|---|---|---|---|
| NFe/infNFe/ide/cMunFGIBS | TCodMunIBGE | 0-1 |  |  | [0-9]{7} | Informar o município de ocorrência do fato gerador do fato gerador do IBS / CBS. Campo preenchido somente quando "indPres = 5 (Operação presencial, fora do estabelecimento)", e não estiver preenchido o endereço do destinatário (grupo: E05) nem o local de entrega (grupo: G01). | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/det/prod/tpCredPresIBSZFM | TTpCredPresIBSZFM | 0-1 |  | 0, 1, 2, 3, 4 |  | Classificação para subapuração do IBS na ZFM | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/det/imposto/IS | TIS | 0-1 |  |  |  | Grupo de informações do Imposto Seletivo | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/det/imposto/IS/CSTIS | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do Imposto Seletivo | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/cClassTribIS | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/vBCIS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/pIS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do Imposto Seletivo (percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/adRemIS | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do Imposto Seletivo (por valor) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/uTrib | TStringRTC | 1-1 | 1-6 |  |  | Unidade de medida apropriada especificada em Lei Ordinaria para fins de apuração do Imposto Seletivo | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/qTrib | TDec_1104OpRTC | 1-1 |  |  | 0\.[1-9]{1}[0-9]{3}\|0\.[0-9]{3}[1-9]{1}\|0\.[0-9]{2}[1-9]{1}[0-9]{1}\|0\.[0-9]{1}[1-9]{1}[0-9]{2}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade com abse no campo uTrib informado | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IS/vIS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Imposto Seletivo calculado | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS | TTribNFe | 0-1 |  |  |  | Grupo de informações dos tributos IBS, CBS e Imposto Seletivo | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  | Indica se a operação é de doação | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS | TCIBS_NFe | 1-1 |  |  |  |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS_NFe | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/tpALCZFMCBS | xs:string | 1-1 |  | 1, 2 |  | Tipo de aplicação da alíquota zero da CBS. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/nProcSuframa | TStringRTC | 0-1 | 8-12 |  |  | Número do processo na Suframa para o item comercializado. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono | TMonofasia | 1-1 |  |  |  | Grupo de Informações do IBS e CBS em operações com imposto monofásico (CST 620) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Ad Rem do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoPadrao | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Padrão | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoPadrao/qBCMono | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade tributada na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoPadrao/adRemIBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad rem do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoPadrao/vIBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoReten | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Sujeita à Retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoReten/qBCMonoReten | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade tributada sujeita à retenção na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoReten/adRemIBSReten | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad rem do IBS sujeito à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoReten/vIBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico sujeito à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoRet | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Retida Anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gMonoRet/vIBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS retido anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gpBioDiferenca | (grupo) | 0-1 |  |  |  | Grupo de informações sobre mistura de EAC com gasolina A em percentual inferior ou superior ao obrigatório | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gpBioDiferenca/qBCBioComb | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade de Biocombustível (EAC) a recolher ou a ressarcir | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdRem/gpBioDiferenca/vIBSDiferenca | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS correspondente a diferença em relação ao pBioObrigatorio | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Ad Valorem do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Padrão | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/vBCMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor tributado na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/pAliqMonoUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad valorem do IBS Estadual | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/vIBSMonoUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico Estadual | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/pAliqMonoMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad valorem do IBS Municipal | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/vIBSMonoMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico do Municipal | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoPadrao/vIBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoReten | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Sujeita à Retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoReten/vBCMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor tributado sujeito à retenção na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoReten/pAliqMonoReten | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad valorem do IBS sujeito à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoReten/vIBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico sujeito à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoRet | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Retida Anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gMonoRet/vIBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS retido anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gpBioDiferenca | (grupo) | 0-1 |  |  |  | Grupo de informações sobre mistura de EAC com gasolina A em percentual inferior ou superior ao obrigatório | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gpBioDiferenca/qBCBioComb | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gIBSMonoAdValorem/gpBioDiferenca/vIBSDiferenca | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Ad Rem da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoPadrao | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Padrão | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoPadrao/qBCMono | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade tributada na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoPadrao/adRemCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad rem da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoPadrao/vCBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS monofásica | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoReten | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Sujeita à Retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoReten/qBCMonoReten | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade tributada sujeita à retenção na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoReten/adRemCBSReten | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad rem da CBS sujeita à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoReten/vCBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS monofásica sujeita à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoRet | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Retida Anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gMonoRet/vCBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS retida anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gpBioDiferenca | (grupo) | 0-1 |  |  |  | Grupo de informações sobre mistura de EAC com gasolina A em percentual inferior ou superior ao obrigatório | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gpBioDiferenca/qBCBioComb | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? | Quantidade de Biocombustível (EAC) a recolher ou a ressarcir | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdRem/gpBioDiferenca/vCBSDiferenca | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS correspondente a diferença em relação ao pBioObrigatorio | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Ad Valorem da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoPadrao | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Padrão | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoPadrao/vBCMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor tributado na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoPadrao/pAliqMonoCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad valorem da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoPadrao/vCBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS monofásica | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoReten | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Sujeita à Retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoReten/vBCMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor tributado sujeito à retenção na monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoReten/pAliqMonoReten | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota ad valorem da CBS sujeita à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoReten/vCBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS monofásica sujeita à retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoRet | (grupo) | 0-1 |  |  |  | Grupo de informações da Tributação Monofásica Retida Anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gMonoRet/vCBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS retida anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gpBioDiferenca | (grupo) | 0-1 |  |  |  | Grupo de informações sobre mistura de EAC com gasolina A em percentual inferior ou superior ao obrigatório | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gpBioDiferenca/qBCBioComb | TDec1104RTC | 1-1 |  |  | 0\|0\.[0-9]{4}\|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/gCBSMonoAdValorem/gpBioDiferenca/vCBSDiferenca | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/vTotIBSMonoItem | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de IBS Monofásico. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gIBSCBSMono/vTotCBSMonoItem | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total da CBS Monofásica. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gTransfCred | TTransfCred | 1-1 |  |  |  | Informar essa opção da Choice para o CST 800 | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gTransfCred/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser transferido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gTransfCred/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser transferida | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gAjusteCompet | TAjusteCompet | 1-1 |  |  |  | Informar essa opção da Choice para o CST 811 | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gAjusteCompet/competApur | TCompetApur | 1-1 |  |  |  | Ano e mês referência do período de apuração (AAAA-MM) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gAjusteCompet/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gAjusteCompet/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper | TCredPresOper | 1-1 |  |  |  | Crédito Presumido da Operação. Informado conforme indicador no cClassTrib. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/vBCCredPres | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da Base de Cálculo do Crédito Presumido da Operação | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/cCredPres | TcCredPres | 1-1 |  |  | \d{2} | Código de Classificação do Crédito Presumido do IBS e da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gIBSCredPres | TCredPres | 0-1 |  |  |  | Grupo de Informações do Crédito Presumido referente ao IBS, quando aproveitado pelo emitente do documento. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gIBSCredPres/pCredPres | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gIBSCredPres/vCredPres | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gIBSCredPres/vCredPresCondSus | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido Condição Suspensiva, preencher apenas para cCredPres que possui indicação de Condição Suspensiva | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gCBSCredPres | TCredPres | 0-1 |  |  |  | Grupo de Informações do Crédito Presumido referente a CBS, quando aproveitado pelo emitente do documento. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gCBSCredPres/pCredPres | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gCBSCredPres/vCredPres | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresOper/gCBSCredPres/vCredPresCondSus | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido Condição Suspensiva, preencher apenas para cCredPres que possui indicação de Condição Suspensiva | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresIBSZFM | TCredPresIBSZFM | 1-1 |  |  |  | Classificação de acordo com o art. 450, § 1º, da LC 214/25 para o cálculo do crédito presumido na ZFM. Informado conforme indicador no cClassTrib. | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd | sim |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresIBSZFM/competApur | TCompetApur | 1-1 |  |  |  | Ano e mês referência do período de apuração (AAAA-MM) | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresIBSZFM/tpCredPresIBSZFM | TTpCredPresIBSZFM | 1-1 |  | 0, 1, 2, 3, 4 |  | Classificação de acordo com o art. 450, § 1º, da LC 214/25 para o cálculo do crédito presumido na ZFM | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/det/imposto/IBSCBS/gCredPresIBSZFM/vCredPresIBSZFM | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do crédito presumido calculado sobre o saldo devedor apurado | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/ISTot | TISTot | 0-1 |  |  |  | Valores totais da NF com Imposto Seletivo | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/total/ISTot/vIS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor Total do Imposto Seletivo | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot | TIBSCBSMonoTot | 0-1 |  |  |  | Valores totais da NF com IBS / CBS | PL_010f_v1.04/leiauteNFe_v4.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS | (grupo) | 0-1 |  |  |  | Totalização do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/vCredPres | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gIBS/vCredPresCondSus | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Crédito Presumido Condição Suspensiva | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS | (grupo) | 0-1 |  |  |  | Totalização da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS/vCredPres | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Crédito Presumido | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gCBS/vCredPresCondSus | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Crédito Presumido Condição Suspensiva | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono | (grupo) | 0-1 |  |  |  | Totais da Monofasia | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vIBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS monofásico | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vCBSMono | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS monofásica | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vIBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS monofásico sujeito a retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vCBSMonoReten | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS monofásica sujeita a retenção | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vIBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS monofásico retido anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gMono/vCBSMonoRet | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS monofásica retida anteriormente | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
| NFe/infNFe/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_010f_v1.04/DFeTiposBasicos_v1.00.xsd |  |
