---
id: nfe-eventos-rtc-e033e97c
titulo: Esquema XML NF-e/NFC-e - Schema dos eventos da NT 2025.002 v.1.30 - RTC (ZIP). Publicado em 07/10/2025 - Atualizado em 30/10/2025
tipo: schema
versao: '1.30'
data: '2025-10-07'
documento_fiscal: NF-e/NFC-e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=HNw47nrc4Xk=
arquivo_original: fontes/acervo/nfe-eventos-rtc-e033e97c.zip
sha256_original: e033e97cba218020ef492fc5af18a07eb4fd57d484ac3550ff331f01ae441783
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 61e6293885fd9a605adccfbe0dd110b61b6b8101cb68a4adb9a4e1aa8f2986d8
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
- Eventos_RTC/e211120_v1.00.xsd
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
| detEvento/gCredPres/gIBS | (grupo) | 0-1 |  |  |  |  | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gIBS/cCredPres | xs:string | 1-1 |  |  | [0-9]{2} | Usar tabela Cred Presumido, para o emitente da nota. | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gIBS/pCredPres | TDec_0302_04 | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gIBS/vCredPres | TDec1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gCBS | (grupo) | 0-1 |  |  |  |  | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gCBS/cCredPres | xs:string | 1-1 |  |  | [0-9]{2} | Usar tabela Cred Presumido, para o emitente da nota. | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gCBS/pCredPres | TDec_0302_04 | 1-1 |  |  | 0\|0\.[0-9]{2,4}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})? | Percentual do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gCredPres/gCBS/vCredPres | TDec1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do Crédito Presumido | Eventos_RTC/e211110_v1.00.xsd |
| detEvento/gConsumo/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211120_v1.00.xsd |
| detEvento/gConsumo/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211120_v1.00.xsd |
| detEvento/gPerecimento/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211124_v1.00.xsd |
| detEvento/gPerecimento/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS na nota de aquisição correspondente à quantidade destinada a uso e consumo pessoal | Eventos_RTC/e211124_v1.00.xsd |
| detEvento/gImobilizacao/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS relativo à imobilização | Eventos_RTC/e211130_v1.00.xsd |
| detEvento/gImobilizacao/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS relativo à imobilização | Eventos_RTC/e211130_v1.00.xsd |
| detEvento/gConsumoComb/vIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor do IBS relativo ao consumo de combustível na nota de aquisição | Eventos_RTC/e211140_v1.00.xsd |
| detEvento/gConsumoComb/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da CBS relativo ao consumo de combustível na nota de aquisição | Eventos_RTC/e211140_v1.00.xsd |
| detEvento/gCredito/vCredIBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da solicitação de crédito a ser apropriado de IBS | Eventos_RTC/e211150_v1.00.xsd |
| detEvento/gCredito/vCredCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? | Valor da solicitação de crédito a ser apropriado de CBS | Eventos_RTC/e211150_v1.00.xsd |
