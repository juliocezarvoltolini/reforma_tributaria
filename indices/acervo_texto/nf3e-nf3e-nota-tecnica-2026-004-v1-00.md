---
id: nf3e-nf3e-nota-tecnica-2026-004-v1-00
titulo: Nota Técnica 2026.004 v.1.00 - Publicada em 01/10/2026
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-01'
documento_fiscal: NF3e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=41v20jvOXhs=
arquivo_original: fontes/acervo/nf3e-nf3e-nota-tecnica-2026-004-v1-00.pdf
sha256_original: d09461c03d96adf3ec9bde9221fd50d730f27c6c4844a3394ee27e99947061f7
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: e75eba6717b136680c84b25182b237b2dae2b51bcf256222d7ab9de633c5c865
---

## Página 1

Projeto Nota Fiscal de Energia 
Elétrica Eletrônica 
 
Nota Técnica 2026.004 – Reforma Tributária do Consumo 
Versão 1.00 de setembro de 2026

## Página 2

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 2 / 13 
 
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
7 Eliminação da NF3e de Ajuste ........................................................................................ 9

## Página 3

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 3 / 13 
 
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
13/10/2026 16/11/2026 
1.00  Descontinuidade da NF3e normal com ajuste 16/11/2026 14/12/2026

## Página 4

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 4 / 13 
 
1 Introdução 
Composição do valor do produto com IBS e CBS 
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. 
Para fins de preenchimento da NF3e, os valores do IBS e da CBS incidentes na prestação do serviço de energia 
elétrica deverão ser acrescidos ao valor do serviço, compondo o valor informado no campo vProd. 
 
A inclusão dos valores do IBS e da CBS no campo vProd não implica sua inclusão na base de cálculo desses 
tributos. A base de cálculo do IBS e da CBS deverá ser determinada de acordo com a legislação aplicável. 
Dessa forma, os valores do IBS e da CBS, por já estarem compreendidos no valor do serviço, não deverão ser 
adicionados novamente na composição do valor total da NF3e (vTotDFe), evitando duplicidade. 
 
Os valores de IBS e CBS permanecem destacados nos respectivos grupos tributários, porém são meramente 
informativos, uma vez que já estão compreendidos no vProd. 
 
2 Inclusão dos campos de valor líquido no Prod 
Com o objetivo de ampliar a transparência na formação do preço da operação, foram criados os campos Valor 
Líquido Unitário e Valor Líquido do Produto. Esses campos permitem identificar o valor do serviço antes da 
incorporação dos tributos vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o 
valor líquido dos valores tributários agregados ao preço. 
 
A medida busca preservar a rastreabilidade da formação do valor informado na NF3e, especialmente diante da 
sistemática do IBS e da CBS, cujos valores passam a compor o valor do serviço para fins de representação 
documental, sem perder a identificação da parcela correspondente ao valor líquido da prestação. 
 
Dessa forma, os novos campos permitem evidenciar tanto o valor líquido unitário quanto o valor líquido total 
do item, proporcionando maior transparência ao contribuinte, ao adquirente e às Administrações Tributárias 
quanto à composição do preço e à participação dos tributos no valor final da prestação.

## Página 5

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 5 / 13 
 
3 Alterações no Leiaute do DFe 
Grupo de detalhamento dos itens (prod) 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 vProd E detItem\prod N 1-1 13v2 Valor total do item 
 
Observação: A partir 2027, os valores de IBS e 
CBS compõem o Valor Total do Item 
# Sequência XML - detItem\prod - 0-1  Os campos vItemLiq e vProdLiq estão associados a 
esta sequencia XML 
 vItemLiq E detItem\prod N 1-1 13v2-
10 
Informar o valor unitário do item sem tributos. 
 vProdLiq E detItem\prod N 1-1 13v2-
10 
Valor Líquido total do item sem tributos 
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
Criação de campo para informar o ICMS Previsto Pagamento 
Antecipado 
 
