---
id: nfcom-nfcom-nota-tecnica-2026-004-v1-00-dd497ae7
titulo: Nota Técnica 2026.004 RTC
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-01'
documento_fiscal: NFCom
url: https://dfe-portal.svrs.rs.gov.br/NFCOM/DownloadArquivoEstatico/?sistema=NFCOM&tipoArquivo=3&nomeArquivo=NFCom_Nota_Tecnica_2026_004_v1.00.pdf
arquivo_original: fontes/acervo/nfcom-nfcom-nota-tecnica-2026-004-v1-00-dd497ae7.pdf
sha256_original: dd497ae77e9aef4a3acd1067302bb98f7d122e90cc3545184d430dd2ba048f10
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: dfb0c74f1f29747e7f4324d2e250ceba44f7b581363e48aa1351de22d9ea6b5c
---

## Página 1

Projeto Nota Fiscal Fatura de 
Serviço de Comunicação 
Eletrônico 
 
Nota Técnica 2026.004 – Reforma Tributária do Consumo 
Versão 1.00 de setembro de 2026

## Página 2

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 2 / 10 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Inclusão dos campos de valor líquido no Prod ................................................................ 4 
3 Alterações no Leiaute do DFe ......................................................................................... 5 
Grupo de detalhamento dos itens (prod) .............................................................................5 
Validações dos novos campos de valor líquido nos itens ............................................................... 5 
Criação de campo para informar o ICMS Previsto Pagamento Antecipado .........................5 
Validações do ICMS Previsto em Pagamento Antecipado ............................................................. 6 
Grupo Totais .......................................................................................................................6 
Validações do total .......................................................................................................................... 6 
4 Validações dos campos do IBS e CBS ............................................................................ 6 
5 Total Geral do Documento Fiscal Eletrônico ................................................................... 8 
6 Criação dos campos de IBS e CBS no grupo de processo judicial referenciado ............. 8 
7 Criação do município do Terminal Principal .................................................................... 9

## Página 3

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 3 / 10 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Criação dos campos que representam os valores líquidos de impostos nos 
itens 
 Exceção nas regras de validação de alíquotas para o ambiente de 
homologação 
 Ajuste na regra do valor total do DFe 
 Criação do Campo de previsão do ICMS para antecipação de pagamento 
 Inclusão do Município do Terminal Principal 
13/10/2026 16/11/2026

## Página 4

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 4 / 10 
 
1 Introdução 
Composição do valor do produto com IBS e CBS 
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. 
Para fins de preenchimento da NFCom, os valores do IBS e da CBS incidentes na prestação do serviço de 
comunicação deverão ser acrescidos ao valor do serviço, compondo o valor informado no campo vProd. 
 
A inclusão dos valores do IBS e da CBS no campo vProd não implica sua inclusão na base de cálculo desses 
tributos. A base de cálculo do IBS e da CBS deverá ser determinada de acordo com a legislação aplicável. 
Dessa forma, os valores do IBS e da CBS, por já estarem compreendidos no valor do serviço, não deverão ser 
adicionados novamente na composição do valor total da NFCom (vTotDFe), evitando duplicidade. 
 
Os valores de IBS e CBS permanecem destacados nos respectivos grupos tributários, porém são meramente 
informativos, uma vez que já estão compreendidos no vProd. 
 
2 Inclusão dos campos de valor líquido no Prod 
Com o objetivo de ampliar a transparência na formação do preço da operação, foram criados os campos Valor 
Líquido Unitário e Valor Líquido do Produto. Esses campos permitem identificar o valor do serviço antes da 
incorporação dos tributos vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o 
valor líquido dos valores tributários agregados ao preço. 
 
A medida busca preservar a rastreabilidade da formação do valor informado na NFCom, especialmente diante da 
sistemática do IBS e da CBS, cujos valores passam a compor o valor do serviço para fins de representação 
documental, sem perder a identificação da parcela correspondente ao valor líquido da prestação. 
 
Dessa forma, os novos campos permitem evidenciar tanto o valor líquido unitário quanto o valor líquido total 
do item, proporcionando maior transparência ao contribuinte, ao adquirente e às Administrações Tributárias 
quanto à composição do preço e à participação dos tributos no valor final da prestação.

