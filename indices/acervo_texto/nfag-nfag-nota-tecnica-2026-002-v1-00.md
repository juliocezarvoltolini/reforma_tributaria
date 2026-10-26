---
id: nfag-nfag-nota-tecnica-2026-002-v1-00
titulo: Nota Técnica 2026.002 v.1.00 - Publicada em 10/06/2026
tipo: nota.tecnica
versao: '1.00'
data: '2026-06-10'
documento_fiscal: NFAg
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Wld322n6MEU=
arquivo_original: fontes/acervo/nfag-nfag-nota-tecnica-2026-002-v1-00.pdf
sha256_original: 642b18f798f8c81a54376d38f14c2250757f296efcc237640691b6a37af9dea2
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: e21bb211aeef6242e1ce841a3efbb08c1dc9ca6b848785a6619fa2bb75b5d8ba
---

## Página 1

Projeto Nota Fiscal de Água e 
Saneamento Eletrônica 
 
Nota Técnica 2026.002 – Reforma Tributária do Consumo 
 
Versão 1.00 de 10 de junho de 2026

## Página 2

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 2 / 14 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 3 
2 Campos do grupo IBS/CBS ............................................................................................. 3 
3 Novo campo Inscrição Suframa do Emitente ................................................................... 6 
4 Validações do grupo de Devolução ................................................................................. 7 
5 Validações Alíquota da CBS e Alíquota zero da CBS (validar em cada item) .................. 8 
6 Antecipação de Pagamento .......................................................................................... 10

## Página 3

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 3 / 14 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Campo da inscrição SUFRAMA do emitente para operações ALC 
 Atualização de regras de validação 
 Regras da CBS com alíquota zero 
 Antecipação de Pagamento 
03/08/2026 31/08/2026 
1 Introdução 
Esta Nota Técnica apresenta evoluções da NT 2025.001 RTC contemplando novos pontos relevantes previstos na 
legislação como Antecipação de Pagamento, obrigatoriedade do preenchimento das informações de IBS e CBS, 
percentual de devolução de tributos (cashback), alíquota zero da CBS em Área de Livre Comércio e melhorias na 
redação das regras de validação. 
 
2 Campos do grupo IBS/CBS 
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
12 pDevTrib E gDevTrib N 0-1 3,2/3,4 Percentual de devolução do tributo, conforme LC 
214/25 art. 118. 
13 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
14 gRed G gIBSUF - 0-1 - Grupo de informações da redução de Alíquota 
15 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
16 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência das UF que 
será aplicada a base de cálculo, incluindo o 
gCompraGov/pRedutor, se houver. 
17 vIBSUF E gIBSUF N 1-1 13,2 Valor do IBS de competência da UF 
18 gIBSMun G gIBSCBS - 1-1 - Grupo de informações do IBS/CBS de competência 
do municipio 
19 pIBSMun E gIBSMun N 1-1 3,2/3,4 Alíquota do IBS Municipal 
20 gDif G gIBSMun - 0-1 - Grupo de campos do diferimento

## Página 4

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 4 / 14 
 
