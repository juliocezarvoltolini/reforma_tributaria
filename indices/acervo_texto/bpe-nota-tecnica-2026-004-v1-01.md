---
id: bpe-nota-tecnica-2026-004-v1-01
titulo: Nota Técnica 2026.004_v1.01 - Publicada em 30/10/2026
tipo: nota.tecnica
versao: '1.01'
data: '2026-10-30'
documento_fiscal: BP-e (BP-e, BP-e TM, BP-e TA)
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ir3st/saoU0=
arquivo_original: fontes/acervo/bpe-nota-tecnica-2026-004-v1-01.pdf
sha256_original: 81bc605202f3d1b64b365aa9c5a0ccb0dc3d2ea9a7b7c1c7986cc83f9a7741d0
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 40a2321ce82e7ba8ecebc25cd2506d56e15331b060df683896f7203b9bdd1c9c
---

## Página 1

Projeto Bilhete de Passagem 
Eletrônico 
 
Nota Técnica 2026.004 – Valor Líquido 
Versão 1.01 outubro de 2026

## Página 2

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 2 / 9 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Alterações no Leiaute do DFe ......................................................................................... 4 
Valor Líquido do Bilhete de Passagem sem tributos ...........................................................4 
Grupo Total (Apenas BPeTM) .............................................................................................4 
Criação do Grupo de informações da Multa e Juros no BPe (Aplicável a BPe e BPeTA) ....5 
3 Validações dos campos do IBS e CBS ............................................................................ 6 
4 Total Geral do Documento Fiscal Eletrônico ................................................................... 8 
6 No BPe TA permitir endereço do comprador opcional ..................................................... 9

## Página 3

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 3 / 9 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Criação dos campos que representam os valores líquidos de impostos  
 Exceção nas regras de validação de alíquotas para o ambiente de 
homologação 
 Ajuste na regra do valor total do DFe 
 Grupo endereço do comprador opcional no BPeTA 
  
1.01  Ajuste da data de Homologação 
 A regra do valor total do DFe retorna a soma de IBS e CBS a partir de 2027 
 Retirada orientação de inclusão de IBS e CBS na composição do vBP 
 Inclusão do grupo de informações de Multa e Juros do BPe 
Até 26/10/2026 16/11/2026

## Página 4

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 4 / 9 
 
1 Introdução 
Criação de campos para o valor líquido do produto 
  
Com o objetivo de ampliar a transparência na formação do preço da operação, foi criado o campo Valor Líquido 
do Bilhete. Esse campo permite identificar o valor da prestação do serviço antes da incorporação dos tributos 
vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o valor líquido dos valores tributários 
agregados ao preço. 
  
A medida busca preservar a rastreabilidade da formação do valor informado no DFe, especialmente diante da 
sistemática do IBS e da CBS. 
  
Dessa forma, o novo campo permite evidenciar o valor líquido total da prestação do serviço, proporcionando maior 
transparência ao contribuinte, ao adquirente e às Administrações Tributárias quanto à composição do preço e à 
participação dos tributos no valor final da prestação. 
  
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. A base de cálculo 
dos tributos deverá ser determinada de acordo com a legislação aplicável. Desta forma: 
 No campo vBPLiq deve ser informado o valor líquido do serviço, sem qualquer tributo; 
 No campo vBP deve ser informado o valor total do serviço, desconsiderados os valores de IBS e CBS; 
No total do documento fiscal: 
 No campo vTotDFe deve ser informado o valor correspondente a soma do vBP (-vDesconto) + IBS + CBS. 
2 Alterações no Leiaute do DFe 
Valor Líquido do Bilhete de Passagem sem tributos 
 
BPe e BPeTA: 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... infValorBPe G infBPe - - - Informações dos valores do Bilhete de 
Passagem 
 vBP E infValorBPe N 1-1 13v2 Valor do Bilhete de Passagem 
Observação: A partir 2027, os valores de IBS e 
CBS compõem o Valor Total do Bilhete 
 vBPLiq E infValorBPe N 0-1 13v2 Valor Líquido total do Bilhete SEM tributos 
 
 
