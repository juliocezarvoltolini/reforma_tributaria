---
id: bpe-pl-bpe-100b-nt2026-002-rtc-1-01
titulo: Schemas NT 2026.002
tipo: schema
data: '2026-06-22'
documento_fiscal: BP-e
url: https://dfe-portal.svrs.rs.gov.br/BPE/DownloadArquivoEstatico/?sistema=BPE&tipoArquivo=2&nomeArquivo=PL_BPe_100b_NT2026.002%20RTC_1.01.zip
arquivo_original: fontes/acervo/bpe-pl-bpe-100b-nt2026-002-rtc-1-01.zip
sha256_original: a06daec0a2fff38acd0b115d7ef5f9e4efcc10ae0d55307b6c73e1417d8f662e
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 2a0410eb1f04200c1e06f3b9e7fb74e2a20e08856b98b8641ad530aca5ad3c38
---

## Arquivos do pacote

- PL_BPe_100b_NT2026.002 RTC_1.01/
- PL_BPe_100b_NT2026.002 RTC_1.01/bpeTA_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/bpeTiposBasico_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/bpeTM_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/bpe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/consSitBPeTiposBasico_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/consSitBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/consStatServBPeTiposBasico_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/consStatServBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evAlteracaoPoltrona_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evCancBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evCancVincPgto_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/eventoBPeTiposBasico_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/eventoBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evExcessoBagagem_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evNaoEmbBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/evVincPgto_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/procBPeTM_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/procBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/procEventoBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/retBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/retConsSitBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/retConsStatServBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/retEventoBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/tiposGeralBPe_v1.00.xsd
- PL_BPe_100b_NT2026.002 RTC_1.01/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| BPeTA/infBPe/imp/IBSCBS | TTribBPe | 1-1 |  |  |  | Grupo de informações do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/bpeTiposBasico_v1.00.xsd |
| BPeTA/infBPe/imp/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTA/infBPe/imp/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS | TTribBPe | 0-1 |  |  |  | Grupo de informações do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/bpeTiposBasico_v1.00.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/detBPeTM/det/imp/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot | TIBSCBSTot | 0-1 |  |  |  | Totais do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/bpeTiposBasico_v1.00.xsd |
| BPeTM/infBPe/total/IBSCBSTot/vBCIBSCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total Base de Calculo | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS | (grupo) | 1-1 |  |  |  | Totalização do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSUF | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSUF/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSUF/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Estadual | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSMun | (grupo) | 1-1 |  |  |  | Totalização do IBS de competência Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSMun/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSMun/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gIBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gCBS | (grupo) | 1-1 |  |  |  | Totalização da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gCBS/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gCBS/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Total de devoluções de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gEstornoCred | (grupo) | 0-1 |  |  |  | Totalização do estorno de crédito | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total do IBS estornado | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPeTM/infBPe/total/IBSCBSTot/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor total da CBS estornada | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS | TTribBPe | 0-1 |  |  |  | Grupo de informações do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/bpeTiposBasico_v1.00.xsd |
| BPe/infBPe/imp/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| BPe/infBPe/imp/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS | TTribBPe | 0-1 |  |  |  | Grupo de informações do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/evExcessoBagagem_v1.00.xsd |
| evExcessoBagagem/IBSCBS/CST | TCST | 1-1 |  |  | \d{3} | Código Situação Tributária do IBS/CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/cClassTrib | TcClassTrib | 1-1 |  |  | \d{6} |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/indDoacao | TIndDoacao | 0-1 |  | 1 |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS | TCIBS | 0-1 |  |  |  |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/vBC | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do BC | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF | (grupo) | 1-1 |  |  |  | Grupo de informações do IBS na UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS de competência das UF (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS de competência das UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun | (grupo) | 1-1 |  |  |  | Grupo de Informações do IBS no Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota do IBS Municipal (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS Municipal | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/vIBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS | (grupo) | 1-1 |  |  |  | Grupo de Tributação da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota da CBS (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDif | TDif | 0-1 |  |  |  | Grupo de campos do Diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDif/pDif | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDif/vDif | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do diferimento | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDevTrib | TDevTrib | 0-1 |  |  |  | Grupo de Informações da devolução de tributos | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDevTrib/pDevTrib | TDec_0302_04RTC | 0-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de devolução do tributo, conforme LC 214/25 art. 118. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gDevTrib/vDevTrib | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do tributo devolvido. (“cashback” de desconto na própria Nota Fiscal / Fatura) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gRed | TRed | 0-1 |  |  |  | Grupo de campos da redução de aliquota | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual de redução de aliquota do cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Aliquota Efetiva que será aplicada a Base de Calculo (em percentual) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS | TALCZFMCBS | 0-1 |  |  |  | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/gALCZFMCBS/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor efetivo sem a redução | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gCBS/vCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular | TTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular. Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com ZFM e ALC. Exemplo 2: Operações com suspensão do tributo. | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/CSTReg | TCST | 1-1 |  |  | \d{3} | Código da Situação Tributária do IBS e CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/cClassTribReg | TcClassTrib | 1-1 |  |  | \d{6} | Informar qual seria o cClassTrib caso não cumprida a condição resolutória/suspensiva | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS da UF | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/vTribRegIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS do Município | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/pAliqEfetRegCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Alíquota da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribRegular/vTribRegCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov | TTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamental | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido ao município, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0302_04RTC | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? |  | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gEstornoCred | TEstornoCred | 0-1 |  |  |  | Informado conforme indicador no cClassTrib | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gEstornoCred/vIBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS a ser estornado | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
| evExcessoBagagem/IBSCBS/gEstornoCred/vCBSEstCred | TDec1302RTC | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS a ser estornada | PL_BPe_100b_NT2026.002 RTC_1.01/DFeTiposBasicos_v1.00_old.xsd |
