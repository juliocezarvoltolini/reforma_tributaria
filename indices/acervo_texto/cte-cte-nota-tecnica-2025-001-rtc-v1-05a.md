---
id: cte-cte-nota-tecnica-2025-001-rtc-v1-05a
titulo: Nota Técnica CTe - Nota_Técnica_2025_001 - RTC_v1.05a - Publicada em 16/06/2025
tipo: nota.tecnica
versao: 1.05a
data: '2025-06-16'
documento_fiscal: CT-e/CT-e OS/GTV-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=byB0EHEkAyM=
arquivo_original: fontes/acervo/cte-cte-nota-tecnica-2025-001-rtc-v1-05a.pdf
sha256_original: 2e84d3cdd519a3605705dcb2905e4b4eca26acdca94e1c5881062aa4298efeae
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 47652beb74275c641ecbdb70855b4151708c194fdbd9be8c9e61a871aa9e56bb
---

## Página 1

Projeto Conhecimento de 
Transporte Eletrônico 
 
Nota Técnica 2025.001 – Reforma Tributária do Consumo 
Versão 1.05 a de 13 de junho de 2025

## Página 2

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 2 / 19 
 
Sumário 
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Tipos básicos da tributação ............................................................................................. 4 
3 Alteração do leiaute do imposto do CTe .......................................................................... 5 
4 Código de Classificação Tributária do IBS/CBS .............................................................. 7 
5 Validações dos campos do IBS e CBS ............................................................................ 7 
6 Criação do grupo de compras governamentais no grupo ide ......................................... 13 
7 Total Geral do Documento Fiscal Eletrônico ................................................................. 14 
8 Alteração em Regra do CTe Simplificado ...................................................................... 14 
9 Alterações no Layout do Modal Dutoviário .................................................................... 14 
10 Criação do grupo de informações da Declaração de Conteúdo Eletrônica nos 
documentos originários ........................................................................................................ 15 
11 Exceção para Substituição sem exigência do evento de prestação em desacordo 
para tomador Exterior ........................................................................................................... 16 
12 Ajuste na regra que define prazo para CTe Complementar ....................................... 16 
13 Eliminar as opções de contingência SVC da GTVe no Leiaute (Schema) .................. 17 
14 Nova regra para CTe OS de Transporte de Valores .................................................. 17 
15 Preparação das expressões regulares do CTe para o futuro CNPJ Alfanumérico ..... 17 
16 Ampliação do cStat de retorno para 4 dígitos ............................................................ 17 
17 Anexo – Novos Grupos para Reforma Tributária ....................................................... 18 
Conhecimento de Transporte Eletrônico– modelo 57 ........................................................ 18 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 ................................... 19 
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67 ........................... 19

## Página 3

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 3 / 19 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Previsão das informações do IBS/CBS no CTe 
 Alteração de regras do CTeOS Transporte Valores exigir UF e Mun 
Fim 
 Alteração das regras do CTe Simplificado para limitar em apenas 
um fim de prestação 
 Alteração no leiaute do Dutoviário 
 Exceção para não exigir evento de prestação em desacordo na 
substituição de tomador do EX 
 Preparação das Expressões Regulares do CNPJ Alfa 
 Eliminação da SVC para GTVe 
 Inclusão da DCe nos documentos originários 
 Ampliação do código de retorno das mensagens suportar até 4 
dígitos (cStat) 
  
1.01  Correções e orientações sobre aplicação das regras de validação 
nos ambientes 
 Renumeração das regras de rejeição 
 Ajuste no grupo de Tributação regular 
 Ajuste na regra do CTe Complementar para Multimodal 
  
1.02  Ajustes nas regras do crédito presumido e tributação regular 
 Ajuste nas regras para Crédito Presumido Condição Suspensiva 
no grupo do crédito presumido 
  
1.03  Ajustes nas regras de compras governamentais, redução de 
alíquota e valores de IBS/CBS 
 Correção no schema dos eventos tipos básicos 
  
