---
id: ct-e-bp-e-nf3e-nfcom-nt-conjunta-dfe-dfe-nota-tecnica-2024-001-ibscbs
titulo: DFe - Nota Técnica 2024.001 - IBS/CBS - Publicada em 01/08/24
tipo: nota.tecnica
versao: '1.00'
data: '2024-08-01'
documento_fiscal: CT-e/BP-e/NF3e/NFCom (NT conjunta DFe)
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=JXfIwug9EGE=
arquivo_original: fontes/acervo/ct-e-bp-e-nf3e-nfcom-nt-conjunta-dfe-dfe-nota-tecnica-2024-001-ibscbs.pdf
sha256_original: 4957b30932d479493d2a81a7c9558f535170b5a654c8e1d61745f92dc93f83ae
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 1c44858ff429493945a0f8740a2461df49be2133cbe5c5fc38f05cf84e3cc091
---

## Página 1

Projeto Reforma Tributária do 
Consumo – Adequação DFe 
 
Nota Técnica 2024.001 
Versão 1.00 de 31 de julho 2024

## Página 2

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 2 / 17 
 
Sumário 
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Tipos básicos da tributação ............................................................................................. 4 
3 Alteração do leiaute dos DFe .......................................................................................... 5 
4 Código Situação Tributária e Classificação da Tributação ............................................... 7 
5 Validações dos campos do IBS e CBS ............................................................................ 7 
6 Grupo de totais do DFe ................................................................................................. 10 
7 Regras de Validação do Grupo de Totais IBS e CBS .................................................... 11 
8 Total Geral do Documento Fiscal Eletrônico ................................................................. 12 
10 Anexo – Novos Grupos para Reforma Tributária ....................................................... 13 
Conhecimento de Transporte Eletrônico– modelo 57 ........................................................ 13 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 ................................... 14 
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67 ........................... 14 
Bilhete de Passagem Eletrônico – Modelo 63 ................................................................... 15 
Bilhete de Passagem Eletrônico Transporte Metropolitano – Modelo 63........................... 15 
Nota Fiscal de Energia Elétrica Eletrônica – Modelo 66 .................................................... 16 
Nota Fiscal Fatura de Comunicação Eletrônica – Modelo 62 ............................................ 17

## Página 3

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 3 / 17 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Previsão das informações do IBS/CBS nos DFe 01/09/2025 31/10/2025

## Página 4

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 4 / 17 
 
1 Introdução 
O PLP 68, aprovado na Câmara dos Deputados e encaminhado para aprovação junto ao Senado Federal, definiu 
na Seção VIII – Disposições transitórias, Art. 61, a obrigatoriedade para Estados, o Distrito Federal e os Municípios, 
adaptarem os sistemas autorizadores de Documentos Fiscais Eletrônicos (DFe) vigentes para utilização de leiaute 
padronizado, que permita aos contribuintes informarem os dados relativos ao Imposto sobre Bens e Serviços (IBS), 
Contribuição sobre Bens e Serviços (CBS) e Imposto Seletivo (IS).. 
 
Como as infraestruturas autorizadoras de Documentos Fiscais Eletrônicos (DFe) das Unidades Federadas e 
Municípios, além das aplicações e sistemas dos contribuintes, necessitam de, no mínimo, 1 ano para o 
desenvolvimento das alterações necessárias, estamos divulgando esta Nota Técnica (NT) para implantação, em 
produção, a partir do dia 31/10/2025, de forma a entrar em efetiva operacionalização em 01/01/2026. 
 
