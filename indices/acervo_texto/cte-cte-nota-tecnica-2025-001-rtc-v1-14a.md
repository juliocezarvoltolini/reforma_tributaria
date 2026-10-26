---
id: cte-cte-nota-tecnica-2025-001-rtc-v1-14a
titulo: Nota Técnica CT-e - Nota_Técnica_2025_001 - RTC_v1.14a - Publicada em 07/04/2026
tipo: nota.tecnica
versao: 1.14a
data: '2026-04-07'
documento_fiscal: CT-e/CT-e OS/GTV-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=wZvIULdEsOs=
arquivo_original: fontes/acervo/cte-cte-nota-tecnica-2025-001-rtc-v1-14a.pdf
sha256_original: fc5bceb63e5a58d04a92916dd8463963b63edc8dddcc07ffda8b0e1fb35d479a
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 425a2d694600302d40e147229ac2f7de28584f0480c53b05dec44dc9c23089a3
---

## Página 1

Projeto Conhecimento de 
Transporte Eletrônico 
 
Nota Técnica 2025.001 – Reforma Tributária do Consumo 
Versão 1.14 a de 11 de março de 2026

## Página 2

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 2 / 21 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 5 
2 Tipos básicos da tributação ............................................................................................. 5 
3 Alteração do leiaute do imposto do CTe .......................................................................... 6 
4 Código de Classificação Tributária do IBS/CBS .............................................................. 8 
5 Validações dos campos do IBS e CBS ............................................................................ 9 
6 Criação do grupo de compras governamentais no grupo ide ......................................... 15 
7 Total Geral do Documento Fiscal Eletrônico ................................................................. 17 
8 Alteração em Regra do CTe Simplificado ...................................................................... 17 
9 Alterações no Layout do Modal Dutoviário .................................................................... 18 
10 Criação do grupo de informações da DCe nos documentos originários ..................... 18 
11 Exceção para Substituição sem exigência do evento de prestação em desacordo 
para tomador Exterior ........................................................................................................... 20 
12 Ajuste na regra que define prazo para CTe Complementar ....................................... 20 
13 Eliminar as opções de contingência SVC da GTVe no Leiaute (Schema) .................. 20 
14 Nova regra para CTe OS de Transporte de Valores .................................................. 20 
15 Ajuste em regras de validação do tomador Contribuinte Isento de IE ........................ 20 
16 Preparação das expressões regulares do CTe para o futuro CNPJ Alfanumérico ..... 20 
17 Ampliação do cStat de retorno para 4 dígitos ............................................................ 21

## Página 3

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 3 / 21 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Previsão das informações do IBS/CBS no CTe 
 Alteração de regras do CTeOS Transporte Valores exigir UF e Mun Fim 
 Alteração das regras do CTe Simplificado para limitar em apenas um fim 
de prestação 
 Alteração no leiaute do Dutoviário 
 Exceção para não exigir evento de prestação em desacordo na 
substituição de tomador do EX 
 Preparação das Expressões Regulares do CNPJ Alfa 
 Eliminação da SVC para GTVe 
 Inclusão da DCe nos documentos originários 
 Ampliação do código de retorno das mensagens suportar até 4 dígitos 
  
1.01  Correções e orientações sobre aplicação das regras de validação  
 Renumeração das regras de rejeição 
 Ajuste no grupo de Tributação regular 
 Ajuste na regra do CTe Complementar para Multimodal 
  
1.02  Ajustes nas regras do crédito presumido e tributação regular 
 Ajuste nas regras para Crédito Presumido Condição Suspensiva no 
grupo do crédito presumido 
  
1.03  Ajustes nas regras de compras governamentais, redução de alíquota e 
valores de IBS/CBS 
 Correção no schema dos eventos tipos básicos 
  
1.04  Ajustes em regras de validação e mensagens   
1.05  Ajuste na regra de compras governamentais e exigência do grupo de 
tributação para SN  
 Novo grupo de informações da tributação para compras governamentais  
  
1.05 a  Correção de datas no texto da introdução   
1.05b   Correção em nome de campos citados nas RVs   
1.06  Novas regras de validação complementares 
 Inclusão do campo vIBS 
 Ajuste na expressão regular do qrcode prevendo o CNPJ Alfa 
  
1.07  Campo vIBS passa a ser obrigatório no schema   
1.08  Alteração da regra de validação 004-a para verificar no cClassTrib sua 
aplicabilidade ao modelo de DFe 
 Correção na posição do campo vIBS no schema 
 Correção na obrigatoriedade das regras 038 e 044 
  
1.08 a  Ajuste na redação da regra de total geral do DFe

## Página 4

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 4 / 21 
 
1.09  Ajustes na regra do diferimento 
 Altera data de exigência do grupo IBSCBS em homologação para 03/11 
  
1.10  Exclusão do grupo de informações do crédito presumido por não se aplicar 
aos cClassTrib associados ao DFe 
 Criação do indicador de doação e do grupo de Estorno de crédito vinculado 
a um novo indicador na tabela cClassTrib para esta finalidade 
  
1.11a  Correção na regra de validação do CBS, permitindo alíquota zero para a CBS 
em operações específicas dentro de áreas incentivadas. 
 
 Ajuste na explicação da regra de valor do tributo negativo 
  
1.12  Esclarecimento do preenchimento do vTotDFe   
1.12 a  Correção da validação da redução de alíquota Já implantado Já implantado 
1.13  Criação de regra específica para exigir vTotDFe quando informado IBSCBS 03/02/2026 02/03/2026 
1.14  Inclusão de campos do tipo de operação e DFe referenciado nas compras 
governamentais 
  
1.14 a  Ajuste nas mensagens de validação das compras gov 06/04/2026 04/05/2026 
Observação: No ambiente de produção, os campos ficam à disposição desde 20 de outubro, validados apenas se 
informados. No ambiente de homologação os campos da reforma tributária estarão à disposição desde julho, 
validados apenas se informados.

## Página 5

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 5 / 21 
 
1 Introdução 
Com a promulgação da Lei Complementar nº 214/2025, foi definida, na Seção V - Disposições Transitórias, 
Art. 62 I, a obrigatoriedade de que os Estados, o Distrito Federal e os Municípios adaptem os sistemas 
autorizadores de Documentos Fiscais Eletrônicos (DFe) vigentes para a utilização de leiaute padronizado, de 
modo a permitir que os contribuintes informem os dados relativos ao Imposto sobre Bens e Serviços (IBS), à 
Contribuição sobre Bens e Serviços (CBS) e ao Imposto Seletivo (IS). 
 