1.04  Ajustes em regras de validação e mensagens   
1.05  Ajuste na regra de compras governamentais e exigência do 
grupo de tributação para SN  
 Novo grupo de informações da tributação para compras 
governamentais no grupo IBSCBS 
Até 28/07/2025 06/10/2025 
1.05 a  Correção de datas no texto da introdução Até 28/07/2025 06/10/2025 
 
Observação: No ambiente de produção as Regras de Validação serão aplicadas somente em 
05 de janeiro de 2026.

## Página 4

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 4 / 19 
 
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
opcionais e validadas apenas se forem informadas. A partir de janeiro de 2026, as novas regras de validação 
referentes a tributação do IBS e da CBS serão aplicadas. 
 
Esta documentação descreve as alterações aplicadas aos Documentos: 
 Conhecimento de Transporte Eletrônico (modelo 57); 
 Conhecimento de Transporte Eletrônico para Outros Serviços (modelo 67); 
 
2 Tipos básicos da tributação 
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos, esta NT introduz o arquivo 
DFeTiposBasicos_v1.00.xsd ao conjunto dos arquivos que compõem do schema da DFe. 
 
Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro das 
informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no leiaute padrão da DFe 
conforme estrutura abaixo:

## Página 5

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 5 / 19 
 
3 Alteração do leiaute do imposto do CTe 
Este grupo de informações facultativas deve ser adicionado ao final do grupo imposto do CTe, CTe Simplificado e 
CTe OS. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBS G imposto - 0-1 - Grupo de informações da Tributação IBS/CBS 
1 CST E IBSCBS N 1-1 3 Código da Situação Tributária do IBS/CBS 
2 cClassTrib E IBSCBS N 1-1 6 Código da Classificação Tributária do IBS/CBS 
3 gIBSCBS G IBSCBS - 0-1 - Grupo de informações específicas do IBS/CBS 
4 vBC E gIBSCBS N 1-1 13,2 Valor da Base de cálculo comum a IBS/CBS 
5 gIBSUF G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
das Unidades Federadas 
6 pIBSUF E gIBSUF N 1-1 3,2/3,4 Alíquota do IBS Estadual 
7 gDif G gIBSUF - 0-1 - Grupo de campos do diferimento 
8 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
9 vDif E gDif N 1-1 13,2 Valor do diferimento 
10 gDevTrib G gIBSUF - 0-1 - Grupo de informações da devolução de tributos 
11 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
12 gRed G gIBSUF - 0-1 - Grupo de informações da redução de Alíquota 
13 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
14 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo, incluindo o 
gCompraGov/pRedutor, se houver. 
pAliqEfet = pIBSUF*(1 – pRedAliq)*(1 -  
gCompraGov/pRedutor) 
15 vIBSUF E gIBSUF N 1-1 13,2 Valor do IBS de competência da UF 
16 gIBSMun G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
do municipio 
17 pIBSMun E gIBSMun N 1-1 3,2/3,4 Alíquota do IBS Municipal 
18 gDif G gIBSMun - 0-1 - Grupo de campos do diferimento 
19 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
20 vDif E gDif N 1-1 13,2 Valor do diferimento 
21 gDevTrib G gIBSMun - 0-1 - Grupo de informações da devolução do tributo 
22 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
23 gRed G gIBSMun - 0-1 - Grupo de informações da redução de Alíquota 
24 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
25 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo, incluindo o 
gCompraGov/pRedutor, se houver. 
pAliqEfet = pIBSUF*(1 – pRedAliq)*(1 -  
gCompraGov/pRedutor) 
26 vIBSMun E gIBSMun N 1-1 13,2 Valor do IBS de competência do município 
27 gCBS G gIBSCBS - 1-1 - Grupo de informações da CBS 
28 pCBS E gCBS N 1-1 3,2/3,4 Alíquota da CBS

## Página 6

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 6 / 19 
 
