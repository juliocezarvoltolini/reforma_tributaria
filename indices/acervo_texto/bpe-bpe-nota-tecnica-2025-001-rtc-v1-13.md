---
id: bpe-bpe-nota-tecnica-2025-001-rtc-v1-13
titulo: Nota Técnica BPe - Nota_Técnica_2025_001 - RTC_v1.13 - Publicada em 26/01/2026
tipo: nota.tecnica
versao: '1.13'
data: '2026-01-26'
documento_fiscal: BP-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YmEWtdaZP7o=
arquivo_original: fontes/acervo/bpe-bpe-nota-tecnica-2025-001-rtc-v1-13.pdf
sha256_original: afda4b349d90c2fed30e39039565ec0e7676911ce0970997db20e0fa7fa7b9dc
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 1210a43ea187a6c74b8933ab109503d5614ede767f8e371b9273b83529ac157f
---

## Página 1

Projeto Bilhete de Passagem 
Eletrônico 
 
Nota Técnica 2025.001 – Reforma Tributária do Consumo 
Versão 1.13 de 22 de janeiro de 2026

## Página 2

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 2 / 18 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 5 
2 Tipos básicos da tributação ............................................................................................. 5 
3 Inclusão dos campos do IBS/CBS ................................................................................... 6 
4 Código de Classificação Tributária do IBS/CBS .............................................................. 8 
5 Validações dos campos do IBS e CBS ............................................................................ 8 
6 Criação do grupo de compras governamentais no grupo ide ......................................... 14 
7 Grupo de totais do DFe ................................................................................................. 15 
8 Regras de Validação do Grupo de Totais IBS e CBS .................................................... 15 
9 Total Geral do Documento Fiscal Eletrônico ................................................................. 17 
10 Ajuste de regras de validação do BPe ....................................................................... 17 
11 Novos valores para o tag Tipo de Desconto .............................................................. 17 
12 Preparação das expressões regulares do BPe para o futuro CNPJ Alfanumérico ..... 18 
13 Ampliação do cStat de retorno para 4 dígitos ............................................................ 18

## Página 3

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 3 / 18 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Previsão das informações do IBS/CBS no BPe, BPeTM e Evento de 
Excesso de Bagagem 
 Preparação das Expressões Regulares do CNPJ Alfa 
 Ampliação do código de retorno das mensagens suportar até 4 dígitos 
(cStat) 
 Novos valores para o campo tipo de desconto 
  
1.01  Correções e orientações sobre aplicação das regras de validação nos 
ambientes 
 Renumeração das regras de rejeição 
 Ajuste no grupo de Tributação regular 
 
  
1.02  Ajustes nas regras do crédito presumido e tributação regular 
 Ajuste nas regras para Crédito Presumido Condição Suspensiva no 
grupo do crédito presumido 
  
1.03  Ajustes nas regras de compras governamentais, redução de alíquota e 
valores de IBS/CBS 
 Correção no schema dos eventos tipos básicos 
  
1.04  Ajustes em regras de validação e mensagens   
1.05  Ajuste na regra de compras governamentais e exigência do grupo de 
tributação para SN  
 Novo grupo de informações de compras governamentais no IBSCBS 
  
1.05 a  Correção de datas no texto da introdução   
1.05b   Correção em nome de campos citados nas RVs   
1.06  Novas regras de validação complementares 
 Inclusão do campo vIBS 
 Ajuste na expressão regular do QRCode para aceitar CNPJ Alfa 
  
1.07  Campo vIBS passa a ser obrigatório no schema   
1.08  Alteração da regra de validação 004-a para verificar no cClassTrib sua 
aplicabilidade ao modelo de DFe 
 Correção na posição do campo vIBS no schema 
 Correção na obrigatoriedade das regras 038 e 044 
  
1.08 a  Correção na redação da regra do total geral do DFe   
1.09  Ajustes na regra do diferimento 
 Altera data de exigência do grupo IBSCBS em homologação para 03/11 
  