Diante disso, esta Nota Técnica substitui e complementa, no âmbito do CTe, a DFe - Nota Técnica 2024.001 
- IBS/CBS v1.10, mantendo a data de implantação em ambiente de produção para 06/10/2025, de modo a viabilizar 
sua efetiva operacionalização a partir de 05/01/2026. 
 
A NT modifica o leiaute dos DFe, inserindo os grupos e campos opcionais relacionados a tributação do IBS, CBS 
e IS, em atendimento à legislação vigente. 
 
Esclarecemos que esta NT poderá ser ajustada ao longo do seu processo de execução, uma vez que as discussões 
envolvendo a implantação da Reforma Tributária ainda estão em curso. 
 
Vale destacar que, em Produção, no ano de 2025 as informações de tributação relativas ao IBS e CBS serão 
opcionais e validadas apenas se forem informadas.  
 
Esta documentação descreve as alterações aplicadas aos Documentos: 
 Conhecimento de Transporte Eletrônico (modelo 57); 
 Conhecimento de Transporte Eletrônico para Outros Serviços (modelo 67); 
 
2 Tipos básicos da tributação 
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos, esta NT introduz o arquivo 
DFeTiposBasicos_v1.00.xsd ao conjunto dos arquivos que compõem do schema da DFe. 
 
Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro das 
informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no leiaute padrão da DFe 
conforme estrutura abaixo:

## Página 6

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 6 / 21 
 
3 Alteração do leiaute do imposto do CTe 
Este grupo de informações facultativas deve ser adicionado ao final do grupo imposto do CTe, CTe Simplificado e 
CTe OS. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBS G imp - 0-1 - Grupo de informações da Tributação IBS/CBS 
1 CST E IBSCBS N 1-1 3 Código da Situação Tributária do IBS/CBS 
2 cClassTrib E IBSCBS N 1-1 6 Código da Classificação Tributária do IBS/CBS 
3 indDoacao E IBSCBS N 0-1 1 Informar quando doação 
4 gIBSCBS G IBSCBS - 0-1 - Grupo de informações específicas do IBS/CBS 
5 vBC E gIBSCBS N 1-1 13,2 Valor da Base de cálculo comum a IBS/CBS 
6 gIBSUF G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
das Unidades Federadas 
7 pIBSUF E gIBSUF N 1-1 3,2/3,4 Alíquota do IBS Estadual 
8 gDif G gIBSUF - 0-1 - Grupo de campos do diferimento 
9 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
10 vDif E gDif N 1-1 13,2 Valor do diferimento 
11 gDevTrib G gIBSUF - 0-1 - Grupo de informações da devolução de tributos 
12 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
13 gRed G gIBSUF - 0-1 - Grupo de informações da redução de Alíquota 
14 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
15 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo, incluindo o 
gCompraGov/pRedutor, se houver. 
16 vIBSUF E gIBSUF N 1-1 13,2 Valor do IBS de competência da UF 
17 gIBSMun G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
do municipio 
18 pIBSMun E gIBSMun N 1-1 3,2/3,4 Alíquota do IBS Municipal 
19 gDif G gIBSMun - 0-1 - Grupo de campos do diferimento 
20 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
21 vDif E gDif N 1-1 13,2 Valor do diferimento 
22 gDevTrib G gIBSMun - 0-1 - Grupo de informações da devolução do tributo 
23 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
24 gRed G gIBSMun - 0-1 - Grupo de informações da redução de Alíquota 
25 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
26 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência dos 
Municipios que será aplicada a base de cálculo, 
incluindo o gCompraGov/pRedutor, se houver. 
26a vIBSMun E gIBSMun N 1-1 13,2 Valor do IBS de competência do município 
27 vIBS E gIBSCBS N 1-1 13,2 Valor do IBS (soma de vIBSUF e vIBSMun) 
28 gCBS G gIBSCBS - 1-1 - Grupo de informações da CBS 
29 pCBS E gCBS N 1-1 3,2/3,4 Alíquota da CBS

## Página 7

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 7 / 21 
 
30 gDif G gCBS - 0-1 - Grupo de campos do diferimento 
31 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
32 vDif E gDif N 1-1 13,2 Valor do diferimento 
33 gDevTrib G gCBS - 0-1 - Grupo de informações da devolução do tributo 
34 vDevTrib E gDevTrib N 1-1 13,2 Valor da CBS devolvida.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
35 gRed G gCBS - 0-1 - Grupo de informações da redução de Alíquota 
36 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
37 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva da CBS que será aplicada a base 
de cálculo, incluindo o gCompraGov/pRedutor, se 
houver. 
38 vCBS E gCBS N 1-1 13,2 Valor da CBS 
39 gTribRegular G gIBSCBS - 0-1 - Grupo de informações da Tributação Regular. 
Informar como seria a tributação caso não cumprida 
a condição resolutória/suspensiva. Exemplo 1: Art. 
442, §4. Operações com ZFM e ALC. Exemplo 2: 
Operações com suspensão do tributo.. 
40 CSTReg E gTribRegular N 1-1 3 Código da Situação Tributária  
Informado como seria o CST caso não cumprida a 
condição resolutória/suspensiva 
41 cClassTribReg E gTribRegular N 1-1 6 Código de Classificação Tributária  
Informado como seria o cClassTrib caso não 
cumprida a condição resolutória/suspensiva 
42 pAliqEfetRegIBSUF E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da UF 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
43 vTribRegIBSUF E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo da UF caso 
não cumprida a condição resolutória/suspensiva 
44 pAliqEfetRegIBSMun E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva do Município 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
45 vTribRegIBSMun E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo do 
Município caso não cumprida a condição 
resolutória/suspensiva 
46 pAliqEfetRegCBS E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da CBS 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
 vTribRegCBS E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo CBS caso 
não cumprida a condição resolutória/suspensiva 
57 gTribCompraGov G gIBSCBS - 0-1 - Grupo de informações da composição do valor do 
IBS e da CBS em compras governamental 
58 pAliqIBSUF E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS da UF utilizada 
59 vTribIBSUF E gTribCompraGov N 1-1 13,2 Valor do Tributo do IBS da UF 
Valor que seria devido a UF, sem aplicação do Art. 
473. da LC 214/20025 
60 pAliqIBSMun E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS do Município utilizada 
61 vTribIBSMun E gTribCompraGov N 1-1 13,2 Valor do Tributo do Município da UF  
Valor que seria devido ao Município, sem aplicação 
do Art. 473. da LC 214/20025 
62 pAliqCBS E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS do CBS utilizada 
63 vTribCBS E gTribCompraGov N 1-1 13,2 Valor do Tributo da CBS  
Valor que seria devido a CBS, sem aplicação do Art. 
473. da LC 214/20025 
64 gEstornoCred G IBSCBS - 0-1 - Grupo de informações de estorno de crédito. 
Informado conforme indicador no cClassTrib

