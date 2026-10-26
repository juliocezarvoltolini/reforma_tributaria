---
id: nfcom-pl-nfcom-1-00-nt2025-001-rtc-1-14
titulo: Esquema XML NFCom - Pacote de Liberação NT 2025.001 v.1.14 (ZIP) - Publicado em 12/05/2026
tipo: schema
versao: '1.14'
data: '2026-05-12'
documento_fiscal: NFCom
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ZyO9ZoX3yzI=
arquivo_original: fontes/acervo/nfcom-pl-nfcom-1-00-nt2025-001-rtc-1-14.zip
sha256_original: 1e937ae42576490e7c6e3440936774c0f4b8e58374a83ea5b50a956b38be39ca
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: a8b394d8864419793a92feaf474bcfc12b0dfa644174a83db298b992ae0b6094
---

## Arquivos do pacote

- PL_NFCOM_1.00_NT2025.001 RTC_1.14/
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/consSitNFComTiposBasico_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/consSitNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/consStatServNFComTiposBasico_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/consStatServNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/evCancNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/eventoNFComTiposBasico_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/eventoNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/nfcomTiposBasico_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/nfcom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/procEventoNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/procNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/retConsSitNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/retConsStatServNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/retEventoNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/retNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/tiposGeralNFCom_v1.00.xsd
- PL_NFCOM_1.00_NT2025.001 RTC_1.14/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| NFCom/infNFCom/det/imposto/IBSCBS | TTribNFCom | 0-1 |  |  |  | Grupo de informações do IBS e CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/nfcomTiposBasico_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  | Indica se a operação é de doação | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. No fornecimento de energia elétrica, água, esgoto e gás natural e em outras hipóteses definidas no regulamento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/det/imposto/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot | TIBSCBSTot | 0-1 |  |  |  | Totais de IBS e CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/nfcomTiposBasico_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
| NFCom/infNFCom/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_NFCOM_1.00_NT2025.001 RTC_1.14/DFeTiposBasicos_v1.00.xsd |