O novo campo 'ICMS Previsto Pagamento Antecipado' deverá ser informado quando o documento fiscal emitido 
for referente a um pagamento realizado antes do fornecimento. O objetivo do campo é permitir a correta tributação 
do pagamento antecipado, com a identificação do valor do ICMS que incidirá no momento do fornecimento futuro. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 gICMSPrevistoPagtoAntecip G imposto G 0-1 - Grupo utilizado exclusivamente na 
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
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 6 / 13 
 
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
Se DFe for de compra governamental ou de 
pagamento antecipado: 
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
Se DFe for de compra governamental ou de 
pagamento antecipado: 
- Se tipo pagamento antecipado (tpPagAnt) for IGUAL 
a 1 - Pagamento Antecipado de Serviços Não 
Continuados ou 2 - Pagamento de serviços 
continuados (antes da prestação) 
OU 
- Se tipo de operação (tpOperGov) com ente 
governamental for IGUAL a 4-Recebimento do 
pagamento com fornecimento posterior 
E NÃO informado Grupo ICMSPrevistoPagtoAntecip 
Observação:  
Implantação em homologação em 01/02/2027. 
Implantação em produção em 01/03/2027. 
Obrig. 1053 Rej. Rejeição: Grupo do ICMS Previsto no Pagamento 
Antecipado DEVE SER informado [nItem: 999] 
Grupo Totais 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
 vProd E total N 1-1 13v2-
10 
Soma dos valores dos produtos ou serviços 
 vProdLiq E total N 0-1 13v2-
10 
Soma dos valores líquidos dos produtos ou serviços 
sem tributos 
Validações do total 
Regra de Validação Aplic. cStat Efeito Mensagem 
Total Líquido dos Produtos ou Serviços sem tributos 
(tag: total\vProdLiq) difere do somatório do valor líquido 
dos produtos ou serviços sem tributos dos itens.  
Obrig. 1054 Rej. Rejeição: Total Líquido dos Produtos ou Serviços 
sem tributos difere do somatório dos itens 
4 Validações dos campos do IBS e CBS 
As validações serão aplicadas a cada item da NF3e. 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
 
A alíquota de IBS da UF (pIBSUF) deverá ser: 
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF inválida

## Página 7

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 7 / 13 
 
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
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 8 / 13 
 
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
Obrig. 1055 Rej. Rejeição: Doação com CNPJ do destinatário igual 
do tomador do serviço 
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
 
N 0-1 13,2 Valor total do documento fiscal  
vNF + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser INFORMADO com 
a soma do valor total da NF3e + IBS + CBS 
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
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 9 / 13 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... gProcRef G detItem - 0-1  Grupo Processo referenciado 
 gIBSCBS G gProcRef - 0-1  Grupo de informações do IBS e CBS a serem 
considerados sem a aplicação do processo judicial 
 vBC E gIBSCBS  N 1-1 13,2 Valor da BC do IBS e CBS 
 vIBSUF E gIBSCBS N 1-1 13,2 Valor de IBS UF 
 vIBSMun E gIBSCBS N 1-1 13,2 Valor de IBS Municipal 
 vCBS E gIBSCBS N 1-1 13,2 Valor de CBS 
7 Eliminação da NF3e de Ajuste 
 
Em definição junto a SEFAZ Paraná, a NF3e de finalidade normal com ajuste será descontinuada a partir de janeiro 
de 2027. Esta mudança visa simplificar o processo de emissão das empresas do setor elétrico e consolida o 
processo de ajuste na nota de substituição, da mesma forma que ocorrem em outros documentos fiscais 
eletrônicos. 
Esse processo de alteração das regras e da sistemática da NF3e normal com ajustes, afeta unicamente as 
autorizações realizadas pela SEFAZ PR para as distribuidoras contribuintes desta UF, visando fasear essa 
desativação, segue o processo da mudança:  
1. Fase 1: Bloqueio Lógico e Governança de Aplicação: Implementação via regras de validação. É 
imperativo destacar que o XML Schema (XSD) permanecerá na versão 1.00, evitando "rejeições de 
schema" estruturais nos sistemas dos contribuintes. O bloqueio será estritamente na camada de lógica 
de negócio. 
2. Fase 2: Limpeza Estrutural e Atualização do MOC: Projeta-se a remoção física das tags de ajuste no 
dicionário de dados em versões futuras do Manual de Orientação do Contribuinte, consolidando a limpeza 
do modelo de dados. 
Para atender essa primeira fase, seguem as mudanças previstas para janeiro de 2027: 
# Se tipo da NF3e = 3 (Normal com Ajustes): 
Rejeitar a NF3e 
 