## Página 8

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 8 / 21 
 
65 vIBSEstCred E gEstornoCred N 1-1 13,2 Valor do IBS a ser estornado 
66 vCBSEstCred E gEstornoCred N 1-1 13,2 Valor do CBS a ser estornado 
 
4 Código de Classificação Tributária do IBS/CBS 
O grupo de informações do IBS, CBS e IS associado aos itens do documento fiscal contém o Código de Situação 
Tributária (CST) e Código de Classificação Tributária (cClassTrib) do IBS, CBS e IS. O Informe Técnico RT 
2025.002 divulga a publicação da tabela com esta codificação, que está disponível no Portal Nacional da NF-e 
(www.nfe.fazenda.gov.br), na aba “Documentos”, opção “Diversos” e no portal dos Documentos Fiscais Eletrônicos 
(dfe-portal.svrs.rs.gov.br).  
 
Cada código “cClassTrib” corresponde a um dispositivo específico da Lei Complementar nº 214/2025, tornando 
objetiva a informação prestada pelo contribuinte quanto à forma como interpreta a tributação do IBS e da CBS para 
cada DFe. 
 
A tabela também contém indicadores que vinculam de forma dinâmica códigos “CST-IBS/CBS” e “cClassTrib” com 
as Regras de Validação descritas nesta NT, ou que contêm informações necessárias para a preparação das 
apurações assistidas do IBS e da CBS, em atendimento ao disposto na legislação vigente.  
 
Vale ressaltar que a tabela poderá sofrer alterações em virtude de aperfeiçoamentos, novidades introduzidas em 
sede de Regulamento, ou para atender a necessidades relacionadas à apuração assistida do IBS e da CBS.

## Página 9

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 9 / 21 
 
5 Validações dos campos do IBS e CBS 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Não informado grupo de imposto IBS e CBS (grupo: 
imp/IBSCBS) 
 
Exceção: Se o CRT informado pelo emitente for 1-
Simples Nacional, 2- Simples Nacional, excesso 
sublimite de receita bruta ou 4 -MEI, o grupo IBSCBS 
NÃO será exigido 
 
IMPORTANTE: Esta regra passou para implementação 
futura, no entanto se o grupo for informado, todas as 
regras de validação serão aplicadas 
Futura 310 Rej. Rejeição: IBS / CBS não informado 
002 Se CST do IBS/CBS for informado, este deve existir na 
tabela de Código de Situação Tributária (tag: 
IBSCBS/CST) 
Obrig. 311 Rej. Rejeição: CST informado inexistente 
003 Se cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
IBSCBS/cClassTrib) 
Obrig. 312 Rej. Rejeição: Classificação Tributária informada 
inexistente 
004 Verificar se o CST informado é compatível com o 
cClassTrib 
Obrig. 313 Rej. Rejeição: Classificação Tributária incompatível com 
o CST informado 
004
a 
Verificar se o cClassTrib informado (tag: 
IBSCBS/cClassTrib) possui indicador que não permite 
ser informado nesse modelo de DFe 
Obrig. 388 Rej. Rejeição: Classificação Tributária do IBS/CBS não 
permitida neste modelo de DFe. 
005 Se o CST informado possuir indicador que VEDA 
preenchimento do grupo de informações específicas do 
IBS/CBS, este grupo NÂO DEVE estar informado 
(grupo: gIBSCBS) 
Obrig 314 Rej. Rejeição: Grupo IBS/CBS não deve ser preenchido 
para o CST informado 
006 Se o CST informado possuir indicador que EXIGE 
preenchimento do grupo de informações específicas do 
IBS/CBS, este grupo DEVE estar informado (grupo: 
gIBSCBS) 
 
Exceção: Se o CRT informado pelo emitente for 1-
Simples Nacional, 2- Simples Nacional, excesso 
sublimite de receita bruta ou 4 -MEI, o grupo gIBSCBS 
NÃO será exigido 
Obrig 315 Rej. Rejeição: Grupo IBS/CBS deve ser preenchido para o 
CST informado 
007 Se informado grupo IBS de competência das Unidades 
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
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF inválida  
009 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o IBS Estadual 
ou informado grupo de compra governamental, o grupo 
gRed DEVE estar informado 
 
Exceção: A regra não se aplica para CST do IBS/CBS 
(tag: IBSCBS/CST)  
que possui indicador que não permite a informação do 
IBS/CBS 
Obrig. 366 Rej. Rejeição: CST informado ou compras governamentais 
obriga informação de redução de alíquota estadual 
009
a 
Se informado grupo de Redução de Alíquota para IBS 
Estadual (gIBSUF/gRed): 
 
Verificar se percentual de Redução de Alíquota 
(pRedAliq) é válido para o cClassTrib informado 
(gIBSCBS/cClassTrib) 
Obrig. 389 Rej. Rejeição: Percentual de redução de alíquota da UF 
não é válido para este cClassTrib 
009
b 
Se informado grupo de Redução de Alíquota para IBS 
Estadual (gIBSUF/gRed), a Alíquota Efetiva (tag: 
pAliqEfet) deve ser o resultado de: 
Se NÃO houver compra governamental (grupo 
gCompraGov não informado):  
Obrig. 390 Rej. Rejeição: Valor da Alíquota Efetiva do IBS da UF 
calculado incorretamente

## Página 10

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 10 / 21 
 
pAliqEfet = pIBSUF × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo gCompraGov 
informado): 
pAliqEfet = pIBSUF × (1 - pRedAliq /100) × (1 - 
pRedutor/100). 
Observação: pRedutor é obtido no grupo 
gCompraGov 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E):  
E = A × (1 – R/100) × (1 – RG/100) = 5,7. 
010 Se CST informado possuir indicador que VEDA a 
informação de redução de alíquota para o IBS 
Estadual, o grupo gRed NÃO DEVE estar informado 
 
