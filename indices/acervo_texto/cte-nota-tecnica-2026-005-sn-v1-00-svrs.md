---
id: cte-nota-tecnica-2026-005-sn-v1-00-svrs
titulo: Nota Técnica 2026.005 - Simples Nacional
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-30'
documento_fiscal: CT-e/CT-e OS
url: https://dfe-portal.svrs.rs.gov.br/CTE/DownloadArquivoEstatico/?sistema=CTE&tipoArquivo=3&nomeArquivo=CTe_Nota_Tecnica_2026_005_SN_v1.00.pdf
arquivo_original: fontes/acervo/cte-nota-tecnica-2026-005-sn-v1-00-svrs.pdf
sha256_original: 5d3524903096bde91c7487b0d0a92d46f6e964d585fa32680fb91e8a0987da20
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 1fa1f24603661d98ace52b11b60eda7fb85a24863fd7eb0e73145f73a0f19e5f
---

## Página 1

Projeto Conhecimento de 
Transporte Eletrônico 
 
Nota Técnica 2026.005 – Simples Nacional 
Versão 1.00 de outubro de 2026

## Página 2

Projeto 
Conhecimento de Transporte Eletrônico – Simples Nacional 
NT 2026.005 v1.00 
 
Sumário  
 
Histórico de Alterações / Cronograma ............................................................................................ 3 
1 Introdução ................................................................................................................................ 3 
2 Orientações Gerais .................................................................................................................. 4 
2.1 Criação do campo tpRegimeIBSCBS .................................................................................... 4 
2.2. Orientação de preenchimento do grupo IBSCBS no fornecimento ....................................... 4 
3 Novo campo no grupo de identificação do Emitente ................................................................ 5 
4 Regras de Validação do Emitente ............................................................................................ 5 
5 Grupo de informações da composição do valor de IBS e CBS para SN................................... 5 
6 Regras de Validação do SN ..................................................................................................... 6 
7 Grupo de Totais do DFe (CTe Simplificado) ............................................................................ 9 
8 Evento de Tributação do Simples Nacional ............................................................................ 10 
9 Evento de Cancelamento da Tributação do Simples Nacional ............................................... 12 
10 Regra de Validação para CTe Complementar .................................................................... 12

## Página 3

Projeto 
Conhecimento de Transporte Eletrônico – Simples Nacional 
NT 2026.005 v1.00 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00 Criação de campos da tributação de IBS e da CBS no Simples Nacional 
 
26/10/2026 16/11/2026 
1.00 Aplicação da Regras de Validação desta NT 
 
16/11/2026 14/12/2026 
1.00 Evento de Tributação do SN Implementação 
Futura 
Implementação 
Futura 
1 Introdução 
Esta Nota Técnica tem por objetivo disciplinar as adequações adicionais nos leiautes do CTe, necessárias à 
implementação das disposições decorrentes da Reforma Tributária do Consumo, regulamentada pela Lei Complementar 
nº 214/2025, aplicáveis às operações realizadas por contribuintes optantes pelo Simples Nacional.  
 
As alterações apresentadas visam viabilizar a apuração assistida do Simples Nacional, por meio da captura estruturada, 
em nível de item do documento fiscal eletrônico, das informações indispensáveis ao cálculo da Receita Bruta do Simples 
Nacional (RBSN) e da receita bruta acumulada nos doze meses antecedentes ao mês anterior ao do período de apuração 
(RBT12), bem como ao cálculo do Imposto sobre Bens e Serviços (IBS) e da Contribuição sobre Bens e Serviços (CBS) 
no âmbito desse regime. 
 
Para atender a esse objetivo, esta Nota Técnica estabelece a inclusão de novos campos e regras de validação destinados 
a identificar:  
• a situação cadastral e o enquadramento do contribuinte no âmbito do Simples Nacional;  
• a adequada classificação tributária das operações para fins de incidência do IBS e da CBS;  
• informações do IBS e da CBS para tributação pelo Simples Nacional. 
 
Adicionalmente, esta Nota Técnica cria o evento fiscal específico denominado “Evento de Tributação do Simples 
Nacional” (tpEvent = 412140). Este evento será gerado automaticamente pela Administração Tributária, com a finalidade 
de apoiar ações de conformidade das informações fiscais.

## Página 4

