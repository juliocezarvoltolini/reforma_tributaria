---
id: nf3e-pl-nf3e-1-00a-nt2026-001-rtc-vincpgto-1-01-aabdbbec
titulo: Schemas NT 2026.001 RTC Vinculação Pagamento v1.01
tipo: schema
versao: '1.01'
data: '2026-03-13'
documento_fiscal: NF3e
url: https://dfe-portal.svrs.rs.gov.br/NF3E/DownloadArquivoEstatico/?sistema=NF3E&tipoArquivo=2&nomeArquivo=PL_NF3E_1.00a_NT2026_001%20-%20RTC_VincPgto_1.01.zip
arquivo_original: fontes/acervo/nf3e-pl-nf3e-1-00a-nt2026-001-rtc-vincpgto-1-01-aabdbbec.zip
sha256_original: aabdbbec938439f8a252a5d758ec0cf8a526faaa7231a2245bbeb01576fae724
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 4d98ef5f70bf8ff2cc655160522ddcc0d60c55cbe1fa33b61ded53d96b7b2cc5
---

## Arquivos do pacote

- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consReciNF3eTiposBasico_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consReciNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consSitNF3eTiposBasico_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consSitNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consStatServNF3eTiposBasico_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/consStatServNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/evCancNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/evCancVincPgto_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/eventoNF3eTiposBasico_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/eventoNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/evVincPgto_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/nf3eTiposBasico_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/nf3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/procEventoNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/procNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/retConsReciNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/retConsSitNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/retConsStatServNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/retEventoNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/retNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/tiposGeralNF3e_v1.00.xsd
- PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS | TTribNF3e | 0-1 |  |  |  | Grupo de informações do IBS e CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/nf3eTiposBasico_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  | Indica se a operação é de doação | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/NFdet/det/detItem/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot | TIBSCBSTot | 0-1 |  |  |  | Totais de IBS e CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/nf3eTiposBasico_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
| NF3e/infNF3e/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_NF3E_1.00a_NT2026_001 - RTC_VincPgto_1.01/DFeTiposBasicos_v1.00.xsd |