Exceção: Se Percentual de redução de alíquota em 
compra governamental (tag:gCompraGov/pRedutor) 
informado, este grupo é exigido e pRed deve ser igual 
a 0. 
Obrig. 367 Rej. Rejeição: CST informado não permite informação de 
redução de alíquota estadual 
011 Se CST informado possuir indicador que EXIGE 
informação de Diferimento para o IBS Estadual, o 
grupo gDif DEVE estar informado 
Obrig. 319 Rej. Rejeição: CST informado obriga informação de 
diferimento Estadual 
012 Se CST informado possuir indicador que VEDA 
informação de Diferimento para o IBS Estadual, o 
grupo gDif NÃO DEVE estar informado 
Obrig. 368 Rej. Rejeição: CST informado não permite informação de 
diferimento Estadual 
013 Se informado grupo do Diferimento (gIBSUF/gDif): 
O valor do Diferimento (vDif) deverá ser resultante de: 
vDif = vBC x (pIBSUF/100) x (pDif/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Obrig. 320 Rej. Rejeição: Valor do Diferimento da UF difere do 
calculado 
013 
a 
Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior a vBC x (pIBSUF/100) 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Obrig. 395 Rej. Rejeição: Valor do IBS UF não pode resultar 
negativo 
014  Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor do IBS (vIBSUF) deverá ser resultante de: 
vIBSUF = vBC x (pIBSUF/100) – vDif - vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Obrig. 318 Rej. Rejeição: Valor do IBS UF difere do calculado 
015 Se informado grupo IBS de competência dos 
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
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Município inválida

## Página 11

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 11 / 21 
 
017 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o IBS 
Municipal ou informado grupo de compra 
governamental, o grupo gRed DEVE estar informado 
 
Exceção: A regra não se aplica para CST do IBS/CBS 
(tag: IBSCBS/CST)  
que possui indicador que não permite a informação do 
IBS/CBS 
Obrig. 369 Rej. Rejeição: CST informado ou compras 
governamentais obriga informação de redução de 
alíquota municipal 
017
a 
Se informado grupo de Redução de Alíquota para IBS 
Municipal (gIBSMun/gRed): 
Verificar se percentual de Redução de Alíquota 
(pRedAliq) é válido para o cClassTrib informado 
(gIBSCBS/cClassTrib) 
Obrig. 391 Rej. Rejeição: Percentual de redução de alíquota do 
Município não é válido para este cClassTrib 
017
b 
Se informado grupo de Redução de Alíquota para IBS 
Municipal (gIBSMun/gRed), a Alíquota Efetiva (tag: 
pAliqEfet) deve ser o resultado de: 
 
Se NÃO houver compra governamental (grupo 
gCompraGov não informado):  
pAliqEfet = pIBSMun × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo 
gCompraGov informado): 
pAliqEfet = pIBSMun × (1 - pRedAliq /100) × (1 - 
pRedutor/100). 
 
Observação: pRedutor é obtido no grupo 
gCompraGov 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E):  
E = A × (1 – R/100) × (1 – RG/100) = 5,7. 
Obrig. 392 Rej. Rejeição: Valor da Alíquota Efetiva do IBS do 
Município calculado incorretamente 
018 Se CST informado possuir indicador que VEDA a 
informação de redução de alíquota para o IBS 
Municipal, o grupo gRed NÃO DEVE estar informado 
 
Exceção: Se Percentual de redução de alíquota em 
compra governamental (tag:gCompraGov/pRedutor) 
informado, este grupo é exigido e pRed deve ser igual 
a 0. 
Obrig. 381 Rej. Rejeição: CST informado não permite informação de 
redução de alíquota municipal 
019 Se CST informado possuir indicador que EXIGE 
informação de Diferimento para o IBS Municipal, o 
grupo gDif DEVE estar informado 
Obrig. 324 Rej. Rejeição: CST informado obriga informação de 
diferimento Municipal 
020 Se CST informado possuir indicador que VEDA 
informação de Diferimento para o IBS Municipal, o 
grupo gDif NÃO DEVE estar informado 
Obrig. 382 Rej. Rejeição: CST informado não permite informação de 
diferimento Municipal 
021 Se informado grupo do Diferimento (gIBSMun/gDif): 
O valor do Diferimento (vDif) deverá ser resultante de 
vDif = vBC x (pIBSMun/100) x (pDif/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 325 Rej. Rejeição: Valor do Diferimento do Município difere do 
calculado 
022 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do IBS (vIBSMun) deverá ser resultante de: 
vIBSMun = vBC x (pIBSMun/100) – vDif - vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
 
Obrig. 323 Rej. Rejeição: Valor do IBS Municipal difere do calculado

## Página 12

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 12 / 21 
 
022 
a 
Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior a vBC x (pIBSMun/100) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 396 Rej. Rejeição: Valor do IBS Municipal não pode resultar 
negativo 
022
b 
Se informados grupos IBS de competência dos 
Estados (gIBSUF) e Municípios (gIBSMun): 
O valor do total de IBS (vIBS) deverá ser a soma do 
vIBSUF e do vIBSMUn 
vIBS = vIBSUF + vIBSMun 
Obrig. 317 Rej. Rejeição: Total de IBS difere do calculado 
023 Se informado grupo CBS (gCBS): 
A alíquota de CBS deverá ser: 
 0,90 % para documento com data de 
emissão no ano de 2026. (Art. 343 da LC 
214/25) 
 Alíquota de referência a ser publicada para 
anos posteriores a 2026 
 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser 
igual a zero quando a condição abaixo for atendida: 
 
CTe ou CTeOS (Não se aplica a CTe Simplificado) 
 
Município do Emitente, Início e Fim da Prestação do 
Serviço de transporte devem estar na mesma área 
incentivada (ou seja, dentro da ZFM, na mesma ALC), 
conforme relação abaixo: 
      - ZFM: AC-Acre, AM-Amazonas, RO-Rondônia, 
RR-Roraima, AP-Amapá (só para municípios 
1600303-Macapá e 1600600-Santana); 
 
      - ALC: conforme tabela abaixo: 
Município Início Município Fim 
1304062-Tabatinga 1304062-Tabatinga 
1600303-Macapá 1600303-Macapá 
1600303-Macapá 1600600-Santana 
1600600-Santana 1600303-Macapá 
1600600-Santana 1600600-Santana 
1100106-Guajará-Mirim 1100106-Guajará-Mirim 
1400100-Boa Vista 1400100-Boa Vista 
1400100-Boa Vista 1400456-Paracaima 
1400456-Paracaima 1400100-Boa Vista 
1400456-Paracaima 1400456-Paracaima 
1400159-Bonfim 1400159-Bonfim 
1200104-Brasileia 1200104-Brasileia 
1200104-Brasileia 1200252-Epitaciolândia 
1200252-Epitaciolândia 1200104-Brasileia 
1200252-Epitaciolândia 1200252-Epitaciolândia 
1200203-Cruzeiro do Sul 1200203-Cruzeiro do Sul 
 
O Município do Emitente tem que estar também em 
uma área incentivada. 
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 13

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 13 / 21 
 
024 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o CBS ou 
informado grupo de compra governamental, o grupo 
gRed DEVE estar informado 
 
Exceção: A regra não se aplica para CST do IBS/CBS 
(tag: IBSCBS/CST)  
que possui indicador que não permite a informação do 
IBS/CBS 
Obrig. 383 Rej. Rejeição: CST informado ou compras 
governamentais obriga informação de redução de 
alíquota do CBS 
024
a 
Se informado grupo de Redução de Alíquota para 
CBS (gCBS/gRed): 
 
Verificar se percentual de Redução de Alíquota 
(pRedAliq) é válido para o cClassTrib informado 
(gIBSCBS/cClassTrib) 
Obrig. 393 Rej. Rejeição: Percentual de redução de alíquota da CBS 
não é válido para este cClassTrib 
024
b 
Se informado grupo de Redução de Alíquota para 
CBS (gCBS/gRed), a Alíquota Efetiva (tag: pAliqEfet) 
deve ser o resultado de: 
Se NÃO houver compra governamental (grupo 
gCompraGov não informado):  
pAliqEfet = pCBS × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo 
gCompraGov informado): 
pAliqEfet = pCBS × (1 - pRedAliq /100) × (1 - 
pRedutor/100). 
 