21 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
22 vDif E gDif N 1-1 13,2 Valor do diferimento 
23 gDevTrib G gIBSMun - 0-1 - Grupo de informações da devolução do tributo 
24 pDevTrib E gDevTrib N 0-1 3,2/3,4 Percentual de devolução do tributo, conforme LC 
214/25 art. 118. 
25 vDevTrib E gDevTrib N 1-1 13,2 Valor do tributo devolvido.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
26 gRed G gIBSMun - 0-1 - Grupo de informações da redução de Alíquota 
27 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
28 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva do IBS de competência dos 
Municipios que será aplicada a base de cálculo, 
incluindo o gCompraGov/pRedutor, se houver. 
29 vIBSMun E gIBSMun N 1-1 13,2 Valor do IBS de competência do município 
30 vIBS E gIBSCBS N 1-1 13,2 Valor do IBS (soma de vIBSUF e vIBSMun) 
31 gCBS G gIBSCBS - 1-1 - Grupo de informações da CBS 
32 pCBS E gCBS N 1-1 3,2/3,4 Alíquota da CBS 
33 gDif G gCBS - 0-1 - Grupo de campos do diferimento 
34 pDif E gDif N 1-1 3,2/3,4 Percentual de diferimento 
35 vDif E gDif N 1-1 13,2 Valor do diferimento 
36 gDevTrib G gCBS - 0-1 - Grupo de informações da devolução do tributo 
37 pDevTrib E gDevTrib N 0-1 3,2/3,4 Percentual de devolução do tributo, conforme LC 
214/25 art. 118. 
38 vDevTrib E gDevTrib N 1-1 13,2 Valor da CBS devolvida.  
No fornecimento de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas no 
regulamento 
39 gRed G gCBS - 0-1 - Grupo de informações da redução de Alíquota 
40 pRedAliq E gRed N 1-1 3,2/3,4 Percentual da redução de Alíquota do cClassTrib 
41 pAliqEfet E gRed N 1-1 3,2/3,4 Alíquota efetiva da CBS que será aplicada a base 
de cálculo, incluindo o gCompraGov/pRedutor, se 
houver. 
42 gALCZFMCBS G gCBS - 0-1 - Grupo de operações em áreas incentivadas 
(ALC/ZFM) - CBS (alíquota zero) 
43 pAliqEfetRegCBS E gALCZFMCBS N 1-1 3,2/3,4 Percentual efetivo sem a redução  
Alíquota efetiva de referência da CBS aplicável à 
operação fora de áreas ou regimes incentivados. 
44 vTribRegCBS E gALCZFMCBS N 1-1 13,2 Valor efetivo sem a redução. 
Valor da CBS calculado para a operação fora de 
áreas ou regimes incentivado 
45 vCBS E gCBS N 1-1 13,2 Valor da CBS 
46 gTribRegular G gIBSCBS - 0-1 - Grupo de informações da Tributação Regular. 
Informar como seria a tributação caso não cumprida 
a condição resolutória/suspensiva. Exemplo 1: Art. 
442, §4. Operações com ZFM e ALC. Exemplo 2: 
Operações com suspensão do tributo. 
47 CSTReg E gTribRegular N 1-1 3 Código da Situação Tributária  
Informado como seria o CST caso não cumprida a 
condição resolutória/suspensiva 
48 cClassTribReg E gTribRegular N 1-1 6 Código de Classificação Tributária  
Informado como seria o cClassTrib caso não 
cumprida a condição resolutória/suspensiva 
49 pAliqEfetRegIBSUF E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da UF 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
50 vTribRegIBSUF E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo da UF caso 
não cumprida a condição resolutória/suspensiva

## Página 5

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 5 / 14 
 
51 pAliqEfetRegIBSMun E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva do Município 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
52 vTribRegIBSMun E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo do 
Município caso não cumprida a condição 
resolutória/suspensiva 
53 pAliqEfetRegCBS E gTribRegular N 1-1 3,2/3,4 Alíquota efetiva da CBS 
Informado a Alíquota caso não cumprida a condição 
resolutória/suspensiva 
54 vTribRegCBS E gTribRegular N 1-1 13,2 Informado como seria o valor do Tributo CBS caso 
não cumprida a condição resolutória/suspensiva 
55 gTribCompraGov G gIBSCBS - 0-1 - Grupo de informações da composição do valor do 
IBS e da CBS em compras governamental 
56 pAliqIBSUF E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS da UF utilizada 
57 vTribIBSUF E gTribCompraGov N 1-1 13,2 Valor do Tributo do IBS da UF 
Valor que seria devido a UF, sem aplicação do Art. 
473. da LC 214/20025 
58 pAliqIBSMun E gTribCompraGov N 1-1 3,2/3,4 Alíquota IBS do Município utilizada 
59 vTribIBSMun E gTribCompraGov N 1-1 13,2 Valor do Tributo do Município da UF  
Valor que seria devido ao Município, sem aplicação 
do Art. 473. da LC 214/20025 
60 pAliqCBS E gTribCompraGov N 1-1 3,2/3,4 Alíquota da CBS utilizada 
61 vTribCBS E gTribCompraGov N 1-1 13,2 Valor do Tributo da CBS  
Valor que seria devido a CBS, sem aplicação do Art. 
473. da LC 214/20025 
62 gEstornoCred G IBSCBS - 0-1 - Grupo de informações de estorno de crédito. 
Informado conforme indicador no cClassTrib 
63 vIBSEstCred E gEstornoCred N 1-1 13,2 Valor do IBS a ser estornado 
64 vCBSEstCred E gEstornoCred N 1-1 13,2 Valor do CBS a ser estornado

