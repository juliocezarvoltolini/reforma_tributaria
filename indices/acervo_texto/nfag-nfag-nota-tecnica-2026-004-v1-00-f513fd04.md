---
id: nfag-nfag-nota-tecnica-2026-004-v1-00-f513fd04
titulo: Nota Técnica 2026.004 RTC
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-01'
documento_fiscal: NFAg
url: https://dfe-portal.svrs.rs.gov.br/NFAG/DownloadArquivoEstatico/?sistema=NFAG&tipoArquivo=3&nomeArquivo=NFAg_Nota_Tecnica_2026_004_v1.00.pdf
arquivo_original: fontes/acervo/nfag-nfag-nota-tecnica-2026-004-v1-00-f513fd04.pdf
sha256_original: f513fd043a6a881f232029922ddd83f2e907a7214414c5126913d3910c232980
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: dda99eedd43d071eabda80e5591549a35de06fd06ef23a6baca1d030d6a2618e
---

## Página 1

Projeto Nota Fiscal de Água e 
Saneamento Eletrônica 
 
Nota Técnica 2026.004 – Reforma Tributária do Consumo 
 
Versão 1.00 de setembro de 2026

## Página 2

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 2 / 10 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Inclusão dos campos de valor líquido no Prod ................................................................ 4 
3 Alterações no Leiaute do DFe ......................................................................................... 5 
Grupo de detalhamento dos itens (prod) .............................................................................5 
Validações dos novos campos de valor líquido nos itens ............................................................... 5 
Grupo Totais .......................................................................................................................5 
Validações do total .......................................................................................................................... 5 
4 Validações dos campos do IBS e CBS ............................................................................ 5 
5 Total Geral do Documento Fiscal Eletrônico ................................................................... 7 
6 Criação dos campos de IBS e CBS no grupo de processo judicial referenciado ............. 7 
7 Criação dos tipos de faturamento Agregado e Agregador ............................................... 8 
Regras de Validação da NFAg ............................................................................................9

## Página 3

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 3 / 10 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Criação dos campos que representam os valores líquidos de impostos nos 
itens 
 Exceção nas regras de validação de alíquotas para o ambiente de 
homologação 
 Ajuste na regra do valor total do DFe 
 Criação dos campos de IBS e CBS no grupo de processo judicial 
 Criação dos tipos de faturamento Agregado e Agregador 
13/10/2026 16/11/2026

## Página 4

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 4 / 10 
 
1 Introdução 
Composição do valor do produto com IBS e CBS 
O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. 
Para fins de preenchimento da NFAg, os valores do IBS e da CBS incidentes na prestação do serviço deverão ser 
acrescidos ao valor do serviço, compondo o valor informado no campo vProd. 
 
A inclusão dos valores do IBS e da CBS no campo vProd não implica sua inclusão na base de cálculo desses 
tributos. A base de cálculo do IBS e da CBS deverá ser determinada de acordo com a legislação aplicável. 
Dessa forma, os valores do IBS e da CBS, por já estarem compreendidos no valor do serviço, não deverão ser 
adicionados novamente na composição do valor total da NFAg (vTotDFe), evitando duplicidade. 
 
Os valores de IBS e CBS permanecem destacados nos respectivos grupos tributários, porém são meramente 
informativos, uma vez que já estão compreendidos no vProd. 
 
2 Inclusão dos campos de valor líquido no Prod 
Com o objetivo de ampliar a transparência na formação do preço da prestação, foram criados os campos Valor 
Líquido Unitário e Valor Líquido do Produto. Esses campos permitem identificar o valor do serviço antes da 
incorporação dos tributos vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o 
valor líquido dos valores tributários agregados ao preço. 
 
A medida busca preservar a rastreabilidade da formação do valor informado na NFAg, especialmente diante da 
sistemática do IBS e da CBS, cujos valores passam a compor o valor do serviço para fins de representação 
documental, sem perder a identificação da parcela correspondente ao valor líquido da prestação. 
 