Implantação Homologação: 07/12/2026 
Implantação Produção: 04/01/2027 
Obrig, 370 Rej. Rejeição: NF3e Normal com Ajustes 
descontinuada. Utilizar finalidade Normal (1) ou 
Substituição (2) 
G50 Se o Tipo da NF3e = 2 (Substituição) (tag: finNF3e): 
- Verificar se tipo de NF3e é permitida na UF do 
emitente 
Obrig. 477 Rej. Rejeição: UF não permite NF3e de 
Substituição 
G51 Se o Tipo da NF3e = 1 (Normal) ou 3 (Normal com 
Ajustes) (tag: finNF3e): 
- O grupo de informações da substituição (grupo: 
gSub) NÃO deve ser informado 
Obrig. 412 Rej. Rejeição: Grupo NF3e de Substituição não 
deve ser informado para NF3e Normal ou de 
Ajuste 
      
Validações da NF-3 de Ajuste 
G62 Se tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e): 
 
- Verificar se tipo de NF3e é permitida na UF do 
emitente 
Obrig. 237 Rej. Rejeição: UF não permite NF3e normal com 
ajustes 
G64 Se tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e): 
 
- Devem ser informados no mínimo duas ocorrências 
do grupo de detalhamento dos Produtos e Serviços 
(grupo: NFdet). 
Obrig. 480 Rej. Rejeição: NF3e Normal com ajuste deve ter no 
mínimo duas NF3e informadas no 
detalhamento de produtos 
G65 Se tipo da NF3e = 3 (Normal com Ajustes) (tag: Obrig. 238 Rej. Rejeição: Chave de acesso anterior deve ser

## Página 10

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 10 / 13 
 
finNF3e): 
 
- Verificar se foi informada chave de acesso da NF3e 
(chNF3eAnt) ou o HashCode do Modelo 6 
(mod6HashAnt) anterior no detalhamento dos 
Produtos e Serviços (grupo: NFdet) 
 
Observação: não aplicar esta regra para o último item 
da NF3e, que pode ter a configuração de um item 
normal. 
informada para NF3e normal com ajustes 
G66 Se tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e): 
 
- Verificar se foi informado somente a chave de 
acesso da NF3e anterior (chNF3eAnt) ou o HashCode 
da Modelo 6 Anterior (mod6HashAnt). 
 
Observação: Não é permitido informar os dois ao 
mesmo tempo, informe chNF3eAnt ou é 
mod6HashAnt. 
Obrig. 677 Rej. Rejeição: Só um dos campos pode ser 
informado: chave de acesso ou hashCode da 
nota anterior 
G67 Se informada chave de acesso de NF3e anterior (tag: 
chNF3eAnt) ou o HashCode do Modelo 6 
(mod6HashAnt no detalhamento dos Produtos e 
Serviços (NFdet): 
 
- Verificar se o tipo da NF3e é igual a 3 (Normal com 
Ajustes) 
 
Obrig. 241 Rej. Rejeição: Não é permitido informar NF3e 
anterior para NF3e diferente de normal com 
ajustes 
G68 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso de NF3e 
anterior (tag: chNF3eAnt) no detalhamento dos 
Produtos e Serviços (grupo: NFdet): 
- Validar chave de acesso da NF3e anterior.  
 
Retornar motivo da rejeição da Chave de Acesso: 
CNPJ zerado ou inválido, Ano < 2019 ou maior que 
atual, Mês inválido (0 ou > 12), Modelo diferente de 
66, Número zerado, Tipo de emissão inválido, UF 
inválida ou DV inválido) 
[Motivo: XXXXXXXXXXXX] 
Obrig. 242 Rej. Rejeição: Rejeição: Chave de Acesso anterior 
inválida 
[Motivo: XXXXXXXXX] 
G69 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):  
- NF3e anterior não pode existir com diferença na 
Chave de Acesso 
 
Retornar a chave de acesso já autorizada, o número 
do protocolo e data de autorização da NF3e 
[chNF3e: 
9999999999999999999999999999999999999999999
9] 
[nProt:999999999999999][dhAut: AAAA-MM-
DDTHH:MM:SS TZD] 
Obrig. 245 Rej. Rejeição: NF3e anterior com diferença de 
Chave de Acesso 
[chNF3e: 
9999999999999999999999999999999999999
9999999] 
[nProt:999999999999999][dhAut: AAAA-MM-
DDTHH:MM:SS TZD] 
G70 Se Tipo da NF3e = 3 (Normal com ajustes) (tag: 
finNF3e) e o motivo do ajuste (tag: motAjuste) for 
diferente de 03 (Decisão Judicial): 
 