29 gDif G gCBS - 0-1 - Grupo de campos do diferimento 
30 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
31 vDif E gDif N 1-1 13,2 Valor do diferimento 
32 gDevTrib G gCBS - 0-1 - Grupo de informações da devolução do tributo 
33 vDevTrib E gDevTrib N 1-1 13,2 Valor da CBS devolvida.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
34 gRed G gCBS - 0-1 - Grupo de informações da redução de Alíquota 
35 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
36 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva da CBS que será aplicada a base 
de cálculo, incluindo o gCompraGov/pRedutor, se 
houver. 
pAliqEfet = pIBSUF*(1 – pRedAliq)*(1 -  
gCompraGov/pRedutor) 
37 vCBS E gCBS N 1-1 13,2 Valor da CBS 
38 gTribRegular G gIBSCBS - 0-1 - Grupo de informações da Tributação Regular. 
Informar como seria a tributação caso não cumprida 
a condição resolutória/suspensiva. Exemplo 1: Art. 
442, §4. Operações com ZFM e ALC. Exemplo 2: 
Operações com suspensão do tributo.. 
39 CSTReg E gTribRegular N 1-1 3 Código da Situação Tributária  
Informado como seria o CST caso não cumprida a 
condição resolutória/suspensiva 
40 cClassTribReg E gTribRegular N 1-1 6 Código de Classificação Tributária  
Informado como seria o cClassTrib caso não 
cumprida a condição resolutória/suspensiva 
41 pAliqEfetRegIBSUF E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da UF 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
42 vTribRegIBSUF E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo da UF caso 
não cumprida a condição resolutória/suspensiva 
43 pAliqEfetRegIBSMun E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva do Município 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
44 vTribRegIBSMun E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo do 
Município caso não cumprida a condição 
resolutória/suspensiva 
45 pAliqEfetRegCBS E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da CBS 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
46 vTribRegCBS E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo CBS caso 
não cumprida a condição resolutória/suspensiva 
47 gIBSCredPres G gIBSCBS - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento.  
48 cCredPres E gIBSCredPres N 1-1  Código do Crédito Presumido (ver Tabela) 
49 pCredPres E gIBSCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
50 vCredPres CE gIBSCredPres N 1-1 13,2 Valor do crédito presumido 
51 vCredPresCondSus CE gIBSCredPres N 1-1 13,2 Valor do Crédito Presumido Condição Suspensiva 
Preencher apenas para cCredPres com indicação 
de Condição Suspensiva 
52 gCBSCredPres G gIBSCBS - 0-1 - Grupo de Informações do Crédito Presumido, 
quando aproveitado pelo emitente do documento.  
53 cCredPres E gCBSCredPres N 1-1  Código do Crédito Presumido (ver Tabela) 
54 pCredPres E gCBSCredPres N 1-1 3,2/3,4 Percentual  de crédito presumido 
55 vCredPres CE gCBSCredPres N 1-1 13,2 Valor do crédito presumido 
56 vCredPresCondSus CE gCBSCredPres N 1-1 13,2 Valor do Crédito Presumido Condição Suspensiva 
Preencher apenas para cCredPres com indicação 
de Condição Suspensiva

## Página 7

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 7 / 19 
 
57 gTribCompraGov G gIBSCBS - 0-1 - Grupo de informações da composição do valor do 
IBS e da CBS em compras governamental 
58 pAliqIBSUF E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS da UF utilizada 
59 vTribBSUF E gTribCompraGov N 1-1 13,2 Valor do Tributo do IBS da UF 
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
5 Validações dos campos do IBS e CBS 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Não informado grupo de imposto IBS e CBS (grupo: 
imp/IBSCBS) 
Observação: Aplicar em ambiente de homologação a 
partir de 06 de outubro/25 e produção a partir de 05 de 
janeiro/26 
Exceção: Se o CRT informado pelo emitente for 1-
Simples Nacional ou 4 -MEI, o grupo IBSCBS NÃO 
será exigido 
Obrig. 310 Rej. Rejeição: IBS / CBS não informado 
002 Se CST do IBS/CBS for informado, este deve existir na 
tabela de Código de Situação Tributária (tag: 
IBSCBS/CST) 
Obrig. 311 Rej. Rejeição: CST informado inexistente 
003 Se cClassTrib for informado, este deve existir na tabela 
de Classificação Tributária do IBS/CBS (tag: 
IBSCBS/cClassTrib) 
Obrig. 312 Rej. Rejeição: Classificação Tributária informada 
inexistente