Observação: pRedutor é obtido no grupo 
gCompraGov 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E): E = A * (1 - R) * (1- RG) 
E = 10 * (1 - 0,4) *(1-0,05) = 5,7 
Obrig. 394 Rej. Rejeição: Valor da Alíquota Efetiva da CBS calculado 
incorretamente 
025 Se CST informado possuir indicador que VEDA a 
informação de redução de alíquota para o CBS, o 
grupo gRed NÃO DEVE estar informado 
 
Exceção: Se Percentual de redução de alíquota em 
compra governamental (tag:gCompraGov/pRedutor) 
informado, este grupo é exigido e pRed deve ser igual 
a 0. 
Obrig. 384 Rej. Rejeição: CST informado não permite informação de 
redução de alíquota do CBS 
026 Se CST informado possuir indicador que EXIGE 
informação de Diferimento para o CBS, o grupo gDif 
DEVE estar informado 
Obrig. 328 Rej. Rejeição: CST informado obriga informação de 
diferimento do CBS 
027 Se CST informado possuir indicador que VEDA 
informação de Diferimento para o CBS, o grupo gDif 
NÃO DEVE estar informado 
Obrig. 385 Rej. Rejeição: CST informado não permite informação de 
diferimento do CBS 
028 Se informado grupo do Diferimento (gCBS/gDif): 
O valor do Diferimento (vDif) deverá ser resultante de: 
vDif = vBC x (pCBS/100) x (pDif/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Obrig. 329 Rej. Rejeição: Valor do Diferimento do CBS difere do 
calculado 
028 
a 
Se informado grupo CBS (gCBS): 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior a vBC x (pCBS/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
 
Obrig. 397 Rej. Rejeição: Valor do CBS não pode resultar negativo

## Página 14

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 14 / 21 
 
029 Se informado grupo CBS (gCBS): 
O valor da CBS (vCBS) deverá ser resultante de: 
vCBS = vBC x (pCBS/100) – vDif – vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet). 
Obrig. 327 Rej. Rejeição: Valor do CBS difere do calculado 
030 Se cClassTrib informado possuir indicador que EXIGE 
informação de tributação regular, o grupo 
gTribRegular DEVE estar informado 
Obrig. 330 Rej. Rejeição: Classificação Tributária informada obriga 
informação da tributação regular  
030 
a 
Se cClassTrib informado NÃO POSSUIR indicador de 
informação de tributação regular, o grupo 
gTribRegular NÃO DEVE estar informado 
Obrig. 322 Rej. Rejeição: Classificação Tributária não permite 
informação da tributação regular 
031 Se informado grupo da tributação regular 
(gTribRegular): 
O CST Regular informado no grupo gTribRegular deve 
existir na tabela de Código de Situação Tributária 
(gTribRegular/CSTReg) 
Obrig. 331 Rej. Rejeição: CST informado no grupo de tributação 
regular inexistente 
032 Se informado grupo da tributação regular 
(gTribRegular): 
O cClassTrib regular for informado, este deve existir 
na tabela de Classificação Tributária do IBS/CBS (tag: 
gTribRegular/cClassTribReg) 
Obrig. 332 Rej. Rejeição: Classificação Tributária informada no grupo 
de tributação regular inexistente 
033 Se informado grupo da tributação regular 
(gTribRegular): 
O valor do tributo regular de IBS dos Estados 
(vTribRegIBSUF) deverá ser resultante de: 
vTribRegIBSUF = vBC x (pAliqEfetRegIBSUF/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos  
Obrig. 333 Rej. Rejeição: Valor da tributação regular da UF difere do 
calculado 
034 Se informado grupo da tributação regular 
(gTribRegular): 
O valor do tributo regular de IBS dos Municípios 
(vTribRegIBSMun) deverá ser resultante de: 
vTribRegIBSMun = vBC x (pAliqEfetRegIBSMun/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 334 Rej. Rejeição: Valor da tributação regular do Município 
difere do calculado 
035 Se informado grupo da tributação regular 
(gTribRegular): 
O valor do tributo regular de CBS (vTribRegCBS) 
deverá ser resultante de: 
vTribRegularCBS = vBC x (pAliqEfetRegCBS/100) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 335 Rej. Rejeição: Valor da tributação regular da CBS difere 
do calculado 
049 Se grupo compra governamental (grupo: 
gCompraGov) estiver informado, o Grupo de 
informações da composição do valor do IBS e da CBS 
em compras governamentais (grupo: 
gTribCompraGov) DEVE ser informado. 
Exceção: A regra não se aplica para CST do IBS/CBS 
(tag: IBSCBS/CST)  
que possui indicador que não permite a informação do 
IBS/CBS 
Obrig. 398 Rej. Rejeição: Grupo de informações da composição do 
valor do IBS e da CBS em compras governamentais 
deve ser informado 
050 Se grupo compra governamental (grupo: 
gCompraGov) NÃO estiver informado, o Grupo de 
informações da composição do valor do IBS e da CBS 
em compras governamentais (grupo: 
gTribCompraGov) NÃO DEVE ser informado. 
Obrig. 399 Rej, Rejeição: Grupo de informações da composição do 
valor do IBS e da CBS em compras governamentais 
não deve ser informado 
051 Verificar se a soma dos valores de IBS e CBS do 
grupo gTribCompraGov (vTribIBSUF + vTribIBSMun + 
vTribCBS) é diferente do resultado de gIBSUF/vIBSUF 
+ gIBSMun/vIBSMun + gCBS/vCBS. 
Obrig. 400 Rej. Rejeição: Somas dos valores de IBS e CBS em 
compras governamentais divergente 
052 Se o cClassTrib informado possuir indicador que 
VEDA preenchimento do grupo de informações do 
estorno de crédito (grupo:gEstornoCred) 
Obrig 303 Rej.  Rejeição: Grupo Estorno de Crédito não deve ser 
preenchido para o cClassTrib informado 
053 Se o cClassTrib informado possuir indicador que 
EXIGE preenchimento do grupo de informações do 
estorno de crédito (grupo:gEstornoCred) 
Obrig 304 Rej. Rejeição: Grupo Estorno de Crédito deve ser 
preenchido para o cClassTrib informado

## Página 15

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 15 / 21 
 
6 Criação do grupo de compras governamentais no grupo ide 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# gCompraGov G ide - 0-1 -  
 tpEnteGov E gCompraGov N 1-1 1 Para administração pública direta e suas autarquias 
e fundações: 
1=União 
2=Estados 
3=Distrito Federal 
4=Municípios 
5=Consórcio Público 
6=Comitê Gestor do IBS 
 pRedutor E gCompraGov N 1-1 3v2-4 Percentual de redução de alíquota em compra 
governamental 
Conforme LC 214/25: TÍTULO II 
DAS COMPRAS GOVERNAMENTAIS, Art. 472 
 tpOperGov E gCompraGov N 1-1 1 Tipo da operação com ente governamental: 
1 – Fornecimento com pagamento posterior; 
2 - Recebimento do pagamento com fornecimento já 
realizado; 
3 – Fornecimento com pagamento já realizado; 
4 – Recebimento do pagamento com fornecimento 
posterior; 
 refDFeAnt E gCompraGov C 0-n 44 Chave de acesso do documento fiscal anterior. 
Deverá ser informado para tpOperGov 2 e 3 e 
vedado para os tipos 1 e 4 
Obs: a chave de acesso deverá ser de um emitente 
com o mesmo CNPJ base 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado o grupo de informações de compra 
governamental (grupo:ide\gCompraGov) e tipo do Ente 
(gCompraGov\tpEntGov) diferente de 5 e 6, o DFe de 
compra governamental deve ter alíquota de outros 
entes igual a zero. 
De 2027 até 2032 
Para compra da união (tag: tpEnteGov = 1): 
 Alíquota do IBS da UF (tag: pIBSUF) deve 
ser igual a zero. 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
Para compra estadual (tag: tpEnteGov = 2): 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
Para compra do DF (tag: tpEnteGov = 3) 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
Para compra municipal (tag: tpEnte = 4) 
 Alíquota do IBS da UF (tag: pIBSUF) deve 
ser igual a zero. 
A partir de 2033: 
Para compra da união (tag: tpEnteGov = 1): 
 Alíquota do IBS da UF (tag: pIBSUF) deve 
ser igual a zero. 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
Para compra estadual (tag: tpEnteGov = 2): 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
 Alíquota do CBS (tag: pCBS) deve ser igual 
a zero. 
Para compra do DF (tag: tpEnteGov = 3) 
 Alíquota do IBS do Município (tag: pIBSMun) 
deve ser igual a zero. 
 Alíquota do CBS (tag: pCBS) deve ser igual 
a zero. 
Para compra municipal (tag: tpEnte = 4) 
 Alíquota do IBS da UF (tag: pIBSUF) deve 
ser igual a zero. 
Obrig. 347 Rej. Rejeição: DFe de compra governamental e alíquota 
dos outros entes diferentes de zero.

## Página 16

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 16 / 21 
 
 Alíquota do CBS (tag: pCBS) deve ser igual 
a zero. 
Observação: Conforme Art. 473, § 1o e seus Incisos I, 
II, III e IV da LC 214/2025. 
002 Se o tipo da operação com ente governamental for 
igual a Fornecimento com pagamento posterior 
(tpOperGov=1) 
A chave de acesso do DFe anterior (refDFeAnt) NÃO 
DEVE ser informada 
Obrig 1004 Rej Rejeição: Chave de acesso referenciada não deve 
ser informada para tipo de operação de 
Fornecimento em compras governamentais 
003 Se o tipo da operação com ente governamental for 
igual a Recebimento do pagamento com fornecimento 
já realizado (tpOperGov=2) 
Deve ser informada UMA chave de acesso de DFe 
referenciado 
 
Observação: Se forem informadas múltiplas chaves de 
acesso ou nenhuma chave causará essa rejeição 
Obrig 1005 Rej Rejeição: Deverá ser informada uma chave de 
acesso de DFe referenciado para tipo de operação 
de Recebimento do pagamento com fornecimento 
realizado em compras governamentais 
004 Se o tipo da operação com ente governamental for 
igual a Fornecimento com pagamento já realizado 
(tpOperGov=3) 
Uma ou mais chaves de acesso de DFe anteriores 
(refDFeAnt) DEVEM ser informadas 
Obrig 1006 Rej Rejeição: Pelo menos uma Chave de acesso de 
DFe referenciado deve ser informada para tipo de 
operação fornecimento com pagamento já realizado 
em compras governamentais 
005 Se o tipo da operação com ente governamental for 
igual a Recebimento do pagamento com fornecimento 
posterior (tpOperGov=4) 
A chave de acesso do DFe anterior (refDFeAnt) NÃO 
DEVE ser informada 
Obrig 1007 Rej Rejeição: Chave de acesso referenciada não deve 
ser informada para tipo de operação recebimento do 
pagamento com fornecimento posterior em compras 
governamentais 
006 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt), para cada 
chave informada: 
- Validar chave de acesso do DFe referenciado.  
Retornar motivo da rejeição da Chave de Acesso: 
CNPJ zerado ou inválido, Ano, Mês inválido (0 ou > 
12), Modelo de DFe diferente, Número zerado, Tipo de 
emissão inválido, UF inválida ou DV inválido) 
[Motivo: XXXXXXXXXXXX] 
Obrig. 1008 Rej. Rejeição: Chave de acesso referenciada em 
compras governamentais inválida 
007 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt): 
- O DFe referenciado deve existir, acesso BD (Chave: 
CNPJ Emit, Modelo, Série, Nro) 
Obrig 1009 Rej Rejeição: DFe referenciado em compras 
governamentais inexistente 
008 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt), para cada 
chave informada: 
- DFe referenciado não pode existir com diferença na 
Chave de Acesso 
Retornar a chave de acesso já autorizada, o número do 
protocolo e data de autorização do DFe 
[chDFe: 
99999999999999999999999999999999999999999999
] 
[nProt:999999999999999][dhAut: AAAA-MM-
DDTHH:MM:SS TZD] 
Obrig. 1010 Rej. Rejeição: DFe referenciado em compras 
governamentais com diferença de Chave de Acesso 
009 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt), para cada 
chave informada: 
- O DFe referenciado deve estar em situação 
Autorizado o Uso 
 