Dessa forma, os novos campos permitem evidenciar tanto o valor líquido unitário quanto o valor líquido total 
do item, proporcionando maior transparência ao contribuinte, ao adquirente e às Administrações Tributárias 
quanto à composição do preço e à participação dos tributos no valor final da prestação.

## Página 5

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 5 / 10 
 
3 Alterações no Leiaute do DFe 
Grupo de detalhamento dos itens (prod) 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
...        
 vProd E det\prod N 1-1 13v2 Valor total do item 
 
Observação: A partir 2027, os valores de IBS e 
CBS compõem o Valor Total do Item 
# Sequência XML - det\prod - 0-1  Os campos vItemLiq e vProdLiq estão associados a 
esta sequencia XML 
 vItemLiq E det\prod N 1-1 13v2 Informar o valor unitário do item sem tributos. 
 vProdLiq E det\prod N 1-1 13v2 Valor Líquido total do item sem tributos 
vProdLiq = vItemLiq x qFaturada 
Validações dos novos campos de valor líquido nos itens 
As validações serão aplicadas a cada item do DFe 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se informados vItemLiq e vProdLiq: 
   – vProdLiq deve ser igual vItemLiq * qFaturada 
Obrig. 1050 Rej. Rejeição: Valor Líquido do Produto difere do produto 
Valor líquido do item e quantidade faturada [nItem: 
999] 
Grupo Totais 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
 vProd E total N 1-1 13v2 Soma dos valores dos produtos ou serviços 
 vProdLiq E total N 0-1 13v2 Soma dos valores líquidos dos produtos ou serviços 
sem tributos 
Validações do total 
Regra de Validação Aplic. cStat Efeito Mensagem 
Total Líquido dos Produtos ou Serviços sem tributos 
(tag: total\vProdLiq) difere do somatório do valor líquido 
dos produtos ou serviços sem tributos dos itens.  
Obrig. 1054 Rej. Rejeição: Total Líquido dos Produtos ou Serviços 
sem tributos difere do somatório dos itens 
4 Validações dos campos do IBS e CBS 
As validações serão aplicadas a cada item da NFAg. 
Em caso de rejeição deverá constar ao final da mensagem o número do item em que foi detectada [nItem: XXX] 
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
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 6 / 10 
 
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
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 7 / 10 
 
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
destinatário for pessoa jurídica, o CNPJ-Base do 
emitente deve ser diferente do CNPJ-Base do 
destinatário do serviço 
Obrig. 1055 Rej. Rejeição: Doação com CNPJ do emitente igual do 
destinatário do serviço 
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
01 vTotDFe E total  
 
E 0-1 13,2 Valor total do documento fiscal  
vNF + total do IBS + total da CBS 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 O total geral do DFe deverá ser INFORMADO com 
a soma do valor total da NFAg + IBS + CBS 
vTotDFe = total/vNF + IBSCBSTot/gIBS/vIBS + 
IBSCBSTot/gCBS/vCBS 
Exceção: Em 2026 não somar IBS e CBS, usar a 
fórmula: 
vTotDFe = total/vNF   
O total geral do DFe deverá ser informado 
REPETINDO o valor de vNF 
Exceção: Na nota de faturamento Agregador 
(tpFat=5) deve ser a soma de 
gAgregadora\vTotDFe nos itens 
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
6 Criação dos campos de IBS  CBS no grupo de processo judicial referenciado 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
... gProcRef G det - 0-1  Grupo Processo referenciado 
 gIBSCBS G gProcRef - 0-1  Grupo de informações do IBS e CBS a serem 
considerados sem a aplicação do processo judicial 
 vBC E gIBSCBS  N 1-1 13,2 Valor da BC do IBS e CBS 
 vIBSUF E gIBSCBS N 1-1 13,2 Valor de IBS UF 
 vIBSMun E gIBSCBS N 1-1 13,2 Valor de IBS Municipal 
 vCBS E gIBSCBS N 1-1 13,2 Valor de CBS

## Página 8

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 8 / 10 
 