Projeto 
Conhecimento de Transporte Eletrônico – Simples Nacional 
NT 2026.005 v1.00 
 
2 Orientações Gerais 
2.1 Criação do campo tpRegimeIBSCBS  
 
Os contribuintes do Simples Nacional (CRT = 1 ou 2) que tenham optado pelo Regime Regular do IBS/CBS devem 
informar: 
 tpRegimeIBSCBS = 1. 
 
Os contribuintes do Regime Normal (CRT = 3) que tenham solicitado opção pelo Simples Nacional e cujo pedido tenha 
sido indeferido, estando este indeferimento em discussão na esfera administrativa ou judicial, devem informar: 
 tpRegimeIBSCBS = 2, se for optante pendente do Simples Nacional (CRT = 1) e não optante do regime regular 
do IBS e da CBS; 
 tpRegimeIBSCBS = 3, se for optante pendente do Simples Nacional, excesso sublimite de receita bruta (CRT = 
2) e não optante do regime regular do IBS e da CBS; 
 tpRegimeIBSCBS = 4, se for optante pendente do Simples Nacional (vai migrar para CRT = 1 ou 2) e optante do 
regime regular do IBS e da CBS. 
Contribuintes nessa situação serão considerados, para todos os fins, como pertencentes ao regime regular. 
A tag não deve ser informada para situações diversas das mencionadas acima. 
2.2. Orientação de preenchimento do grupo IBSCBS no fornecimento 
O preenchimento das informações de tributação do IBS e da CBS serão conforme a tabela abaixo: 
Regime de Apuração do 
Emitente 
Como Preencher 
CRT tpRegimeIBSCBS gIBSCBS (*) gTribSN 
Simples Nacional com 
Regime Regular do 
IBS/CBS 
 
1 Informar “1” Informar: 
 - gIBSUF 
 - gIBSMun 
 - gCBS 
Não informar 
Simples Nacional, excesso 
sublimite de receita bruta 
com Regime Regular do 
IBS/CBS 
2 Informar “1” Informar: 
 - gIBSUF 
 - gIBSMun 
 - gCBS 
Não informar 
Simples Nacional sem 
Regime Regular do 
IBS/CBS 
 
1 Não informar Não informar Informar: 
 - gIBSSN 
 - gCBSSN 
Simples Nacional, excesso 
sublimite de receita bruta 
sem Regime Regular do 
IBS/CBS  
2 Não informar Informar:  
 - gIBSUF 
 - gIBSMun 
 - gCBS, com alíquota zerada 
Informar: 
 - gCBSSN 
Contribuinte do Regime 
Normal com opção 
pendente pelo CRT=”1-
simples Nacional” sem 
regime regular do IBS e da 
CBS 
3 Informar “2” Informar: 
 - gIBSUF 
 - gIBSMun 
 - gCBS 
Informar: 
 - gIBSSN 
 - gCBSSN 
Contribuinte do Regime 
Normal com opção 
pendente pelo CRT=”2-
Simples Nacional, excesso 
sublimite de receita bruta” 
sem regime regular do IBS 
e da CBS 
3 Informar “3” Informar: 
 - gIBSUF 
 - gIBSMun 
 - gCBS 
Informar: 
 - gCBSSN 
Contribuinte do Regime 
Normal com opção 
pendente pelo Simples 
Nacional (CRT=1 ou 2), 
com regime regular do IBS 
e da CBS 
3 Informar “4” Informar: 
 - gIBSUF 
 - gIBSMun 
 - gCBS 
Não informar 
 (*) informar o grupo gIBSCBS caso seja exigido pelo CST. 
O Simples Nacional - Microempreendedor Individual - MEI (CRT = 4) não deve informar o grupo IBSCBS.

## Página 5