## Página 6

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 6 / 14 
 
3 Novo campo Inscrição Suframa do Emitente 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 ISUFEmit E Emit C 0-1 8-9 Informar o número do Cadastro do emitente na 
Suframa. Campo obrigatório nas operações que se 
beneficiam de incentivos fiscais existentes nas áreas 
sob controle da SUFRAMA com alíquota zero da 
CBS referente aos arts. 451 e 466 da LC 214/25. 
 
 
  
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se Inscrição do emitente na SUFRAMA (emit/ISUFemit) 
informada: 
 - Município do Emitente (tag:emit/cMun) diferente de:  
 
ZFM:  
1302603-Manaus,  
1303569-Rio Preto da Eva,  
1301902-Itacoatiara 
 
ALC:  
1304062-Tabatinga (AM),  
1600303-Macapá (AP),  
1600600-Santana (AP),  
1100106-Guajará-Mirim (RO),  
1400100-Boa Vista (RR),  
1400159-Bonfim (RR),  
1200104-Brasileia (AC),  
1200252-Epitaciolândia (AC),  
1200203-Cruzeiro do Sul (AC) 
Obrig. 1015 Rej. Rejeição: Município do Emitente não pertence à 
área incentivada - CBS 
002 Se inscrição do emitente na SUFRAMA 
(emit/ISUFemit) informada: 
- Validar inscrição com dígito verificador inválido 
Obrig. 1016 Rej. Rejeição: Inscrição do emitente na Suframa com 
dígito verificador inválido

## Página 7

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 7 / 14 
 
4 Validações do grupo de Devolução 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado grupo de Devolução do IBS da UF 
(gIBSUF/gDevTrib): 
 
- Percentual de devolução do IBS UF (pDevTrib) DEVE 
SER informado 
Obrig. 1040 Rej. Rejeição: Percentual de devolução de IBS Estadual 
não informado 
002 Se informado grupo de Devolução do IBS da UF 
(gIBSUF/gDevTrib):  
 
- Valor do IBS UF devolvido (vDevTrib) deverá ser 
resultante da Base de Cálculo x Percentual do IBS UF 
x Percentual do tributo devolvido:  
vDevTrib = vBC x (pIBSUF / 100) x (pDevTrib / 100)  
 
Observação 1: Em caso de preenchimento do grupo de 
Redução de Alíquota (gIBSUF/gRed) a alíquota utilizada 
deverá ser a tag Alíquota Efetiva 
(gIBSUF/gRed/pAliqEfet) ao invés do pIBSUF. 
 
Observação 2: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig 1041 Rej. Rejeição: Valor do IBS UF devolvido difere do 
calculado 
003 Se informado grupo de Devolução do IBS do Munícipio 
(gIBSMun/gDevTrib): 
 
- Percentual de devolução do IBS Mun (pDevTrib) 
DEVE SER informado 
Obrig. 1042 Rej. Rejeição: Percentual de devolução de IBS Municipal 
não informado 
004 Se informado grupo de Devolução do IBS do Município 
(gIBSMun/gDevTrib):  
 
- Valor do IBS Mun devolvido (vDevTrib) deverá ser 
resultante da Base de Cálculo x Percentual do IBS Mun 
x Percentual do tributo devolvido:  
vDevTrib = vBC x (pIBSMun / 100) x (pDevTrib / 100)  
 
