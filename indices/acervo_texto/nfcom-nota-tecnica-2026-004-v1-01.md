---
id: nfcom-nota-tecnica-2026-004-v1-01
titulo: Nota Técnica 2026.004 v1.01 - Publicada em 30/10/2026
tipo: nota.tecnica
versao: '1.01'
data: '2026-10-30'
documento_fiscal: NFCom
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=l1zCFp1N84c=
arquivo_original: fontes/acervo/nfcom-nota-tecnica-2026-004-v1-01.pdf
sha256_original: 44df3269c835fa60fdb2ed1bfec5b9b3ea9123ace11cd942b610848089fd70fe
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 8b2696538e07a42bd8fdb8009df47924473b0c79b34250899014df14c66cb54d
---

## Página 1

Projeto Nota Fiscal Fatura de 
Serviços de Comunicação 
Eletrônica 
 
Nota Técnica 2026.004 – Valor Líquido 
Versão 1.01 de outubro de 2026

## Página 2

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 2 / 9 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Alterações no Leiaute do DFe ......................................................................................... 5 
Grupo de detalhamento dos itens (prod) .............................................................................5 
Criação de campo para informar o ICMS Previsto Pagamento Antecipado .........................5 
Grupo Totais .......................................................................................................................6 
3 Validações dos campos do IBS e CBS ............................................................................ 6 
4 Total Geral do Documento Fiscal Eletrônico ................................................................... 8 
5 Criação dos campos de IBS e CBS no grupo de processo judicial referenciado ............. 9 
6 Criação do município do Terminal Principal .................................................................... 9

## Página 3

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 3 / 9 
 
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
  
1.01  Ajuste da data de Homologação 
 A regra do valor total do DFe retorna a soma de IBS e CBS a partir de 2027 
 Retirada orientação de inclusão de IBS e CBS na composição do vProd 
Até 26/10/2026 16/11/2026

## Página 4

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 4 / 9 
 
1 Introdução 
Com o objetivo de ampliar a transparência na formação do preço da operação, foram criados os campos Valor 
Líquido Unitário e Valor Líquido do Item. Esses campos permitem identificar o valor da mercadoria ou do serviço 
antes da incorporação dos tributos vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o 
valor líquido da operação dos valores tributários agregados ao preço. 
  
A medida busca preservar a rastreabilidade da formação do valor informado no DFe, especialmente diante da 
sistemática do IBS e da CBS. 
  
Dessa forma, os novos campos permitem evidenciar tanto o valor líquido unitário quanto o valor líquido total do 
item, proporcionando maior transparência ao contribuinte, ao adquirente e às Administrações Tributárias quanto à 
composição do preço e à participação dos tributos no valor final da operação. 
  
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. A base de cálculo 
dos tributos deverá ser determinada de acordo com a legislação aplicável. Desta forma, em cada item: 
 No campo vProdLiq deve ser informado o valor líquido do produto ou serviço, sem qualquer tributo; 
 No campo vProd deve ser informado o valor total do produto ou serviço, desconsiderados os valores de 
IBS e CBS; 
No total do documento fiscal: 
 No campo vTotDFe deve ser informado o valor correspondente a soma do vNF + IBS + CBS. 
  
Criação de campo para informar o ICMS previsto 
  
O novo campo “Valor do ICMS Previsto no Pagamento Antecipado” (tag: vICMSPrevisto) deverá ser informado 
quando o documento fiscal emitido for referente a um pagamento realizado antes do fornecimento. O objetivo do 
campo é permitir a correta tributação do IBS e da CBS no pagamento antecipado, com a identificação do valor do 
ICMS que incidirá no momento do fornecimento futuro.

## Página 5

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 5 / 9 
 
2 Alterações no Leiaute do DFe 
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
Obrig. 1052 Rej. Rejeição: Grupo do ICMS Previsto no Pagamento 
Antecipado informado indevidamente [nItem: 999]

## Página 6

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 6 / 9 
 
- Se tipo pagamento antecipado (tpPagAnt) for 
DIFERENTE de: 1 - Pagamento Antecipado de 
Serviços Não Continuados ou 2 - Pagamento de 
serviços continuados (antes da prestação) 
E 
- Se tipo de operação (tpOperGov) com ente 
governamental for DIFERENTE de 4-Recebimento do 
pagamento com fornecimento posterior 
E informado Grupo ICMSPrevistoPagtoAntecip 
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
3 Validações dos campos do IBS e CBS 
As validações serão aplicadas a cada item da NFCom. 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
A alíquota de IBS da UF (pIBSUF) deverá ser: 
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
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF inválida  
Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
A alíquota de IBS Municipal deverá ser: 
 0% para documento com data de emissão no 
ano de 2026. (Art. 343 da LC 214/25) 
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Município inválida

## Página 7

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 7 / 9 
 
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
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 8

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 8 / 9 
 
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
4 Total Geral do Documento Fiscal Eletrônico 
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

## Página 9

Projeto 
Nota Fiscal Fatura de Serviços de Comunicação Eletrônica – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 9 / 9 
 
5 Criação dos campos de IBS e CBS no grupo de processo judicial 
referenciado 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... gProcRef G det - 0-1  Grupo Processo referenciado 
 gIBSCBS G gProcRef - 0-1  Grupo de informações do IBS e CBS a serem 
considerados sem a aplicação do processo judicial 
 vBC E gIBSCBS  N 1-1 13,2 Valor da BC do IBS e CBS 
 vIBSUF E gIBSCBS N 1-1 13,2 Valor de IBS UF 
 vIBSMun E gIBSCBS N 1-1 13,2 Valor de IBS Municipal 
 vCBS E gIBSCBS N 1-1 13,2 Valor de CBS 
6 Criação do município do Terminal Principal 
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
Código do Município do Terminal Principal inexistente 
(Tabela Municípios do IBGE) 
Obrig
. 
410 Rej. Rejeição: Município do Terminal Principal 
inexistente