- Rejeitar se a data da emissão da NF3e anterior 
informada ou a competência da NF papel forem 
anteriores a 5 anos da data atual 
Obrig. 638 Rej. Rejeição: NF3e ou NF anterior informada com 
data de emissão anterior a 5 anos da data 
atual 
G71 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):  
- A NF3e anterior deve existir 
Acesso BD NF3e (Chave: CNPJ Emit, Modelo, Série, 
Nro) 
 
Observação: Esta validação leva em consideração o 
ambiente de autorização do DF-e (nSiteAutoriz) 
Obrig 246 Rej Rejeição: NF3e anterior inexistente 
G72 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):  
- A NF3e anterior não pode estar cancelada  
Obrig. 250 Rej Rejeição: NF3e a anterior não pode estar 
cancelada

## Página 11

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 11 / 13 
 
G73 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):  
- A NF3e anterior não pode estar substituída 
Obrig. 251 Rej Rejeição: NF3e a anterior não pode ter sido 
substituída  
G74 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):    
- A NF3e anterior não pode ter sido ajustada 
Obrig. 254 Rej. Rejeição: NF3e anterior não pode ter sido 
ajustada anteriormente 
G75 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) e informada chave de acesso da NF3e 
anterior (tag: chNF3eAnt):  
- CNPJ do emitente da NF3e anterior deve ser igual 
ao informado na NF3e de ajuste 
 
Exceção: os casos de alteração do CNPJ da 
Distribuidora por motivo de aquisição, fusão, 
incorporação deve ser tratados no ambiente de 
autorização da NF3e   
Obrig. 255 
 
Rej. Rejeição: CNPJ do emitente da NF3e anterior 
deve ser igual ao informado na NF3e de ajuste 
G76 Se Tipo da NF3e = 3 (Normal com Ajustes) (tag: 
finNF3e) deve ser informado o grupo gAjusteNF3eAnt 
 
Observação: não aplicar esta regra para o último item 
da NF3e, que pode ter a configuração de um item 
normal. 
Facult. 256 Rej. Rejeição: Grupo de ajuste da NF3e anterior 
deve ser informado para NF-3 normal com 
ajuste 
G77 Se Tipo da NF3e diferente de 3 (Normal com Ajustes) 
(tag: finNF3e) não deve ser informado o grupo de 
identificação do ajuste do item de NF3e anterior 
(grupo: gAjusteNF3eAnt) 
Facult. 257 Rej. Rejeição: Grupo de ajuste da NF3e anterior 
não deve ser informado para NF3e normal e 
substituição 
G78 Se tipo de ajuste a ser aplicado ao item (tag: tpAjuste) 
igual a 1 (Item a ser substituído) ou 3 (item a ser 
eliminado) deve ser informado o grupo de 
informações referentes ao item da NF3-e anterior 
(grupo: detItemAnt) 
Facult. 258 Rej. Rejeição: Detalhamento do item da NF3e 
anterior deve ser informado para tipos de 
ajuste 1 e 3 
G79 Se tipo de ajuste a ser aplicado ao item (tag: tpAjuste) 
diferente de 1 (Item a ser substituído) ou 3 (item a ser 
eliminado) não deve ser informado o grupo de 
informações referentes a item da NF3-e anterior 
(grupo: detItemAnt) 
Facult. 259 Rej. Rejeição: Detalhamento do item da NF3e 
anterior não deve ser informado para tipos de 
ajuste 2 e 4 
G80 Se tipo de ajuste a ser aplicado ao item (tag: tpAjuste) 
igual 1 (Item a ser substituído), o próximo item (tag: 
det/nItem) deve ser do tipo de ajuste (tag: tpAjuste) 
igual a 2 (Item de substituição) 
Facult. 260 Rej. Rejeição: Após um item com tipo de ajuste 
igual a 1 deve sempre ser informado um item 
com tipo de ajuste igual a 2 
Validações da NF-3 de Ajuste (Banco de Dados) 
G81 Se informado Grupo de informações referentes a item 
da NF3e anterior (grupo: detItemAnt): 
- Acessar BD e verificar se número do item da NF3e 
anterior (tag: detItemAnt /nItemAnt) informado existe 
na NF3e anterior  
Facult. 261 Rej. Rejeição: Número de item da NF3e de ajuste 
não existe na NF3e anterior 
G82 - Acessar BD e verificar se o valor unitário do item 
(tag: detItemAnt 
/vItem) é igual ao valor unitário do item da NF3e 
anterior  
Facult. 262 Rej. Rejeição: Valor unitário do item da NF3e de 
ajuste é diferente do valor do item ajustado na 
NF3e anterior 
G83 - Acessar BD e verificar se a quantidade faturada (tag: 
detItemAnt/qFaturada) é igual à quantidade faturada 
do item da NF3e anterior. 
Facult. 263 Rej. Rejeição: Quantidade Faturada do item da 
NF3e de ajuste é diferente da quantidade 
faturada do item ajustado na NF3e anterior 
G84 - Acessar BD e verificar se o valor total do item (tag: 
detItemAnt/vProd) é igual ao valor total do item da 
NF3e anterior  
Facult. 264 Rej. Rejeição: Valor total do item da NF3e de ajuste 
é diferente do valor total do item ajustado na 
NF3e anterior 
G85 - Acessar BD e verificar se o código de classificação 
(tag: detItemAnt/cClass) é igual ao código de 
classificação do item da NF3-e anterior  
Facult. 265 Rej. Rejeição: Código de classificação do item da 
NF3e de ajuste é diferente do código de 
classificação do item ajustado na NF3e anterior 
G86 - Acessar BD e verificar se o valor da BC do ICMS 
(tag: detItemAnt/vBC) é igual ao valor da BC do ICMS 
do item da NF3e anterior  
Facult. 266 Rej. Rejeição: BC do ICMS do item da NF3e de 
ajuste é diferente do BC do ICMS do item 
ajustado na NF3e anterior 
G87 - Acessar BD e verificar se a alíquota do ICMS (tag: 
detItemAnt/pICMS) é igual a alíquota do ICMS do item 
da NF3e anterior  
Facult. 267 Rej. Rejeição: Alíquota do ICMS do item da NF3e 
de ajuste é diferente da alíquota do ICMS do 
item ajustado na NF3e anterior 
G88 - Acessar BD e verificar se o valor o ICMS (tag: 
detItemAnt/vICMS) é igual ao valor do ICMS do item 
da NF3e anterior  
Facult. 268 Rej. Rejeição: Valor do ICMS do item da NF3e de 
ajuste é diferente do valor do ICMS do item 
ajustado na NF3e anterior