BPeTM: 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... det G detBPeTM - 1-99 - Grupo de informações detalhadas do BPe TM 
 vBP E det N 1-1 13v2 Valor da soma dos Bilhetes de Passagem da 
viagem 
Observação: A partir 2027, os valores de IBS e 
CBS compõem o Valor Total do Bilhete 
 vBPLiq E det N 0-1 13v2 Valor Líquido total da soma dos Bilhetes da viagem 
SEM tributos 
Grupo Total (Apenas BPeTM) 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
 vBP E total N 1-1 13v2 Valor Total do Bilhete de Passagem Transporte 
Metropolitano 
 vBPLiq E total N 0-1 13v2 Valor Total Líquido Sem Tributos do Bilhete de 
Passagem Transporte Metropolitano

## Página 5

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 5 / 9 
 
Validações do total 
Regra de Validação Aplic. cStat Efeito Mensagem 
Total Líquido do BPeTM sem tributos (tag: 
total\vBPLiq) difere do somatório do valor líquido sem 
tributos do detalhamento do BPeTM.  
Obrig. 1054 Rej. Rejeição: Total Líquido Sem tributos difere do 
somatório dos bilhetes 
Criação do Grupo de informações da Multa e Juros no BPe (Aplicável a BPe e 
BPeTA) 
O novo grupo de informações deverá ser utilizado para lançar um BPe com multa e juros referente a um BPe 
emitido anteriormente. O BPe de multa e juros deverá apresentar os mesmos dados do BPe referenciado. A 
tributação do IBS e CBS deverá ser somente o complemento que representa a multa e o juros.  
No caso do BPe rodoviário, aquaviário e ferroviário, o ICMS deverá ser declarado com CST 41. 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 gMultaJuros G Ide G 0-1 - Grupo de informações de multa e juros 
 chBPeRef E gMultaJuros E 1-1 44 Chave de acesso do BPe de referenciado 
 
Validações da Multa e Juros 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informado grupo de Multa e Juros do BPe: 
 
- O CST do ICMS informado deverá ser 41 (grupo 
ICMS45) 
Obrig. 1072 Rej. Rejeição: BPe de multa e juros não pode ser 
tributado pelo ICMS 
Se informado grupo de Multa e Juros do BPe: 
- Validar chave de acesso do BPe Referenciado 
 
Retornar a primeira chave inválida e o motivo da 
rejeição da Chave de Acesso: CNPJ zerado ou 
inválido, Ano < 2017 ou maior que atual, Mês inválido 
(0 ou > 12), Modelo diferente de 63, Número zerado, 
Tipo de emissão inválido, UF inválida ou DV inválido) 
[chBPe: 
99999999999999999999999999999999999999999999
][Motivo: XXXXXXXXXXXX] 
Obrig. 1073 Rej. Rejeição: Chave de acesso do BPe referenciado em 
Multa e Juros inválida 
Se informado grupo de Multa e Juros do BPe: 
- Acessar BD CHAVES BPE (Chave: UF, CNPJ Emit, 
Modelo, Série, Nro): 
    - O BPe referenciado (chBPeRef) deve existir  
Facult. 1074 Rej. Rejeição: BPe referenciado em Multa e Juros 
inexistente na base de dados da SEFAZ 
[chBPe: 
999999999999999999999999999999999999999999
99] 
Se informado grupo de Multa e Juros do BPe: 
 
-Acessar BD CHAVES BPE (Chave: UF, CNPJ Emit, 
Modelo, Série, Nro): 
    - O BPe referenciado (chBPeRef) não pode existir 
com diferença de chave de acesso 
Facult. 1075 Rej. Rejeição: BPe referenciado em Multa e Juros existe 
com diferença de chave de acesso 
[chBPe: 
999999999999999999999999999999999999999999
99] 
[nProt:999999999999999][dhAut: AAAA-MM-
DDTHH:MM:SS TZD] 
Se informado grupo de Multa e Juros do BPe: 
 