## Página 8

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 8 / 19 
 
004 Verificar se o CST informado é compatível com o 
cClassTrib 
Obrig. 313 Rej. Rejeição: Classificação Tributária incompatível com 
o CST informado 
004
a 
Verificar se o CST informado (tag: IBSCBS/CST) 
possui indicador que não permite ser informado nesse 
modelo de DFe 
Obrig. 388 Rej. Rejeição: CST do IBS/CBS não permitido neste 
modelo de DFe. 
005 Se o CST informado possuir indicador que VEDA 
preenchimento do grupo de informações específicas do 
IBS/CBS, este grupo NÂO DEVE estar informado 
(grupo: gIBSCBS) 
Obrig 314 Rej. Rejeição: Grupo IBS/CBS não deve ser preenchido 
para o CST informado 
006 Se o CST informado possuir indicador que EXIGE 
preenchimento do grupo de informações 
específicas do IBS/CBS, este grupo DEVE estar 
informado (grupo: gIBSCBS) 
 
Exceção: Se o CRT informado pelo emitente for 1-
Simples Nacional ou 4 -MEI, o grupo gIBSCBS NÃO 
será exigido 
Obrig 315 Rej. Rejeição: Grupo IBS/CBS deve ser preenchido para o 
CST informado 
007 Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
A alíquota de IBS da UF (pIBSUF) deverá ser igual a 
0,1% para documento com data de emissão no ano de 
2026. Art. 343 da LC 214/25 
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF deve ser igual a 
0,1% para documento emitido em 2026 
008 Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
A alíquota de IBS da UF (pIBSUF) deverá ser igual a 
0,05% para documento com data de emissão nos anos 
de 2027 a 2028. Art. 344 da LC 214/25 
Obrig. 317 Rej. Rejeição: Alíquota do IBS da UF deve ser igual a 
0,05% para documento emitido em 2027 e 2028 
009 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o IBS Estadual 
ou informado grupo de compra governamental, o grupo 
gRed DEVE estar informado 
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
Estadual (gIBSUF/gRed): 
A Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado 
da aplicação do percentual de redução da alíquota 
(tag: pRedAliq) na alíquota do IBS da UF (tag: 
pIBSUF). 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E): E = A * (1 - R)*(1- RG) 
E = 10 * (1 - 0,4) *(1-0,05) = 5,7 
Obrig. 390 Rej. Rejeição: Valor da Alíquota Efetiva do IBS da UF 
calculado incorretamente 
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
O valor do Diferimento (vDif) deverá ser resultante do 
Valor do IBS UF x Percentual do Diferimento ((vBC x 
pIBSUF) x pDif) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
 
Obrig. 320 Rej. Rejeição: Valor do Diferimento da UF difere do 
calculado

## Página 9

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 9 / 19 
 