3 Novo campo no grupo de identificação do Emitente 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 tpRegimeIBSCBS E emit C 0-1 1 Tipo de Regime de Apuração do IBS e da 
CBS 
1 - Contribuinte do Simples Nacional (CRT=1 ou 2) com 
opção pelo regime regular do IBS e da CBS; 
2 - Contribuinte do Regime Normal (CRT=3) com opção 
pendente pelo CRT=”1 - Simples Nacional” sem regime 
regular do IBS e da CBS; 
3 - Contribuinte do Regime Normal (CRT=3) com opção 
pendente pelo CRT=”2-Simples Nacional, excesso 
sublimite de receita bruta” sem regime regular do IBS e da 
CBS; 
4 - Contribuinte do Regime Normal (CRT=3) com opção 
pendente pelo Simples Nacional (CRT=1 ou 2), com regime 
regular do IBS e da CBS. 
4 Regras de Validação do Emitente 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 Se CRT do emitente for igual a 1 (Simples Nacional) ou 
2 (Simples Nacional, excesso sublimite) e a tag 
tpRegimeIBSCBS estiver informada: o valor DEVE ser 
igual a 1. 
Obrig. 1090 Rej. Rejeição: Tipo de Regime de Apuração incompatível 
com contribuinte Optante pelo Simples Nacional 
02 Se CRT do emitente for igual a 3 (Regime Normal) e a 
tag tpRegimeIBSCBS estiver informada: o valor DEVE 
ser igual a 2, 3 ou 4. 
Obrig. 1091 Rej. Rejeição: Tipo de Regime de Apuração incompatível 
com contribuinte do Regime Normal 
03 Se CRT do emitente for igual a 4 (MEI - 
Microempreendedor Individual): o campo 
tpRegimeIBSCBS NÃO DEVE ser informado. 
Obrig. 1092 Rej. Rejeição: Tipo de Regime de Apuração não deve ser 
informado para MEI 
5 Grupo de informações da composição do valor de IBS e CBS para SN 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 gTribSN G IBSCBS - 0-1  Grupo de informações da composição do valor do 
IBS e da CBS para o Simples Nacional 
2 gIBSSN G gTribSN - 0-1  Grupo de informações da composição do valor do 
IBS para o Simples Nacional 
3 pIBSSN E gIBSSN N 1-1 3v2-4 Alíquota efetiva do IBS para os Optantes do 
Simples 
Observação: nos anos de 2027 e 2028, no caso de 
Compra Governamental: 
   - Se tpEnteGov igual a ”1-União”, pIBSSN deve ser zero; 
   - Se tpEnteGov diferente de ”1-União”, pIBSSN deve ser 
a alíquota efetiva do Simples Nacional para o IBS. 
4 vIBSSN E gIBSSN N 1-1 13v2 Valor do IBS para os Optantes do Simples Nacional 
5 gCBSSN G gTribSN - 0-1  Grupo de informações da composição do valor da 
CBS para o Simples Nacional 
6 pCBSSN E gCBSSN N 1-1 3v2-4 Alíquota efetiva da CBS para os Optantes do 
Simples 
Observação: nos anos de 2027 e 2028, no caso de 
Compra Governamental: 
   - Se tpEnteGov igual a ”1-União”, pCBSSN deve ser a 
soma das alíquotas efetivas de IBS e CBS para o Simples 
Nacional; 
   - Se tpEnteGov diferente de ”1-União”, pCBSSN deve ser 
a alíquota efetiva do Simples Nacional para a CBS. 
7 vCBSSN E gCBSSN N 1-1 13v2 Valor do CBS para os Optantes do Simples 
Nacional

## Página 6

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 6 / 12 
 
 
6 Regras de Validação do SN 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 Se o CST informado possuir indicador que EXIGE 
preenchimento do grupo de informações específicas do 
IBS/CBS, este grupo DEVE estar informado (grupo: 
gIBSCBS) 
 
Exceção: Se o CRT informado pelo emitente for 1-
Simples Nacional, 2- Simples Nacional, excesso 
sublimite de receita bruta ou 4 -MEI, o grupo gIBSCBS 
NÃO será exigido 
 
