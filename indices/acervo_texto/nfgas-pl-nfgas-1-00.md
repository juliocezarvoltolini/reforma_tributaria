---
id: nfgas-pl-nfgas-1-00
titulo: Schemas XML NFGas - Pacote de Liberação 1.00 (ZIP) - Publicado em 24/12/2025
tipo: schema
versao: '1.00'
data: '2025-12-24'
documento_fiscal: NFGas
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=4eijQpstDYM=
arquivo_original: fontes/acervo/nfgas-pl-nfgas-1-00.zip
sha256_original: 6874515e8c87716882f08579340bff9fef45c98ec2a3852ab3547e6cc5b8282e
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 307172029e57adc8d44052f77127c6522257e02fe552af0e75c2112cb0c73783
---

## Arquivos do pacote

- PL_NFGas_1.00/
- PL_NFGas_1.00/consSitNFGasTiposBasico_v1.00.xsd
- PL_NFGas_1.00/consSitNFGas_v1.00.xsd
- PL_NFGas_1.00/consStatServNFGasTiposBasico_v1.00.xsd
- PL_NFGas_1.00/consStatServNFGas_v1.00.xsd
- PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd
- PL_NFGas_1.00/evCancNFGas_v1.00.xsd
- PL_NFGas_1.00/eventoNFGasTiposBasico_v1.00.xsd
- PL_NFGas_1.00/eventoNFGas_v1.00.xsd
- PL_NFGas_1.00/nfgasTiposBasico_v1.00.xsd
- PL_NFGas_1.00/nfgas_v1.00.xsd
- PL_NFGas_1.00/procEventoNFGas_v1.00.xsd
- PL_NFGas_1.00/procNFGas_v1.00.xsd
- PL_NFGas_1.00/retConsSitNFGas_v1.00.xsd
- PL_NFGas_1.00/retConsStatServNFGas_v1.00.xsd
- PL_NFGas_1.00/retEventoNFGas_v1.00.xsd
- PL_NFGas_1.00/retNFGas_v1.00.xsd
- PL_NFGas_1.00/tiposGeralNFGas_v1.00.xsd
- PL_NFGas_1.00/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS | TTribNFGas | 1-1 |  |  |  | Grupo de informações do IBS e CBS | PL_NFGas_1.00/nfgasTiposBasico_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/det/gNormal/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot | TIBSCBSTot | 1-1 |  |  |  | Totais de IBS e CBS | PL_NFGas_1.00/nfgasTiposBasico_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
| nfgasProc/NFGas/infNFGas/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_NFGas_1.00/DFeTiposBasicos_v1.00.xsd |