013 
a 
Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior ao valor do IBS (vIBSUF) 
Obrig. 395 Rej. Rejeição: Valor do IBS UF não pode resultar 
negativo 
014  Se informado grupo IBS de competência das Unidades 
Federadas (gIBSUF): 
O valor do IBS (vIBSUF) deverá ser resultante da Base 
de Cálculo x Alíquota (vBC x pIBSUF) – vDif - vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Observação 3: Conforme cClassTrib escolhido, o valor 
do crédito presumido (vCredPres) deve ser subtraído 
do total do IBS. 
Obrig. 318 Rej. Rejeição: Valor do IBS UF difere do calculado 
015 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
A alíquota de IBS do Município (pIBSMun) deverá ser 
igual a 0 para documento com data de emissão no ano 
de 2026. Art. 343 da LC 214/25 
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Município deve ser 
igual a zero para documento emitido em 2026 
016 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
A alíquota de IBS do Município (pIBSMun) deverá ser 
igual a 0,05% para documento com data de emissão 
nos anos de 2027 a 2028. Art. 344 da LC 214/25 
Obrig. 322 Rej. Rejeição: Alíquota do IBS do Município deve ser 
igual a 0,05% para documento emitido em 2027 e 
2028 
017 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o IBS 
Municipal ou informado grupo de compra 
governamental, o grupo gRed DEVE estar informado 
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
Municipal (gIBSMun/gRed): 
A Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado 
da aplicação do percentual de redução da alíquota 
(tag: pRedAliq) na alíquota do IBS do Município (tag: 
pIBSMun). 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E): E = A * (1 - R)*(1- RG) 
E = 10 * (1 - 0,4) *(1-0,05) = 5,7 
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
O valor do Diferimento (vDif) deverá ser resultante do 
Valor do IBSMun x Percentual do Diferimento ((vBC x 
pIBSMun) x pDif) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Obrig. 325 Rej. Rejeição: Valor do Diferimento do Município difere do 
calculado

## Página 10

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 10 / 19 
 
022 Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
O valor do IBS (vIBSMun) deverá ser resultante da 
Base de Cálculo x Alíquota (vBC x pIBSMun) – vDif - 
vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Observação 3: Conforme cClassTrib escolhido, o valor 
do crédito presumido (vCredPres) deve ser subtraído 
do total do IBS. 
Obrig. 323 Rej. Rejeição: Valor do IBS Municipal difere do calculado 
022 
a 
Se informado grupo IBS de competência dos 
Municípios (gIBSMun): 
 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior ao valor do IBS (vIBSMun) 
Obrig. 396 Rej. Rejeição: Valor do IBS Municipal não pode resultar 
negativo 
023 Se informado grupo CBS (gCBS): 
A alíquota da CBS (pCBS) deverá ser igual a 0,9% 
para documento com data de emissão no ano de 
2026. Art. 343 da LC 214/25 
 
Obrig. 326 Rej. Rejeição: Alíquota da CBS deve ser igual a 0,9% para 
documento emitido em 2026 
024 Se CST informado possuir indicador que EXIGE 
informação de redução de alíquota para o CBS ou 
informado grupo de compra governamental, o grupo 
gRed DEVE estar informado 
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
CBS (gCBS/gRed): 
A Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado 
da aplicação do percentual de redução da alíquota 
(tag: pRedAliq) na alíquota da CBS (tag: pCBS). 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E): E = A * (1 - R)*(1- RG) 
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
O valor do Diferimento (vDif) deverá ser resultante do 
Valor da CBS x Percentual do Diferimento ((vBC x 
pCBS) x pDif) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 329 Rej. Rejeição: Valor do Diferimento do CBS difere do 
calculado 
028 
a 
Se informado grupo CBS (gCBS): 
O valor resultante da soma do diferimento (vDif) e 
Devolução (DevTrib) QUANDO INFORMADOS, NÃO 
pode ser superior ao valor da CBS (vCBS) 
Obrig. 397 Rej. Rejeição: Valor do CBS não pode resultar negativo

## Página 11

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 11 / 19 
 