Como as discussões envolvendo a implantação da Reforma Tributária ainda estão em curso, esclarecemos que 
esta NT poderá ser ajustada ao longo do seu processo de execução, da mesma forma como ocorre com as demais 
NT já implementadas. 
 
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
NT 2024.001 v1.00 
 
 
Página 5 / 17 
 
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
9 gCredPres G gIBSUF - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento. 
Exemplos:  
1 - Aquisição de PR não contribuinte.  
2 - Tomador de serviço de transporte de TAC PF não 
contrib.  
3 - Aquisição de pessoa física com destino a reciclagem.  
4 - Aquisição de bens móveis de PF não contrib. para 
revenda (veículos / brecho).  
5 - Regime opcional para cooperativa. 
10 pCredPres E gCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
11 vCredPres E gCredPres N 1-1 13,2 Valor do crédito presumido 
12 gDif G gIBSUF - 0-1 - Grupo de campos do diferimento 
13 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
14 vDif E gDif N 1-1 13,2 Valor do diferimento 
15 gDevTrib G gIBSUF - 0-1 - Grupo de informações da devolução de tributos 
16 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
17 gRed G gIBSUF - 0-1 - Grupo de informações da redução de aliquota 
18 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
19 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo 
20 gDeson G gIBSUF - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
21 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
22 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
23 vBC E gDeson N 0-1 13,2 Base de calculo (igual ao do elemento anterior) 
24 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem desoneração 
25 vDeson E gDeson N 1-1 13,2 Valor da desoneraçao.  
Não é descontado do valor do IBS. 
26 vIBSUF E gIBSUF N 1-1 13,2 Valor do IBS de competência da UF 
27 gIBSMun G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
do municipio

## Página 6

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 6 / 17 
 
28 pIBSMun E gIBSMun N 1-1 3,2/3,4 Aliquota do IBS Municipal 
29 Sequência XML - gIBSMun - 0-1 - - 
30 vTribOp E gIBSMun N 1-1 13,2 Valor do Tributo Bruto na operação 
31 gCredPres G gIBSMun - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento. 
Exemplos:  
1 - Aquisição de PR não contribuinte.  
2 - Tomador de serviço de transporte de TAC PF não 
contrib.  
3 - Aquisição de pessoa física com destino a reciclagem.  
4 - Aquisição de bens móveis de PF não contrib. para 
revenda (veículos / brecho).  
5 - Regime opcional para cooperativa. 
32 pCredPres E gCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
33 vCredPres E gCredPres N 1-1 13,2 Valor do crédito presumido 
34 gDif G gIBSMun - 0-1 - Grupo de campos do diferimento 
35 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
36 vDif E gDif N 1-1 13,2 Valor do diferimento 
37 gDevTrib G gIBSMun - 0-1 - Grupo de informações da devolução do tributo 
38 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
39 gRed G gIBSMun - 0-1 - Grupo de informações da redução de aliquota 
40 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
41 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo 
42 gDeson G gIBSUF - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
43 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
44 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
45 vBC E gDeson N 0-1 13,2 Base de calculo (igual do elemento anterior) 
46 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem desoneração 
47 vDeson E gDeson N 1-1 13,2 Valor da desoneração 
48 vIBSMun E gIBSMun N 1-1 13,2 Valor do IBS de competência do município 
49 gCBS G gIBSCBS - 1-1 - Grupo de informações da CBS 
50 pCBS E gCBS N 1-1 3,2/3,4 Aliquota da CBS 
51 Sequência XML - gCBS - 0-1 - - 
52 vTribOp E gCBS N 1-1 13,2 Valor do Tributo Bruto na operação 
53 gCredPres G gCBS - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento. 
Exemplos:  
1 - Aquisição de PR não contribuinte.  
2 - Tomador de serviço de transporte de TAC PF não 
contrib.  
3 - Aquisição de pessoa física com destino a reciclagem.  
4 - Aquisição de bens móveis de PF não contrib. para 
revenda (veículos / brecho).  
5 - Regime opcional para cooperativa. 
54 pCredPres E gCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
55 vCredPres E gCredPres N 1-1 13,2 Valor do crédito presumido 
56 gDif G gCBS - 0-1 - Grupo de campos do diferimento

## Página 7

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 7 / 17 
 