-Acessar BD CHAVES BPE (Chave: UF, CNPJ Emit, 
Modelo, Série, Nro): 
    - O BPe referenciado (chBPeRef) não pode estar 
cancelados 
 
Facult. 1076 Rej. Rejeição: BPe referenciado em Multa e juros não 
pode estar cancelado  
 
Se informado grupo de Multa e Juros do BPe: 
 
-Acessar BD CHAVES BPE (Chave: UF, CNPJ Emit, 
Modelo, Série, Nro): 
    - O BPe referenciado (chBPeRef) não pode estar 
substituído 
 
Facult. 1077 Rej. Rejeição: BPe referenciado em Multa e juros não 
pode estar substituído  
 
Se informado grupo de Multa e Juros do BPe: 
 
O Emitente do BPe referenciado em multa e juros deve 
ser igual ao emitente do BPe de Multa e Juros 
Obrig. 1078 Rej. Rejeição: O emitente do BPe referenciado deve ser 
o mesmo do BPe de Multa e Juros

## Página 6

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 6 / 9 
 
Se informado grupo de Multa e Juros do BPe e 
comprador informado: 
 
O Comprador do BPe referenciado em multa e juros 
deve ser igual ao comprador do BPe de Multa e Juros 
Obrig. 1079 Rej. Rejeição: O comprador do BPe referenciado deve 
ser o mesmo do BPe de Multa e Juros 
 
Se informado grupo de Multa e Juros do BPe: 
 
As UF de início e fim da prestação devem ser as 
mesmas do BPe de Multa e Juros e do BPe 
referenciado 
Obrig. 1080 Rej. Rejeição: Início e fim de prestação do BPe 
referenciado em Multa e Juros deve ser o mesmo do 
BPe de Multa e Juros 
 
Se informado grupo de Multa e Juros do BPe: 
 
O CST e o cClassTrib do grupo IBSCBS deve ser o 
mesmo do BPe referenciado 
Obrig. 1081 Rej. Rejeição: Classificação tributária do BPe 
referenciado deve ser a mesma do BPe de Multa e 
Juros 
 
Se informado grupo de Multa e Juros do BPe: 
 
O tipo de BPe do BPe referenciado deve ser o mesmo 
do BPe de Multa e Juros 
Obrig. 1082 Rej. Rejeição: Tipo de BPe do BPe referenciado deve 
ser o mesmo do BPe de Multa e Juros 
 
Se tipo de emissão for Normal (tag:tpEmis=1): Data-
Hora de Emissão com atraso superior a 5 minutos em 
relação ao horário de recepção na SEFAZ 
Autorizadora. 
 
Exceção 1: A critério da UF, a rejeição acima pode ser 
efetuada para qualquer Tipo de Emissão. 
 
Exceção 2: A critério da UF, pode ser aceito BPe com 
Data de Emissão muito atrasada, desde que tenha sido 
emitido em contingência Off-Line (tag:tpEmis=2).  
O BPe transmitido para a SEFAZ Autorizadora após o 
prazo de 24 horas deve retornar: cStat=”150- 
Autorizado Uso do BPe, autorização fora de prazo”. 
 
Exceção 3: Essa regra não será aplicada se informado 
grupo de Juros e Multa (gMultaJuros)  
 
Observação: A emissão do BPe deve ocorrer de forma 
on-line, real-time, com uma tolerância de até 5 minutos, 
devido ao sincronismo de horário do Servidor da 
Empresa e o servidor da SEFAZ Autorizadora 
Obrig. 228 Rej. Rejeição: BPe com Data-Hora de Emissão muito 
atrasada 
3 Validações dos campos do IBS e CBS 
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
 0.05% para documento com data de emissão 
no ano de 2027 e 2028. (Art. 344 da LC 
214/25) 
 Alíquota de referência ou específica do 
Município a ser publicada para anos 
posteriores a 2028 
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Município inválida