## Página 5

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 5 / 10 
 
3 Alterações no Leiaute do DFe 
Grupo de detalhamento dos itens (prod) 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 vProd E det\prod N 1-1 13v2 Valor total do item 
 
Observação: A partir 2027, os valores de IBS e 
CBS compõem o Valor Total do Item 
# Sequência XML - det\prod - 0-1  Os campos vItemLiq e vProdLiq estão associados a 
esta sequencia XML 
 vItemLiq E det\prod N 1-1 13v2 Informar o valor unitário do item sem tributos. 
 vProdLiq E det\prod N 1-1 13v2 Valor Líquido total do item sem tributos 
vProdLiq = vItemLiq x qFaturada 
Validações dos novos campos de valor líquido nos itens 
As validações serão aplicadas a cada item do DFe 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informados vItemLiq e vProdLiq: 
   – vProdLiq deve ser igual vItemLiq * qFaturada 
Obrig. 1050 Rej. Rejeição: Valor Líquido do Produto difere do produto 
Valor líquido do item e quantidade faturada [nItem: 
999] 
Criação de campo para informar o ICMS Previsto Pagamento Antecipado 
 
O novo campo 'ICMS Previsto Pagamento Antecipado' deverá ser informado quando o documento fiscal emitido 
for referente a um pagamento realizado antes do fornecimento. O objetivo do campo é permitir a correta tributação 
do pagamento antecipado, com a identificação do valor do ICMS que incidirá no momento do fornecimento futuro. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 gICMSPrevistoPagtoAntecip CG imposto G 0-1 - Grupo utilizado exclusivamente na 
determinação da BC de IBS e CBS em 
cenários específicos de pagamento 
antecipado, informar nas hipóteses: 
   - tpPagAnt = 1 - Pagamento 
Antecipado de Serviços Não 
Continuados ou 2 - Pagamento de 
serviços continuados (antes da 
prestação) 
   - tpOperGov = 4-Recebimento do 
pagamento com fornecimento 
posterior. 
 vICMSPrevisto E gICMSPrevistoPagtoAntecip E 1-1 13v2 Valor do ICMS a incidir no momento do 
fornecimento futuro. 
Observação: Em cenários onde não há 
valor de ICMS devido, informar 0.

## Página 6

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 6 / 10 
 
Validações do ICMS Previsto em Pagamento Antecipado 
As validações serão aplicadas a cada item do DFe 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se o DFe não for de compra governamental ou de 
pagamento antecipado: 
- Grupo ICMSPrevistoPagtoAntecip não deve ser 
informado 
Obrig. 1051 Rej. Rejeição: Grupo do ICMS Previsto no Pagamento 
Antecipado informado indevidamente [nItem: 999] 
Se DFe for de compra governamento ou de pagamento 
antecipado: 
- Se tipo pagamento antecipado (tpPagAnt) for 
DIFERENTE de: 1 - Pagamento Antecipado de 
Serviços Não Continuados ou 2 - Pagamento de 
serviços continuados (antes da prestação) 
E 
- Se tipo de operação (tpOperGov) com ente 
governamental for DIFERENTE de 4-Recebimento do 
pagamento com fornecimento posterior 
E informado Grupo ICMSPrevistoPagtoAntecip 
Obrig. 1052 Rej. Rejeição: Grupo do ICMS Previsto no Pagamento 
Antecipado informado indevidamente [nItem: 999] 
Se DFe for de compra governamento ou de pagamento 
antecipado: 
- Se tipo pagamento antecipado (tpPagAnt) for IGUAL 
a 1 - Pagamento Antecipado de Serviços Não 
Continuados ou 2 - Pagamento de serviços 
continuados (antes da prestação) 
OU 
- Se tipo de operação (tpOperGov) com ente 
governamental for IGUAL de 4-Recebimento do 
pagamento com fornecimento posterior 
E NÃO informado Grupo ICMSPrevistoPagtoAntecip 
Observação:  
Implantação em homologação em 01/02/2027. 
Implantação em produção em 01/03/2027. 
Obrig. 1053 Rej. Rejeição: Grupo do ICMS Previsto no Pagamento 
Antecipado DEVE SER informado [nItem: 999] 
Grupo Totais 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
 vProd E total N 1-1 13v2 Soma dos valores dos produtos ou serviços 
 vProdLiq E total N 0-1 13v2 Soma dos valores líquidos dos produtos ou serviços 
