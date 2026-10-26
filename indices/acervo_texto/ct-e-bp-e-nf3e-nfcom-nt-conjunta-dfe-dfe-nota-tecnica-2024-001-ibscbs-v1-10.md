---
id: ct-e-bp-e-nf3e-nfcom-nt-conjunta-dfe-dfe-nota-tecnica-2024-001-ibscbs-v1-10
titulo: DFe - Nota Técnica 2024.001.v.1.10 - IBS/CBS - Publicada em 11/12/24
tipo: nota.tecnica
versao: '1.10'
data: '2024-12-11'
documento_fiscal: CT-e/BP-e/NF3e/NFCom (NT conjunta DFe)
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=OK31wgvsgf0=
arquivo_original: fontes/acervo/ct-e-bp-e-nf3e-nfcom-nt-conjunta-dfe-dfe-nota-tecnica-2024-001-ibscbs-v1-10.pdf
sha256_original: 43bcdb9d4040978900a235ea1f7d9f04c5a62ce2c01ca469478a9e537554cf7c
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 8d7ec693addc7fe02c0770d5ecd401f434f15a8ec19948e09744b9c0630f87d2
---

## Página 1

Projeto Reforma Tributária do 
Consumo – Adequação DFe 
 
Nota Técnica 2024.001 
Versão 1.10 de 06 de dezembro de 2024

## Página 2

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 2 / 16 
 
Sumário 
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Tipos básicos da tributação ............................................................................................. 4 
3 Alteração do leiaute dos DFe .......................................................................................... 5 
4 Código de Classificação Tributária do IBS/CBS .............................................................. 7 
5 Validações dos campos do IBS e CBS ............................................................................ 7 
6 Grupo de totais do DFe ................................................................................................. 11 
7 Regras de Validação do Grupo de Totais IBS e CBS .................................................... 11 
8 Total Geral do Documento Fiscal Eletrônico ................................................................. 12 
9 Anexo – Novos Grupos para Reforma Tributária ........................................................... 13 
Conhecimento de Transporte Eletrônico– modelo 57 ........................................................ 13 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 ................................... 14 
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67 ........................... 14 
Bilhete de Passagem Eletrônico – Modelo 63 ................................................................... 15 
Bilhete de Passagem Eletrônico Transporte Metropolitano – Modelo 63........................... 15 
Nota Fiscal de Energia Elétrica Eletrônica – Modelo 66 .................................................... 16 
Nota Fiscal Fatura de Comunicação Eletrônica – Modelo 62 ............................................ 16

## Página 3

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 3 / 16 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Previsão das informações do IBS/CBS nos DFe   
1.10  Atualização da documentação e leiaute 01/09/2025 31/10/2025

## Página 4

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 4 / 16 
 
1 Introdução 
O Projeto de Lei Complementar Federal PLP 68, aprovado na Câmara dos Deputados e encaminhado para 
aprovação junto ao Senado federal, definiu na Seção VIII – Disposições transitórias, Art. 61, a obrigatoriedade para 
Estados, o Distrito Federal e os Municípios adaptarem os sistemas autorizadores de Documentos Fiscais 
Eletrônicos (DFe) vigentes para utilização de leiaute padronizado, que permita aos contribuintes informarem os 
dados relativos ao Imposto sobre Bens e Serviços (IBS), Contribuição sobre Bens e Serviços (CBS) e Imposto 
Seletivo (IS).  
 
Como as infraestruturas autorizadoras de Documentos Fiscais Eletrônicos (DFe) das Unidades Federadas e 
Municípios, além das aplicações e sistemas dos contribuintes, necessitam de, no mínimo, 1 ano para o 
desenvolvimento das alterações necessárias, estamos divulgando esta Nota Técnica (NT) para implantação, em 
produção, a partir do dia 31/10/2025, de forma a entrar em efetiva operacionalização a partir 01/01/2026.  
 
Como as discussões envolvendo a implantação da Reforma Tributária ainda estão em curso, esclarecemos que 
esta NT será ajustada ao longo do seu processo de execução, da mesma forma como ocorre com as demais NT 
já implementadas. 
 
A NT modifica o leiaute dos DFe, inserindo os grupos e campos opcionais relacionados a tributação do IBS, CBS 
e IS, em atendimento as alterações previstas na Emenda Constitucional 132 de 20 de dezembro de 2023, para 
implementação da Reforma Tributária. 
 