## Página 12

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 12 / 13 
 
G89 - Acessar BD e verificar se o valor do PIS (tag: 
detItemAnt/vPIS) é igual ao valor do PIS do item da 
NF3e anterior  
Facult. 269 Rej. Rejeição: PIS do item da NF3e de ajuste é 
diferente do PIS do item ajustado na NF3e 
anterior 
G90 - Acessar BD e verificar se o valor do COFINS (tag: 
detItemAnt/vCOFINS) é igual ao valor do COFINS do 
item da NF3e anterior  
Facult. 270 Rej. Rejeição: COFINS do item da NF3e de ajuste é 
diferente do COFINS do item ajustado na NF3e 
anterior 
G91 - Acessar BD e verificar se o valor do PIS retido (tag: 
detItemAnt/vRetPIS) é igual ao valor do PIS retido do 
item da NF3e anterior 
Facult. 639 Rej. Rejeição: Valor do PIS retido da NF3e de 
ajuste é diferente do valor do PIS retido do 
item ajustado na NF3e anterior 
G92 - Acessar BD e verificar se o valor do COFINS retido 
(tag: detItemAnt/vRetCofins) é igual ao valor do 
COFINS retido do item da NF3e anterior 
Facult. 640 Rej. Rejeição: Valor do COFINS retido da NF3e de 
ajuste é diferente do valor do COFINS retido 
do item ajustado na NF3e anterior 
G93 - Acessar BD e verificar se o valor da CSLL retida 
(tag: detItemAnt/vRetCSLL) é igual ao valor da CSLL 
retida do item da NF3e anterior 
Facult. 641 Rej. Rejeição: Valor de CSLL retido da NF3e de 
ajuste é diferente do valor de CSLL retido do 
item ajustado na NF3e anterior 
G94 - Acessar BD e verificar se o valor do IRRF retido (tag: 
detItemAnt/vIRRF) é igual ao valor do IRRF retido do 
item da NF3e anterior 
Facult. 642 Rej. Rejeição: Valor do IRRF retido da NF3e de 
ajuste é diferente do valor do IRRF retido do 
item ajustado na NF3e anterior 
G95 - Acessar BD e verificar se o valor do FCP (tag: 
detItemAnt/vFCP) é igual ao valor do FCP do item da 
NF3e anterior 
Facult. 484 Rej. Rejeição: Valor do FCP da NF3e de ajuste é 
diferente do valor do FCP do item ajustado na 
NF3e anterior 
G96 - Acessar BD e verificar se o valor do ICMS ST (tag: 
detItemAnt/vICMSST) é igual ao valor do ICMS ST do 
item da NF3e anterior 
Facult. 485 Rej. Rejeição: Valor do ICMS ST da NF3e de ajuste 
é diferente do valor do ICMS ST do item 
ajustado na NF3e anterior 
G97 - Acessar BD e verificar se o valor do FCP ST (tag: 
detItemAnt/vFCPST) é igual ao valor do FCP ST do 
item da NF3e anterior 
Facult. 486 Rej. Rejeição: Valor do FCP ST da NF3e de ajuste 
é diferente do valor do FCP ST do item 
ajustado na NF3e anterior 
G98 - Acessar BD e verificar se o valor do PIS efetivo (tag: 
detItemAnt/vPISEfet) é igual ao valor do PIS efetivo 
do item da NF3e anterior 
Facult. 487 Rej. Rejeição: Valor do PIS Efetivo da NF3e de 
ajuste é diferente do valor do PIS Efetivo do 
item ajustado na NF3e anterior 
G99 - Acessar BD e verificar se o valor do COFINS efetivo 
(tag: detItemAnt/vCOFINSEfet) é igual ao valor do 
COFINS efetivo do item da NF3e anterior 
Facult. 488 Rej. Rejeição: Valor do COFINS Efetivo da NF3e de 
ajuste é diferente do valor do COFINS Efetivo 
do item ajustado na NF3e anterior 
G127 Se tipo da NF3e = 3 (Normal com Ajuste) (tag: 
finNF3e), total do ICMS difere do somatório dos 
valores dos itens menos o somatório dos valores de 
detItemAnt/vICMS. 
Facult. 449 Rej. Rejeição: Total do ICMS da NF3e de ajuste 
difere do somatório dos valores de ICMS dos 
itens, menos o somatório dos valores de ICMS 
dos itens de NF3e anteriores 
G158 Se tipo da NF3e = 3 (Normal com Ajuste) (tag: 
finNF3e): valor total da NF (vNF) difere do somatório 
de: 
 