## Página 7

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 7 / 9 
 
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
Observação: As cores definem quais municípios são 
da mesma área incentivada, e isto será observado na 
regra de validação 
EXCEÇÂO: Até que seja publicada a alíquota de 
referência da CBS para 2027, deverá ser informada a 
alíquota de 2026, inclusive para testes de simulação de 
2027 no AMBIENTE DE HOMOLOGAÇÃO (tpAmb=2), 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 8

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 8 / 9 
 
quando a alíquota de 2027 estiver publicada, ela 
também será aceita para testes ainda em 2026 
Se informado o indicador de Doação (indDoacao=1) e 
comprador estiver informado e for pessoa jurídica, o 
CNPJ-Base do emitente deve ser diferente do CNPJ-
Base do comprador 
Obrig. 1055 Rej. Rejeição: Doação com CNPJ do emitente igual do 
comprador 
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
01 vTotDFe E imp (BPe e BPeTA) ou 
total (BPeTM) 
 
E 0-1 13,2 Valor total do documento fiscal  
vBP - vDesconto + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser INFORMADO com 
a soma do total do BPe + IBS + CBS 
Para BPe e BPeTA: 
vTotDFe = infValorBPe/vBP (-
infValorBPe/vDesconto) + gIBSCBS/vIBS + 
gCBS/vCBS 
Para BPeTM: 
vTotDFe = total/vBP + IBSCBSTot/gIBS/vIBS + 
IBSCBSTot/gCBS/vCBS 
Para evento excesso de bagagem: 
vTotDFe = vTotBag + gIBSCBS/vIBS + gCBS/vCBS 
Exceção: Em 2026 não somar IBS e CBS, usar a 
fórmula:  
Para BPe: vTotDFe = infValorBPe/vBP  
Para BPeTM: vTotDFe = total/vBP  
Para excesso de bagagem: vTotDFe = vTotBag 
O total geral do DFe deverá ser informado 
REPETINDO o valor de vBP 
Obrig. 365 Rej. Rejeição: Total do DFe inválido

## Página 9

Projeto 
Bilhete de Passagem Eletrônico – Valor Líquido 
NT 2026.004 v1.01 
 
 
Página 9 / 9 
 
6 No BPe TA permitir endereço do comprador opcional 
F36 Se informado Comprador e informado endereço do 
comprador:  
- Município do Comprador deve pertencer à UF 
(verificar se as 2 posições da esquerda do código de 
município que identifica o código da UF é compatível 
com a sigla da UF informada) 
Obrig. 424 Rej Rejeição: Código de Município diverge da 
UF de localização comprador 
 
F37 Se informado Comprador,informado endereço do 
comprador e endereço do Comprador não for exterior 
(tag:enderComp/UF <> “EX”) 
- Código do Município do Comprador deve existir 
(Tabela Municípios do IBGE) 
Obrig. 425 Rej. Rejeição: Município do comprador 
inexistente 
 
F38 Se informado Comprador, informado endereço do 
comprador e endereço do Comprador for exterior 
(tag:enderComp/UF = “EX”) 
- Código do Município do Comprador deve ser 
9999999 
Obrig. 426 Rej. Rejeição: Código de Município inválido 
para comprador residente no exterior 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... comp G infBPe - 0-1 - Informações do comprador do BPe 
Informar quando diferente do passageiro 
 xNome E comp C 1-1 2-60 Razão social ou nome do comprador 
- Choice XML      A choice define que só pode ser usado uma das 3 
tags posteriores (CNPJ/CPF ou idEstrangeiro) 
 CNPJ CE comp C 1-1 14 CNPJ do comprador 
 CPF CE comp N 1-1 11 CPF do comprador 
 idEstrangeiro CE comp C 1-1 2-20 Identificador do comprador quando estrangeiro 
 IE E comp N 0-1 0-14 Informar a IE do comprador ou ISENTO se 
comprador é contribuinte do ICMS isento de 
inscrição no cadastro de contribuintes do ICMS. 
Caso o remetente não seja contribuinte do ICMS 
não informar a tag. 
 enderComp G comp - 0-1  Grupo de informações do endereço do comprador 
...