Observação:  Rejeitar se documento estiver cancelado 
ou substituído na base de dados do ambiente de 
autorização 
Obrig. 1011 Rej Rejeição: DFe referenciado em compras 
governamentais em situação inválida

## Página 17

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 17 / 21 
 
010 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt), para cada 
chave informada: 
- O emitente do DFe referenciado deve ter o mesmo 
CNPJ Base do emitente do documento fiscal 
Exceção: os casos de alteração do CNPJ da empresa 
por motivo de aquisição, fusão, incorporação deve ser 
tratados no ambiente de autorização 
Obrig. 1012 Rej Rejeição: DFe referenciado em compras 
governamentais deve possuir mesmo CNPJ base do 
emitente do documento 
011 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt) e tipo de 
operação for Recebimento do pagamento com 
fornecimento já realizado; (tpOperGov = 2), para cada 
chave informada: 
- O DFe referenciado deve ser de compras 
governamentais e possuir o tipo de operação 
Fornecimento com pagamento posterior (tpOperGov = 
1) 
Obrig. 1013 Rej. Rejeição: DFe referenciado em compras 
governamentais deve ser de Fornecimento com 
pagamento posterior 
012 Se informado documento anterior no grupo de compras 
governamentais (gCompraGov/refDFeAnt) e tipo de 
operação for de Fornecimento com pagamento já 
realizado (tpOperGov = 3), para cada chave informada: 
- O DFe referenciado deve ser de compras 
governamentais e possuir o tipo de operação 
Recebimento do pagamento com fornecimento 
posterior (tpOperGov = 4) 
Obrig. 1014 Rej. Rejeição: DFe referenciado em compras 
governamentais deve ser de operação de 
Recebimento do pagamento com fornecimento 
posterior 
7 Total Geral do Documento Fiscal Eletrônico 
Deverá ser criada a tag Valor Total do DFe (vTotDFe). 
No CTe, CTe Simplificado, CTe OS essa tag aparecerá dentro do grupo imp, após o grupo IBSCBS. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E imp E 0-1 13,2 Valor total do documento fiscal  
vTPrest + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 A tag de Total do Documento Fiscal Eletrônico 
deverá ser informada (tag: imp\vTotDFe) sempre 
que existir informação no grupo IBSCBS (grupo: 
imp\IBSCBS) 
Obrig. 360 Rej. Rejeição: Total do DFe de preenchimento obrigatório 
02 O total geral do DFe deverá ser INFORMADO 
com a soma do total da prestação + IBS + CBS 
vTotDFe = vPrest/vTPrest + gIBSCBS/vIBS + 
gCBS/vCBS 
Exceção: Em 2026 não somar IBS e CBS, usando 
a fórmula:  
vTotDFe = vPrest/vTPrest  
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
8 Alteração em Regra do CTe Simplificado 
G101a O município de fim de prestação em todos os itens do 
CTe Simplificado (det:cMunFim) devem ser iguais  
Obrig. 370 Rej. Rejeição: O CTe Simplificado deve ter a 
prestação terminada em apenas um 
município