sem tributos 
Validações do total 
Regra de Validação Aplic. cStat Efeito Mensagem 
Total Líquido dos Produtos ou Serviços sem tributos 
(tag: total\vProdLiq) difere do somatório do valor líquido 
dos produtos ou serviços sem tributos dos itens.  
Obrig. 1054 Rej. Rejeição: Total Líquido dos Produtos ou Serviços 
sem tributos difere do somatório dos itens 
4 Validações dos campos do IBS e CBS 
As validações serão aplicadas a cada item da NFCom. 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
 
A alíquota de IBS da UF (pIBSUF) deverá ser: 
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF inválida

## Página 7

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 7 / 10 
 
 0,1% para documento com data de emissão 
no ano de 2026. (Art. 343 da LC 214/25) 
 0.05% para documento com data de emissão 
no ano de 2027 e 2028. (Art. 344 da LC 
214/25) 
 Alíquota de referência ou específica da UF a 
ser publicada para anos posteriores a 2028. 
 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pIBSUF deve ser igual a zero 
 
EXCEÇÂO: Em 2026 será permitido informar as 
alíquotas de 2026 e 2027 APENAS no AMBIENTE DE 
HOMOLOGAÇÃO (tpAmb=2) viabilizando testes das 
empresas. 
Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
A alíquota de IBS Municipal deverá ser: 
 0% para documento com data de emissão no 
ano de 2026. (Art. 343 da LC 214/25) 
 0.05% para documento com data de emissão 
no ano de 2027 e 2028. (Art. 344 da LC 
214/25) 
 Alíquota de referência ou específica do 
Município a ser publicada para anos 
posteriores a 2028 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pIBSMun deve ser igual a zero 
 
EXCEÇÂO: Em 2026 será permitido informar as 
alíquotas de 2026 e 2027 APENAS no AMBIENTE DE 
HOMOLOGAÇÃO (tpAmb=2) viabilizando testes das 
empresas. 
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Município inválida  
VÁLIDA PARA 2026: 
Se informado grupo CBS (gCBS), a alíquota de CBS 
deverá ser de 0,90 % para documento com data de 
emissão no ano de 2026. (Art. 346 da LC 214/25) 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser 
igual a zero quando as condições abaixo forem 
atendidas: 
- Código de Classificação do Produto (cClass) permitir 
alíquota zero para CBS em zona incentivada. 
- Município do Fato Gerador (cMunFG) e emitente 
devem pertencer a um município da ZFM 
Cod. IBGE Nome Município 
1302603 Manaus 
1303569 Rio Preto da Eva 
1301902 Itacoatiara 
 
OU 
- Município do Fato Gerador (cMunFG) e Município 
do Emitente devem estar localizados nos municípios 
pares da mesma ALC. 
ALC  Município Início  Município Fim 
1  1304062-Tabatinga (AM)  1304062-Tabatinga (AM)  
2  1100106-Guajará-Mirim (RO)  1100106-Guajará-Mirim (RO)  
3  1400100-Boa Vista (RR)  1400100-Boa Vista (RR)  
1400100-Boa Vista (RR)  1400159-Bonfim (RR)  
1400159-Bonfim (RR)  1400100-Boa Vista (RR)  
1400159-Bonfim (RR)  1400159-Bonfim (RR)  
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 8

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 8 / 10 
 
