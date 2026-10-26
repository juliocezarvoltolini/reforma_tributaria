---
id: nfe-eventos-rtc
titulo: Esquema XML NF-e/NFC-e - Schema dos eventos da NT 2025.002 v.1.40 - RTC (ZIP). Publicado em 27/07/2026
tipo: schema
versao: '1.40'
data: '2026-07-27'
documento_fiscal: NF-e/NFC-e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=kp0SXLu+ZdI=
arquivo_original: fontes/acervo/nfe-eventos-rtc.zip
sha256_original: a4c57ce95b225cd8852f90bd6c39ca28ae551636ff3f67eb2602b9fa847129b2
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: fbb7a68a1b31f887c0b31ef110bb17f48e459eb77af9973f2274f20ca78aff10
---

## Arquivos do pacote

- Eventos_RTC/
- Eventos_RTC/e110001_v1.00.xsd
- Eventos_RTC/e112110_v1.00.xsd
- Eventos_RTC/e112120_v1.00 .xsd
- Eventos_RTC/e112130_v1.00.xsd
- Eventos_RTC/e112140_v1.00.xsd
- Eventos_RTC/e112150_v1.00.xsd
- Eventos_RTC/e211110_v1.00.xsd
- Eventos_RTC/e211124_v1.00.xsd
- Eventos_RTC/e211128_v1.00.xsd
- Eventos_RTC/e211130_v1.00.xsd
- Eventos_RTC/e211140_v1.00.xsd
- Eventos_RTC/e211150_v1.00.xsd
- Eventos_RTC/e212110_v1.00.xsd
- Eventos_RTC/e212120_v1.00.xsd
- Eventos_RTC/e412120_v1.00.xsd
- Eventos_RTC/e412130_v1.00.xsd
- Eventos_RTC/tiposBasico_v1.03.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| detEvento/gConsumo/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS correspondente à quantidade que não atendeu aos requisitos para a conversão em isenção | Eventos_RTC/e112120_v1.00 .xsd |
| detEvento/gConsumo/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do CBS correspondente à quantidade que não atendeu aos requisitos para a conversão em isenção | Eventos_RTC/e112120_v1.00 .xsd |
| detEvento/gPerecimento/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS na Nota de Fornecimento correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento. | Eventos_RTC/e112130_v1.00.xsd |
| detEvento/gPerecimento/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS na Nota de Fornecimento correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento. | Eventos_RTC/e112130_v1.00.xsd |
| detEvento/gPerecimento/gControleEstoque/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do crédito IBS referente às aquisições a ser estornado correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento | Eventos_RTC/e112130_v1.00.xsd |
| detEvento/gPerecimento/gControleEstoque/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do crédito CBS referente às aquisições a ser estornado correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento | Eventos_RTC/e112130_v1.00.xsd |
| detEvento/gItemNaoFornecido/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS na nota de débito de pagamento antecipado correspondente à quantidade que não foi fornecida | Eventos_RTC/e112140_v1.00.xsd |
| detEvento/gItemNaoFornecido/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS na nota de débito de pagamento antecipado correspondente à quantidade que não foi fornecida. | Eventos_RTC/e112140_v1.00.xsd |
| detEvento/gCredPresOper/gIBSCredPres | (grupo) | 0-1 |  |  |  |  | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPresOper/gIBSCredPres/pCredPres | TDec_0302_04 | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPresOper/gIBSCredPres/vCredPres | TDec1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPresOper/gCBSCredPres | (grupo) | 0-1 |  |  |  |  | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPresOper/gCBSCredPres/pCredPres | TDec_0302_04 | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPresOper/gCBSCredPres/vCredPres | TDec1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gPerecimento/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211124_v1.00.xsd |
| detEvento/gPerecimento/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211124_v1.00.xsd |
| detEvento/gImobilizacao/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS relativo à imobilização | Eventos_RTC/e211130_v1.00.xsd |
| detEvento/gImobilizacao/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS relativo à imobilização | Eventos_RTC/e211130_v1.00.xsd |
| detEvento/gConsumoComb/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS relativo ao consumo de combustível na nota de aquisição | Eventos_RTC/e211140_v1.00.xsd |
| detEvento/gConsumoComb/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS relativo ao consumo de combustível na nota de aquisição | Eventos_RTC/e211140_v1.00.xsd |
| detEvento/gCredito/vCredIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da solicitação de crédito a ser apropriado de IBS | Eventos_RTC/e211150_v1.00.xsd |
| detEvento/gCredito/vCredCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da solicitação de crédito a ser apropriado de CBS | Eventos_RTC/e211150_v1.00.xsd |