## Página 18

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 18 / 21 
 
9 Alterações no Layout do Modal Dutoviário 
Foram criados campos no schema específico do Modal Dutoviário. 
# Campo Nível Descrição Ele Tipo Ocorr. Tam Observações 
1 duto 0 Informações do modal Dutoviário G  1 - 1   
2 vTar 1 Valor da tarifa E C 0 - 1 9, 6 15 posições, sendo 9 inteiras e 6 
casas decimais. 
3 dIni 1 Data de Início da prestação do serviço E D 1 - 1 10  
4 dFim 1 Data de Fim da prestação do serviço E D 1 - 1 10  
5 classDuto 1 Classificação Dutoviário E N 0-1 1 Informar:  
1 – Gasoduto;  
2 – Mineroduto ou 
3 - Oleoduto 
6 tpContratacao 1 Tipo de contratação do serviço de 
transporte (apenas para gasoduto) 
E N 0-1 1 Informar:  
0 – Ponto a ponto 
1 – Capacidade de Entrada ou  
2 – Capacidade de Saída 
7 codPontoEntrada 1 Código do Ponto de Entrada E C 0-1 20  
8 codPontoSaida 1 Código do Ponto de Saída E C 0-1 20  
9 nContrato 1 Número do Contrato de Capacidade E C 0-1 20  
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado classificação do dutoviário = Gasoduto 
(tag: classDuto = 1), o tipo de contratação deve ser 
informado (tag: tpContratacao) 
Obrig. 371 Rej. Rejeição: Tipo de contratação deve ser informado 
para tipo de dutoviário gasoduto 
002 Se Tipo de contratação for ponto a ponto (tag: 
tpContratacao=0), os campos do código dos pontos de 
entrada e saída devem ser informados 
Obrig. 372 Rej. Rejeição: Dutoviário com tipo de contratação ponto 
a ponto deve informar Código dos pontos de entrada 
e saída 
003 Se Tipo de contratação for capacidade de entrada 
(tag: tpContratacao=1), o campo do código do ponto 
de entrada deve ser informado 
Obrig. 373 Rej. Rejeição: Dutoviário com tipo de contratação 
capacidade de entrada deve informar Código do ponto 
de entrada  
004 Se Tipo de contratação for capacidade de saída (tag: 
tpContratacao=2), o campo do código do ponto de 
saída deve ser informado 
Obrig. 374 Rej. Rejeição: Dutoviário com tipo de contratação 
capacidade de saída deve informar Código do ponto 
de saída 
 
 
10 Criação do grupo de informações da DCe nos documentos originários 
Validações dos Documentos Transportados 
G045a Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informado grupo informação de documentos (infDoc): 
Quantidade de documentos informados 
(infNF/infNFe/infOutros/infDCe) não pode ultrapassar 
2000 documentos 
Obrig. 601 Rej. Rejeição: Quantidade de documentos 
informados no remetente excede limite de 
2000 
G045b Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e Obrig. 375 Rej. Rejeição: DCe duplicada no CTe

## Página 19

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 19 / 21 
 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe) 