Exceção: Esta RV não se aplica quando CRT=”1-
Simples Nacional” e tpRegimeIBSCBS não informado. 
Obrig 315 Rej. Rejeição: Grupo IBS/CBS deve ser preenchido para o 
CST informado 
02 Se CRT = 1 e tpRegimeIBSCBS NÃO estiver informado 
(Optante SN sem Regime Regular): 
– O grupo gIBSCBS NÃO DEVE ser informado. 
Obrig. 1100 Rej. Rejeição: Grupo de informações do IBS e CBS 
(gIBSCBS) NÃO PODE ser informado para optante 
sem regime regular  
03 Se CRT = 1 e tpRegimeIBSCBS NÃO estiver informado 
(Optante SN sem Regime Regular): 
– O grupo gTribSN DEVE ser informado, contendo 
obrigatoriamente os subgrupos gIBSSN e gCBSSN. 
Obrig. 1101 Rej. Rejeição: Grupo de tributação do Simples Nacional 
(gTribSN) obrigatório para optante sem regime 
regular  
04 Se CRT = 1 ou 2 com tpRegimeIBSCBS = 1 (Optante 
Regime Regular) OU CRT = 3 com tpRegimeIBSCBS = 
4 (Normal Pendente com Regime Regular): 
– O grupo gTribSN NÃO DEVE ser informado. 
Obrig. 1102 Rej. Rejeição: Grupo de tributação do Simples Nacional 
(gTribSN) não deve ser informado para contribuinte 
no regime regular  
05 VÁLIDA PARA 2026: 
Se informado grupo CBS (gCBS), a alíquota de CBS 
deverá ser de 0,90 % para documento com data de 
emissão no ano de 2026. (Art. 346 da LC 214/25) 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser 
igual a zero quando as condições abaixo forem 
atendidas: 
- Se CRT = 2 e tpRegimeIBSCBS NÃO estiver 
informado (Excesso Sublimite sem Regime Regular) 
- Código de Classificação do Produto (cClass) permitir 
alíquota zero para CBS em zona incentivada. 
- Município do Fato Gerador (cMunFG) e emitente 
devem pertencer a um município da ZFM 
Cod. IBGE Nome Município 
1302603 Manaus 
1303569 Rio Preto da Eva 
1301902 Itacoatiara 
 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 7

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 7 / 12 
 
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
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
EXCEÇÂO: Até que seja publicada a alíquota de 
referência da CBS para 2027, deverá ser informada a 
alíquota de 2026, inclusive para testes de simulação de 
2027 no AMBIENTE DE HOMOLOGAÇÃO (tpAmb=2), 
quando a alíquota de 2027 estiver publicada, ela 
também será aceita para testes ainda em 2026 
06 VÁLIDA A PARTIR de 2027: 
A alíquota da CBS (tag: pCBS) deve ser igual a 
alíquota vigente para o período conforme legislação. 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: Se o grupo gALCZFMCBS estiver 
preenchido, o pCBS deve ser igual a zero.  
Exceção 3:  Se CRT = 2 e tpRegimeIBSCBS NÃO 
estiver informado (Excesso Sublimite sem Regime 
Regular), o pCBS deve ser igual a zero 
Observação: Consultar Tabela de Alíquotas da CBS. 
IMPORTANTE: Somente serviços PRESENCIAIS 
podem utilizar o benefício da alíquota zero para Área 
Incentivada. 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida  
07 Se CRT = 2 e tpRegimeIBSCBS NÃO estiver informado 
(Excesso Sublimite sem Regime Regular): 
– O grupo gTribSN DEVE ser informado contendo o 
subgrupo gCBSSN  
Obrig. 1103 Rej. Rejeição: Para excesso de sublimite sem regime 
regular o grupo gCBSSN deve ser informado

## Página 8

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 8 / 12 
 