Observação 1: Em caso de preenchimento do grupo de 
Redução de Alíquota (gIBSMun/gRed) a alíquota 
utilizada deverá ser a tag Alíquota Efetiva 
(gIBSMun/gRed/pAliqEfet) ao invés do pIBSMun..  
 
Observação 2: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig 1043 Rej. Rejeição: Valor do IBS Mun devolvido difere do 
calculado 
005 Se informado grupo de Devolução da CBS 
(gCBS/gDevTrib): 
 
- Percentual de devolução da CBS (pDevTrib) DEVE 
SER informado 
Obrig. 1044 Rej. Rejeição: Percentual de devolução da CBS não 
informado 
006 Se informado grupo de Devolução da CBS 
(gCBS/gDevTrib):  
 
- Valor da CBS devolvida (vDevTrib) deverá ser 
resultante da Base de Cálculo x Percentual da CBS x 
Percentual do tributo devolvido:  
vDevTrib = vBC x (pCBS / 100) x (pDevTrib / 100)  
 
Observação 1: Em caso de preenchimento do grupo de 
Redução de Alíquota (gCBS/gRed) a alíquota utilizada 
deverá ser a tag Alíquota Efetiva (gCBS/gRed/pAliqEfet) 
ao invés do pCBS.  
 
Observação 2: Aceitar uma tolerância de 0,01 a mais 
ou a menos 
Obrig. 1045 Rej. Rejeição: Valor da CBS devolvida difere do 
calculado

## Página 8

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 8 / 14 
 
5 Validações Alíquota da CBS e Alíquota zero da CBS (validar em cada item) 
A tabela de Classificação de Produtos (cClass) receberá um indicador para sinalizar quais códigos dizem respeito 
a serviços executados presencialmente e que permitirão alíquota zero de CBS quando a prestação ocorrer em 
área incentivada (ZFM e ALC). As validações a seguir são executadas em cada item da nota: 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 VÁLIDA PARA 2026: 
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
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 9

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 9 / 14 
 
002 VÁLIDA A PARTIR de 2027: 
A alíquota da CBS (tag: pCBS) deve ser igual a 
alíquota vigente para o período conforme legislação. 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: Se o grupo gALCZFMCBS estiver 
preenchido, o pCBS deve ser igual a zero.  
Observação: Consultar Tabela de Alíquotas da CBS. 
IMPORTANTE: Somente serviços PRESENCIAIS 
podem utilizar o benefício da alíquota zero para Área 
Incentivada. 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida 
003 Se informado gCBS/gALCZFMCBS: 
Inscrição do emitente na Suframa (tag:emit/ISUFemit) 
DEVE SER informada 
Obrig. 1021 Rej. Rejeição: Inscrição do emitente na Suframa não 
informado 
004 Se informado gCBS/gALCZFMCBS: 
Somente aceitar o preenchimento deste grupo se: 
- Código de Classificação de Produto (cClass) do item 
permitir CBS com alíquota zero em zona incentivada 
- Município do Fato Gerador (cMunFG) e Município 
do Emitente devem pertencer a um município da ZFM 
Cod. IBGE Nome Município 
1302603 Manaus 
1303569 Rio Preto da Eva 
1301902 Itacoatiara 
 
OU 
- Município do Fato Gerador e Município do 
Emitente devem estar localizados nos municípios 
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
Observação: As cores definem quais municípios são da 
mesma área incentivada, e isto será observado na regra 
de validação 
Obrig. 1022 Rej. Rejeição: Grupo de operações em áreas 
incentivadas (ALC/ZFM) - CBS (alíquota zero) não 
permitido

## Página 10

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 10 / 14 
 
Esta RV verifica se contribuinte preenche os requisitos 
do art. 451 ou 466 LCP 214/25 para a alíquota zero da 
CBS 
 Se informado gCBS/gALCZFMCBS:  