7 Incluir valor Mínimo no Indicador da Origem da 
Quantidade Faturada 
A tag indOrigemQtd presente no grupo prod em detalhamento dos itens da NFAg, passa a aceitar também o valor 
8 – Mínimo, ficando com as seguintes opções: 
1 - Media;  
2 - Medido;  
3 - Contratada;  
4 - Calculada ou estimado;  
5 - Residual Calculado; 
6 - Sem quantidade  
7 - Por Faixa; 
8 - Mínimo 
8 Criação dos tipos de faturamento Agregado e Agregador 
O campo tpFat no grupo ide passa a aceitar novos valores: 4 - Faturamento Agregado e 5 - Faturamento 
Agregador 
 
  
A estrutura de itens da nota passa a contar com uma choice que deverá ser informada em caso de nota com tipo 
de faturamento agregador (tpFat=5), neste caso, todos os grupos gTarif, prod, imposto, gProcRef e infAdProd não 
poderão ser informados no XML.

## Página 9

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 9 / 10 
 
 
O grupo de informações da Agência reguladora passa a ser dispensado apenas para a Nota com tipo de 
faturamento agregador (tpFat=5) 
 
 A nota de faturamento agregador (tpFat=5) deverá informar em todos os itens as chaves de acesso das 
notas de faturamento agregado (tpFat=4) de períodos anteriores e vTotDFe (da nota anterior) para cada 
item e sinalizar cClass com indicador de faturamento agregado. 
 A nota de faturamento agregador (tpFat=5) não poderá informar dados da agência reguladora, além de 
ser exigido o grupo de dados da fatura. 
 A nota de faturamento agregado (tpFat=4) deverá ter os dados completos da tributação nos itens e não 
poderá utilizar cClass com indicador de faturamento agregado. Esta nota não poderá informar dados da 
fatura e será exigido informar dados da Agência reguladora 
 Eventos de marcação do fisco deverão ser gerados automaticamente na nota de faturamento agregado 
quando uma nota agregadora for autorizada, cancelada ou substituída. 
Regras de Validação da NFAg 
# Regra de Validação Aplic. cStat. Efeito Mensagem 
Validação da Nota Agregadora (verificar nos itens) 
01 Se o Tipo de Faturamento Agregador (5) para todos os 
itens: 
 
- Verificar se foi informada chave de acesso (chNFAgAnt) 
como atributo no detalhamento dos Produtos e Serviços 
(grupo: det): 
Obrig. 1060 Rej. Rejeição: Chave de acesso anterior deve ser 
informada para item de nota de Faturamento 
Agregador 
02 Se tipo de faturamento da NFAg DIFERENTE de 
Faturamento Agregador (tag: tpFat <> 5): 
- Rejeitar se informado grupo da Nota Agregadora em algum 
item (grupo: gAgregadora) 
Obrig. 1061 Rej. Rejeição: Item com grupo da Nota Agregadora 
vedado para tipo de faturamento diferente de 
Agregador 
03 Se tipo de faturamento da NFAg = 5 (Agregadora) (tag: 
tpFat): 
O grupo da  
Nota Agregadora DEVE ser informado em todos os itens 
(grupo: gAgregadora) 
Obrig. 1062 Rej. Rejeição: Todos os itens da nota agregadora 
devem informar o grupo Agregadora 
04 Se tipo de faturamento da NFAg for agregador (tpFat=5) e 
informada chave de acesso de NFAg anterior (tag: 
chNFAgAnt) no detalhamento dos Produtos e Serviços 
(grupo: det): 
- A NFAg anterior deve ser do tipo de faturamento Agregado 
(tpFat=4)  
Obrig. 1063 Rej Rejeição: NFAg a anterior deve ser do tipo de 
faturamento Agregado

## Página 10

Projeto 
Nota Fiscal de Água e Saneamento Eletrônica 
NT 2026.004 v1.00 
 
 
Página 10 / 10 
 
05 Se tipo de faturamento da NFAg for DIFERENTE de 
agregador (tpFat=5) e informada chave de acesso de NFAg 
anterior (tag: chNFAgAnt) no detalhamento dos Produtos e 
Serviços (grupo: det): 
- A NFAg anterior NÃO PODE SER do tipo de faturamento 
Agregado (tpFat=4)  
Obrig. 1064 Rej Rejeição: NFAg anterior NÃO PODE ser do tipo 
de faturamento Agregado  
06 Se tipo de faturamento da NFAg =1 (Normal) ou 2 (Faturado 
por terceiro) ou 4 (Agregado) 
 