1.10  Exclusão do grupo de informações do crédito presumido por não se 
aplicar aos cClassTrib associados ao DFe 
 Criação do indicador de doação e do grupo de Estorno de crédito 
vinculado a um novo indicador na tabela cClassTrib para esta finalidade 
  
1.11a  Ajuste na explicação da regra de valor do tributo negativo

## Página 4

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 4 / 18 
 
1.12  Esclarecimento sobre o preenchimento do vTotDFe    
1.12a  Exclusão da observação da regra F70   
1.12b  Correção na regra da redução de alíquota Já implantado Já implantado 
1.13  Criação de regra específica para exigir vTotDFe quando informado 
IBSCBS 
03/02/2026 02/03/2026 
 
Observação: No ambiente de produção, os campos ficam à disposição desde 20 de outubro, validados apenas se 
informados. No ambiente de homologação os campos da reforma tributária estarão à disposição desde julho, 
validados apenas se informados.

## Página 5

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 5 / 18 
 
1 Introdução 
Com a promulgação da Lei Complementar nº 214/2025, foi definida, na Seção V - Disposições Transitórias, Art. 
62 I, a obrigatoriedade de que os Estados, o Distrito Federal e os Municípios adaptem os sistemas autorizadores 
de Documentos Fiscais Eletrônicos (DFe) vigentes para a utilização de leiaute padronizado, de modo a permitir 
que os contribuintes informem os dados relativos ao Imposto sobre Bens e Serviços (IBS), à Contribuição sobre 
Bens e Serviços (CBS) e ao Imposto Seletivo (IS). 
 
Diante disso, esta Nota Técnica substitui e complementa, no âmbito do BPe, a DFe - Nota Técnica 2024.001 - 
IBS/CBS v1.10, mantendo a data de implantação em ambiente de produção para 06/10/2025, de modo a viabilizar 
sua efetiva operacionalização a partir de 05/01/2026. 
 
A NT modifica o leiaute dos DFe, inserindo os grupos e campos opcionais relacionados a tributação do IBS, CBS 
e IS, em atendimento à legislação vigente. 
 
Esclarecemos que esta NT poderá ser ajustada ao longo do seu processo de execução, uma vez que as discussões 
envolvendo a implantação da Reforma Tributária ainda estão em curso.  
 
Vale destacar que, em Produção, no ano de 2025 as informações de tributação relativas ao IBS e CBS serão 
opcionais e validadas apenas se forem informadas 
 
Esta documentação descreve as alterações aplicadas aos Documentos: 
 Bilhete de Passagem Eletrônico (modelo 63); 
 Bilhete de Passagem Eletrônico Transporte Metropolitano (modelo 63 - Tipo BPe 4); 
 
2 Tipos básicos da tributação 
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos, esta NT introduz o arquivo 
DFeTiposBasicos_v1.00.xsd ao conjunto dos arquivos que compõem do schema da DFe. 
 
Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro das 
informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no leiaute padrão da DFe.

## Página 6

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 6 / 18 
 
3 Inclusão dos campos do IBS/CBS 
Este grupo de informações facultativas deve ser adicionado ao final do grupo imposto do BPe e BPeTM (em cada 
item do grupo det) e no evento Excesso de Bagagem. 
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
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 7 / 18 
 
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
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 8 / 18 
 
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
apurações assistidas do IBS e da CBS, em atendimento ao disposto na Legislação vigente.  
Vale ressaltar que a tabela poderá sofrer alterações em virtude de aperfeiçoamentos, novidades introduzidas em 
sede de Regulamento, ou para atender a necessidades relacionadas à apuração assistida do IBS e da CBS.  
5 Validações dos campos do IBS e CBS 
Para o BPe essas validações serão aplicadas ao grupo infBPe\imp\IBSCBS, no caso do BPeTM serão aplicadas 
a cada ocorrência de viagem do grupo infBPe\detBPeTM[1..99]\det[1..990]\IBSCBS. Ao evento excesso de 
Bagagem as validações serão aplicadas a evExcessoBagagem\IBSCBS. 
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