029 Se informado grupo CBS (gCBS): 
O valor do CBS (vCBS) deverá ser resultante da Base 
de Cálculo x Alíquota (vBC x pCBS) – vDif - vDevTrib 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a 
tag Alíquota Efetiva (pAliqEfet) 
Observação 3: Conforme cClassTrib escolhido, o valor 
do crédito presumido (vCredPres) deve ser subtraído 
do total do CBS. 
Obrig. 327 Rej. Rejeição: Valor do CBS difere do calculado 
030 Se cClassTrib informado possuir indicador que EXIGE 
informação de tributação regular, o grupo 
gTribRegular DEVE estar informado 
Obrig. 330 Rej. Rejeição: Classificação Tributária informada obriga 
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
(vTribRegIBSUF) deverá ser resultante da Base de 
Cálculo do item x Alíquota Efetiva Regular de IBS da 
UF (vBC x pAliqEfetRegIBSUF) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos  
Obrig. 333 Rej. Rejeição: Valor da tributação regular da UF difere do 
calculado 
034 Se informado grupo da tributação regular 
(gTribRegular): 
O valor do tributo regular de IBS dos Municípios 
(vTribRegIBSMun) deverá ser resultante da Base de 
Cálculo do item x Alíquota Efetiva Regular de IBS do 
Município (vBC x pAliqEfetRegIBSMun) 
 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 334 Rej. Rejeição: Valor da tributação regular do Município 
difere do calculado 
035 Se informado grupo da tributação regular 
(gTribRegular): 
O valor do tributo regular de CBS (vTribRegCBS) 
deverá ser resultante da Base de Cálculo do item x 
Alíquota Efetiva Regular de CBS (vBC x 
pAliqEfetRegCBS) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 335 Rej. Rejeição: Valor da tributação regular da CBS difere 
do calculado 
036 Se cClassTrib informado possuir indicador que NÃO 
PERMITE informação de Crédito Presumido para o 
IBS, o grupo gIBSCredPres NÃO deve estar 
informado 
Obrig. 336 Rej. Rejeição: Classificação Tributária informada não 
permite informação de crédito presumido para o IBS 
037 Se informado grupo do crédito presumido 
(gIBSCredPres): 
O valor do cCredPres deve existir na tabela de 
códigos de crédito presumido 
Obrig. 337 Rej. Rejeição: Código de crédito presumido do IBS 
inexistente 
038 Se informado grupo do crédito presumido 
(gIBSCredPres): 
A tag vCredPresCondSus não poderá ser informada 
até 2033 
Obrig. 386 Rej. Rejeição: O valor do crédito presumido condição 
suspensiva só poderá ser informado a partir de 2033 
para IBS 
039 Se o cCredPres do IBS possuir indicação de Condição 
Suspensiva e a tag vCredPresCondSus não estiver 
informada 
Observação: Esta regra só será aplicada a partir de 
2033 
Obrig. 338 Rej. Rejeição: O valor do crédito presumido (condição 
suspensiva) para o IBS deve ser informado 
040 Se o cCredPres do IBS NÂO possuir indicação de 
Condição Suspensiva e a tag vCredPres não estiver 
informada 
Observação: Esta regra só será aplicada a partir de 
2033 
Obrig. 339 Rej. Rejeição: O valor do crédito presumido para o IBS 
deve ser informado

## Página 12

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 12 / 19 
 