Esta documentação descreve as alterações aplicadas aos Documentos: 
 Conhecimento de Transporte Eletrônico (modelo 57); 
 Conhecimento de Transporte Eletrônico para Outros Serviços (modelo 67); 
 Bilhete de Passagem Eletrônico (modelo 63); 
 Nota Fiscal de Energia Elétrica Eletrônica (modelo 66); 
 Nota Fiscal Fatura de Serviço de Comunicação Eletrônica (modelo 62). 
 
Observação: A Nota Fiscal Eletrônica (modelo 55), juntamente com a Nota Fiscal de Consumidor Eletrônica 
(modelo 65) serão tratadas em Nota Técnica específica. 
 
IMPORTANTE: Durante essa fase inicial, esta será uma NT conjunta para CTe, BPe, NF3e e NFCom. A versão 
final desta documentação deverá originar NT´s específicas de cada um desses DFe. 
 
2 Tipos básicos da tributação 
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos, esta NT introduz o arquivo 
DFeTiposBasicos_v1.00.xsd ao conjunto dos arquivos que compõem do schema da DFe. 
 
Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro das 
informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no leiaute padrão da DFe 
conforme estrutura abaixo:

## Página 5

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 5 / 16 
 
 
3 Alteração do leiaute dos DFe 
Este grupo de informações facultativas deve ser adicionado a cada item do DFe, em caso de DFe apresentar itens 
(NF3e/NFCom); ou no corpo do DFe quando este não possui itens (CTe/BPe). 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBS G imposto / imp  
<ver anexo> 
- 0-1 - Grupo de informações da Tributação IBS/CBS 
1 CST E IBSCBS N 1-1 3 Código da Situação Tributária do IBS/CBS 
2 cClassTrib E IBSCBS N 1-1 6 Código da Classificação Tributária do IBS/CBS 
3 gIBSCBS G IBSCBS - 0-1 - Grupo de informações específicas do IBS/CBS 
4 vBC E gIBSCBS N 1-1 13,2 Valor da Base de cálculo comum a IBS/CBS 
5 gIBSUF G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
das Unidades Federadas 
6 pIBSUF E gIBSUF N 1-1 3,2/3,4 Aliquota do IBS Estadual 
7 Sequência XML - gIBSUF - 0-1 - - 
8 vTribOp E gIBSUF N 1-1 13,2 Valor do Tributo Bruto na operação 
9 gDif G gIBSUF - 0-1 - Grupo de campos do diferimento 
10 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
11 vDif E gDif N 1-1 13,2 Valor do diferimento 
12 gDevTrib G gIBSUF - 0-1 - Grupo de informações da devolução de tributos 
13 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
14 gRed G gIBSUF - 0-1 - Grupo de informações da redução de aliquota 
15 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
16 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo 
17 gDeson G gIBSUF - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
18 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
19 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
20 vBC E gDeson N 0-1 13,2 Base de calculo (igual ao do elemento anterior) 
21 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem desoneração 
22 vDeson E gDeson N 1-1 13,2 Valor da desoneraçao.  
Não é descontado do valor do IBS. 
23 vIBSUF E gIBSUF N 1-1 13,2 Valor do IBS de competência da UF 
24 gIBSMun G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
do municipio 
25 pIBSMun E gIBSMun N 1-1 3,2/3,4 Aliquota do IBS Municipal 
26 Sequência XML - gIBSMun - 0-1 - - 
27 vTribOp E gIBSMun N 1-1 13,2 Valor do Tributo Bruto na operação 
28 gDif G gIBSMun - 0-1 - Grupo de campos do diferimento 
29 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
30 vDif E gDif N 1-1 13,2 Valor do diferimento 
31 gDevTrib G gIBSMun - 0-1 - Grupo de informações da devolução do tributo

## Página 6

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 6 / 16 
 