08 Se CRT = 2 e tpRegimeIBSCBS NÃO estiver informado 
(Excesso Sublimite sem Regime Regular): 
– O grupo gTribSN DEVE ser informado SEM 
INFORMAR o grupo gIBSSN  
Obrig. 1104 Rej. Rejeição: Para excesso de sublimite sem regime 
regular o grupo gIBSSN Não deve ser informado 
09 Se CRT = 3 e tpRegimeIBSCBS = 2 (Opção pendente 
CRT=1 sem regime regular): 
– O grupo gIBSCBS DEVE ser informado normalmente 
(respeitando o indicador de exigência de gIBSCBS no 
CST). 
– O grupo gTribSN DEVE ser informado contendo 
gIBSSN e gCBSSN. 
Obrig, 1105 Rej. Rejeição: Grupo gTribSN (com gIBSSN e gCBSSN) 
e gIBSCBS devem ser informados.  
10 Se CRT = 3 e tpRegimeIBSCBS = 3 (Opção pendente 
CRT=2 sem regime regular): 
– O grupo gIBSCBS DEVE ser informado normalmente 
(respeitando o indicador de exigência de gIBSCBS no 
CST). 
– O grupo gTribSN DEVE ser informado contendo 
apenas o subgrupo gCBSSN (o subgrupo gIBSSN 
NÃO DEVE ser informado). 
Obrig. 1106 Rej. Rejeição: Para opção pendente CRT=2, informar 
apenas gCBSSN no grupo gTribSN  
11 Se CRT = 4 (MEI - Microempreendedor Individual): 
– Os grupos gIBSCBS e gTribSN NÃO DEVEM ser 
informados no item. 
Obrig. 1107 Rej. Rejeição: Grupos gIBSCBS e gTribSN não devem 
ser preenchidos para MEI  
12 Se informado o grupo de Compra Governamental 
(ide/gCompraGov) com Ente da União (tpEnteGov = 1) 
para documento com data de emissão em 2027 ou 
2028 e informados gTribSN e gIBSSN: 
– A alíquota do IBS do Simples Nacional 
(gTribSN/gIBSSN/pIBSSN) deve ser igual a zero  
Obrig 1108 Rej. Rejeição: Alíquota do IBS do Simples Nacional deve 
ser zero para compras governamentais da União 
nos anos de 2027 e 2028  
13 Se informado o grupo de Compra Governamental 
(ide/gCompraGov) com Ente da União (tpEnteGov = 1) 
para documento com data de emissão em 2027 ou 
2028 e informados gTribSN e gIBSSN: 
– O valor do IBS SN ((gTribSN/gIBSSN/vIBSSN)) deve 
ser igual a 0,00 
Obrig 1109 Rej. Rejeição: Valor do IBS do Simples Nacional deve 
ser zero para compras governamentais da União 
nos anos de 2027 e 2028

## Página 9

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 9 / 12 
 
7 Grupo de Totais do DFe (CTe Simplificado) 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 gTribSN G IBSCBSTot - 0-1  Grupo de informações de totais do IBS e da CBS 
para o Simples Nacional 
4 vIBSSN E gTribSN N 1-1 13v2 Valor Total do IBS para os Optantes do Simples 
Nacional 
7 vCBSSN E gTribSN N 1-1 13v2 Valor Total do CBS para os Optantes do Simples 
Nacional 
 
  
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O grupo total da tributação do Simples Nacional 
deverá ser informado se pelo menos um dos itens 
apresentar o grupo gTribSN (IBSCBS\gTribSN) 
Obrig. 1110 Rej. Rejeição: Total de Tributação SN deve ser informada 
se existir tributação de Simples Nacional no 
documento 
02 O total de IBS SN (Se informando) deverá ser a 
soma do campo vIBSSN informados nos itens 
Obrig. 1111 Rej. Rejeição: Total de IBS SN difere da soma dos itens 
03 O total do CBS SN (Se informando) deverá ser a 
soma do campo vCBSSN informados nos itens 
Obrig. 1112 Rej. Rejeição: Total de CBS SN difere da soma dos itens

## Página 10

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 10 / 12 
 
8 Evento de Tributação do Simples Nacional 
O evento “Tributação do Simples Nacional” (tpEvent = 412140) será gerado automaticamente pela Administração 
Tributária, com base nos DFe recebidos e emitidos por contribuintes enquadrados no Simples Nacional ou por 
contribuintes do Regime Normal que estejam com a opção pelo Simples Nacional pendente. O CGIBS e a RFB 
usarão os mesmos algoritmos para cálculo dos tributos e verificação de conformidade, tendo como referência inicial 
as regras implementadas na calculadora de tributos. 
 
Função: Evento gerado pela administração tributária contendo informações relativas à tributação do Simples 
Nacional para fins de análise da conformidade da composição da receita bruta, dos valores dos tributos informados 
e da eventual necessidade de constituição de crédito tributário. 
 
Autor do Evento: Administração Tributária 
 
Código do Tipo de Evento: 412140 
 
Schema XML: evTributacaoSN_v9.99.xsd 
  #  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# evTribSN Raiz detEvento G 1-1  Schema XML de validação do evento de 