041 Se informado grupo do crédito presumido 
(gIBSCredPres) COM Condição Suspensiva: 
O valor do Crédito Presumido Condição Suspensiva 
(vCredPresCondSus) deverá ser resultante da Base 
de Cálculo x Percentual do Crédito Presumido (vBC x 
pCredPres) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação: Esta regra só será aplicada a partir de 
2033 
Obrig. 340 Rej. Rejeição: Valor do Crédito Presumido Condição 
Suspensiva de IBS difere do calculado 
042 Se informado grupo do crédito presumido 
(gIBSCredPres) SEM Condição Suspensiva: 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 341 Rej. Rejeição: Valor do Crédito Presumido de IBS difere 
do calculado 
043 Se informado grupo do crédito presumido 
(gCBSCredPres): 
O valor do cCredPres deve existir na tabela de 
códigos de crédito presumido 
Obrig. 342 Rej. Rejeição: Código de crédito presumido da CBS 
inexistente 
044 Se informado grupo do crédito presumido 
(gCBSCredPres): 
A tag vCredPresCondSus não poderá ser informada 
até 2027 
Obrig. 387 Rej. Rejeição: O valor do crédito presumido condição 
suspensiva só poderá ser informado a partir de 2027 
para CBS 
045 Se o cCredPres da CBS possuir indicação de 
Condição Suspensiva e a tag vCredPresCondSus não 
estiver informada 
Observação: Esta regra só será aplicada a partir de 
2027 
Obrig. 343 Rej. Rejeição: O valor do crédito presumido (condição 
suspensiva) para a CBS deve ser informado 
046 Se o cCredPres da CBS NÃO possuir indicação de 
Condição Suspensiva e a tag vCredPres não estiver 
informada 
Observação: Esta regra só será aplicada a partir de 
2027 
Obrig. 344 Rej. Rejeição: O valor do crédito presumido para a CBS 
deve ser informado 
047 Se informado grupo do crédito presumido 
(gCBSCredPres) COM Condição Suspensiva: 
O valor do Crédito Presumido Condição Suspensiva 
(vCredPresCondSus) deverá ser resultante da Base 
de Cálculo x Percentual do Crédito Presumido (vBC x 
pCredPres) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Observação: Esta regra só será aplicada a partir de 
2027 
Obrig. 345 Rej. Rejeição: Valor do Crédito Presumido Condição 
Suspensiva de CBS difere do calculado 
048 Se informado grupo do crédito presumido 
(gCBSCredPres) SEM Condição Suspensiva: 
O valor do Crédito Presumido (vCredPres) deverá ser 
resultante da Base de Cálculo x Percentual do Crédito 
Presumido (vBC x pCredPres) 
Observação: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 346 Rej. Rejeição: Valor do Crédito Presumido de CBS difere 
do calculado 
049 Se grupo compra governamental (grupo: 
gCompraGov) estiver informado, o Grupo de 
informações da composição do valor do IBS e da CBS 
em compras governamentais (grupo: 
gTribCompraGov) DEVE ser informado. 
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
grupo gTribCompraGov (vIBSUF + vIBSMun + vCBS) 
é diferente do resultado de gIBSUF/vIBSUF + 
gIBSMun/vIBSMun + gCBS/vCBS. 
Obrig. 400 Rej. Rejeição: Somas dos valores de IBS e CBS em 
compras governamentais divergente

## Página 13

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 13 / 19 
 
6 Criação do grupo de compras governamentais no grupo ide 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# gCompraGov G ide - 0-1 -  
 tpEnteGov E Tipo de Ente N 1-1 1 Para administração pública direta e suas autarquias 
e fundações: 
1=União 
2=Estados 
3=Distrito Federal 
4=Municípios 
 pRedutor E Percentual de redução 
de alíquota em compra 
governamental 
N 1-1 3v2-4 Conforme LC 214/25: TÍTULO II 
DAS COMPRAS GOVERNAMENTAIS, Art. 472 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado o grupo de informações de compra 
governamental (grupo:ide\gCompraGov), o DFe de 
compra governamental deve ter alíquota de outros 
entes igual a zero. 
Se 2027 até 2032 
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
 Alíquota do CBS (tag: pCBS) deve ser igual 
a zero. 
Observação: Conforme Art. 473, § 1o e seus Incisos I, 
II, III e IV da LC 214/2025. 
Obrig. 347 Rej. Rejeição: DFe de compra governamental e alíquota 
dos outros entes diferentes de zero.

## Página 14

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 14 / 19 
 