- vTribRegCBS deverá ser resultante de:  
vTribRegCBS = gIBSCBS/vBC x 
(gALCZFMCBS/pAliqEfetRegCBS / 100) 
Obrig, 1024 Rej. Rejeição: Valor da CBS para operação fora de áreas 
ou regimes incentivado difere do calculado 
6 Antecipação de Pagamento 
A Antecipação de Pagamento em notas fatura ocorrerá da seguinte forma: 
 
Tabela Classificação de Produtos (cClass): 
 
 A tabela de classificação de produtos (cClass) receberá um novo atributo para diferenciar prestação 
continuada de prestação não continuada. 
 Este atributo tipo de prestação do serviço estará visível no portal da SVRS e terá as seguintes opções: 
0 - Não se aplica 
1 - Continuada 
2 - Não Continuada 
3 - Ambos (continuada e não continuada) 
 
Antecipação de Serviço Não Continuado: 
 
 A Nota de antecipação deve ter a informação do tipo de pagamento antecipado para serviços não 
continuados (tpPagAnt=1). 
 Todos os itens desta nota devem indicar cClass de serviço não continuado (cClass do tipo de prestação 
2 e 3).  
 A nota de fornecimento que será emitida posteriormente poderá ter itens normais do faturamento para o 
cliente e itens que fazem referência à nota de pagamento antecipado, esta nota deverá ter o tipo de 
pagamento de Fornecimento de Pagamento realizado anteriormente (tpPagAnt = 3) 
 Cada item que estiver fornecendo serviços já pagos deve referenciar a chave de acesso no campo 
gPagAntecipado\chDFePagAnt.  
 Este item NÃO ACEITARÁ Classificação Tributária (cClassTrib) de Documento com informações de 
fornecimento, mas com tributação realizada em fatura anterior (820008) 
Antecipação de Serviço Continuado: 
 
 A Nota de antecipação deve ter a informação do tipo de pagamento de serviços continuados (antes da 
prestação) (tpPagAnt=2). 
 Todos os itens desta nota devem indicar cClass de serviço continuado (cClass do tipo de prestação 1 e 
3).

## Página 11

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 11 / 14 
 
 A nota de fornecimento emitida posteriormente poderá ter itens normais do faturamento para o cliente e 
itens que fazem referência à nota de pagamento antecipado, esta nota deverá ter o tipo de pagamento 
de Fornecimento de Pagamento realizado anteriormente (tpPagAnt = 3) 
 Cada item que estiver fornecendo serviços já pagos deve referenciar a chave de acesso no campo 
gPagAntecipado\chDFePagAnt. 
 Este item DEVERÁ ter Classificação Tributária (cClassTrib) de Documento com informações de 
fornecimento, mas com tributação realizada em fatura anterior (820008) 
IMPORTANTE: As notas de antecipação de pagamento podem ser referenciadas em várias notas de fornecimento. 
 
Notas de faturamento padrão que não possuem antecipação NÃO DEVEM informar o campo tpPagAnt. 
 
Itens que fazem referência a antecipação não podem utilizar cClass de dedução (iniciados por 5). Para deduzir o 
valor antecipado, indica-se lançar um item adicional de dedução. 
Notas de antecipação (tpPagAnt=3) devem obrigatoriamente ter pelo menos um item com grupo gPagAntecipado 
informado. 
Alteração no grupo ide: 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 tpPagAnt E ide N 0-1 1 Tipo Pagamento ou Pagamento Antecipado 
Informar: 
1 - Pagamento Antecipado de Serviços Não 
Continuados 
2 - Pagamento de serviços continuados (antes da 
prestação) 
3 - Fornecimento com pagamento realizado 
anteriormente 
Este campo é opcional e apenas deve ser 
informado em notas de pagamento que ocorre antes 
da prestação do serviço e na nota de fornecimento 
associada a esses pagamentos,  
Notas Normais que retratam a prestação de serviço 
continuado mensal da nota fatura (contendo ou não 
itens de serviço não continuado) em que o 
pagamento não foi antecipado NÃO DEVEM 
INFORMAR ESSE CAMPO. 
A tabela cClass terá uma flag que sinaliza se o tipo 
de item é de prestação continuada ou não 
continuada