- Rejeitar se existir algum item no detalhamento de Produtos 
e serviços com cClass de Faturamento Conjunto 
 
Observação: Ver indicadores da tabela cClass publicados 
no portal da NFag 
Obrig. 534 Rej. Rejeição: Classificação de produto inválida para 
faturamento normal, agregado ou faturamento de 
terceiro 
[nItem: NNN] 
07 Se tipo de faturamento da NFAg DIFERENTE DE 5 
(Agregadora)  
- Rejeitar se existir algum item no detalhamento de Produtos 
e serviços com cClass de Faturamento Agregado 
 
Observação: Ver indicadores da tabela cClass publicados 
no portal da NFAg 
Obrig. 1066 Rej. Rejeição: Classificação de produto inválida para 
este tipo de faturamento [nItem: NNN] 
08 Se tipo de faturamento da NFAg =5 (Faturamento 
Agregador)  
- Todos os itens devem ser do cClass de Nota Agregadora 
 
Observação: Ver indicadores da tabela cClass publicados 
no portal da NFag 
Obrig. 1067 Rej. Rejeição: Todos os itens devem ser do cClass de 
Faturamento Agregado 
[nItem: NNN] 
Validações da Agência  
09 Se tipo de faturamento da NFAg DIFERENTE de Agregador 
(tag: tpFat): 
- O grupo de informações da agência DEVE SER informado 
(grupo: gAgencia) 
Obrig. 1068 Rej. Rejeição: Grupo Agência deve ser informado para 
este tipo de faturamento  
10 Se tipo de faturamento da NFAg = 5 (Agregadora) (tag: 
tpFat): 
- O grupo de informações da agência NÃO deve ser 
informado (grupo: gAgencia) 
Obrig. 1069 Rej. Rejeição: Grupo agência não deve ser informada 
para NFAg Agregadora 
Validações da Fatura da NFAg 
11 Se tipo de faturamento da NFAg =1 (Normal) ou 3 
(Faturamento Conjunto) ou 5 (Faturamento Agregador) (tag: 
tpFat): 
 
- O grupo de informações da fatura deve ser informado 
(grupo: gFat) 
Obrig. 270 Rej. Rejeição: Fatura deve ser informada para tipo de 
faturamento normal, conjunto e agregador 
12 Se tipo de faturamento da NFAg = 2 (Faturado por terceiro) 
ou 4 (Agregada) (tag: tpFat): 
 
- O grupo de informações da fatura NÃO deve ser informado 
(grupo: gFat) 
Obrig. 273 Rej. Rejeição: Fatura não deve ser informada para 
NFAg faturada por terceiro ou agregada 
Validações dos Itens da NFAg (Tributos) 
Aplicável somente para Tipo de Faturamento Normal, Conjunto, faturada por Terceiro e Faturamento Agregado  
Observação: O Tipo de Faturamento Agregador (tpFat=5) não possui tributação nos itens, todos os itens são referência a chaves de acesso de notas que 
estão sendo agregadas, portanto não há detalhamento de valores ou tributos nesta nota. 
Validações dos Totais da NFAg 
Observação: No caso do tipo de faturamento Agregador (tpFat=5) todos os campos de totais devem ser informados com ZERO porque não há soma nos 
itens.  
O campo vNF e vTotDFe devem ser IGUAIS, contendo a soma da tag Valor Total do DFe Anterior dos itens (det\gAgregadora\vTotDFe) 
13 Valor total da NF (vNF) difere do somatório de: 
 
(+) vProd  
(-) vRetPIS 
(-) vRetCofins 
(-) vRetCSLL 
(-) vIRRF 
 
Exceção: Na nota de faturamento Agregador (tpFat=5) deve 
ser a soma de gAgregadora\vTotDFe nos itens 
Obrig. 460 Rej. Rejeição: Total da NFAg difere do somatório dos 
valores que compõem o valor total da NFAg