57 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
58 vDif E gDif N 1-1 13,2 Valor do diferimento 
59 gDevTrib G gCBS - 0-1 - Grupo de informações da devolução do tributo 
60 vDevTrib E gDevTrib N 1-1 13,2 Valor da CBS devolvida.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
61 gRed G gCBS - 0-1 - Grupo de informações da redução de aliquota 
62 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de aliquota 
63 pAliqEfet E gRed N 1-1 3,2/3,4 Aliquota efetiva da CBS que será aplicada a base de 
cálculo 
64 gDeson G gIBSUF - 0-1 - Grupo de informações da Desoneração.  
Exemplo  
1: Art. 442, §4. Operações com ZFM e ALC. Exemplo  
2: Operações com suspensão do tributo. 
65 CST E gDeson N 1-1 3 Código da Situação Tributária caso o item não sofra 
desoneração 
66 cClassTrib E gDeson N 1-1 6 Código de Classificação Tributária caso o item não 
sofra desoneração 
67 vBC E gDeson N 0-1 13,2 Base de calculo (igual do elemento anterior) 
68 pAliq E gDeson N 1-1 3,2/3,4 Aliquota sem a desoneração 
69 vDeson E gDeson N 1-1 13,2 Valor da desoneração 
70 vCBS E gCBS N 1-1 13,2 Valor da CBS 
 
4 Código Situação Tributária e Classificação da Tributação 
O grupo de informações do IBS, CBS e IS deve ser classificado de acordo com Código de Situação Tributária 
(CST) e Código de Classificação Tributária (cClassTrib). 
As duas tabelas estarão publicadas nos portais nacionais dos documentos fiscais eletrônicos e as ocorrências 
previstas para preenchimento estão relacionadas às previsões legais do texto da Reforma Tributária. 
Associados a estas tabelas, serão publicados indicadores de obrigatoriedade de preenchimento dos grupos de 
informações do IBS/CBS nos DFe. Essas configurações vinculam de forma dinâmica os CST e cClassTrib com as 
Regras de Validação descritas logo abaixo. 
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
Obrig. 315 Rej. Rejeição: Valor do IBS UF diferente de Base de 
Cálculo x Alíquota