## Página 12

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 12 / 14 
 
Alteração no grupo det\prod: 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 gPagAntecipado G prod (em cada item) - 0-1 - Grupo de antecipação de pagamento 
Permite informar apenas quando tpPagAnt=3 
2 chDFePagAnt E gPagAntecipado C 1-1 44 Chave de acesso do DFe de antecipação de 
pagamento (com tpPagAnt=1 ou 2) 
Referência a DFe emitido anteriormente, referente a 
pagamento antecipado 
3 nItemPagAnt E gPagAntecipado N 0-1 3 Número do item do DFe de antecipação para 
referência direta a um item.  
Observação: se a nota de antecipação for retradada 
na forma de um item apenas na nota de 
fornecimento, essa campo não deve ser informado. 
 Validações a serem executadas em cada item da nota: 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
Rejeitar se Tipo de Antecipação de pagamento 
(tag:ide\tpPagAnt) for DIFERENTE de 3 (Fornecimento 
com pagamento realizado anteriormente) 
Obrig. 1026 Rej. Rejeição: Grupo de pagamento antecipado não 
deve ser informado [nItem: NNN] 
002 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
Se Tipo de Antecipação de pagamento 
(tag:ide\tpPagAnt) for IGUAL de 3 (Fornecimento com 
pagamento realizado anteriormente), PELO MENOS 
UM ITEM deverá ter o grupo de Pagamento 
Antecipado informada (det\prod\gPagAntecipado) 
Obrig. 1027 Rej. Rejeição: Grupo de pagamento antecipado deve 
deve ser informado em pelo menos um item da nota 
003 Se Tipo de Antecipação de pagamento 
(tag:ide\tpPagAnt) for informado IGUAL a 1 
(Pagamento Antecipado de Serviços Não 
Continuados): 
Rejeitar a nota SE PELO MENOS UM cClass de 
produto informado nos itens for de Serviço Continuado 
ou Não aplicável 
Obrig. 1028 Rej. Rejeição: Classificação de Produto de serviço 
continuado inválida para o tipo de pagamento 
antecipado [nItem: NNN] 
004 Se Tipo de Antecipação de pagamento 
(tag:ide\tpPagAnt) for informado IGUAL a 2 
(Pagamento de serviços continuados antes da 
prestação): 
Rejeitar a nota SE PELO MENOS UM cClass de 
produto informado nos itens for de Serviço NÃO 
Continuado ou Não aplicável 
Obrig. 1029 Rej. Rejeição: Classificação de Produto de serviço não 
continuado inválida para o tipo de pagamento 
antecipado [nItem: NNN] 
005 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
- Validar chave de acesso da NFAg de Pagamento 
antecipadoRetornar motivo da rejeição da Chave de 
Acesso: CNPJ zerado ou inválido, Ano < 2026 ou maior 
que atual, Mês inválido (0 ou > 12), Modelo diferente de 
75, Número zerado, Tipo de emissão inválido, UF 
inválida ou DV inválido) 
[chNFAg:999999999999999999999999999999999999
99999999] 
[Motivo: XXXXXXXXXXXX] 
Obrig 1030 Rej. Rejeição: Chave de acesso da NFAg de pagamento 
antecipado inválida [nItem: NNN]

## Página 13

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 13 / 14 
 
006 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
- Verificar se existe a NFAg de Pagamento antecipado. 
Acesso BD NFAg (Chave: UF, CNPJ Emit, Modelo, 
Série, Nro) 
Obrig 1031 Rej. Rejeição: NFAg de de pagamento antecipado 
inexistente [nItem: NNN] 
007 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
Acessar BD NFAg (Chave: UF, CNPJ Emit, Modelo, 
Série, Nro) 
 - Verificar se a NFAg de pagamento antecipado existe 