7 Total Geral do Documento Fiscal Eletrônico 
Deverá ser criada a tag Valor Total do DFe (vTotDFe). 
No CTe, CTe Simplificado, CTe OS essa tag aparecerá dentro do grupo imp, após o grupo IBSCBS. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E imp E 0-1 13,2 Valor total do documento fiscal  
vTPrest + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser a soma do total 
da prestação (vTPrest) + vTotIBS + vTotCBS 
Exceção: Em 2026 não somar vTotIBS e 
vTotCBS  
Observação: Implementação futura 
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
8 Alteração em Regra do CTe Simplificado 
G101a O município de fim de prestação em todos os itens do 
CTe Simplificado (det:cMunFim) devem ser iguais  
Obrig. 370 Rej. Rejeição: O CTe Simplificado deve ter a 
prestação terminada em apenas um 
município 
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

## Página 15

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 15 / 19 
 
 
10 Criação do grupo de informações da Declaração de 
Conteúdo Eletrônica nos documentos originários 
Validações dos Documentos Transportados 
G045a Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informado grupo informação de documentos (infDoc): 
Quantidade de documentos informados 
(infNF/infNFe/infOutros/infDCe) não pode ultrapassar 
2000 documentos 
Obrig. 601 Rej. Rejeição: Quantidade de documentos 
informados no remetente excede limite de 
2000 
G045b Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e 
informados grupos de informações de documentos 
(infDoc) e DCe (infDCe) 
- Verificar se existe alguma chave de acesso de DCe 
duplicada no CTe 
Retornar a chave duplicada 
Obrig. 375 Rej. Rejeição: DCe duplicada no CTe 
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
Facult. 378 Rej. Rejeição: DCe com diferença de Chave de 
Acesso

## Página 16

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 16 / 19 
 
 - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF 
Emit, Modelo, Série, Nro): 
            - A DCe não pode existir com diferença de chave 
de acesso 
Retornar a primeira chave de acesso de DCe com 
situação inválida. 
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
 
 
11 Exceção para Substituição sem exigência do evento de 
prestação em desacordo para tomador Exterior 
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
 
Exceção: Em caso de modal ferroviário ou aquaviário 
multimodal permitir até 24 meses da Data de 
Autorização do CTe 
Obrig. 933 Rej. Rejeição: Chave de acesso do CTe 
complementado muito antiga 
[chCTe: 
99999999999999999999999999999999999
999999999]

## Página 17

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 17 / 19 
 
13 Eliminar as opções de contingência SVC da GTVe no 
Leiaute (Schema) 
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
15 Preparação das expressões regulares do CTe para o 
futuro CNPJ Alfanumérico 
As alterações serão feitas no arquivo de tipos gerais e aplicam-se automaticamente a todos campos do tipo CNPJ 
e Chave de acesso em qualquer um dos schemas do projeto CTe, entretanto, até que seja publicada uma Nota 
Técnica que modifica as validações desses campos, as letras não devem ser utilizadas. 
 
A expressão regular que valida um campo do tipo CNPJ é: [0-9]{14} 
Alteração: a Expressão regular do CNPJ passa a aceitar letras maiúsculas nas primeiras 12 posições:  
[A-Z0-9]{12}[0-9]{2} 
 
Expressão Regular Atual da Chave de Acesso é: [0-9]{44} 
Alteração: a expressão regular passa a suportar letras maiúsculas nas 12 primeiras posições que correspondem 
ao CNPJ dentro da chave de acesso: [0-9]{6}[A-Z0-9]{12}[0-9]{26} 
16 Ampliação do cStat de retorno para 4 dígitos 
A expressão regular que define a tag cStat dos schemas de retorno de todos os serviços passa a suportar até 
códigos com 4 dígitos. 
 
Nova expressão regular para o tipo TStat do arquivo Tipos Geral: [0-9]{3,4}

## Página 18

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 18 / 19 
 
17 Anexo – Novos Grupos para Reforma Tributária 
Conhecimento de Transporte Eletrônico– modelo 57

## Página 19

Projeto 
Conhecimento de Transporte Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.05 a 
 
 
Página 19 / 19 
 
Conhecimento de Transporte Eletrônico Simplificado – Modelo 57 
 
  
Conhecimento de Transporte Eletrônicos Outros Serviços – modelo 67