## Página 9

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 9 / 18 
 
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
O valor do Diferimento (vDif) deverá ser resultante de: 
vDif = vBC x (pIBSUF/100) x (pDif/100) 
 
Observação: Aceitar uma tolerância de 0,01 a mais ou 
a menos 
 
Observação 2: Em caso de preenchimento do grupo 
de redução (gRed) a alíquota utilizada deverá ser a tag 
Alíquota Efetiva (pAliqEfet) 
Obrig. 320 Rej. Rejeição: Valor do Diferimento da UF difere do 
calculado

## Página 10

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 10 / 18 
 
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

## Página 11

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 11 / 18 
 
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
  
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida 
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

## Página 12

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 12 / 18 
 
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

## Página 13

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 13 / 18 
 
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

## Página 14

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 14 / 18 
 
6 Criação do grupo de compras governamentais no grupo ide 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# gCompraGov G ide - 0-1 -  
 tpEnteGov E gCompraGov N 1-1 1 Para administração pública direta e suas autarquias 
e fundações: 
1=União 
2=Estados 
3=Distrito Federal 
4=Municípios 
 pRedutor E gCompraGov N 1-1 3v2-4 Percentual de redução de alíquota em compra 
governamental 
Conforme LC 214/25: TÍTULO II 
DAS COMPRAS GOVERNAMENTAIS, Art. 472 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado o grupo de informações de compra 
governamental (grupo:ide\gCompraGov), o DFe de 
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
 Alíquota do CBS (tag: pCBS) deve ser igual 
a zero. 
Observação: Conforme Art. 473, § 1o e seus Incisos I, 
II, III e IV da LC 214/2025. 
Obrig. 347 Rej. Rejeição: DFe de compra governamental e alíquota 
dos outros entes diferentes de zero.

## Página 15

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 15 / 18 
 
7 Grupo de totais do DFe 
Para BPe TM, no grupo total do DFe deverá ser adicionado o grupo de totais do IBS/CBS. 
Para BPe e para o evento de Excesso de Bagagem esse grupo não deverá ser criado. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# IBSCBSTot G total - 0-1 - Grupo de informações para apuração do IBS e 
CBS declarado pelo contribuinte 
1 vBCIBSCBS E IBSCBSTot N 1-1 13,2 Total da Base de cálculo do IBS/CBS 
2 gIBS G IBSCBSTot - 1-1 - Totalização do IBS 
3 gIBSUF G gIBS - 1-1 - Totalização do IBS de competência da UF 
4 vDif E gIBSUF N 1-1 13,2 Total do Diferimento 
5 vDevTrib E gIBSUF N 1-1 13,2 Total de Devolução de Tributo IBS UF 
6 vIBSUF E gIBSUF N 1-1 13,2 Total do IBS UF 
7 gIBSMun G gIBS - 1-1 - Totalização do IBS de competência Municipal 
8 vDif E gIBSMun N 1-1 13,2 Total do Diferimento 
9 vDevTrib E gIBSMun N 1-1 13,2 Total de Devolução de Tributo IBS Municipal 
10 vIBSMun E gIBSMun N 1-1 13,2 Total do IBS Municipal 
11 vIBS E gIBS N 1-1 13,2 Total do IBS (IBS UF + IBS Mun) 
14 gCBS G IBSCBSTot - 1-1 - Total do CBS 
15 vDif E gCBS N 1-1 13,2 Total do Diferimento 
16 vDevTrib E gCBS N 1-1 13,2 Total de Devolução do tributo CBS 
17 vCBS E gCBS N 1-1 13,2 Total do CBS 
18 gEstornoCred G IBSCBSTot - 0-1 - Total do Estorno de crédito 
19 vIBSEstCred E gIBS N 1-1 13,2 Total do Estorno de crédito IBS  
20 vCBSEstCred E gCBS N 1-1 13,2 Total do Estorno de crédito CBS 
 