32 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
33 gRed G gIBSMun - 0-1 - Grupo de informações da redução de aliquota 
34 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
35 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo 
36 gDeson G gIBSMun - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
37 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
38 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
39 vBC E gDeson N 0-1 13,2 Base de calculo (igual do elemento anterior) 
40 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem desoneração 
41 vDeson E gDeson N 1-1 13,2 Valor da desoneração 
42 vIBSMun E gIBSMun N 1-1 13,2 Valor do IBS de competência do município 
43 gCBS G gIBSCBS - 1-1 - Grupo de informações da CBS 
44 pCBS E gCBS N 1-1 3,2/3,4 Aliquota da CBS 
45 Sequência XML - gCBS - 0-1 - - 
46 vTribOp E gCBS N 1-1 13,2 Valor do Tributo Bruto na operação 
47 gDif G gCBS - 0-1 - Grupo de campos do diferimento 
48 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
49 vDif E gDif N 1-1 13,2 Valor do diferimento 
50 gDevTrib G gCBS - 0-1 - Grupo de informações da devolução do tributo 
51 vDevTrib E gDevTrib N 1-1 13,2 Valor da CBS devolvida.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
52 gRed G gCBS - 0-1 - Grupo de informações da redução de aliquota 
53 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
54 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva da CBS que será aplicada a base de 
cálculo 
55 gDeson G gCBS - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
56 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
57 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
58 vBC E gDeson N 0-1 13,2 Base de calculo (igual do elemento anterior) 
59 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem a desoneração 
60 vDeson E gDeson N 1-1 13,2 Valor da desoneração 
51 vCBS E gCBS N 1-1 13,2 Valor da CBS 
52 gIBSCredPres G gIBSCBS - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento.  
53 cCredPres E gIBSCredPres N 1-1  Código do Crédito Presumido (ver Tabela) 
 
54 pCredPres E gIBSCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido

## Página 7

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 7 / 16 
 
55 vCredPres CE gIBSCredPres N 1-1 13,2 Valor do crédito presumido 
56 vCredPresCondSus CE gIBSCredPres N 1-1 13,2 Valor do Crédito Presumido Condição Suspensiva 
Preencher apenas para cCredPres com indicacao 
de Condição Suspensiva 
57 gCBSCredPres G gIBSCBS - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento.  
58 cCredPres E gCBSCredPres N 1-1  Código do Crédito Presumido (ver Tabela) 
 
59 pCredPres E gCBSCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
60 vCredPres CE gCBSCredPres N 1-1 13,2 Valor do crédito presumido 
61 vCredPresCondSus CE gCBSCredPres N 1-1 13,2 Valor do Crédito Presumido Condição Suspensiva 
Preencher apenas para cCredPres com indicacao 
de Condição Suspensiva 
 
4 Código de Classificação Tributária do IBS/CBS 
O grupo de informações do IBS, CBS e IS associado aos itens do documento fiscal contém o Código de Situação 
Tributária (CST) e Código de Classificação Tributária (cClassTrib) do IBS, CBS e IS. O Informe Técnico RT 
2024.001 divulga a publicação da tabela com esta codificação, que está disponível no Portal Nacional da NF-e 
(www.nfe.fazenda.gov.br), na aba “Documentos”, opção “Diversos” e no portal dos Documentos Fiscais Eletrônicos 
(dfe-portal.svrs.rs.gov.br).  
 
Cada código “cClassTrib” corresponde a um dispositivo específico do PLP68, tornando objetiva a informação do 
contribuinte sobre como interpreta que é realizada a tributação do IBS e da CBS para cada item do DFe (para DFe 
que possuem itens).  
 
A tabela também contém indicadores que vinculam de forma dinâmica códigos “CST-IBS/CBS” e “cClassTrib” com 
as Regras de Validação descritas na RT Nota Técnica 2024.002 - IBS/CBS, ou que contêm informações 
necessárias para a preparação das apurações assistidas do IBS e da CBS, em atendimento ao disposto no PLP68.  
 
Caso a versão final aprovada pelo Congresso Nacional altere algum dos dispositivos do PLP68, a tabela será 
alterada para refletir esta modificação. Da mesma maneira, a tabela poderá sofrer alterações em virtude de 
aperfeiçoamentos, novidades introduzidas em sede de Regulamento, ou para atender a necessidades 
relacionadas com a apuração assistida do IBS e da CBS.  
5 Validações dos campos do IBS e CBS 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se CST do IBS/CBS for informado, este deve existir na 
tabela de Código de Situação Tributária (tag: 
gTribIBSCBS/CST) 
Obrig. 310 Rej. Rejeição: CST informado inexistente 
002 Se cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gTribIBSCBS/cClassTrib) 
Obrig. 311 Rej. Rejeição: Classificação Tributária informada 
inexistente 
003 Verificar se o CST informado é compatível com o 
cClassTrib 
Obrig. 312 Rej. Rejeição: Classificação Tributária incompatível com 
o CST informado 
004 Se o CST informado VEDAR preenchimento do grupo 
de informações específicas do IBS/CBS, este grupo 
NÂO DEVE estar informado (grupo: gIBSCBS) 
Obrig 313 Rej. Rejeição: Grupo IBS/CBS não deve ser preenchido 
para o CST informado