- Verificar se existe alguma chave de acesso de DCe 
duplicada no CTe 
Retornar a chave duplicada 
[chDCe: 
9999999999999999999999999999999999
9999999999] 
G045c Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe), para cada uma das DCe´s 
relacionadas: 
- Validar chave de acesso  
Retornar a primeira chave inválida e o motivo da 
rejeição da Chave de Acesso: CNPJ / CPF zerado ou 
inválido, Ano < 2025 ou maior que atual, Mês inválido (0 
ou > 12), Modelo diferente de 99, Número zerado, Tipo 
de emissão inválido, UF inválida ou DV inválido) 
[chDCe: 
99999999999999999999999999999999999999999999] 
[Motivo: XXXXXXXXXXXX] 
Obrig. 376 Rej. Rejeição: Chave de acesso da DCe 
transportada inválida 
G045d Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe), para cada uma das DCe´s 
relacionadas: 
 - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF 
Emit, Modelo, Série, Nro): 
            - A DCe deve existir 
Retornar a primeira chave de acesso de DCe 
inexistente. 
Exceção: DCe em contingência fica dispensada dessa 
validação (verificar tpEmis da chave de acesso da DCe)  
Facult. 377 Rej. Rejeição: DCe inexistente na base de 
dados da SEFAZ 
G045e Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe), para cada uma das DCe´s 
relacionadas: 
 - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF 
Emit, Modelo, Série, Nro): 
            - A DCe não pode existir com diferença de chave 
de acesso 
Retornar a primeira chave de acesso de DCe com 
situação inválida. 
Facult. 378 Rej. Rejeição: DCe com diferença de Chave de 
Acesso 
G045f Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe), para cada uma das DCe´s 
relacionadas: 
 - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF 
Emit, Modelo, Série, Nro): 
            - A DCe não pode estar cancelada 
Retornar a primeira chave de acesso de DCe com 
situação inválida. 
Facult. 379 Rej. Rejeição: DCe não pode estar cancelada 
ou denegada 
 
As regras G45d, G45e e G45f dependem do ambiente de autorização do CTe possuir acesso a base de dados de 
DCe.

## Página 20

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 20 / 21 
 
11 Exceção para Substituição sem exigência do evento de prestação em 
desacordo para tomador Exterior 
A exigência do registro do tomador de prestação de serviço em desacordo para permitir a substituição de um CTe 
se torna impeditiva quando o tomador for pessoa do exterior, uma vez que esta não tem meios para autorizar o 
evento. 
G084/ 
H067 
Se Tipo do CTe=3 (Substituição): 
- O CTe substituído deve possuir evento de Prestação do 
Serviço em Desacordo em situação autorizado. 
 
Observação: Eventos de Cancelamento do Evento de 
Prestação em desacordo anulam eventos de Prestação 
em Desacordo 
Exceção: O evento não será exigido para CTe com 
tomador do exterior 
Obrig
. 
739 Rej. Rejeição: O CTe substituído deve possuir 
evento de Prestação do Serviço em 
Desacordo  
12 Ajuste na regra que define prazo para CTe Complementar 
G161a 
H102a 
 
Se Tipo do CTe= 1 (Complementar), para cada chave 
de CTe informado: 
Verificar se o Ano/Mês da chave de acesso são 
anteriores a 12 meses da Data de Autorização do CTe 
 
Exceção: Em caso de modal ferroviário ou multimodal 
permitir até 24 meses da Data de Autorização do CTe 
Obrig. 933 Rej. Rejeição: Chave de acesso do CTe 
complementado muito antiga 
[chCTe: 
99999999999999999999999999999999999
999999999] 
13 Eliminar as opções de contingência SVC da GTVe no Leiaute (Schema) 
A GTVe já possui previsão de emissão offline, portanto não há necessidade do schema e do ambiente de 
autorização suportar emissão em contingência SVC 
Alteração: tag tpEmis aceita apenas os valores 1 – Normal e 2- Contingência offline  
14 Nova regra para CTe OS de Transporte de Valores 
Devido a apuração do imposto na reforma tributária ser em razão da UF e município de destino, o CTe OS de 
Transporte de Valores deverá passar a exigir essas informações. 
H020a Se tipo de serviço = Transporte de Valores 
- UF de fim e Município de Fim da prestação devem estar 
preenchidos 
Observação: Esta regra será aplicada em produção 
somente a partir de 05/01/2026 
Obrig. 380 Rej. Rejeição: UF e Município de Fim da 
prestação devem estar preenchidas para 
Transporte de Valores 
15 Ajuste em regras de validação do tomador Contribuinte Isento de IE 
G024 Rejeitar quando informado tomador como Contribuinte 
Isento de Inscrição Estadual (indIEToma=2) em UF que 
não permite esta situação, conforme abaixo: 
AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ 
Obrig. 617 Rej. Rejeição: UF do tomador não aceita 
ISENTO com Inscrição Estadual 
H093 Rejeitar quando informado tomador como Contribuinte 
Isento de Inscrição Estadual (indIEToma=2) em UF que 
não permite esta situação, conforme abaixo: 
AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ 
Obrig. 617 Rej. Rejeição: UF do tomador não aceita 
ISENTO com Inscrição Estadual 
 
I15 Rejeitar quando informado tomador como Contribuinte Isento de Inscrição 
Estadual  
(indIEToma=2) em UF que não permite esta situação, conforme abaixo:
 AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ 
Obrig. 617 Rej. Rejeição: UF do tomador não aceita 
ISENTO com Inscrição Estadual 
 
16 Preparação das expressões regulares do CTe para o futuro CNPJ 
Alfanumérico

## Página 21

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.14 a 
 
 
Página 21 / 21 
 
As alterações serão feitas no arquivo de tipos gerais e aplicam-se automaticamente a todos campos do tipo CNPJ 
e Chave de acesso em qualquer um dos schemas do projeto CTe, entretanto, até que seja publicada uma Nota 
Técnica que modifica as validações desses campos, as letras não devem ser utilizadas. 
 
A expressão regular que valida um campo do tipo CNPJ é: [0-9]{14} 
Alteração: a Expressão regular do CNPJ passa a aceitar letras maiúsculas nas primeiras 12 posições:  
[A-Z0-9]{12}[0-9]{2} 
 
Expressão Regular Atual da Chave de Acesso é: [0-9]{44} 
Alteração: a expressão regular passa a suportar letras maiúsculas nas 12 primeiras posições que correspondem 
ao CNPJ dentro da chave de acesso: [0-9]{6}[A-Z0-9]{12}[0-9]{26} 
A expressão regular do QR Code também seguirá essa regra de formação na parte da chave de acesso. 
17 Ampliação do cStat de retorno para 4 dígitos 
A expressão regular que define a tag cStat dos schemas de retorno de todos os serviços passa a suportar até 
códigos com 4 dígitos. 
 
Nova expressão regular para o tipo TStat do arquivo Tipos Geral: [0-9]{3,4}