8 Regras de Validação do Grupo de Totais IBS e CBS 
Aplicável apenas BPeTM. 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 O grupo de totais do IBS e CBS (IBSCBSTot) só 
deve ser informado se existir pelo menos uma 
ocorrência de IBS/CBS nos itens 
Obrig. 348 Rej. Rejeição: Total de IBS/CBS só deve ser informado 
se existir IBS/CBS declarado nos itens do DFe 
002 O grupo de totais do IBS e CBS (IBSCBSTot) 
deve ser informado se existir pelo menos uma 
ocorrência de IBS/CBS nos itens 
Obrig. 349 Rej. Rejeição: Total de IBS/CBS deve ser informado se 
existir IBS/CBS declarado nos itens do DFe 
003 O total do Diferimento do IBS UF deverá ser a 
soma do campo vDif do IBS UF informados nos 
itens 
Obrig. 350 Rej. Rejeição: Total de Diferimento do IBS UF difere da 
soma dos itens 
004 O total Devolvido do IBS UF deverá ser a soma do 
campo vDevTrib do IBS UF informados nos itens 
Obrig. 351 Rej. Rejeição: Total Devolvido do IBS UF difere da soma 
dos itens 
005 O total do IBS UF deverá ser a soma do campo 
vIBSUF informados nos itens 
 
Obrig. 352 Rej. Rejeição: Total de IBS UF difere da soma dos itens 
006 O total do Diferimento do IBS Municipal deverá ser 
a soma do campo vDif do IBS Municipal 
informados nos itens 
 
Obrig. 353 Rej. Rejeição: Total de Diferimento do IBS Municipal 
difere da soma dos itens

## Página 16

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 16 / 18 
 
007 O total Devolvido do IBS Municipal deverá ser a 
soma do campo vDevTrib do IBS Municipal 
informados nos itens 
 
Obrig. 354 Rej. Rejeição: Total Devolvido do IBS Municipal difere da 
soma dos itens 
008 O total do IBS Municipal deverá ser a soma do 
campo vIBSMun informados nos itens 
Obrig. 355 Rej. Rejeição: Total de IBS Municipal difere da soma dos 
itens 
009 O Total do IBS deverá ser a soma do IBS das UF 
e do IBS Municipal (vIBSUF + vIBSMun) 
Obrig. 356 Rej. Rejeição: Total do IBS difere da soma do IBS UF e 
IBS Municipal 
010 O total do Diferimento do CBS deverá ser a soma 
do campo vDif do CBS informados nos itens 
Obrig. 357 Rej. Rejeição: Total de Diferimento do CBS difere da soma 
dos itens 
011 O total Devolvido do CBS deverá ser a soma do 
campo vDevTrib do CBS informados nos itens 
Obrig. 358 Rej. Rejeição: Total Devolvido do CBS difere da soma dos 
itens 
012 O total do CBS deverá ser a soma do campo vCBS 
informados nos itens 
Obrig. 359 Rej. Rejeição: Total de CBS difere da soma dos itens 
013 Se informado grupo de estorno de crédito nos itens 
(gEstornoCred) o total do IBS estornado deverá 
ser igual a soma campo valor do IBS estornado 
nos itens (gEstornoCred/vIBS) 
Obrig. 305 Rej. Rejeição: Total de IBS estornado difere da soma dos 
itens 
014 Se informado grupo de estorno de crédito nos itens 
(gEstornoCred) o total da CBS estornada deverá 
ser igual a soma campo valor da CBS estornada 
nos itens (gEstornoCred/vCBS) 
Obrig. 306 Rej. Rejeição: Total de CBS estornada difere da soma dos 
itens 
017 O total geral do DFe só deve ser informado se o 
grupo de totais do IBS e CBS estiver informado 
Obrig. 364 Rej. Rejeição: O Total do DFe não deve ser informado 
quando não houver IBS e CBS

## Página 17

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 17 / 18 
 