(+) vProd 
(-) vRetPIS 
(-) vRetCofins 
(-) vRetCSLL 
(-) vIRRF 
(-) somatório dos detItemAnt/vProd 
 
Observação:  Nos casos em que houver ICMS-ST, o 
valor do ICMS-ST deve estar incluído no vProd 
Facult. 461 Rej. Rejeição: Total da NF3e de ajuste difere do 
somatório dos valores que compõe o valor total 
da NF3e ajuste 
G99a - Acessar BD e verificar se o indicador de devolução 
(tag: detItemAnt/indDevolucao) está igual ao item da 
NF3e anterior 
Facult 510 Rej. Rejeição: Indicador de devolução da NF3e de 
ajuste é diferente do informado no item 
ajustado na NF3e anterior 
No Evento de Cancelamento: 
# Regra de Validação Aplic. cStat Efeito Mensagem 
L07 Verificar se NF3e já está ajustada por outra Obrig
. 
299 Rej. Rejeição: NF3e já está ajustada na base de 
dados da SEFAZ. 
[nProt:999999999999999][dhAjuste: AAAA-MM-
DDTHH:MM:SS TZD]. 
L09 Rejeitar se o Tipo da NF3e = 3 (Normal com Ajustes) 
(tag: finNF3e) 
Obrig
. 
506 Rej. Rejeição: NF3e Normal com Ajustes não pode 
ser cancelada 
 
 
Outras alterações: 
 
 Evento do Fisco (240150): Interrupção definitiva da geração automática do evento "Autorizada NF3e de 
Ajuste". 
 Status de Consulta (110): Remoção do status "Ajuste de NF3e homologado" dos Web Services de 
Consulta Situação e portais públicos.

## Página 13

Projeto 
Nota Fiscal de Energia Elétrica Eletrônica - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 13 / 13