Tributação do SN 412140 
1 descEvento E evTribSN E 1-1 30 Descrição do Evento - “Tributação do 
Simples Nacional” 
2 nProt E evTribSN E 1-1 15 Número do protocolo de autorização do 
DFe 
3 gTribItemSN G evTribSN  1-990  Detalhamento dos tributos. 
Observação: Para CTe e CTeOS será 
gerado apenas um item 
Para CTe Simplificado a mesma qtd de 
viagens declaradas com tributação.  
4 nItem A gTribItemSN N 1 - 1 1 - 3 Número do item (1-990) 
5 vRBSNitem E gTribItemSN N 1 - 1 13v2 Valor da receita bruta do Simples Nacional 
atribuída ao item 
Se item tributável, RBSNitem = vTPrest  
6 tpRBSN E gTribItemSN N 1 - 1 1 Tipo de Receita Bruta do Simples Nacional 
referente ao cClassTrib do item 
0 - Não é receita bruta 
1 - Receita bruta - interna 
2 - Receita bruta - interna sem cálculo de 
IBS e CBS 
3 - Receita bruta – exportação direta 
4 - Receita bruta - exportação indireta 
5 - Receita bruta - mercado interno e 
exportação 
9 - Fornecimento incompatível com SN 
7 pIBSSN E gTribItemSN N 0 - 1 3v2-4 Alíquota aplicável de cálculo do IBS 
referente ao item 
 
8 vIBSSN E gTribItemSN N 0 - 1 13v2 Valor do IBS devido pelo Simples 
Nacional. 
9 pCBSSN E gTribItemSN N 0 - 1 3v2-4 Alíquota aplicável de cálculo da CBS 
referente ao item

## Página 11

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 11 / 12 
 
10 vCBSSN E gTribItemSN N 0 - 1 13v2 Valor da CBS devida pelo Simples 
Nacional. 
11 vIBSPendSusp E gTribItemSN N 0 - 1 13v2 Valor do IBS pendente ou suspenso 
referente ao item 
 
12 vCBSPendSusp E gTribItemSN N 0 - 1 13v2 Valor da CBS pendente ou suspenso 
referente ao item. 
13 gTotalSN G evTribSN - 1-1 - Totais do CTe 
14 vRBSNtot E gTotalSN N 1 - 1 13v2 Valor total da receita bruta do Simples 
Nacional, correspondente ao somatório 
dos valores atribuídos aos itens do DFe 
 
15 vIBSSNtot E gTotalSN N 0 - 1 13v2 Valor total do IBS devido pelo Simples 
Nacional apurado no documento 
16 vIBSSNtotPendSusp E gTotalSN N 0 - 1 13v2 Valor total do IBS devido pelo Simples 
Nacional cuja apropriação encontra-se 
pendente ou com exigibilidade suspensa 
17 vCBSSNtot E gTotalSN N 0 - 1 13v2 Valor total da CBS devida pelo Simples 
Nacional apurada no documento 
18 vCBSSNtotPendSusp E gTotalSN N 0 - 1 13v2 Valor total da CBS devida pelo Simples 
Nacional

## Página 12

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2026.005 v1.00 
 
 
Página 12 / 12 
 
9 Evento de Cancelamento da Tributação do Simples Nacional 
Função: Evento para indicar o cancelamento de um evento de Tributação do Simples Nacional nas ocasiões em que ocorrer 
erro na geração do evento. 
Autor do Evento: Administração Tributária 
 
Código do Tipo de Evento: 412141 (Este evento exige existência do DFe em situação autorizado) 
 
Schema XML: evCancTribSN_v9.99.xsd 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
IP01 evCancTribSN G - - - - TAG raiz  
IP02 descEvento E IP01 C 1-1 46 Descrição do Evento: “Cancelamento da 
Tributação do Simples Nacional”  
IP03 nProt E IP01 N 1-1 15 Informar o número do protocolo de autorização do 
DFe  
IP04 nProtEvTribSN E IP01 N 1-1 15 Informar o número do protocolo de autorização do 
evento de tributação do SN que será cancelado  
 
10 Regra de Validação para CTe Complementar 
Se Tipo do CTe=1 (Complementar) e emitente com CRT 
1=Simples Nacional OU 2 = Simples Nacional, excesso 
sublimite de receita bruta OU 3 = Regime Normal com 
indicador de SN Pendente (tag tpRegimeIBSCBS = 2) 
OU CRT 4=Simples Nacional - Microempreendedor 
Individual – MEI: 
 
Quando Informados múltiplos CTes para serem 
complementados 
- Chaves de acesso dos CTes complementados com 
ano e mês de emissão diferentes. 
Obrig. 909 Rej. Rejeição: As chaves de acesso de todos os CTes 
complementados devem corresponder ao mesmo 
período (ano e mês).