## Página 8

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 8 / 16 
 
005 Se o CST informado EXIGIR preenchimento do grupo 
de informações específicas do IBS/CBS, este grupo 
DEVE estar informado (grupo: gIBSCBS) 
Obrig 314 Rej. Rejeição: Grupo IBS/CBS deve ser preenchido para o 
CST informado 
006 Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor do IBS (vIBSUF) deverá ser resultante da Base 
de Cálculo x Alíquota (vBC x pIBSUF) 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Obrig. 315 Rej. Rejeição: Valor do IBS UF diferente de Base de 
Cálculo x Alíquota 
007 Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor do Tributo Bruto da Operação (vTribOp) deverá 
ser resultante da Base de Cálculo x Alíquota vigente da 
UF (ver tabela de alíquotas Estaduais) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig; 316 Rej. Rejeição: Valor do Tributo Bruto da Operação 
diferente da Base de Cálculo x Alíquota vigente da 
UF 
008 Se CST informado exigir informação de Diferimento 
para o IBS Estadual, o grupo gDif deve estar informado 
Obrig. 317 Rej. Rejeição: CST informado obriga informação de 
diferimento Estadual 
009 Se informado grupo do Diferimento (gIBSUF/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 318 Rej. Rejeição: Valor do Diferimento da UF diferente de 
Base de Cálculo x Percentual 
010 Se CST informado exigir informação de Desoneração 
para o IBS Estadual, o grupo gDeson deve estar 
informado 
Obrig. 319 Rej. Rejeição: CST informado obriga informação da 
desoneração 
011 Se informado grupo da desoneração (gIBSUF/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 320 Rej. Rejeição: CST informado na desoneração 
inexistente 
012 Se informado grupo da desoneração (gIBSUF/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 321 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
013 Se informado grupo da desoneração (gIBSUF/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos  
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 322 Rej. Rejeição: Valor Desonerado da UF diferente de 
Base de Cálculo x Alíquota 
014 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do IBS (vIBSMun) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pIBSMun) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 323 Rej. Rejeição: Valor do IBS Municipal diferente de Base de 
Cálculo x Alíquota 
015 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do Tributo Bruto da Operação (vTribOp) 
deverá ser resultante da Base de Cálculo x Alíquota 
vigente do Município (ver tabela de alíquotas 
Municipais) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig; 324 Rej. Rejeição: Valor do Tributo Bruto da Operação 
diferente da Base de Cálculo x Alíquota vigente do 
Município 
016 Se CST informado exigir informação de Diferimento 
para o IBS Municipal, o grupo gDif deve estar 
informado 
Obrig. 325 Rej. Rejeição: CST informado obriga informação de 
diferimento Municipal 
017 Se informado grupo do Diferimento (gIBSMun/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Obrig. 326 Rej. Rejeição: Valor do Diferimento do Município diferente 
de Base de Cálculo x Percentual

## Página 9

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 9 / 16 
 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
018 Se CST informado exigir informação de Desoneração 
para o IBS Municipal, o grupo gDeson deve estar 
informado 
Obrig. 327 Rej. Rejeição: CST informado obriga informação da 
desoneração 
019 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 328 Rej. Rejeição: CST informado na desoneração inexistente 
020 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 329 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
021 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Aliquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 330 Rej. Rejeição: Valor Desonerado do Município diferente de 
Base de Cálculo x Alíquota 
022 Se informado grupo CBS (gCBS): 
O valor do CBS (vCBS) deverá ser resultante da Base 
de Cálculo x Alíquota (vBC x pCBS) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 331 Rej. Rejeição: Valor do CBS diferente de Base de Cálculo 
x Alíquota 
023 Se informado grupo CBS (gCBS): 
O valor do Tributo Bruto da Operação (vTribOp) 
deverá ser resultante da Base de Cálculo x Alíquota 
vigente da CBS  
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig; 332 Rej. Rejeição: Valor do Tributo Bruto da Operação 
diferente da Base de Cálculo x Alíquota vigente da 
CBS 
024 Se CST informado exigir informação de Diferimento 
para o CBS, o grupo gDif deve estar informado 
Obrig. 333 Rej. Rejeição: CST informado obriga informação de 
diferimento do CBS 
025 Se informado grupo do Diferimento (gCBS/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 334 Rej. Rejeição: Valor do Diferimento do CBS diferente de 
Base de Cálculo x Percentual 
026 Se CST informado exigir informação de Desoneração 
para a CBS, o grupo gDeson deve estar informado 
Obrig. 335 Rej. Rejeição: CST informado obriga informação da 
desoneração 
027 Se informado grupo da desoneração (gCBS/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 336 Rej. Rejeição: CST informado na desoneração inexistente 
028 Se informado grupo da desoneração (gCBS/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 337 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
029 Se informado grupo da desoneração (gCBS/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 338 Rej. Rejeição: Valor Desonerado da CBS diferente de 
Base de Cálculo x Alíquota 
030 Se CST informado exigir informação de Crédito 
Presumido para o IBS, o grupo gIBSCredPres deve 
estar informado 
Obrig. 339 Rej. Rejeição: CST informado obriga informação de 
crédito presumido para o IBS

## Página 10

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 10 / 16 
 
031 Se informado grupo do crédito presumido 
(gIBSCredPres): 
O valor do cCredPres deve existir na tabela de 
códigos de crédito presumido 
Obrig. 340 Rej. Rejeição: Código de crédito presumido do IBS 
inexistente 
032 Se o cCredPres do IBS possuir indicação de Condição 
Suspensiva e a tag vCredPresCondSus não estiver 
informada 
Obrig. 341 Rej. Rejeição: O valor do crédito presumido (condição 
suspensiva) para o IBS deve ser informado 
033 Se o cCredPres do IBS NÂO possuir indicação de 
Condição Suspensiva e a tag vCredPres não estiver 
informada 
Obrig. 342 Rej. Rejeição: O valor do crédito presumido para o IBS 
deve ser informado 
034 Se informado grupo do crédito presumido 
(gIBSCredPres) COM Condição Suspensiva: 
O valor do Crédito Presumido Condição Suspensiva 
(vCredPresCondSus) deverá ser resultante da Base 
de Cálculo x Percentual do Crédito Presumido (vBC x 
pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 343 Rej. Rejeição: Valor do Crédito Presumido Condição 
Suspensiva de IBS diferente de Base de Cálculo x 
Percentual 
035 Se informado grupo do crédito presumido 
(gIBSCredPres) SEM Condição Suspensiva: 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 344 Rej. Rejeição: Valor do Crédito Presumido de IBS 
diferente de Base de Cálculo x Percentual 
031 Se informado grupo do crédito presumido 
(gCBSCredPres): 
O valor do cCredPres deve existir na tabela de 
códigos de crédito presumido 
Obrig. 345 Rej. Rejeição: Código de crédito presumido da CBS 
inexistente 
032 Se o cCredPres da CBS possuir indicação de 
Condição Suspensiva e a tag vCredPresCondSus não 
estiver informada 
Obrig. 346 Rej. Rejeição: O valor do crédito presumido (condição 
suspensiva) para a CBS deve ser informado 
033 Se o cCredPres da CBS NÂO possuir indicação de 
Condição Suspensiva e a tag vCredPres não estiver 
informada 
Obrig. 347 Rej. Rejeição: O valor do crédito presumido para a CBS 
deve ser informado 
032 Se informado grupo do crédito presumido 
(gCBSCredPres) COM Condição Suspensiva: 
O valor do Crédito Presumido Condição Suspensiva 
(vCredPresCondSus) deverá ser resultante da Base 
de Cálculo x Percentual do Crédito Presumido (vBC x 
pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 348 Rej. Rejeição: Valor do Crédito Presumido Condição 
Suspensiva de CBS diferente de Base de Cálculo x 
Percentual 
032 Se informado grupo do crédito presumido 
(gCBSCredPres) SEM Condição Suspensiva: 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 349 Rej. Rejeição: Valor do Crédito Presumido de CBS 
diferente de Base de Cálculo x Percentual

## Página 11

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 11 / 16 
 
6 Grupo de totais do DFe 
Para NF3e, NFCom e BPe TM, no grupo total do DFe deverá ser adicionado o grupo de totais do IBS/CBS. 
Para CTe, CTe Simplificado, CTeOS e BPe não será criado esse grupo de totais do IBS/CBS. 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBSTot G total - 0-1 - Grupo de informações para apuração do IBS e 
CBS declarado pelo contribuinte 
1 vBCCIBS E gTotIBSCBS N 1-1 13,2 Total da Base de cálculo do IBS/CBS 
2 gIBS G gIPA - 1-1 - Totalização do IBS 
3 gIBSUFTot G gIBS - 1-1 - Total do IBS das UF 
4 vDif E gIBSUFTot N 1-1 13,2 Total do Diferimento 
5 vDevTrib E gIBSUFTot N 1-1 13,2 Total de Devolução de Tributo IBS UF 
6 vDeson E gIBSUFTot N 1-1 13,2 Total desonerado do IBS UF 
7 vIBSUF E gIBSUFTot N 1-1 13,2 Total do IBS UF 
8 gIBSMunTot G gIBS - 1-1 - Total do IBS dos Municípios 
9 vDif E gIBSMunTot N 1-1 13,2 Total do Diferimento 
10 vDevTrib E gIBSMunTot N 1-1 13,2 Total de Devolução de Tributo IBS Municipal 
11 vDeson E gIBSMunTot N 1-1 13,2 Total desonerado do IBS Municipal 
12 vIBSMun E gIBSMunTot N 1-1 13,2 Total do IBS Municipal 
13 vCredPres E gIBS N 1-1 13,2 Total do Crédito Presumido 
14 vCredPresCondSus E gIBS N 1-1 13,2 Total do Crédito Presumido Condição Suspensiva 
15 vIBSTot E gIBS N 1-1 13,2 Total do IBS (IBS UF + IBS Mun) 
16 gCBS G gIPA - 1-1 - Total do CBS 
17 vDif E gCBS N 1-1 13,2 Total do Diferimento 
18 vDevTrib E gCBS N 1-1 13,2 Total de Devolução do tributo CBS 
19 vDeson E gCBS N 1-1 13,2 Total desonerado do tributo CBS 
20 vCredPresCondSus E gCBS N 1-1 13,2 Total do Crédito Presumido Condição Suspensiva 
21 vCBS E gCBS N 1-1 13,2 Total do CBS 
7 Regras de Validação do Grupo de Totais IBS e CBS 
Aplicável apenas para NF3e, NFCom e BPe TM. 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 O grupo de totais do IBS e CBS (IBSCBSTot) só 
deve ser informado se existir pelo menos uma 
ocorrência de IBS/CBS nos itens 
Obrig. 350 Rej. Rejeição: Total de IBS/CBS só deve ser informado 
se existir IBS/CBS declarado nos itens do DFe 
002 O total do Diferimento do IBS UF deverá ser a 
soma do campo vDif do IBS UF informados nos 
itens 
Obrig. 351 Rej. Rejeição: Total de Diferimento do IBS UF difere da 
soma dos itens 
003 O total Devolvido do IBS UF deverá ser a soma do 
campo vDevTrib do IBS UF informados nos itens 
Obrig. 352 Rej. Rejeição: Total Devolvido do IBS UF difere da soma 
dos itens 
004 O total Desonerado do IBS UF deverá ser a soma 
do campo vDeson do IBS UF informados nos itens 
Obrig. 353 Rej. Rejeição: Total Desonerado do IBS UF difere da 
soma dos itens 
005 O total do IBS UF deverá ser a soma do campo 
vIBSUF informados nos itens 
Obrig. 354 Rej. Rejeição: Total de IBS UF difere da soma dos itens

## Página 12

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 12 / 16 
 
006 O total do Diferimento do IBS Municipal deverá ser 
a soma do campo vDif do IBS Municipal 
informados nos itens 
Obrig. 355 Rej. Rejeição: Total de Diferimento do IBS Municipal 
difere da soma dos itens 
007 O total Devolvido do IBS Municipal deverá ser a 
soma do campo vDevTrib do IBS Municipal 
informados nos itens 
Obrig. 356 Rej. Rejeição: Total Devolvido do IBS Municipal difere da 
soma dos itens 
008 O total do IBS Municipal deverá ser a soma do 
campo vIBSMun informados nos itens 
Obrig. 357 Rej. Rejeição: Total de IBS Municipal difere da soma dos 
itens 
009 O total Desonerado do IBS Municipal deverá ser a 
soma do campo vDeson do IBS Municipal 
informados nos itens 
Obrig. 358 Rej. Rejeição: Total Desonerado do IBS Municipal difere 
da soma dos itens 
010 O Total do IBS deverá ser a soma do IBS das UF 
e do IBS Municipal (vIBSUF + vIBSMun) 
Obrig. 359 Rej. Rejeição: Total do IBS difere da soma do IBS UF e 
IBS Municipal 
011 O total do Diferimento do CBS deverá ser a soma 
do campo vDif do CBS informados nos itens 
Obrig. 360 Rej. Rejeição: Total de Diferimento do CBS difere da soma 
dos itens 
012 O total Devolvido do CBS deverá ser a soma do 
campo vDevTrib do CBS informados nos itens 
Obrig. 361 Rej. Rejeição: Total Devolvido do CBS difere da soma dos 
itens 
013 O total Desonerado do CBS deverá ser a soma do 
campo vDeson do CBS informados nos itens 
Obrig. 362 Rej. Rejeição: Total Desonerado do CBS difere da soma 
dos itens 
014 O total do CBS deverá ser a soma do campo vCBS 
informados nos itens 
Obrig. 363 Rej. Rejeição: Total de CBS difere da soma dos itens 
015 O total do Crédito Presumido do IBS deverá ser a 
soma do campo vCredPres do IBS informados nos 
itens 
Obrig. 364 Rej. Rejeição: Total de Crédito Presumido do IBS difere da 
soma dos itens 
016 O total do Crédito Presumido Condição 
Suspensiva do IBS deverá ser a soma do campo 
vCredPresConsSus do IBS informados nos itens 
Obrig. 365 Rej. Rejeição: Total de Crédito Presumido Condição 
Suspensiva do IBS difere da soma dos itens 
017 O total do Crédito Presumido da CBS deverá ser a 
soma do campo vCredPres de CBS informados 
nos itens 
Obrig. 366 Rej. Rejeição: Total de Crédito Presumido da CBS difere da 
soma dos itens 
018 O total do Crédito Presumido Condição 
Suspensiva da CBS deverá ser a soma do campo 
vCredPresCondSus de CBS informados nos itens 
Obrig. 367 Rej. Rejeição: Total de Crédito Presumido Condição 
Suspensiva da CBS difere da soma dos itens 
019 O total geral do DFe só deve ser informado se o 
grupo de totais do IBS e CBS estiver informado 
Obrig. 368 Rej. Rejeição: O Total do DFe não deve ser informado 
quando não houver IBS e CBS 
8 Total Geral do Documento Fiscal Eletrônico 
Deverá ser criada a tag Valor Total do DFe (vTotDFe) que somará o valor do documento fiscal com o ICMS (tributos 
“por dentro”) + o valor total do IBS e da CBS (tributos “por fora”). 
 
Para NF3e, NFCom e BPe TM esta tag será inserida no grupo total. 
 
No CTe, CTe Simplificado, CTe OS e BPe essa tag aparecerá dentro do grupo imp, após o grupo IBSCBS. 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E total / imp E 0-1 13,2 Valor total do documento fiscal  
(vNF/vTPrest + total do IBS + total da CBS) 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser a soma do total do 
documento (grupo total/vNF) ou (imp/vTPrest) + 
vTotIBS + vTotCBS 
Obrig. 369 Rej. Rejeição: Total do DFe difere da soma do total do XXX 
+ IBS e CBS 
Observação: XXX poderá ser CTe, BPe, NF3e ou 
NFCom

## Página 13

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 13 / 16 
 
9 Anexo – Novos Grupos para Reforma Tributária 
Conhecimento de Transporte Eletrônico– modelo 57

## Página 14

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 14 / 16 
 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 
 
  
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67

## Página 15

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 15 / 16 
 
Bilhete de Passagem Eletrônico – Modelo 63 
 
 
Bilhete de Passagem Eletrônico Transporte Metropolitano – Modelo 63

## Página 16

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.10 
 
 
Página 16 / 16 
 
Nota Fiscal de Energia Elétrica Eletrônica – Modelo 66 
 
  
 
Nota Fiscal Fatura de Comunicação Eletrônica – Modelo 62