9 Total Geral do Documento Fiscal Eletrônico 
Deverá ser criada a tag Valor Total do DFe (vTotDFe). 
Para BPeTM esta tag será inserida no grupo total. 
No BPe essa tag aparecerá dentro do grupo imp, após o grupo IBSCBS. 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E total (BPeTM) ou   
imp (BPe) 
E 0-1 13,2 Valor total do documento fiscal  
vBP + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 A tag de Total do Documento Fiscal Eletrônico 
deverá ser informada (tag imp\vTotDFe no BPe ou   
tag: total\vTotDFe em BPeTM) sempre que existir 
informação no grupo IBSCBS (grupo: 
imp\IBSCBS) 
Observação: no BPeTM basta que exista uma 
ocorrência do grupo IBSCBS no detalhamento das 
viagens 
Obrig. 360 Rej. Rejeição: Total do DFe de preenchimento 
obrigatório 
02 O total geral do DFe deverá ser INFORMADO com 
a soma do total do BPe + IBS + CBS 
Para BPe: 
vTotDFe = infValorBPe/vBP + gIBSCBS/vIBS + 
gCBS/vCBS 
Para BPeTM: 
vTotDFe = total/vBP + IBSCBSTot/gIBS/vIBS + 
IBSCBSTot/gCBS/vCBS 
Exceção: Em 2026 não somar IBS e CBS, usar a 
fórmula:  
Para BPe: vTotDFe = infValorBPe/vBP  
Para BPeTM: vTotDFe = total/vBP  
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
10 Ajuste de regras de validação do BPe 
F69 Validar se o somatório das formas de pagamento 
(tag:pag/vPag) é diferente do valor pago do BPe 
(tag:vPgto) + Troco (tag:vTroco)  
* Considerar uma tolerância de R$ 1,00 para mais ou 
para menos 
 
Observação: a partir de 2027 deverá considerar 
vIBS e vCBS para consolidar a soma 
Obrig. 438 Rej. Rejeição: BPe com somatório dos 
pagamentos diferente do total pago 
F70 Validar se o valor pago pelo BPe (tag:vPgto) 
corresponde ao valor total do bilhete (tag: vBP) 
menos o valor do desconto (tag:vDesconto) 
 
Obrig. 403 Rej. Rejeição: Valor pago difere do Valor Total 
menos o desconto concedido 
11 Novos valores para o tag Tipo de Desconto 
Acrescentam-se as seguintes opções na tag tpDesconto: 
11 - Idoso 50% 
12 - Acompanhante PCD; 
13 - Pessoa Obesa

## Página 18

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2025.001 v1.13 
 
 
Página 18 / 18 
 
12 Preparação das expressões regulares do BPe para o futuro CNPJ 
Alfanumérico 
As alterações serão feitas no arquivo de tipos gerais e aplicam-se automaticamente a todos campos do tipo CNPJ 
e Chave de acesso em qualquer um dos schemas do projeto BPe, entretanto, até que seja publicada uma Nota 
Técnica que modifica as validações desses campos, as letras não devem ser utilizadas. 
 
A expressão regular que valida um campo do tipo CNPJ é: [0-9]{14} 
Alteração: a Expressão regular do CNPJ passa a aceitar letras maiúsculas nas primeiras 12 posições:  
[A-Z0-9]{12}[0-9]{2} 
 
Expressão Regular Atual da Chave de Acesso é: [0-9]{44} 
Alteração: a expressão regular passa a suportar letras maiúsculas nas 12 primeiras posições que correspondem 
ao CNPJ dentro da chave de acesso: [0-9]{6}[A-Z0-9]{12}[0-9]{26} 
A expressão regular do QR Code também seguirá essa regra de formação na parte da chave de acesso. 
13 Ampliação do cStat de retorno para 4 dígitos 
A expressão regular que define a tag cStat dos schemas de retorno de todos os serviços passa a suportar até 
códigos com 4 dígitos. 
Nova expressão regular para o tipo TStat do arquivo Tipos Geral: [0-9]{3,4}
