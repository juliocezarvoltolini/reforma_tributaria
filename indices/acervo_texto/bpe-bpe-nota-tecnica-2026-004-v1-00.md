---
id: bpe-bpe-nota-tecnica-2026-004-v1-00
titulo: Nota Técnica BP-e 2026.004 v.1.00 - Publicada em 01/10/2026
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-01'
documento_fiscal: BP-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Fa+ynqmiRww=
arquivo_original: fontes/acervo/bpe-bpe-nota-tecnica-2026-004-v1-00.pdf
sha256_original: b09cab695f26ef5e3823c5d39fc76a5ddc7edc3a6ec984fae938c744f99a0b39
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 24383d594b746fa2fb2a1db9a54a1f6b831c8edca475ad9e71eefd12b0383804
---

## Página 1

Projeto Bilhete de Passagem 
Eletrônico 
 
Nota Técnica 2026.004 – Reforma Tributária do Consumo 
Versão 1.00 setembro de 2026

## Página 2

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 2 / 8 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Inclusão dos campos de valor líquido .............................................................................. 4 
3 Alterações no Leiaute do DFe ......................................................................................... 5 
Valor Líquido do Bilhete de Passagem sem tributos ...........................................................5 
Grupo Total (Apenas BPeTM) .............................................................................................5 
Validações do total .......................................................................................................................... 5 
4 Validações dos campos do IBS e CBS ............................................................................ 5 
5 Total Geral do Documento Fiscal Eletrônico ................................................................... 7 
6 No BPe TA permitir endereço do comprador opcional ..................................................... 8

## Página 3

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 3 / 8 
 
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
13/10/2026 16/11/2026

## Página 4

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 4 / 8 
 
1 Introdução 
Composição do valor do produto com IBS e CBS 
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. 
Para fins de preenchimento do BPe, os valores do IBS e da CBS incidentes na operação deverão ser acrescidos 
ao valor do produto ou serviço, compondo o valor informado no campo vBP. 
 
A inclusão dos valores do IBS e da CBS no campo vBP não implica sua inclusão na base de cálculo desses 
tributos. A base de cálculo do IBS e da CBS deverá ser determinada de acordo com a legislação aplicável. 
Dessa forma, os valores do IBS e da CBS, por já estarem compreendidos no valor do produto ou serviço, não 
deverão ser adicionados novamente na composição do valor total da BPe (vTotDFe), evitando duplicidade. 
 
Os valores de IBS e CBS permanecem destacados nos respectivos grupos tributários, porém são meramente 
informativos, uma vez que já estão compreendidos no vBP. 
 
2 Inclusão dos campos de valor líquido  
Com o objetivo de ampliar a transparência na formação do preço da operação, foi criado o campo Valor Líquido 
da Prestação do Serviço. Esse campo permite identificar o valor do serviço antes da incorporação dos tributos 
vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o valor líquido dos valores 
tributários agregados ao preço. 
 
A medida busca preservar a rastreabilidade da formação do valor informado na BPe, especialmente diante da 
sistemática do IBS e da CBS, cujos valores passam a compor o valor do serviço para fins de representação 
documental, sem perder a identificação da parcela correspondente ao valor líquido da prestação. 
 
Dessa forma, o novo campo permite evidenciar o valor líquido total da prestação, proporcionando maior 
transparência ao contribuinte, ao adquirente e às Administrações Tributárias quanto à composição do preço e à 
participação dos tributos no valor final da prestação.

## Página 5

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 5 / 8 
 
3 Alterações no Leiaute do DFe 
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
Validações do total 
Regra de Validação Aplic. cStat Efeito Mensagem 
Total Líquido do BPeTM sem tributos (tag: 
total\vBPLiq) difere do somatório do valor líquido sem 
tributos do detalhamento do BPeTM.  
Obrig. 1054 Rej. Rejeição: Total Líquido Sem tributos difere do 
somatório dos bilhetes 
4 Validações dos campos do IBS e CBS 
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

## Página 6

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 6 / 8 
 
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
4  1600303-Macapá (AP)  1600303-Macapá (AP)  
1600303-Macapá (AP)  1600600-Santana (AP)  
1600600-Santana (AP)  1600303-Macapá (AP)  
1600600-Santana (AP)  1600600-Santana (AP)  
5  1200104-Brasileia (AC)  1200104-Brasileia (AC)  
1200104-Brasileia (AC)  1200252-Epitaciolândia (AC)  
1200104-Brasileia (AC)  1200203-Cruzeiro do Sul (AC)  
1200252-Epitaciolândia (AC)  1200104-Brasileia (AC)  
1200252-Epitaciolândia (AC)  1200252-Epitaciolândia (AC)  
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida

## Página 7

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 7 / 8 
 
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
5 Total Geral do Documento Fiscal Eletrônico 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
01 vTotDFe E imp (BPe e BPeTA) ou 
total (BPeTM) 
 
E 0-1 13,2 Valor total do documento fiscal  
vBP + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser INFORMADO com 
a soma do total do BPe + IBS + CBS 
Para BPe: 
vTotDFe = infValorBPe/vBP + gIBSCBS/vIBS + 
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

## Página 8

Projeto 
Bilhete de Passagem Eletrônico - Reforma Tributária do Consumo 
NT 2026.004 v1.00 
 
 
Página 8 / 8 
 
7 No BPe TA permitir endereço do comprador opcional 
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
