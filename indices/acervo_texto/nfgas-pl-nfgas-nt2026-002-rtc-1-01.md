---
id: nfgas-pl-nfgas-nt2026-002-rtc-1-01
titulo: Schemas XML NFGas - Pacote de Liberação 1.00d 2026.002 v.1.01 (ZIP) - Publicado em 29/06/2026
tipo: schema
versao: '1.01'
data: '2026-06-29'
documento_fiscal: NFGas
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=I6wOA08exzM=
arquivo_original: fontes/acervo/nfgas-pl-nfgas-nt2026-002-rtc-1-01.zip
sha256_original: 8d751ba15135a1a755732e8492c37d0f7b44c4465af1f37438f687d1fd4d6ca2
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 04686be42ec52d979f8ff73d389e8d51f80e926dec3405035e527cded5246018
---

## Arquivos do pacote

- PL_NFGas_NT2026.002 RTC_1.01/
- PL_NFGas_NT2026.002 RTC_1.01/consSitNFGasTiposBasico_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/consSitNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/consStatServNFGasTiposBasico_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/consStatServNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/evCancNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/evCancVincPgto_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/eventoNFGasTiposBasico_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/eventoNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/evVincPgto_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/nfgasTiposBasico_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/nfgas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/procEventoNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/procNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/retConsSitNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/retConsStatServNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/retEventoNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/retNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/tiposGeralNFGas_v1.00.xsd
- PL_NFGas_NT2026.002 RTC_1.01/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo | escolha |
|---|---|---|---|---|---|---|---|---|
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS | TTribNFGas | 1-1 |  |  |  | Grupo de informações do IBS e CBS | PL_NFGas_NT2026.002 RTC_1.01/nfgasTiposBasico_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido ("cashback" de desconto na própria Nota Fiscal / Fatura) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot | TIBSCBSTot | 1-1 |  |  |  | Totais de IBS e CBS | PL_NFGas_NT2026.002 RTC_1.01/nfgasTiposBasico_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
| NFGas/infNFGas/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_NFGas_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd |  |
