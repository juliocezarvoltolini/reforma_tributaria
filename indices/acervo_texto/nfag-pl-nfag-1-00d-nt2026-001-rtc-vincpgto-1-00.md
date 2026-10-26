---
id: nfag-pl-nfag-1-00d-nt2026-001-rtc-vincpgto-1-00
titulo: Schemas XML NFAg - Pacote de Liberação 1.00d 2026.001 v.1.00 (ZIP) - Publicado em 04/02/2026
tipo: schema
versao: '1.00'
data: '2026-02-04'
documento_fiscal: NFAg
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=0wbRngrGoaU=
arquivo_original: fontes/acervo/nfag-pl-nfag-1-00d-nt2026-001-rtc-vincpgto-1-00.zip
sha256_original: 5fb06c4833b5795a27ca2882d16312ae35600ab7824b3fad7c58da29c4971d6c
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: dc6bf845b0ebfbc051e18b194e12f00bad546a04c1eb9d0192a48dbd446d5c2e
---

## Arquivos do pacote

- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/consSitNFAgTiposBasico_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/consSitNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/consStatServNFAgTiposBasico_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/consStatServNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/evCancNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/evCancVincPgto_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/eventoNFAgTiposBasico_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/eventoNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/evVincPgto_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/nfagTiposBasico_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/nfag_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/procEventoNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/procNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/retConsSitNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/retConsStatServNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/retEventoNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/retNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/tiposGeralNFAg_v1.00.xsd
- PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo | escolha |
|---|---|---|---|---|---|---|---|---|
| NFAg/infNFAg/det/imposto/IBSCBS | TTribNFAg | 1-1 |  |  |  | Grupo de informações do IBS e CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/nfagTiposBasico_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/det/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot | TIBSCBSTot | 1-1 |  |  |  | Totais de IBS e CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/nfagTiposBasico_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
| NFAg/infNFAg/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_NFAg_1.00d_NT2026.001 RTC_VincPgto_1.00/DFeTiposBasicos_v1.00.xsd |  |