com diferença na Chave de Acesso 
Retornar a chave de acesso já autorizada, o número do 
protocolo e data de autorização da NFAg 
[chNFAg:999999999999999999999999999999999999
99999999] 
[[nProt:999999999999999][dhAut:AAAA-MM-
DDTHH:MM:SS TZD]. 
Obrig 1032 Rej. Rejeição: NFAg de pagamento antecipado com 
diferença de Chave de Acesso 
[chNFAg: 
99999999999999999999999999999999999999999999] 
[nProt:999999999999999][dhAut: AAAA-MM-
DDTHH:MM:SS TZD] [nItem: NNN] 
008 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
NFAg de pagamento antecipado deve ser do tipo 
Normal ou Substituição. 
Acessar BD NFAg (Chave: UF, CNPJ Emit, Modelo, 
Série, Nro) 
Obrig 1033 Rej. Rejeição: NFAg de pagamento antecipado é 
diferente de Normal ou Substituição [nItem: NNN] 
009 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
- Verificar se a NFAg de pagamento antecipado está 
com Situação: Autorizado o Uso. 
Acesso BD NFAg (Chave: UF, CNPJ Emit, Modelo, 
Série, Nro) 
Obrig 1034 Rej. Rejeição: NFAg de pagamento antecipado deve 
estar com a situação autorizada (não pode estar 
cancelado) [nItem: NNN] 
010 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
- Verificar se a NFAg de pagamento antecipado foi 
substituída. 
Obrig. 1035 Rej. Rejeição: NFAg de pagamento antecipado não pode 
ter sido substituída [nItem: NNN] 
011 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item: 
 
O Código de Classificação do Produto (cClass) NÃO 
PODERÁ SER de dedução (iniciado por 5), caso 
contrário deverá ser rejeitado 
 
Observação: a dedução deste valor poderá ser feita em 
um outro item adicional da nota que não faça indicação 
de antecipação de pagamento 
Obrig. 1036 Rej. Rejeição: Código de classificação de produto de 
dedução não é permitido para NFAg de pagamento 
antecipado referenciada [nItem: NNN] 
012 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item e 
informado grupo de IBSCBS: 
Se a NFAg de pagamento antecipado possuir tpPagAnt 
= 1 (Pagamento Antecipado de Serviços Não 
Continuados). 
 
O Código de Classificação Tributário (cClassTrib) NÃO 
PODERÁ ser de tributação realizada em fatura anterior 
(820008) 
Obrig. 1037 Rej. Rejeição: cClassTrib inválido para NFAg de 
pagamento antecipado referenciada de serviço não 
continuado [nItem: NNN] 
013 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item e 
informado grupo de IBSCBS: 
Se a NFAg de pagamento antecipado possuir tpPagAnt 
= 2 (Pagamento de serviços continuados antes da 
prestação): 
O Código de Classificação Tributário (cClassTrib) DEVE 
SER de Tributação Realizada em Fatura Anterior 
(820008) 
Obrig. 1038 Rej. Rejeição: cClassTrib para NFAg de pagamento 
antecipado referenciada de serviço continuado deve 
utilizar código 820008 [nItem: NNN]

## Página 14

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.002 v1.00 
 
 
Página 14 / 14 
 
014 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item e 
informado grupo de IBSCBS: 
 
- O CNPJ-Base da chave de acesso da NFAg de 
pagamento antecipado deve ser do mesmo CNPJ-Base 
do emitente da NFAg de fornecimento 
Obrig. 1020 Rej. Rejeição: CNPJ Base do DFe de antecipação deve 
ser igual ao CNPJ Base do DFe de fornecimento 
015 Se o grupo de antecipação de pagamento (grupo: 
det\prod\gPagAntecipado) estiver informado no item e 
informado grupo de IBSCBS: 
 
- Não aceitar chaves de acesso repetidas dentro do 
grupo gPagAntecipado 
Obrig. 1046 Rej. Rejeição: Chave de acesso de DFe de antecipação 
repetida no grupo de informações do Pagamento 
antecipado