4  1600303-Macapá (AP)  1600303-Macapá (AP)  
1600303-Macapá (AP)  1600600-Santana (AP)  
1600600-Santana (AP)  1600303-Macapá (AP)  
1600600-Santana (AP)  1600600-Santana (AP)  
5  1200104-Brasileia (AC)  1200104-Brasileia (AC)  
1200104-Brasileia (AC)  1200252-Epitaciolândia (AC)  
1200104-Brasileia (AC)  1200203-Cruzeiro do Sul (AC)  
1200252-Epitaciolândia (AC)  1200104-Brasileia (AC)  
1200252-Epitaciolândia (AC)  1200252-Epitaciolândia (AC)  
1200252-Epitaciolândia (AC)  1200203-Cruzeiro do Sul (AC)  
1200203-Cruzeiro do Sul (AC)  1200104-Brasileia (AC)  
1200203-Cruzeiro do Sul (AC)  1200252-Epitaciolândia (AC)  
1200203-Cruzeiro do Sul (AC)  1200203-Cruzeiro do Sul (AC)  
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
EXCEÇÂO: Até que seja publicada a alíquota de 
referência da CBS para 2027, deverá ser informada a 
alíquota de 2026, inclusive para testes de simulação de 
2027 no AMBIENTE DE HOMOLOGAÇÃO (tpAmb=2), 
quando a alíquota de 2027 estiver publicada, ela 
também será aceita para testes ainda em 2026 
Se informado o indicador de Doação (indDoacao=1) e 
destinatário pessoa jurídica, o CNPJ-Base do emitente 
deve ser diferente do CNPJ-Base do destinatário do 
serviço 
Obrig. 1055 Rej. Rejeição: Doação com CNPJ/ do emitente igual do 
destinatário do serviço 
Se o cClassTrib informado possuir indicador que VEDA 
uso de doação, o campo indDoacao não pode ser 
informado.  
Obrig 1056 Rej. Rejeição: O cClassTrib é incompatível com o campo 
de indicador de doação preenchido 
Se o cClassTrib informado possuir indicador que 
EXIGE indicação de doação, o campo indDoacao 
DEVE ser informado. 
Obrig 1057 Rej. Rejeição: O cClassTrib informado necessita que o 
indicador de doação seja preenchido 
5 Total Geral do Documento Fiscal Eletrônico 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E total  
 
E 0-1 13,2 Valor total do documento fiscal  
vNF + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser INFORMADO com 
a soma do valor total da NFCom + IBS + CBS 
vTotDFe = total/vNF + IBSCBSTot/gIBS/vIBS + 
IBSCBSTot/gCBS/vCBS 
Exceção: Em 2026 não somar IBS e CBS, usar a 
fórmula: 
vTotDFe = total/vNF   
O total geral do DFe deverá ser informado 
REPETINDO o valor de vNF 
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
6 Criação dos campos de IBS e CBS no grupo de processo judicial 
referenciado

## Página 9

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 9 / 10 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... gProcRef G det - 0-1  Grupo Processo referenciado 
 gIBSCBS G gProcRef - 0-1  Grupo de informações do IBS e CBS a serem 
considerados sem a aplicação do processo judicial 
 vBC E gIBSCBS  N 1-1 13,2 Valor da BC do IBS e CBS 
 vIBSUF E gIBSCBS N 1-1 13,2 Valor de IBS UF 
 vIBSMun E gIBSCBS N 1-1 13,2 Valor de IBS Municipal 
 vCBS E gIBSCBS N 1-1 13,2 Valor de CBS 
 
7 Criação do município do Terminal Principal 
Criado campo de município de instalação do terminal principal, este campo deverá ser preenchido prestando 
informação que será utilizada pela apuração do IBS e CBS para determinação do destino da tributação. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
 assinante G infNFCom - 1-1  Dados do assinante 
 ...       
 cMunPrinc E assinante N 0-1 7 Código do Municipio do Terminal 
 
  
Se o município do terminal principal NÃO ESTIVER 
INFORMADO  
 
Observação: Regra de implementação futura 
Obrig 434 Rej Rejeição: Código do Município do Terminal 
Principal deve ser informado 
Se informado Município do Terminal (cMunPrinc), ele 
não pode divergir da UF do Terminal: 
- Verificar se as 2 posições da esquerda do código de 
município que identifica o código da UF (cUFPrinc) é 
compatível com a UF informada 
Obrig
. 
409 Rej Rejeição: Código de Município do Terminal 
Principal diverge da UF do Terminal Principal 
da NFCom

## Página 10

Projeto 
Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 10 / 10 
 
Código do Município do Terminal Principal inexistente 
(Tabela Municípios do IBGE) 
Obrig
. 
410 Rej. Rejeição: Município do Terminal Principal 
inexistente