## Página 8

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 8 / 17 
 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
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
008 Se CST informado exigir informação de Crédito 
Presumido para o IBS Estadual, o grupo gCredPres 
deve estar informado 
Obrig. 317 Rej. Rejeição: CST informado obriga informação de 
crédito presumido 
009 Se informado grupo do crédito presumido 
(gIBSUF/gCredPres): 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 318 Rej. Rejeição: Valor do Crédito Presumido da UF 
diferente de Base de Cálculo x Percentual 
010 Se CST informado exigir informação de Diferimento 
para o IBS Estadual, o grupo gDif deve estar informado 
Obrig. 319 Rej. Rejeição: CST informado obriga informação de 
diferimento Estadual 
011 Se informado grupo do Diferimento (gIBSUF/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Obrig. 320 Rej. Rejeição: Valor do Diferimento da UF diferente de 
Base de Cálculo x Percentual 
012 Se CST informado exigir informação de Desoneração 
para o IBS Estadual, o grupo gDeson deve estar 
informado 
Obrig. 321 Rej. Rejeição: CST informado obriga informação da 
desoneração 
013 Se informado grupo da desoneração (gIBSUF/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 322 Rej. Rejeição: CST informado na desoneração 
inexistente 
014 Se informado grupo da desoneração (gIBSUF/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 323 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
015 Se informado grupo da desoneração (gIBSUF/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos  
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 324 Rej. Rejeição: Valor Desonerado da UF diferente de 
Base de Cálculo x Alíquota 
016 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do IBS (vIBSMun) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pIBSMun) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 325 Rej. Rejeição: Valor do IBS Municipal diferente de Base de 
Cálculo x Alíquota 
017 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do Tributo Bruto da Operação (vTribOp) 
deverá ser resultante da Base de Cálculo x Alíquota 
vigente do Município (ver tabela de alíquotas 
Municipais) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig; 326 Rej. Rejeição: Valor do Tributo Bruto da Operação 
diferente da Base de Cálculo x Alíquota vigente do 
Município 
018 Se CST informado exigir informação de Crédito 
Presumido para o IBS Municipal, o grupo gCredPres 
deve estar informado 
Obrig. 327 Rej. Rejeição: CST informado obriga informação de 
crédito presumido

## Página 9

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 9 / 17 
 
019 Se informado grupo do crédito presumido 
(gIBSMun/gCredPres): 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 328 Rej. Rejeição: Valor do Crédito Presumido do Município 
diferente de Base de Cálculo x Percentual 
020 Se CST informado exigir informação de Diferimento 
para o IBS Municipal, o grupo gDif deve estar 
informado 
Obrig. 329 Rej. Rejeição: CST informado obriga informação de 
diferimento Municipal 
021 Se informado grupo do Diferimento (gIBSMun/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 330 Rej. Rejeição: Valor do Diferimento do Município diferente 
de Base de Cálculo x Percentual 
022 Se CST informado exigir informação de Desoneração 
para o IBS Municipal, o grupo gDeson deve estar 
informado 
Obrig. 331 Rej. Rejeição: CST informado obriga informação da 
desoneração 
023 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 332 Rej. Rejeição: CST informado na desoneração inexistente 
024 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 333 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
025 Se informado grupo da desoneração 
(gIBSMun/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Aliquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 334 Rej. Rejeição: Valor Desonerado do Município diferente de 
Base de Cálculo x Alíquota 
026 Se informado grupo CBS (gCBS): 
O valor do CBS (vCBS) deverá ser resultante da Base 
de Cálculo x Alíquota (vBC x pCBS) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 335 Rej. Rejeição: Valor do CBS diferente de Base de Cálculo 
x Alíquota 
027 Se informado grupo CBS (gCBS): 
O valor do Tributo Bruto da Operação (vTribOp) 
deverá ser resultante da Base de Cálculo x Alíquota 
vigente da CBS  
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig; 336 Rej. Rejeição: Valor do Tributo Bruto da Operação 
diferente da Base de Cálculo x Alíquota vigente da 
CBS 
028 Se CST informado exigir informação de Crédito 
Presumido para o CBS, o grupo gCredPres deve estar 
informado 
Obrig. 337 Rej. Rejeição: CST informado obriga informação de 
crédito presumido 
029 Se informado grupo do crédito presumido 
(gCBS/gCredPres): 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 338 Rej. Rejeição: Valor do Crédito Presumido do CBS 
diferente de Base de Cálculo x Percentual 
030 Se CST informado exigir informação de Diferimento 
para o CBS, o grupo gDif deve estar informado 
Obrig. 339 Rej. Rejeição: CST informado obriga informação de 
diferimento do CBS 
031 Se informado grupo do Diferimento (gCBS/gDif): 
O valor do Diferimento (vDif) deverá ser resultante da 
Base de Cálculo x Percentual do Diferimento (vBC x 
pDif) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 340 Rej. Rejeição: Valor do Diferimento do CBS diferente de 
Base de Cálculo x Percentual

## Página 10

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 10 / 17 
 
032 Se CST informado exigir informação de Desoneração 
para a CBS, o grupo gDeson deve estar informado 
Obrig. 341 Rej. Rejeição: CST informado obriga informação da 
desoneração 
033 Se informado grupo da desoneração (gCBS/gDeson): 
O CST informado no grupo gDeson deve existir na 
tabela de Código de Situação Tributária (gDeson/CST) 
Obrig. 342 Rej. Rejeição: CST informado na desoneração inexistente 
034 Se informado grupo da desoneração (gCBS/gDeson): 
O cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
gDeson/cClassTrib) 
Obrig. 343 Rej. Rejeição: Classificação Tributária informada na 
desoneração inexistente 
035 Se informado grupo da desoneração (gCBS/gDeson): 
O valor desonerado (vDeson) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pAliq) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: A base de cálculo deverá ser a do 
IBS/CBS, exceto se informado o vBC do próprio grupo 
gDeson 
Obrig. 344 Rej. Rejeição: Valor Desonerado da CBS diferente de 
Base de Cálculo x Alíquota 
 
6 Grupo de totais do DFe 
Para NF3e, NFCom e BPe TM, no grupo total do DFe deverá ser adicionado o grupo de totais do IBS/CBS. 
Para CTe, CTe Simplificado, CTeOS e BPe não será criado esse grupo de totais do IBS/CBS. 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBSTot G total - 0-1 - Grupo de informações para apuração do IBS e 
CBS declarado pelo contribuinte 
1 vBCCIBS E gTotIBSCBS N 1-1 13,2 Total da Base de cálculo do IBS/CBS 
2 gIBS G gIPA - 1-1 - Totalização do IBS 
3 gIBSUFTot G gIBS - 1-1 - Total do IBS das UF 
4 vCredPres E gIBSUFTot N 1-1 13,2 Total do Crédito Presumido 
5 vDif E gIBSUFTot N 1-1 13,2 Total do Diferimento 
6 vDevTrib E gIBSUFTot N 1-1 13,2 Total de Devolução de Tributo IBS UF 
7 vDeson E gIBSUFTot N 1-1 13,2 Total desonerado do IBS UF 
8 vIBSUF E gIBSUFTot N 1-1 13,2 Total do IBS UF 
9 gIBSMunTot G gIBS - 1-1 - Total do IBS dos Municípios 
10 vCredPres E gIBSMunTot N 1-1 13,2 Total do Crédito Presumido 
11 vDif E gIBSMunTot N 1-1 13,2 Total do Diferimento 
12 vDevTrib E gIBSMunTot N 1-1 13,2 Total de Devolução de Tributo IBS Municipal 
13 vDeson E gIBSMunTot N 1-1 13,2 Total desonerado do IBS Municipal 
14 vIBSMun E gIBSMunTot N 1-1 13,2 Total do IBS Municipal 
15 vIBSTot E gIBS N 1-1 13,2 Total do IBS (IBS UF + IBS Mun) 
16 gCBS G gIPA - 1-1 - Total do CBS 
17 vCredPres E gCBS N 1-1 13,2 Total do Crédito Presumido 
18 vDif E gCBS N 1-1 13,2 Total do Diferimento 
19 vDevTrib E gCBS N 1-1 13,2 Total de Devolução do tributo CBS 
20 vDeson E gCBS N 1-1 13,2 Total desonerado do tributo CBS 
21 vCBS E gCBS N 1-1 13,2 Total do CBS

## Página 11

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 11 / 17 
 
7 Regras de Validação do Grupo de Totais IBS e CBS 
Aplicável apenas para NF3e, NFCom e BPe TM. 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 O grupo de totais do IBS e CBS (IBSCBSTot) só 
deve ser informado se existir pelo menos uma 
ocorrência de IBS/CBS nos itens 
Obrig. 345 Rej. Rejeição: Total de IBS/CBS só deve ser informado 
se existir IBS/CBS declarado nos itens do DFe 
002 O total do Crédito Presumido do IBS UF deverá 
ser a soma do campo vCredPres do IBS UF 
informados nos itens 
Obrig. 346 Rej. Rejeição: Total de Crédito Presumido do IBS UF 
difere da soma dos itens 
003 O total do Diferimento do IBS UF deverá ser a 
soma do campo vDif do IBS UF informados nos 
itens 
Obrig. 347 Rej. Rejeição: Total de Diferimento do IBS UF difere da 
soma dos itens 
004 O total Devolvido do IBS UF deverá ser a soma do 
campo vDevTrib do IBS UF informados nos itens 
Obrig. 348 Rej. Rejeição: Total Devolvido do IBS UF difere da soma 
dos itens 
005 O total Desonerado do IBS UF deverá ser a soma 
do campo vDeson do IBS UF informados nos itens 
Obrig. 349 Rej. Rejeição: Total Desonerado do IBS UF difere da 
soma dos itens 
006 O total do IBS UF deverá ser a soma do campo 
vIBSUF informados nos itens 
Obrig. 350 Rej. Rejeição: Total de IBS UF difere da soma dos itens 
007 O total do Crédito Presumido do IBS Municipal 
deverá ser a soma do campo vCredPres do IBS 
Municipal informados nos itens 
Obrig. 351 Rej. Rejeição: Total de Crédito Presumido do IBS 
Municipal difere da soma dos itens 
008 O total do Diferimento do IBS Municipal deverá ser 
a soma do campo vDif do IBS Municipal 
informados nos itens 
Obrig. 352 Rej. Rejeição: Total de Diferimento do IBS Municipal 
difere da soma dos itens 
009 O total Devolvido do IBS Municipal deverá ser a 
soma do campo vDevTrib do IBS Municipal 
informados nos itens 
Obrig. 353 Rej. Rejeição: Total Devolvido do IBS Municipal difere da 
soma dos itens 
010 O total do IBS Municipal deverá ser a soma do 
campo vIBSMun informados nos itens 
Obrig. 354 Rej. Rejeição: Total de IBS Municipal difere da soma dos 
itens 
011 O total Desonerado do IBS Municipal deverá ser a 
soma do campo vDeson do IBS Municipal 
informados nos itens 
Obrig. 355 Rej. Rejeição: Total Desonerado do IBS Municipal difere 
da soma dos itens 
012 O Total do IBS deverá ser a soma do IBS das UF 
e do IBS Municipal (vIBSUF + vIBSMun) 
Obrig. 356 Rej. Rejeição: Total do IBS difere da soma do IBS UF e 
IBS Municipal 
013 O total do Crédito Presumido do CBS deverá ser a 
soma do campo vCredPres do CBS informados 
nos itens 
Obrig. 357 Rej. Rejeição: Total de Crédito Presumido do CBS difere da 
soma dos itens 
014 O total do Diferimento do CBS deverá ser a soma 
do campo vDif do CBS informados nos itens 
Obrig. 358 Rej. Rejeição: Total de Diferimento do CBS difere da soma 
dos itens 
015 O total Devolvido do CBS deverá ser a soma do 
campo vDevTrib do CBS informados nos itens 
Obrig. 359 Rej. Rejeição: Total Devolvido do CBS difere da soma dos 
itens 
016 O total Desonerado do CBS deverá ser a soma do 
campo vDeson do CBS informados nos itens 
Obrig. 360 Rej. Rejeição: Total Desonerado do CBS difere da soma 
dos itens 
017 O total do CBS deverá ser a soma do campo vCBS 
informados nos itens 
Obrig. 361 Rej. Rejeição: Total de CBS difere da soma dos itens 
018 O total geral do DFe só deve ser informado se o 
grupo de totais do IBS e CBS estiver informado 
Obrig. 362 Rej. Rejeição: O Total do DFe não deve ser informado 
quando não houver IBS e CBS

## Página 12

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 12 / 17 
 
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
Obrig. 363 Rej. Rejeição: Total do DFe difere da soma do total do XXX 
+ IBS e CBS 
Observação: XXX poderá ser CTe, BPe, NF3e ou 
NFCom

## Página 13

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 13 / 17 
 
10 Anexo – Novos Grupos para Reforma Tributária 
Conhecimento de Transporte Eletrônico– modelo 57

## Página 14

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 14 / 17 
 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 
 
  
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67

## Página 15

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 15 / 17 
 
Bilhete de Passagem Eletrônico – Modelo 63 
 
 
Bilhete de Passagem Eletrônico Transporte Metropolitano – Modelo 63

## Página 16

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 16 / 17 
 
Nota Fiscal de Energia Elétrica Eletrônica – Modelo 66 
Grupo IBS/CBS dentro do item: 
  
Grupo de Totais:

## Página 17

Projeto 
Reforma Tributária do Consumo 
NT 2024.001 v1.00 
 
 
Página 17 / 17 
 
Nota Fiscal Fatura de Comunicação Eletrônica – Modelo 62 
Grupo IBS/CBS dentro do item: 
  
Grupo de Totais:
