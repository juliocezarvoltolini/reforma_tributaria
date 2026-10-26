---
id: bpe-bpe-nota-tecnica-2026-002-v1-01
titulo: Nota Técnica BP-e 2026.002 v.1.01 - Publicada em 04/08/2026
tipo: nota.tecnica
versao: '1.01'
data: '2026-08-04'
documento_fiscal: BP-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Yh82ACQFsMw=
arquivo_original: fontes/acervo/bpe-bpe-nota-tecnica-2026-002-v1-01.pdf
sha256_original: 41a1ffbd52be79cbad4b687578162ca0918b0895ad74801f0d2fe6ae149925bc
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 644c822bb6a6f614d4c9c73083963addb5d4d5ee0a738bd39d8046b6c15b75af
---

## Página 1

Projeto Bilhete de Passagem 
Eletrônico 
 
Nota Técnica 2026.002 – Reforma Tributária do Consumo 
Versão 1.01 de 16 de julho de 2026

## Página 2

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 2 / 9 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 3 
2 Exigência das informações de IBS e CBS ....................................................................... 3 
3 Campos do grupo IBS/CBS ............................................................................................. 3 
4 Novo campo Inscrição Suframa do Emitente ................................................................... 6 
5 Validações do grupo de Devolução ................................................................................. 6 
6 Validações Alíquota da CBS e Alíquota zero da CBS ...................................................... 7

## Página 3

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 3 / 9 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Obrigatoriedade do preenchimento dos campos da RTC 01/07/2026 03/08/2026 
1.00  Campo da inscrição SUFRAMA do emitente para operações ALC 
 Atualização de regras de validação 
 Regras do CBS e CBS alíquota zero 
03/08/2026 31/08/2026 
1.01  Alteração da data de exigência do preenchimento dos campos da RTC Implantada Implementação 
futura 
Observação: Esta NT tem 2 datas, uma para a Regra de Preenchimento dos campos da RTC e outra para o 
restante das definições desta NT 
1 Introdução 
Esta Nota Técnica apresenta evoluções da NT 2025.001 RTC contemplando novos pontos relevantes previstos na 
legislação como Antecipação de Pagamento, obrigatoriedade do preenchimento das informações de IBS e CBS, 
percentual de devolução de tributos (cashback), alíquota zero da CBS em Área de Livre Comércio e melhorias na 
redação das regras de validação. 
Esta NT é aplicável a BPe, BPeTA e BPeTM. 
2 Exigência das informações de IBS e CBS 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Não informado grupo de imposto IBS e CBS (grupo: 
imp/IBSCBS) 
 
HOMOLOGAÇÃO: 01/07/2026 
PRODUÇÃO: implementação futura 
 
IMPORTANTE: Aplicável para emitente com CRT 
3=Regime Normal 
Obrig. 310 Rej. Rejeição: IBS / CBS não informado 
 
3 Campos do grupo IBS/CBS 
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

## Página 4

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 4 / 9 
 
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

## Página 5

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 5 / 9 
 
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
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 6 / 9 
 
4 Novo campo Inscrição Suframa do Emitente 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
1 ISUFEmit E emit C 0-1 8-9 Informar o número do Cadastro do emitente na 
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
5 Validações do grupo de Devolução 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 Se informado grupo de Devolução do IBS da UF 
(gIBSUF/gDevTrib): 
- Grupo de devolução do IBS da UF informado 
indevidamente 
 
Observação: esse grupo só poderá ser informado em notas 
fatura (NF3e, NFCom, NFAg e NFGas) 
Obrig. 1017 Rej. Rejeição: Grupo de devolução não permitido para 
este modelo de DFe 
002 Se informado grupo de Devolução do IBS do Munícipio 
(gIBSMun/gDevTrib): 
- Grupo de devolução do IBS de competência do 
Município informado indevidamente 
 
Observação: esse grupo só poderá ser informado em notas 
fatura (NF3e, NFCom, NFAg e NFGas) 
Obrig. 1018 Rej. Rejeição: Grupo de devolução não permitido para 
este modelo de DFe 
003 Se informado grupo de Devolução da CBS 
(gCBS/gDevTrib): 
- Grupo de devolução da CBS informado 
indevidamente 
 
Observação: esse grupo só poderá ser informado em notas 
fatura (NF3e, NFCom, NFAg e NFGas) 
Obrig. 1019 Rej. Rejeição: Grupo de devolução não permitido para 
este modelo de DFe

## Página 7

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 7 / 9 
 
6 Validações Alíquota da CBS e Alíquota zero da CBS 
# Regra de Validação Aplic. cStat Efeito Mensagem 
001 VÁLIDA PARA 2026: 
Se informado grupo CBS (gCBS), a alíquota de CBS 
deverá ser de 0,90 % para documento com data de 
emissão no ano de 2026. (Art. 346 da LC 214/25) 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser 
igual a zero quando a condição abaixo for atendida: 
-Tipo do BPe diferente de BPeTM 
- Município de Início, Fim da Prestação e Emitente 
devem pertencer a um município da ZFM 
Cod. IBGE Nome Município 
1302603 Manaus 
1303569 Rio Preto da Eva 
1301902 Itacoatiara 
OU 
- Município de Início e Fim da Prestação devem 
estar localizados nos municípios pares da mesma ALC 
E o Emitente deve estar localizado em um município 
da mesma ALC que os municípios de início e fim 
fizerem parte. 
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
1200203-Cruzeiro do Sul 
(AC)  1200104-Brasileia (AC)  
1200203-Cruzeiro do Sul 
(AC)  1200252-Epitaciolândia (AC)  
1200203-Cruzeiro do Sul 
(AC)  1200203-Cruzeiro do Sul (AC)  
 
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 8

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 8 / 9 
 
002 VÁLIDA A PARTIR de 2027: 
A alíquota da CBS (tag: pCBS) deve ser igual a 
alíquota vigente para o período conforme legislação. 
Exceção: Se o cClassTrib possuir indicador de 
tributação regular o pCBS deve ser igual a zero 
Exceção 2: Se o grupo gALCZFMCBS estiver 
preenchido, o pCBS deve ser igual a zero.  
Observação: Consultar Tabela de Alíquotas da CBS. 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida 
003 Se informado gCBS/gALCZFMCBS: 
Inscrição do emitente na Suframa (tag:emit/ISUFemit) 
DEVE SER informada 
Obrig. 1021 Rej. Rejeição: Inscrição do emitente na Suframa não 
informado 
004 Se informado gCBS/gALCZFMCBS: 
Rejeitar se o tipo do BPe for igual a 4 – BPe Transporte 
Metropolitano 
Obrig. 1023 Rej. Rejeição: Informação da operação em zona 
incentivada CBS Zero não permitida para BPeTM 
004 Se informado gCBS/gALCZFMCBS: 
Somente aceitar o preenchimento deste grupo se: 
- Município de Início, Fim da Prestação e Emitente 
devem pertencer a um município da ZFM 
Cod. IBGE Nome Município 
1302603 Manaus 
1303569 Rio Preto da Eva 
1301902 Itacoatiara 
 
OU 
- Município de Início e Fim da Prestação devem 
estar localizados nos municípios pares da mesma ALC 
E o Emitente deve estar localizado em um município 
da mesma ALC que os municípios de início e fim 
fizerem parte.  
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
1200203-Cruzeiro do Sul 
(AC)  1200104-Brasileia (AC)  
1200203-Cruzeiro do Sul 
(AC)  1200252-Epitaciolândia (AC)  
1200203-Cruzeiro do Sul 
(AC)  1200203-Cruzeiro do Sul (AC)  
Obrig. 1022 Rej. Rejeição: Grupo de operações em áreas 
incentivadas (ALC/ZFM) - CBS (alíquota zero) não 
permitido

## Página 9

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.002 v1.01 
 
 
Página 9 / 9 
 
Observação: As cores definem quais municípios são da 
mesma área incentivada, e isto será observado na regra 
de validação 
Esta RV verifica se contribuinte preenche os requisitos 
do art. 451 ou 466 LCP 214/25 para a alíquota zero da 
CBS 
 Se informado gCBS/gALCZFMCBS:  
- vTribRegCBS deverá ser resultante de:  
vTribRegCBS = gIBSCBS/vBC x 
(gALCZFMCBS/pAliqEfetRegCBS / 100) 
Obrig, 1024 Rej. Rejeição: Valor da CBS para operação fora de áreas 
ou regimes incentivado difere do calculado
