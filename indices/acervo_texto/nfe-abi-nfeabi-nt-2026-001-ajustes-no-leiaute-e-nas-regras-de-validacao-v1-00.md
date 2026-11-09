---
id: nfe-abi-nfeabi-nt-2026-001-ajustes-no-leiaute-e-nas-regras-de-validacao-v1-00
titulo: Nota Técnica 2026.001 v1.00 - Publicada em 30/10/2026
tipo: nota.tecnica
versao: '1.00'
data: '2026-10-30'
documento_fiscal: NF-e ABI
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=vDwdfHkjfNc=
arquivo_original: fontes/acervo/nfe-abi-nfeabi-nt-2026-001-ajustes-no-leiaute-e-nas-regras-de-validacao-v1-00.pdf
sha256_original: 98cae11e3efd288a5ead4e6b455eca3ed75998ec27450c0507d9873228355d4c
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 92d92de604f36a24756e0d4d6db6397afb7f70309184066977bd4e78f33ff663
---

## Página 1

Sistema Nota Fiscal Eletrônica 
 
 Nota Técnica 2026.001 
Ajustes no Leiaute e nas Regras de Validação da NF-e ABI 
Versão 1.00 – Outubro de 2026

## Página 2

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
Página 2 / 43 
 
 
Sumário 
Controle de Versões ............................................................................................................................................ 3 
Histórico de Alterações / Cronograma ................................................................................................................. 3 
1. Descrição das alterações ................................................................................................................................. 4 
2. Leiaute da NF-e ABI ........................................................................................................................................ 5 
Grupo B. Identificação da NF-e ABI ................................................................................................................. 5 
Grupo BA. Informação de Documentos Fiscais referenciados ......................................................................... 6 
Grupo BB. Grupo de notas de antecipação de pagamento ............................................................................. 6 
Grupo C. Identificação do Emitente da NFe ABI .............................................................................................. 6 
Grupo E. Identificação dos Transmitentes da Operação da NF-e ABI ................................................................ 7 
Grupo F. Identificação dos Adquirentes da Operação da NF-e ABI .................................................................... 9 
Grupo G. Identificação do Imóvel ................................................................................................................... 10 
Grupo H. Informações da Operação .............................................................................................................. 11 
Grupo U. Informações da Tributação ............................................................................................................. 13 
Grupo UA. Informações da Tributação no Regime de Transição ................................................................... 14 
Grupo Y. Detalhes de Pagamento .................................................................................................................. 15 
Grupo W. Total da NF-e ABI .......................................................................................................................... 16 
3. Eventos ......................................................................................................................................................... 17 
Lista de Eventos ............................................................................................................................................ 17 
Evento: Apropriação de créditos individuais ................................................................................................... 18 
Evento: Desfazimento da Alienação .............................................................................................................. 18 
4. Regras de Negócio ........................................................................................................................................ 20 
5. QR Code da NF-e ABI ................................................................................................................................... 32 
5.1 Grupo de informações suplementares e preenchimento da URL ............................................................. 32 
5.2 QR Code para NF-e ABI com tipo de emissão normal (tpEmis=1) ........................................................... 33 
5.3 QR Code para NF-e ABI com tipo de emissão em contingência off-line (tpEmis=9) ................................ 33 
5.3.1 Geração da assinatura (parâmetro sign) ........................................................................................... 33 
5.3.2 Exemplo de formação ....................................................................................................................... 34 
5.3.3 Validação e consulta do QR Code de contingência ........................................................................... 34 
5.4 Regras para geração e representação .................................................................................................... 34 
5.6 Regras de validação do QR Code ........................................................................................................... 35 
6. DANFE-ABI ................................................................................................................................................... 37 
6.1 Formato e apresentação .......................................................................................................................... 37 
6.2 Mensagens obrigatórias .......................................................................................................................... 37 
6.3 Chave de acesso e código de barras ....................................................................................................... 37 
6.4 QR Code no DANFE-ABI ......................................................................................................................... 38 
6.5 DANFE-ABI com mais de uma folha ........................................................................................................ 38 
6.6 Correspondência com o XML .................................................................................................................. 39 
6.7 Especificação dos campos ...................................................................................................................... 39 
6.8 NF-e ABI do Tipo de Documento Fiscal “2=Transição” ............................................................................ 41 
6.9 Modelo de referência ............................................................................................................................... 42 
6.10 Modelo de referência – formato paisagem ............................................................................................. 43

## Página 3

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
Página 3 / 43 
 
 
Controle de Versões 
 
Versão Publicação Descrição 
1.00 Outubro/2026 Publicação da primeira versão 
 
 
 
 
 
 
Histórico de Alterações / Cronograma 
 
Versão Histórico de atualizações Implantação Homologação 
Implantação Produção 
1.00 Publicação da primeira versão                       30/11/2026* 14/12/2026 
* Versão em homologação inicial

## Página 4

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
Página 4 / 43 
 
 
1. Descrição das alterações 
 
Esta Nota Técnica divulga ajustes no Leiaute e nas Regras de Validação da NF-e ABI a definição do leiaute 
da NF-e de Alienação de Bens Imóveis. 
 
Além dos tipos de NF-e ABI já existentes (0. Simplificado e 1.Completo), foi acrescido o Tipo de Documento 
Fiscal “2. Transição”, exclusiva para quando forem reunidas TODAS as condições abaixo: 
a) O ato de alienação deve ser anterior à 2027; e 
b) O contribuinte deve ser optante de algum dos regimes previstos nos artigos 485 ou 486 da LC 
214/2025; e 
c) A situação deve estar enquadrada na hipótese prevista no artigos 408, § 2° da LC 214/2025. 
 
A NF-e ABI de transição não é emitida a cada operação de alienação de bem imóvel, mas de forma unificada 
para cada receita mensal ou receita bruta enquadrada em algum dos regimes opcionais do art. 485 ou 486 
da LC 214/2025. 
 
Também foram incluídos os campos e grupos necessários para documentar as antecipações de 
pagamento, bem como as operações de fornecimento com pagamento realizado anteriormente (art. 10, § 
4° da LC 214/2025). 
 
A descrição da modalidade de operação (tag: ide/modOper) “2. Arrematação, Adjudicação ou Remição” foi 
alterada para “2. Arrematação Judicial, Adjudicação ou Remição”, uma vez que as arrematações em leilão 
extrajudicial estão enquadradas na modalidade “1. Alienação em geral” com IBS e CBS devidos pelo 
vendedor ou transmitente. 
 
Além disso, foram eliminados da sistemática da NF-e ABI os indicadores abaixo (que seriam futuramente 
inseridos na tabela do CST/cClassTrib): 
 Indicador que obriga ou veda a informação do Enquadramento do imóvel (ind_Enquadr_NFeABI); 
 Indicador que obriga ou veda a informação do Redutor de Ajuste (ind_RedAjuste_NFeABI); 
 Indicador que obriga ou veda a informação do Redutor Social (ind_RedSocial_NFeABI). 
 
Também foi adicionado o Evento de Desfazimento da Alienação (tag: evDesfazimAlienac) com o objetivo 
de registrar, mediante evento, o desfazimento de uma operação de alienação de bem imóvel, mediante 
distrato, resolução, decisão judicial, sentença arbitral, reversão da consolidação da propriedade, etc. 
 
Foram definidos os códigos de identificação dos eventos da NF-e ABI (tag: tpEvento), até então não 
especificados para os eventos de Pagamento de Parcela, Apropriação de créditos individuais e 
Desfazimento da Alienação, conforme a tabela de códigos incluída no capítulo 3 (Lista de Eventos). 
 
Os campos Valor Total da Operação (tag: total/vTotalOperacao – id W03) e Valor da Operação Individual 
(tag: total/vOperacIndiv – id W04) passam a ter ocorrência 0-1, não devendo ser informados na NF-e ABI 
de transição (tpNF=2) e na NF-e ABI de pagamento antecipado (tpPagAnt=1), que não possuem o grupo 
de Informações da Operação (tag: infOper) nem o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv). 
 
Foi corrigido, no leiaute, o grupo pai do grupo de Informação de Documentos Fiscais referenciados (tag: 
NFref – id BA01), que passa de “B01” para “A01”, conforme o schema XML (NFeABI_v1.00.xsd), em que o 
grupo NFref é filho do grupo infNFeABI, posicionado entre os grupos de Identificação da NF-e ABI (tag: ide) 
e de Identificação do Emitente da NFe ABI (tag: emit). 
 
Foram incluídas regras de validação para rejeitar a NF-e ABI de emitente bloqueado pelo Fisco. 
 
Foram reformuladas as especificações do QR Code (capítulo 5), com nova estrutura de parâmetros e 
disciplina da emissão em contingência off-line, e do DANFE-ABI (capítulo 6), com especificação dos 
campos, regras para mais de uma folha e modelos nos formatos retrato e paisagem. 
 
Por fim, algumas explicações de campos, grupos e regras de validação já existentes foram ajustadas para 
dar maior clareza sobre o funcionamento do documento fiscal.

## Página 5

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 5 / 43 
1 
 
2. Leiaute da NF-e ABI 
A seguir são apresentados os ajustes dos campos do leiaute da NF-e ABI. 
 
Grupo B. Identificação da NF-e ABI 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
B01 ide Informações de identificação da NF-e ABI G A01  1-1   
... ... ... ... ... ... ... ... ... 
B08 tpNF Tipo de Documento Fiscal E B01 N 1-1 1 0=Simplificado 
1=Completo 
2=Transição 
ORIENTAÇÃO 1: O Tipo “0=Simplificado” só poderá ser 
utilizado nas operações que se referirem à totalidade do bem 
imóvel,  quando se enquadrar em uma das condições abaixo: 
(1) Operações abrangidas pelas modalidades “01. Alienação 
em geral”, “03. Cessão ou Transmissão de direitos” ou 
“04. Permuta” com somente um vendedor ou 
transmitente; ou 
(2) Operações abrangidas pela modalidade “02. 
Arrematação Judicial, Adjudicação ou Remição” com 
somente um adquirente. 
ORIENTAÇÃO 2: O Tipo “1=Completo” só poderá ser utilizado 
nos casos abaixo: 
(1) Operações que se referirem à parte do bem imóvel, não 
abrangendo a sua totalidade (Ex.: Venda da metade de 
uma casa); ou 
(2) Operações abrangidas pelas modalidades “01. Alienação 
em geral”, “03. Cessão ou Transmissão de direitos” ou 
“04. Permuta” com mais de um vendedor ou 
transmitente; ou 
(3) Operações abrangidas pela modalidade “02. 
Arrematação Judicial, Adjudicação ou Remição” com 
mais de um adquirente. 
ORIENTAÇÃO 3: O Tipo “2=Transição” só poderá se utilizado 
quando reunidas TODAS as condições abaixo: 
a) O ato de alienação deve ser anterior à 2027; e 
b) O contribuinte deve ser optante de algum dos regimes 
previstos nos arts. 485 ou 486 da LC 214/2025; e 
c) A situação deve estar enquadrada na hipótese prevista 
no art. 408, § 2° da LC 214/2025.

## Página 6

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 6 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
B09 tpImp Formato de Impressão do DANFE E B01 N 1-1 1 0=Sem geração de DANFE; 
1=DANFE-ABI normal, Retrato; 
2=DANFE-ABI normal, Paisagem. 
OBSERVAÇÃO: Para o Tipo de Documento Fiscal 
“2=Transição” (tag: tpNF=2), informar obrigatoriamente 
“0=Sem geração de DANFE”. 
... ... ... ... ... ... ... ... ... 
B10 gModNat Grupo Modalidade e Natureza da operação G B01 - 0-1  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
... ... ... ... ... ... ... ... ... 
B18a tpPagAnt Tipo de pagamento E B01 N 0-1 1 1=Pagamento antecipado; 
2=Fornecimento com pagamento realizado anteriormente. 
 
Grupo BA. Informação de Documentos Fiscais referenciados 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
BA01 NFref Informação de Documentos Fiscais referenciados G A01  0-500  Grupo com informações de Documentos Fiscais 
referenciados. 
 
Grupo BB. Grupo de notas de antecipação de pagamento 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
BB01 gPagAntecipado Grupo de notas de antecipação de pagamento G A01 - 0-1  Informado para abater as parcelas de antecipação de 
pagamento, conforme Art. 10. § 4º da LC 214/2025. 
OBSERVAÇÃO: Este grupo será aberto somente quando o 
Tipo de pagamento (tag: ide/tpPagAnt) for “2=Fornecimento 
com pagamento realizado anteriormente”. 
BB02 chNFePagAnt Chave de acesso da NF-e ABI de antecipação de pagamento E BB01 C 1-99 44 Referência uma NF-e ABI (modelo 77) emitida anteriormente, 
referente a pagamento antecipado. 
 
Grupo C. Identificação do Emitente da NFe ABI 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
C01 emit Identificação do emitente da NF-e ABI G A01  1-1   
... ... ... ... ... ... ... ... ...

## Página 7

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 7 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
C18 tpEmit Tipo do Emitente E C01 N 1-1 2 01=Vendedor, Transmitente ou Cedente  
02=Comprador, Adquirente ou Cessionário  
03=Leiloeiro (em nome do arrematante) 
04=Tabelionato de Notas (em nome do vendedor ou 
transmitente) 
05=Junta Comercial (em nome do transmitente) 
06=Banco ou instituição financeira (em nome do vendedor ou 
transmitente) 
07=Organização gestora de fundo patrimonial 
08=Credor fiduciário (na consolidação da propriedade) 
09=Grupo de consórcio (na consolidação da propriedade) 
10=Sucessora em virtude de incorporação, cisão ou fusão 
11=Instituição administradora em nome do Fundo de 
Investimento (FII ou Fiagro) 
99=Outros Emitentes 
OBSERVAÇÃO 1: Proibido utilizar a opção “01=Vendedor, 
Transmitente ou Cedente” quando a modalidade for “02= 
Arrematação Judicial, Adjudicação ou Remição”. 
OBSERVAÇÃO 2: Proibidas as opções “02=Comprador, 
Adquirente ou Cessionário” e “03=Leiloeiro (em nome do 
arrematante)” quando as modalidades forem diferentes de 
“02= Arrematação Judicial, Adjudicação ou Remição”. 
OBSERVAÇÃO 3: Proibida utilizar a opção “99=Outros 
Emitentes” quando houver destaque de tributo na nota. 
 
Grupo E. Identificação dos Transmitentes da Operação da NF-e ABI 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
E01 transmit Vendedor, Transmitente ou Cedente do imóvel G A01  0-99  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
... ... ... ... ... ... ... ... ...

## Página 8

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 8 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
E02 indDeclarante Indicador de declarante E E01 N 0-1  1 Q. O vendedor, transmitente ou cedente aqui identificado é 
o declarante desta Nota Fiscal? 
0=Não / 1=Sim 
OBSERVAÇÃO 1: Não abrir para a modalidade 
“02.Arrematação Judicial, Adjudicação ou Remição” (tag: 
modOper<>2) 
OBSERVAÇÃO 2: O transmitente com Indicador de declarante 
igual à 1 (tag: indDeclarante=1) deverá corresponder ao 
Número Sequencial do Transmitente igual à 1 (tag: 
nTransmit=1). 
OBSERVAÇÃO 3: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao Tipo de 
Documento Fiscal  do grupo “Identificação da NF- e ABI” (tag: 
ide/tpNF). 
1. Para o Tipo de Documento Fiscal “0=Simplificado” (tag: 
tpNF=0): 
     → Não abrir o campo indDeclarante 
2. Para o Tipo de Documento Fiscal “1=Completo” (tag: 
tpNF=1): 
2.1. Se a modalidade for diferente de “02.Arrematação 
Judicial, Adjudicação ou Remição” (tag: modOper<>2): 
     → Abrir o campo indDeclarante 
2.2. Se a modalidade for igual à “02.Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper=2): 
     → Não abrir o campo indDeclarante 
... ... ... ... ... ... ... ... ... 
E18 pTransIndiv Proporção Transmitida Individual E E01 N 0-1 3v4 ORIENTAÇÃO: Preencher a proporção do imóvel (em formato 
percentual) que o vendedor, transmitente ou cedente está 
transferindo individualmente. 
OBSERVAÇÃO: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao Tipo de 
Documento Fiscal  do grupo “Identificação da NF- e ABI” (tag: 
ide/tpNF). 
1. Para o Tipo de Documento Fiscal “0=Simplificado” (tag: 
tpNF=0): 
     → Não abrir o campo pTransIndiv 
2. Para o Tipo de Documento Fiscal “1=Completo” (tag: 
tpNF=1): 
     → Abrir o campo pTransIndiv 
E19 indContrib Indicador de Contribuinte do Regime regular do IBS/CBS E E01 N 0-1 1 0=Não Contribuinte do IBS/CBS 
1=Contribuinte do Regime Regular do IBS/CBS 
2=Optante do Simples Nacional 
OBS: Não abrir para a modalidade "02.Arrematação Judicial, 
Adjudicação ou Remição" (tag: modOper=2)

## Página 9

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 9 / 43 
1 
 
Grupo F. Identificação dos Adquirentes da Operação da NF-e ABI 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
F01 adquirente Comprador, Adquirente ou Cessionário G A01  0-99  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
... ... ... ... ... ... ... ... ... 
F02 indDeclarante Indicador de Declarante E F01 N 0-1 1 Q. O comprador, adquirente ou cessionário aqui identificado 
é o declarante desta Nota Fiscal? 
0=Não / 1=Sim 
OBSERVAÇÃO 1: Abrir somente para a modalidade 
“02.Arrematação Judicial, Adjudicação ou Remição” (tag: 
modOper=2). 
OBSERVAÇÃO 2: O adquirente com Indicador de declarante 
igual à 1 (tag: indDeclarante=1) deverá corresponder ao 
Número Sequencial do Adquirente igual à 1 (tag: nAdquir=1). 
OBSERVAÇÃO 3: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao Tipo de 
Documento Fiscal  do grupo “Identificação da NF- e ABI” (tag: 
ide/tpNF). 
1. Para o Tipo de Documento Fiscal “0=Simplificado” (tag: 
tpNF=0): 
     → Não abrir o campo indDeclarante 
2. Para o Tipo de Documento Fiscal “1=Completo” (tag: 
tpNF=1): 
2.1. Se a modalidade for igual à “02.Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper=2): 
     → Abrir o campo indDeclarante 
2.2. Se a modalidade for diferente de “02.Arrematação 
Judicial, Adjudicação ou Remição” (tag: modOper<>2): 
     → Não abrir o campo indDeclarante 
... ... ... ... ... ... ... ... ... 
F18 pAquisicao Percentual de Aquisição E F01 N 0-1 3v4 OBSERVAÇÃO: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao Tipo de 
Documento Fiscal  (tag: ide/tpNF). 
1. Para o Tipo de Documento Fiscal “0=Simplificado” (tag: 
tpNF=0): 
     → Não abrir o campo pAquisicao 
2. Para o Tipo de Documento Fiscal “1=Completo” (tag: 
tpNF=1): 
2.1. Se a modalidade for igual à “02.Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper=2): 
     → Abrir o campo pAquisicao 
2.2. Se a modalidade for diferente de “02.Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper<>2): 
          → Não abrir o campo pAquisicao

## Página 10

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 10 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
F19 indContrib Indicador de Contribuinte do Regime regular do IBS/CBS E F01 N 0-1 1 0=Não Contribuinte do IBS/CBS 
1=Contribuinte do Regime Regular do IBS/CBS 
2=Optante do Simples Nacional 
OBS: Não abrir para a modalidade "02.Arrematação Judicial, 
Adjudicação ou Remição" (tag: modOper=2) 
 
Grupo G. Identificação do Imóvel 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
G01 imovel Identificação do imóvel transmitido G A01  0-1  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
ORIENTAÇÃO: Na permuta com torna envolvendo 
exclusivamente bens imóveis (indTorna=1), informar os 
dados do imóvel de maior valor. 
... ... ... ... ... ... ... ... ... 
G03 cadastro Informações Cadastrais do imóvel G G01  1-1   
... ... ... ... ... ... ... ... ... 
G06 nIPTU Número do IPTU E G03 C 0-1 2 - 60 OBSERVAÇÃO: Campo obrigatório somente para Indicador se 
o imóvel possui IPTU (tag: indIPTU) igual a “1=Possui IPTU” 
(tag: indIPTU=1). 
... ... ... ... ... ... ... ... ... 
G07 indINCRA Indicador se o imóvel possui INCRA E G03 N 0-1 1 0=Não possui INCRA 
1=Possui INCRA 
G08 nINCRA Número do INCRA E G03 C 0-1 2 - 60 OBSERVAÇÃO: Campo obrigatório somente para Indicador se 
o imóvel possui INCRA (tag: indIPTU) igual a “1=Possui INCRA” 
(tag: indINCRA=1). 
G08a indRIP Indicador se o imóvel possui RIP E G03 N 0-1 1 0=Não possui RIP 
1=Possui RIP 
ESCLARECIMENTO: O RIP (Registro Imobiliário Patrimonial) é 
o número utilizado para identificar imóveis administrados 
pela Secretaria do Patrimônio da União - SPU. 
G08b nRIP Número do RIP E G03 C 0-1 2 - 60 OBSERVAÇÃO: Campo obrigatório somente para Indicador se 
o imóvel possui RIP (tag: indRIP) igual a “1=Possui RIP” (tag: 
indRIP=1). 
... ... ... ... ... ... ... ... ... 
G11 enquadramento Enquadramento do imóvel E G01 N 1-1 2 Verificar Tabela de códigos da NFe ABI, publicada no Portal 
da NFe ABI. 
OBSERVAÇÃO: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao indicador 
“ind_Enquadr_NFeABI” da tabela de cClassTrib do IBS e da 
CBS. 
Se cClassTrib do IBS/CBS (tag: IBSCBS/cClassTrib) possui 
indicador que não permite a informação do Enquadramento 
do imóvel (ind_Enquadr_NFeABI=0):

## Página 11

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 11 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
        --> Não abrir o campo enquadramento 
Se cClassTrib do IBS/CBS (tag: IBSCBS/cClassTrib) possui 
indicador que obriga a informação do Enquadramento do 
imóvel (ind_Enquadr NFeABI=1): 
 --> Abrir o campo enquadramento 
 
Grupo H. Informações da Operação 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
H01 infOper Informações da Operação G A01  0-1  OBSERVAÇÃO 1: Este grupo NÃO será aberto se o Tipo de 
pagamento (tag: tpPagAnt) for “1=Pagamento antecipado”. 
OBSERVAÇÃO 2: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
... ... ... ... ... ... ... ... ... 
H08 gIncorpLote Grupo de informações relativas ao empreendimento 
imobiliário 
G H01  0-1  Este grupo será aberto somente para a modalidade “01. 
Alienação em Geral” 
H09 indIncorpLote Indicador de alienação decorrente de incorporação, 
loteamento ou desmembramento 
E H08 N 1-1 1 Q. Trata-se de alienação decorrente de incorporação, 
loteamento ou desmembramento (art. 262 da LC 214/2025)? 
0=Não 
1=Alienação decorrente de incorporação 
2=Alienação decorrente de loteamento ou desmembramento 
Se o Indicador de alienação decorrente de incorporação, 
loteamento ou desmembramento for igual à 1 ou 2 (tag: 
indIncorpLote = 1 ou 2): 
  → a NF-e ABI deverá ser emitida sem destaque de IBS e CBS; 
Se o Indicador de alienação decorrente de incorporação, 
loteamento ou desmembramento for igual à 0 (tag: 
indIncorpLote = 0): 
  → a NF-e ABI deverá ser emitida com destaque de IBS e CBS. 
H10 CNPJempImob CNPJ do Empreendimento Imobiliário E H08 C 0-1 14 Informar o CNPJ específico do empreendimento imobiliário 
(incorporação ou parcelamento do solo) 
Abrir somente se o Indicador de alienação decorrente de 
incorporação, loteamento ou desmembramento for igual à 1 
ou 2 (tag: indIncorpLote = 1 ou 2). 
H10a cCIBObra Cadastro do CIB da obra CE H08 C 0-1 2-60 OBSERVAÇÃO: Este campo será aberto somente se o 
Indicador de alienação decorrente de incorporação, 
loteamento ou desmembramento for igual à 1 ou 2 (tag: 
indIncorpLote = 1 ou 2). 
H10b CNO Cadastro Nacional de Obras CE H08 N 0-1 2-60 OBSERVAÇÃO: Este campo será aberto somente se o 
Indicador de alienação decorrente de incorporação, 
loteamento ou desmembramento for igual à 1 ou 2 (tag: 
indIncorpLote = 1 ou 2).

## Página 12

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 12 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
H11 gRedAjusteImovel Redutor de Ajuste do Imóvel G H01  0-1  ORIENTAÇÃO: Caso o vendedor ou transmitente tenha 
adquirido o imóvel de contribuinte sujeito ao regime regular 
do IBS e da CBS mediante instrumento de aquisição posterior 
à 31/12/2026, o emitente poderá preencher diretamente o 
campo Valor do Redutor de Ajuste Imovel (tag: 
vRedAjusteImovel) sem a inserção dos campos abaixo: 
  → Valor Inicial do Redutor de Ajuste atualizado (tag: 
vInicial); 
  → Valor do ITBI atualizado (tag: vITBI); 
  → Valor do Laudêmio atualizado (tag: vLaudemio); 
  → Valor das contrapartidas atualizadas (tag: vContrap). 
OBSERVAÇÃO: O Redutor de Ajuste do Imóvel NÃO será 
preenchido: 
(1) Se o Indicador de alienação decorrente de 
incorporação, loteamento ou desmembramento for igual 
à 1 ou 2 (tag: indIncorpLote = 1 ou 2); ou 
(2) Se o CST do IBS/CBS (tag: IBSCBS/CST) possui indicador 
que não permite a informação do IBS/CBS (tag: 
ind_gIBSCBS=0); ou 
(3) Se a modalidade da operação for igual a “03. Cessão ou 
transmissão de direitos” (tag: modOper = 3); ou 
(4) Se o Indicador de Torna for igual à "1=Sim" (tag: 
indTorna=1). 
... ... ... ... ... ... ... ... ... 
H16 indRedSocial Indicador de Redutor Social E H01 N  0-1 1  Q. Deseja utilizar o redutor social previsto no art. 259 da LC 
214/2025 para reduzir a base de cálculo do IBS e da CBS? 
0=Não 
1=Sim 
OBSERVAÇÃO: A obrigatoriedade ou vedação do 
preenchimento deste campo está condicionada ao indicador 
“ind_gIBSCBS” da tabela de cClassTrib do IBS e da CBS. 
1. Nas modalidades diferentes de “03. Cessão ou transmissão 
de direitos” (modOper <> 3) e Indicador de Torna (tag: 
indTorna) diferente de 1 (indTorna<>1): 
1.1. Se o CST do IBS/CBS (tag: IBSCBS/CST) possui indicador 
que não permite a informação do IBS/CBS 
(ind_gIBSCBS=0): 
     → Não abrir o Indicador de Redutor Social 
1.2. Se o CST do IBS/CBS (tag: IBSCBS/CST) possui indicador 
que exige a informação do IBS/CBS (ind_gIBSCBS=1) e o 
Enquadramento do Imóvel (tag: imóvel/enquadramento) 
for “01=Imóvel Residencial Novo”: 
     → Abrir o Indicador de Redutor Social

## Página 13

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 13 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
        1.3. Se o CST do IBS/CBS (tag: IBSCBS/CST) possui indicador 
que exige a informação do IBS/CBS (ind_gIBSCBS=1) e o 
Enquadramento do Imóvel (tag: imovel/enquadramento) 
for “03=Lote Residencial”: 
     → Abrir o Indicador de Redutor Social 
2. Na modalidade igual a “03. Cessão ou transmissão de 
direitos” (tag: modOper = 3): 
     → Não abrir o Indicador de Redutor Social 
3. Nas permuta com Indicador de Torna igual à "1=Sim" (tag: 
indTorna=1): 
     → Não abrir o Indicador de Redutor Social 
ORIENTAÇÃO: O Redutor Social somente poderá ser utilizado 
uma única vez para cada bem imóvel (art. 259, parág. 2°, da 
LC 214/2025). 
 
Grupo U. Informações da Tributação 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
U01 gInfTrib Informações da Tributação G A01  0-1  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
... ... ... ... ... ... ... ... ... 
U09a gInfPagAntecip Grupo de informações do pagamento antecipado G U09  0-1 - OBSERVAÇÃO: Este grupo será aberto somente quando o 
Tipo de pagamento (tag: ide/tpPagAnt) for “1=Pagamento 
antecipado”. 
U09b vPagAntecip Valor do pagamento antecipado E U09a N 1-1 13v2  
U09c dtPagAntecip Data do pagamento antecipado E U09a D 1-1   
U09d indCNPJempImob Indicador de CNPJ do Empreendimento Imobiliário E U09a N 1-1 1 Q. Trata-se de alienação decorrente de incorporação ou 
loteamento vinculado à empreendimento com CNPJ 
específico? 
0=Não  
1=Sim 
U09e CNPJempImob CNPJ do Empreendimento Imobiliário E U09a C 0-1 14 Informar o CNPJ específico do empreendimento imobiliário 
(incorporação ou loteamento) 
OBSERVAÇÃO: Este campo será aberto somente quando o 
Indicador de CNPJ do Empreendimento Imobiliário  (tag: 
indCNPJempImob) for igual à “1=Sim”. 
U10 vOperacIndiv Valor da Operação individual do Declarante E U09 N 0-1 13v2 Verificar Tabela de códigos da NFe ABI, publicada no Portal da 
NFe ABI. 
OBSERVAÇÃO: Este campo não será aberto quando o Tipo de 
pagamento (tag: tpPagAnt) for “1=Pagamento antecipado”.

## Página 14

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 14 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
U11 vTornaIndiv Valor da Torna Individual do Declarante E U09 N 0-1 13v2 Verificar Tabela de códigos da NFe ABI, publicada no Portal da 
NFe ABI. 
OBSERVAÇÃO 1: Este campo será aberto somente quando o 
Indicador de Torna na permuta com torna envolvendo 
exclusivamente bens imóveis (tag: indTorna) for igual à 
“1=Sim”. 
OBSERVAÇÃO 2: Este campo NÃO será aberto quando o Tipo 
de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
U12 vRedAjusteIndiv Valor do Redutor de Ajuste Individual do Declarante E U09 N 0-1 13v2 Verificar Tabela de códigos da NFe ABI, publicada no Portal da 
NFe ABI. 
OBSERVAÇÃO 1: Este campo NÃO será aberto quando:  
 a modalidade for “03.Cessão ou Transmissão de 
direitos” (tag: modOper=3); ou 
 o Indicador de Torna na permuta com torna envolvendo 
exclusivamente bens imóveis (tag: indTorna) for igual à 
“1=Sim”. 
OBSERVAÇÃO 2: Este campo NÃO será aberto quando o Tipo 
de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
U13 vRedSocialIndiv Valor do Redutor Social Individual do Declarante E U09 N 0-1 13v2 Verificar Tabela de códigos da NFe ABI, publicada no Portal da 
NFe ABI. 
OBSERVAÇÃO 1: Este campo NÃO será aberto quando:  
 a modalidade for “03.Cessão ou Transmissão de 
direitos” (tag: modOper=3); ou 
 o Indicador de Torna na permuta com torna envolvendo 
exclusivamente bens imóveis (tag: indTorna) for igual à 
“1=Sim”. 
OBSERVAÇÃO 2: Este campo NÃO será aberto quando o Tipo 
de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
 
Grupo UA. Informações da Tributação no Regime de Transição 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
UA01 gInfTribTransic Informações da Tributação no Regime de Transição G A01  0-1  OBSERVAÇÃO: Este grupo será aberto somente se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
UA02 CNPJ CNPJ do contribuinte CE UA01 C 1-1 14 Informar o CNPJ do contribuinte 
UA03 CPF CPF do contribuinte CE UA01 C 1-1 11  
UA04 xNome Razão Social ou Nome do contribuinte E UA01 C 1-1 2 - 60  
UA05 IBSCBS Informações do Imposto de Bens e Serviços - IBS e da 
Contribuição de Bens e Serviços - CBS G UA01   1-1     
UA06 CST Código de Situação Tributária do IBS/CBS E UA05 N 1-1 3 Utilizar tabela CST do IBS/CBS 
UA07 cClassTrib Código de Classificação Tributária do IBS/ CBS E UA05 N 1-1 6 Utilizar tabela cClassTrib

## Página 15

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 15 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
UA08 gExigSusp Grupo de Informações para a Suspensão da Exigibilidade do 
IBS e da CBS G UA05   0-1   
UA09 tpSusp Tipo de Suspensão de Exigibilidade E UA08 N 1-1 2 
ORIENTAÇÃO: Preencher com uma das seguintes opções: 
01=Exigibilidade do IBS e da CBS suspensas por decisão 
judicial 
02= Exigibilidade do IBS e da CBS suspensas por decisão 
administrativa 
UA10 nProcesso Número do processo judicial ou administrativo de suspensão 
da exigibilidade. E UA08 C 1-1 30 
ORIENTAÇÃO: Preencher com o número completo do 
processo judicial ou administrativo de suspensão da 
exigibilidade. 
UA11 gIBSCBSTransic Grupo de Informações do IBS e da CBS do Regime de 
Transição CG UA05   1-1   
UA12 CNPJIncImob CNPJ do Empreendimento imobiliário optante pelo RET E UA11 C 1-1 14  
UA13 dtRecUni Data do Recolhimento unificado do IRPJ e da CSLL E UA11 D 0-1  
ORIENTAÇÃO: Inserir a data do recolhimento unificado do 
Imposto sobre a Renda das Pessoas Jurídicas – IRPJ e da 
Contribuição Social sobre o Lucro Líquido – CSLL (se houver). 
UA14 vRecRecebRET Receitas recebidas na venda das unidades imobiliárias E UA11 N 1-1 13v2 
ORIENTAÇÃO: Valor das receitas recebidas na venda das 
unidades imobiliárias que compõem o empreendimento 
imobiliário. 
UA15 vRecFinRET Receitas financeiras e variações monetárias vinculadas às 
vendas E UA11 N 1-1 13v2 
ORIENTAÇÃO: Valor das receitas recebidas na venda das 
unidades imobiliárias submetidas ao Regime Especial de 
Tributação – RET. 
UA15a vRecTotal Receita total de venda das unidades imobiliárias E UA11 N 1-1 13v2 vRecTotal = vRecRecebRET + vRecFinRET 
UA16 vBC Valor da Base de Cálculo do IBS e da CBS E UA11 N 1-1 13v2  
UA17 gIBSUF Grupo de informações do IBS da UF G UA11   1-1   
UA18 pIBSUF Alíquota do IBS de competência das UF E UA17 N 1-1 3v4  
UA19 vIBSUF Valor do IBS de competência das UF E UA17 N 1-1 13v2 vIBSUF = pIBSUF * vBC 
UA20 gIBSMun Grupo de informações do IBS no Município G UA11   1-1   
UA21 pIBSMun Alíquota do IBS Municipal E UA20 N 1-1 3v4  
UA22 vIBSMun Valor do IBS de competência dos Municípios E UA20 N 1-1 13v2 vIBSMun = pIBSMun * vBC 
UA23 gCBS Grupo de Tributação da CBS G UA11  1-1   
UA24 pCBS Alíquota da CBS E UA23 N 1-1 3v4  
UA25 vCBS Valor da CBS E UA23 N 1-1 13v2 vCBS = pCBS * vBC 
 
Grupo Y. Detalhes de Pagamento 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
Y01 pag Grupo de pagamento inicialmente previsto G A01  0-1  OBSERVAÇÃO: Este grupo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
ORIENTAÇÃO: Este grupo NÃO deverá ser preenchido se o 
Detalhamento da operação (tag: ide/detOper) for “15. 
Doação sem contraprestação a favor do doador”.

## Página 16

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 16 / 43 
1 
 
Grupo W. Total da NF-e ABI  
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
W01 total Grupo Totais da NF-e ABI G A01  0-1  A obrigatoriedade ou vedação do preenchimento deste grupo 
está condicionada ao “Indicador de alienação decorrente de 
incorporação, loteamento ou desmembramento” (tag: 
indIncorpLote) 
 Se indIncorpLote=1 ou 2: Não abrir o grupo “Total da NF-e 
ABI” 
 Se indIncorpLote=0: Abrir o grupo “Total da NF-e ABI” 
... ... ... ... ... ... ... ... ... 
W03 vTotalOperacao Valor Total da Operação E W01 N 0-1 13v2 OBSERVAÇÃO: Este campo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição” ou se 
o Tipo de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
W04 vOperacIndiv Valor da Operação Individual E W01 N 0-1 13v2 OBSERVAÇÃO: Este campo NÃO será aberto se o Tipo de 
Documento Fiscal (tag: tpNF) for igual à “2=Transição” ou se 
o Tipo de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
... ... ... ... ... ... ... ... ... 
W11 vNF Valor Total da NF-e ABI E W01 N 1-1 13v2 OBSERVAÇÃO: O Valor Total da NF-e ABI pode variar de 
acordo com tipo e a finalidade do documento fiscal. 
1. Se o Tipo de Documento Fiscal (tag: tpNF) for igual à 
“0=Simplificado” ou "1=Completo": 
1.1. Com Tipo de pagamento (tag: tpPagAnt) 
correspondente à “1=Pagamento antecipado”. 
     → vNF = vBC + vIBSUF + vIBSMun + vCBS 
1.2. Com Tipo de pagamento (tag: itpPagAnt) 
correspondente à “2=Fornecimento com pagamento 
realizado anteriormente”. 
     → vNF = vOperacIndiv + vIBSUF + vIBSMun + vCBS 
1.3. Com Tipo de pagamento (tag: tpPagAnt) não 
preenchido: 
     → vNF = vBC + vIBSUF + vIBSMun + vCBS 
2. Se o Tipo de Documento Fiscal (tag: tpNF) for igual à 
“2=Transição”: 
     → vNF = vBC + vIBSUF + vIBSMun + vCBS

## Página 17

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 17 / 43 
1 
 
3. Eventos 
Lista de Eventos 
 
ID Campo Descrição Autor Finalidade 
ZZA01 evPagParcelaNFeABI Evento de Pagamento de Parcela 
Código do evento (tag: tpEvento): 112310 
Emitente ou Transmitente Registrar mediante evento: 
1) Os pagamentos de parcela nas alienações decorrentes de incorporação ou 
parcelamento, a fim de que sejam declarados o IBS e a CBS devidos nos termos 
do art. 262 da LC 214/2025; ou 
2) Os pagamentos de parcela ou prestações nas alienações NÃO decorrentes de 
incorporação ou parcelamento, a fim de que sejam declarados o IBS e a CBS 
incidentes sobre os respectivos acréscimos. 
OBSERVAÇÃO 1: Nas alienações decorrentes de incorporação ou parcelamento, a 
NF-e ABI original será emitida sem destaque de tributo, devendo ser posteriormente 
acompanhada de eventos de pagamento de parcela com destaque de IBS e da CBS 
incidentes sobre cada pagamento. 
OBSERVAÇÃO 2: Nas alienações NÃO decorrentes de incorporação ou parcelamento, 
a NF-e ABI original será emitida com destaque do IBS e da CBS sobre a totalidade do 
valor da operação, devendo ser posteriormente acompanhada de eventos de 
pagamento complementar com destaque de IBS e da CBS incidentes somente sobre 
os acréscimos (multa, atualização, juros etc.) surgidos após o ato de alienação. 
ZZB01 evApropCredIndNFeABI Evento de Apropriação de créditos individuais 
Código do evento (tag: tpEvento): 211310 
Adquirente Registrar mediante evento a apropriação de créditos individuais nas alienações com 
mais de um comprador ou adquirente. 
OBSERVAÇÃO: A NF-e ABI com modalidade da operação diferente de “02. 
Arrematação Judicial, Adjudicação ou Remição” (tag: modOper<>02) não permitirá a 
apropriação de crédito quando houver mais de um adquirente na operação, razão 
pela qual será necessário que cada comprador ou adquirente que se enquadre na 
condição de contribuinte registre um evento para se apropriar do crédito de IBS e 
CBS na proporção do seu percentual de participação na aquisição. 
ZZC01 evDesfazimAlienac Evento de Desfazimento da Alienação 
Código do evento (tag: tpEvento): 112320 
Emitente, Transmitente ou 
Adquirente 
(conforme o caso) 
Registrar mediante evento o desfazimento de uma operação de alienação de bem 
imóvel. 
O evento só poderá ser registrado quando o Tipo de Documento Fiscal da NF-e ABI 
referenciada for igual à “0=Simplidcado” ou “1=Completo”. 
Tabela de códigos dos eventos da NF-e ABI (tag: infEvento/tpEvento): 
   110111 – Cancelamento (evCancNFeABI) – Autor: Emitente (manƟdo, conforme MOC Visão Geral); 
   112310 – Pagamento de Parcela (evPagParcelaNFeABI) – Autor: Emitente ou Transmitente; 
   112320 – Desfazimento da Alienação (evDesfazimAlienac) – Autor: Emitente, Transmitente ou Adquirente, conforme o caso; 
   211310 – Apropriação de créditos individuais (evApropCredIndNFeABI) – Autor: Adquirente. 
Os códigos seguem a convenção dos DF-e: preﬁxo “11” para eventos registrados pelo emitente ou pelo declarante da operação e preﬁxo “21” para eventos registrados pelo adquirente. A 
faixa 1123xx/2113xx foi reservada à NF-e ABI para evitar sobreposição com os códigos de eventos da NF-e/NFC-e da Reforma Tributária. Códigos não constantes desta tabela serão 
rejeitados pela regra genérica de tpEvento inválido (cStat 491).

## Página 18

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 18 / 43 
1 
 
Evento: Apropriação de créditos individuais 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
ZZB01 evApropCredIndNFeABI Evento de Apropriação de créditos individuais G P17  1-1  ORIENTAÇÃO: O “Evento de Apropriação de créditos 
individuais” deverá ser registrado pelo comprador ou 
adquirente quando, na NF-e ABI referenciada, forem reunidas 
as duas condições abaixo: 
(1) A modalidade da operação for diferente de “02. 
Arrematação Judicial, Adjudicação ou Remição” 
(modOper<>02); e 
(2) Houver mais de um adquirente na operação imobiliária. 
 
Evento: Desfazimento da Alienação 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
ZZC01 evDesfazimAlienac Evento de Desfazimento da Alienação G P17  1-1  OBSERVAÇÃO 1: Se a modalidade da operação da NF-e ABI 
referenciada for diferente de “02. Arrematação Judicial, 
Adjudicação ou Remição” (modOper<>02), o “Evento de 
Desfazimento da Alienação” deverá ser registrado:  
 Pelo emitente ou transmitente da NF-e ABI do tipo 
simplificada (tpNF=0); ou 
 Pelo emitente ou transmitente declarante (tag: 
indDeclarante=1) da NF-e ABI do tipo completa 
(tpNF=1). 
Se a modalidade da operação da NF-e ABI referenciada for 
igual à “02. Arrematação Judicial, Adjudicação ou Remição” 
(modOper=02), o “Evento de Desfazimento da Operação” 
deverá ser registrado pelo: 
 Pelo emitente ou adquirente da NF-e ABI do tipo 
simplificada (tpNF=0); ou 
 Pelo emitente ou adquirente declarante (tag: 
indDeclarante=1) da NF-e ABI do tipo completa 
(tpNF=1). 
OBSERVAÇÃO 2: Código do evento (tag: tpEvento): 112320. 
ZZC01a versao Versão do Evento A ZZC01 N 1-1 2v2  
ZZC01b descEvento Descrição do Evento E ZZC01 C 1-1 5-60 Informar o literal “Evento de Desfazimento da Alienação” 
ZZC02 tpDesfaz Tipo de desfazimento E ZZC01 N 1-1 2 Verificar Tabela de códigos da NFe ABI, publicada no Portal 
da NFe ABI. 
ORIENTAÇÃO: O usuário deverá informar se a alienação está 
sendo desfeita por conta de distrato, decisão judicial, 
reversão da consolidação da propriedade, etc.

## Página 19

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 19 / 43 
1 
 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
ZZC03 dtDesfaz Data do ato de desfazimento E ZZC01 D 1-1  EXEMPLOS: 
 Caso o desfazimento tenha ocorrido mediante um 
distrato, deverá ser inserida a data do respectivo 
instrumento de distrato; 
 Caso o desfazimento tenha ocorrido mediante 
determinação judicial, deverá ser inserida a data da 
respectiva decisão judicial. 
ZZC04 xDesfaz Descrição do ato de desfazimento E ZZC01 C 0-1 5-150 OBSERVAÇÃO: Obrigatório quando o Tipo de desfazimento 
(tag: tpDesfaz)  for “99=Outros”.

## Página 20

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 20 / 43 
1 
 
4. Regras de Negócio 
A seguir são apresentados os ajustes nas regras de negócio da NF-e ABI. 
B. Identificação da NF-e ABI 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
B09-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual a “2=Transição”: 
→ O Formato de Impressão do DANFE (tag: tpImp) deve ser igual a “0=Sem geração de 
DANFE”. 
1043 Rej. Rejeição: NF-e ABI de transição não admite geração de DANFE-ABI (tpImp deve ser igual 
a 0). 
B10-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo”: 
  → Obrigatório preencher o grupo Modalidade e Natureza da operação (tag: gModNat) 
1000 Rej. Rejeição: É obrigatório preencher o grupo Modalidade e Natureza da operação (tag: 
gModNat) quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” 
ou “1=Completo”. 
B10-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo Modalidade e Natureza da operação (tag: gModNat) 
1001 Rej. Rejeição: Não é permitido preencher o grupo Modalidade e Natureza da operação (tag: 
gModNat) quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
B13-10 Se a Modalidade da operação (tag: modOper) for “02=Arrematação Judicial, Adjudicação 
ou Remição” ou “04=Permuta”: 
   Proibido preencher o detalhamento da operação (tag: detOper) 
1050 Rej. Rejeição: Não é permitido preencher o detalhamento da operação (tag: detOper) 
quando a modalidade da operação for for igual à “02=Arrematação Judicial, 
Adjudicação ou Remição” ou “04=Permuta”. 
 
BB. Grupo de notas de antecipação de pagamento 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
BB01-10 Se o Tipo de pagamento (tag: tpPagAnt) não for preenchido: 
  → Proibido preencher o Grupo de notas de antecipação de pagamento (tag: 
gPagAntecipado) 
1002 Rej. Rejeição: Não é permitido preencher o Grupo de notas de antecipação de pagamento 
(tag: gPagAntecipado) quando o Tipo de pagamento (tag: tpPagAnt) não for preenchido. 
BB01-20 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”: 
  → Proibido preencher o Grupo de notas de antecipação de pagamento (tag: 
gPagAntecipado) 
1003 Rej. Rejeição: Não é permitido preencher o Grupo de notas de antecipação de pagamento 
(tag: gPagAntecipado) quando o Tipo de pagamento (tag: tpPagAnt) for igual à 
“1=Pagamento antecipado”. 
BB01-30 Se o Tipo de pagamento (tag: tpPagAnt) for igual à“2=Fornecimento com pagamento 
realizado anteriormente”. 
  → Obrigatório preencher o Grupo de notas de antecipação de pagamento (tag: 
gPagAntecipado) 
1004 Rej. Rejeição: É obrigatório preencher o Grupo de notas de antecipação de pagamento (tag: 
gPagAntecipado) quando o Tipo de pagamento (tag: tpPagAnt) for igual à 
“2=Fornecimento com pagamento realizado anteriormente”. 
 
 
C. Identificação do Emitente 
 
Campo-
Seq Regra de Validação Msg Efeito Descrição Erro 
C04-10 Se tpAmb (id:B24) = 2 e informado xNome (C04) 
   xNome (C04) deve ser informado com a literal “NF-E ABI EMITIDA EM AMBIENTE DE 
HOMOLOGACAO - SEM VALOR FISCAL” 
858 Rej. Rejeição: NF-e emitida em ambiente de homologação com Razão Social do emitente 
diferente de NF-E ABI EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL 
C18-10 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02):  
  Proibido informar o Tipo de Emitente (tag: tpEmit) igual à “03=Leiloeiro (em nome do 
arrematante)”  
274 Rej. Rejeição: Tipo de Emitente inválido para a modalidade da operação [tpEmit=XX, 
modOper=XX]

## Página 21

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 21 / 43 
1 
 
Campo-
Seq Regra de Validação Msg Efeito Descrição Erro 
C18-20 Se a Modalidade da operação for igual à “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02):  
 Tipo de Emitente não pode ser diferente de “02=Comprador, Adquirente ou 
Cessionário” ou “03=Leiloeiro (em nome do arrematante)” (tag: tpEmit<>02 ou 03) 
274 Rej. Rejeição: Tipo de Emitente inválido para a modalidade da operação [tpEmit=XX, 
modOper=XX] 
 
E. Identificação dos Transmitentes da Operação da NF-e ABI 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
E01-10 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo”:  
  → Obrigatório preencher o grupo de IdenƟﬁcação dos Transmitentes da Operação da NF-e 
ABI (tag: transmit) 
1005 Rej. Rejeição: É obrigatório preencher o grupo de Identificação dos Transmitentes da 
Operação da NF-e ABI (tag: transmit) quando o Tipo de Documento Fiscal (tag: 
tpNF) for igual à “0=Simplificado” ou “1=Completo”. 
E01-20 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo de Identificação dos Transmitentes da Operação da NF-e ABI 
(tag: transmit) 
1006 Rej. Rejeição: Não é permitido preencher o grupo de Identificação dos Transmitentes 
da Operação da NF-e ABI (tag: transmit) quando o Tipo de Documento Fiscal (tag: 
tpNF) for igual à “2=Transição”. 
E01a-20 Número sequencial dos Transmitentes (atributo: nTransmit) não poderá ser maior do que 1 
(tag: nTransmit > 1) quando reunidas as seguitnes condições: 
  Tipo de Documento Fiscal  (tag: ide/tpNF) for “0=Simplificado”; e  
  Modalidade da Operação (tag: ide/modOper) for diferente de “02=Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper<>02) 
Exceção: 
  A regra não se aplica quando o Tipo de Emitente (tag: tpEmit) for igual à “02=Comprador, 
Adquirente ou Cessionário)” (tag: tpEmit=02) 
801 Rej. Rejeição: Número sequencial dos Transmitentes não pode ser maior do que 1 
para NF-e ABI do tipo “0=Simplificado” e modalidade da operação diferente de 
“02=Arrematação Judicial, Adjudicação ou Remição”. 
E02-10 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou Remição” 
(tag: modOper=02) ou o Tipo de Documento Fiscal  (tag: ide/tpNF) for “0=Simplificado”: 
  Não pode ser informado o Indicador de Declarante (tag: indDeclarante) 
802 Rej. Rejeição: Proibido informar o Indicador de Declarante 
E02-20 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for 
“1=Completo”: 
  Obrigatório informar o Indicador de Declarante (tag: indDeclarante) 
803 Rej. Rejeição: Obrigatório informar o Indicador de Declarante 
E02-30 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for 
“1=Completo”: 
  Não pode haver mais de um Indicador de Declarante (tag: indDeclarante) que seja igual à 1 
804 Rej. Rejeição: Não pode ser informado mais de um Indicador de Declarante que seja 
igual à 1 
E02-40 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for 
“1=Completo”: 
  Obrigatório haver um Indicador de Declarante (tag: indDeclarante) que seja igual à 1 
805 Rej. Rejeição: Obrigatório haver um Indicador de Declarante que seja igual à 1 
E19-10 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou Remição” 
(tag: modOper=02): 
  Não pode ser informado o Indicador de Contribuinte do Regime regular do IBS/CBS (tag: 
indContrib) 
929 Rej. Rejeição: Proibido informar o Indicador de Contribuinte do Regime regular do 
IBS/CBS (tag: indContrib) para a modalidade da operação igual a “02=Arrematação 
Judicial, Adjudicação ou Remição”.

## Página 22

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 22 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
E19-20 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02): 
  Deve ser informado o Indicador de Contribuinte do Regime regular do IBS/CBS (tag: 
indContrib) 
930 Rej. Rejeição: Obrigatório informar o Indicador de Contribuinte do Regime regular do 
IBS/CBS (tag: indContrib) para a modalidade da operação diferente a 
“02=Arrematação Judicial, Adjudicação ou Remição”. 
E19-30 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02) e o Tipo de Emitente for igual à “02=Comprador, Adquirente 
ou Cessionário)” (tag: tpEmit=02):  
  O Indicador de Contribuinte do Regime regular do IBS/CBS deve ser igual à 0 (tag: indContrib=0) 
1007 Rej. Rejeição: O Indicador de Contribuinte do Regime regular do IBS/CBS deverá ser igual 
à 0 (tag: indContrib=0) quando a Modalidade da operação for diferente de 
“02=Arrematação Judicial, Adjudicação ou Remição” (tag: modOper<>02) e o Tipo 
de Emitente for igual à “02=Comprador, Adquirente ou Cessionário)” (tag: 
tpEmit=02). 
 
F. Identificação dos Adquirentes da Operação da NF-e ABI 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
F01-10 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo”:  
  → Obrigatório preencher o grupo de IdenƟﬁcação dos Adquirentes da Operação da NF-e 
ABI (tag: adquirente) 
1008 Rej. Rejeição: É obrigatório preencher o grupo de Identificação dos Adquirentes da 
Operação da NF-e ABI (tag: adquirente) quando o Tipo de Documento Fiscal (tag: 
tpNF) for igual à “0=Simplificado” ou “1=Completo”. 
F01-20 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo de IdenƟﬁcação dos Adquirentes da Operação da NF-e ABI 
(tag: adquirente) 
1009 Rej. Rejeição: Não é permitido preencher o grupo Identificação dos Adquirentes da 
Operação da NF-e ABI (tag: adquirente) quando o Tipo de Documento Fiscal (tag: 
tpNF) for igual à “2=Transição”. 
F01a-20 Número sequencial dos Adquirentes (atributo: nAdquir) não poderá ser maior do que 1 (tag: 
nAdquir > 1) quando reunidas as seguintes condições: 
 Tipo de Documento Fiscal  (tag: ide/tpNF) for “0=Simplificado”; e  
 Modalidade da Operação (tag: ide/modOper) for igual a “02=Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper=02) 
807 Rej. Rejeição: Número sequencial dos Adquirentes não pode ser maior do que 1 para 
NF-e ABI do tipo “0=Simplificado” e modalidade da operação igual à 
“02=Arrematação Judicial, Adjudicação ou Remição”. 
F02-10 Se a Modalidade da operação for diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02) ou o Tipo de Documento Fiscal  (tag: ide/tpNF) for 
“0=Simplificado”: 
  Não pode ser informado o Indicador de Declarante (tag: indDeclarante) 
802 Rej. Rejeição: Proibido informar o Indicador de Declarante. 
F02-20 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou Remição” 
(tag: modOper=02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for “1=Completo”: 
  Obrigatório informar o Indicador de Declarante (tag: indDeclarante) 
803 Rej. Rejeição: Obrigatório informar o Indicador de Declarante 
F02-30 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou Remição” 
(tag: modOper=02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for “1=Completo”: 
  Proibido mais de um Indicador de Declarante (tag: indDeclarante) que seja igual à 1 
810 Rej. Rejeição: Não pode ser informado mais de um Indicador de.Declarante que seja 
igual à 1 
F02-40 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou Remição”  
(tag: modOper=02) e o Tipo de Documento Fiscal  (tag: ide/tpNF) for “1=Completo”: 
  Obrigatório haver um Indicador de Declarante (tag: indDeclarante) que seja igual à 1 
811 Rej. Rejeição: Obrigatório haver um Indicador de Declarante que seja igual à 1. 
F18-20 Se o Tipo de Documento Fiscal (tag: ide/tpNF) for “1=Completo” e a modalidade da operação 
for diferente de “02=Arrematação Judicial, Adjudicação ou Remição” (tag: modOper<>02): 
   Proibido informar o Percentual de Aquisição (tag: pAquisicao) 
819 Rej. 
 
  Rejeição: É proibido informar o Percentual de Aquisição 
F18-30 Se o Tipo de Documento Fiscal (tag: ide/tpNF) for “1=Completo” e a modalidade da operação 
for igual à “02=Arrematação Judicial, Adjudicação ou Remição” (tag: modOper=02): 
   Obrigatório informar o Percentual de Aquisição (tag: pAquisicao) 
820 Rej. 
 
  Rejeição: É obrigatório informar o Percentual de Aquisição

## Página 23

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 23 / 43 
1 
 
G. Identificação do Imóvel 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
G01-10 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo”:  
 → Obrigatório preencher o grupo de Identificação do imovel (tag: imovel) 
1010 Rej. Rejeição: É obrigatório preencher o grupo de Identificação do imovel (tag: imovel) se o 
Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo”. 
G01-20 Se Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo de Identificação do imovel (tag: imovel) 
1011 Rej. Rejeição: É proibido preencher o grupo de Identificação do imovel (tag: imovel) quando 
o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
G03-10 Se: 
  → Cadastro do CIB (tag: cCIB) não for preenchido; e  
  → Indicador se o imóvel possui IPTU for igual à 0 (tag: indIPTU=0); e  
  → Indicador se o imóvel possui INCRA for igual à 0 (tag: indINCRA=0) 
Então: 
  → Obrigatório informar o  Cadastro do CIB (tag: cCIB), o número do IPTU (tag: nIPTU) 
ou o número do Incra (tag: nINCRA) 
(OBS: Regra de implementação futura) 
1012 Rej. Rejeição: Obrigatório informar o  Cadastro do CIB (tag: cCIB), o número do IPTU (tag: 
nIPTU) ou o número do Incra (tag: nINCRA) 
G06-10 Se informado indIPTU igual a 1 (tag: indIPTU=1): 
   Obrigatório informar o número do IPTU (tag: nIPTU) 
824 Rej. Rejeição: Obrigatório informar o número do IPTU 
G08-10 Se informado indINCRA igual a 1 (tag: indINCRA=1): 
   Obrigatório informar o número do INCRA (tag: nINCRA) 
825 Rej. Rejeição: Obrigatório informar o número do INCRA 
G08b-10 Se informado indRIP igual a 1 (tag: indRIP=1): 
   Obrigatório informar o número do RIP (tag: nRIP) 
1013 Rej. Rejeição: Obrigatório informar o número do RIP (Registro Imobiliário Patrimonial) da 
Secretaria do Patrimônio da União (SPU). 
G11-20 Se o indicador “ind_Enquadr_NFeABI” da tabela de cClassTrib do IBS e da CBS for igual a 
0 (tag: ind_Enquadr_NFeABI=0): 
  Proibido informar Enquadramento do imóvel (tag: enquadramento) 
829 Rej. 
 
 Rejeição: É proibido informar o Enquadramento do imóvel 
G11-30 Se o indicador “ind_Enquadr_NFeABI” da tabela de cClassTrib do IBS e da CBS for igual a 
1 (tag: ind_Enquadr_NFeABI=1): 
  Obrigatório informar Enquadramento do imóvel (tag: enquadramento) 
830 Rej. 
 
 Rejeição: É obrigatório informar o Enquadramento do imóvel 
G24-10 Se o indicador “ind_Area_NFeABI” da tabela de cClassTrib do IBS e da CBS igual a 0 (tag: 
ind_Area_NFeABI=0): 
  Proibido informar a Área Total (tag: areaTotal)  
831 Rej. 
 
 Rejeição: É proibido informar a Área Total do Imóvel 
G25-10 Se o indicador “ind_uArea_NFeABI” da tabela de cClassTrib do IBS e da CBS igual a 0 (tag: 
ind_uArea_NFeABI=0): 
  Proibido informar a Unidade de Medida da Área Total (tag: uAreaTotal)  
833 Rej. 
 
 Rejeição: É proibido informar a Unidade de Medida da Área Total 
 
H. Informações da Operação 
 
Campo- 
Seq Regra de Validação Msg Efeito Descrição Erro 
H01-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo” 
com Tipo de pagamento (tag: tpPagAnt) igual à “1=Pagamento antecipado”. 
  → Proibido preencher o grupo de Informações da Operação (tag: infOper) 
1014 Rej. Rejeição: Não é permitido preencher o grupo de Informações da Operação (tag: infOper) 
quando o Tipo de pagamento (tag: tpPagAnt) igual à “1=Pagamento antecipado”. 
H01-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo” 
com Tipo de pagamento (tag: tpPagAnt) igual à “2=Fornecimento com pagamento 
realizado anteriormente”: 
  → Obrigatório preencher o grupo de Informações da Operação (tag: infOper) 
1015 Rej. Rejeição: É obrigatório preencher o grupo de Informações da Operação (tag: infOper).

## Página 24

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 24 / 43 
1 
 
Campo- 
Seq Regra de Validação Msg Efeito Descrição Erro 
H01-30 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo” 
com Tipo de pagamento (tag: tpPagAnt) não preenchido. 
  → Obrigatório preencher o grupo de Informações da Operação (tag: infOper) 
1015 Rej. Rejeição: É obrigatório preencher o grupo de Informações da Operação (tag: infOper). 
H01-40 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo de Informações da Operação (tag: infOper) 
1016 Rej. Rejeição: Não é permitido preencher o grupo de grupo de Informações da Operação 
(tag: infOper) quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
H10b-10 Se o Indicador de alienação decorrente de incorporação, loteamento ou desmembra- 
mento for igual à 0 (tag: indIncorpLote=0): 
  Proibido informar o Cadastro Nacional da Obra (tag: CNO) 
1017 Rej. Rejeição: Proibido informar o Cadastro Nacional da Obra (CNO). 
H10b-20 Se o Indicador de alienação decorrente de incorporação, loteamento ou desmembra- 
mento for igual à 1 (tag: indIncorpLote=1): 
  Obrigatório informar o Cadastro do CIB da obra (tag: cCIBObra) ou o Cadastro 
Nacional da Obra (tag: CNO). 
1018 Rej. Rejeição: Obrigatório informar o Cadastro do CIB da obra (tag: cCIBObra) ou o Cadastro 
Nacional da Obra (tag: CNO). 
H11-10 Se: 
  Modalidade da operação diferente de “03=Cessão ou Transmissão de direitos” (tag: 
modOper<>03); e 
  Indicador de Torna diferente de 1 (tag: indTorna<>1); e  
  Indicador de alienação decorrente de incorporação, loteamento ou 
desmembramento igual à 0 (tag: indIncorpLote=0); e  
   Indicador “ind_RedAjuste_NFeABI” da tabela de cClassTrib do IBS e da CBS igual a 1 
(tag: ind_RedAjuste_NFeABI=1) 
Então: 
  Obrigatório informar o grupo de Redutor de Ajuste Imovel (tag: gRedAjusteImovel) 
847 Rej. Rejeição: Obrigatório informar o grupo de Redutor de Ajuste Imóvel 
H11-20 Se o indicador “ind_gIBSCBS” da tabela de cClassTrib do IBS e da CBS igual a 0 (tag: 
ind_gIBSCBS=0) 
Então: 
 → Proibido informar o grupo de Redutor de Ajuste Imóvel (tag: gRedAjusteImovel) 
848 Rej. Rejeição: Proibido informar o grupo de Redutor de Ajuste Imóvel 
H16-10 Se: 
  Modalidade da operação for igual a “03=Cessão ou Transmissão de direitos” (tag: 
modOper=03); ou 
  Indicador de Torna igual a 1 (tag: indTorna=1); ou 
  Indicador “ind_gIBSCBS” da tabela de cClassTrib do IBS e da CBS igual a 0 (tag: 
ind_gIBSCBS=0); ou 
  Enquadramento do Imóvel for igual a “02=Imóvel Residencial Usado” (tag: 
enquadramento=02) ou “04=Não Residencial” (tag: enquadramento=04). 
Então: 
 Proibido informar o Indicador do Redutor Social (tag: indRedSocial) 
850 Rej. Rejeição: Proibido informar o Indicador de Redutor Social 
H21-10 Se a Modalidade da operação for “01=Alienação em Geral” (tag: modOper=01) 
  → Obrigatório informar o Indicador de Intermediação ou Corretagem (tag: 
indIntermedCorret) 
(OBS: Regra de implementação futura) 
855 Rej. Rejeição: Obrigatório informar o Indicador de Intermediação ou Corretagem

## Página 25

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 25 / 43 
1 
 
Campo- 
Seq Regra de Validação Msg Efeito Descrição Erro 
H22-10 Se o Indicador de Intermediação ou Corretagem for igual a “1=Sim” (tag: 
indIntermedCorret=1) 
  Obrigatório informar o Grupo de informações de Intermediação ou Corretagem (tag: 
gIntermedCorret) 
(OBS: Regra de implementação futura) 
1051 Rej. Rejeição: Obrigatório informar o Grupo de informações de Intermediação ou 
Corretagem 
 
U. Informações da Tributação 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
U01-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou 
“1=Completo”: 
  → Obrigatório preencher o grupo de Informações da Tributação (tag: infTrib) 
1019 Rej. Rejeição: É obrigatório preencher o grupo de Informações da Tributação (tag: infTrib) 
quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou 
“1=Completo”. 
U01-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
   → Proibido preencher o grupo de Informações da Tributação (tag: infTrib) 
1020 Rej. Rejeição: Não é permitido preencher o grupo de Informações da Tributação (tag: 
infTrib) quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
U09a-10 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”. 
  → Obrigatório preencher o Grupo de informações do pagamento antecipado (tag: 
gInfPagAntecip) 
1021 Rej. Rejeição: É obrigatório preencher Grupo de informações do pagamento antecipado 
(tag: gInfPagAntecip) quando o Tipo de pagamento (tag: tpPagAnt) for igual à 
“1=Pagamento antecipado”. 
U09a-20 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “2=Fornecimento com pagamento 
realizado anteriormente”: 
  → Proibido preencher o Grupo de informações do pagamento antecipado (tag: 
gInfPagAntecip) 
1022 Rej. Rejeição: Não é permitido preencher o Grupo de informações do pagamento 
antecipado (tag: gInfPagAntecip) quando o Tipo de pagamento (tag: tpPagAnt) for igual 
à “2=Fornecimento com pagamento realizado anteriormente”. 
U09a-30 Se o Tipo de pagamento (tag: tpPagAnt) não for preenchido. 
  → Proibido preencher o Grupo de informações do pagamento antecipado (tag: 
gInfPagAntecip) 
1023 Rej. Rejeição: Não é permitido preencher o Grupo de informações do pagamento 
antecipado (tag: gInfPagAntecip) quando o Tipo de pagamento (tag: tpPagAnt) não for 
preenchido. 
U10-10 Se: 
  Modalidade da operação diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02); e 
  Tipo de Documento Fiscal for “0=Simplificado” (tag: tpNF=0); e  
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1) 
Então: 
   vOperacIndiv = vTotalOperacao 
906 Rej. 
 
Rejeição: Valor da Operação Individual do Declarante difere do calculado 
U10-20 Se: 
  Modalidade da operação diferente de “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper<>02); e 
  Tipo de Documento Fiscal for “1=Completo” (tag: tpNF=1); e  
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1) 
Então: 
   vOperacIndiv = vTotalOperacao * pTransIndiv / pTransImovel     (*1) 
906 Rej. 
 
Rejeição: Valor da Operação Individual do Declarante difere do calculado 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos

## Página 26

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 26 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
U10-30 Se: 
  Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e   
  Tipo de Documento Fiscal for “0=Simplificado” (tag: tpNF=0): 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
Então: 
   vOperacIndiv = vTotalOperacao 
906 Rej. 
 
Rejeição: Valor da Operação Individual do Declarante difere do calculado 
U10-40 Se: 
  Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e 
  Tipo de Documento Fiscal for “1=Completo” (tag: tpNF=1); e 
 Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
Então: 
   vOperacIndiv = vTotalOperacao * pAquisicao / pTransImovel     (*1) 
906 Rej. 
 
Rejeição: Valor da Operação Individual do Declarante difere do calculado 
U10-50 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”. 
  → Proibido preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) 
1024 Rej. Rejeição: Não é permitido preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) quando o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento 
antecipado”. 
U10-60 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “2=Fornecimento com pagamento 
realizado anteriormente”: 
  → Obrigatório preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) 
1025 Rej. Rejeição: É Obrigatório preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) quando o Tipo de pagamento (tag: tpPagAnt) for igual à “2=Fornecimento 
com pagamento realizado anteriormente”. 
 
U10-70 Se o Tipo de pagamento (tag: tpPagAnt) não for preenchido: 
  → Obrigatório preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) 
1026 Rej. Rejeição: É Obrigatório preencher o Valor da Operação Individual do Declarante (tag: 
vOperacIndiv) quando o Tipo de pagamento (tag: tpPagAnt) não for preenchido. 
U11-60 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”. 
  → Proibido preencher o Valor da Torna Individual do Declarante (tag: vTornaIndiv) 
1027 Rej. Rejeição: Não é permitido preencher o Valor da Torna Individual do Declarante (tag: 
vTornaIndiv) quando o Tipo de pagamento (tag: tpPagAnt) for “1=Pagamento 
antecipado”. 
U12-30 Se: 
  Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); 
  Tipo de Documento Fiscal for “0=Simplificado” (tag: tpNF=0); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
 Então: 
   vRedAjusteIndiv = vRedAjusteImovel 
910 Rej. 
 
Rejeição: Valor do Redutor de Ajuste Individual do Declarante difere do calculado 
U12-40 Se a Modalidade da operação for igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02) e o Tipo de Documento Fiscal for “1=Completo” (tag: 
tpNF=1), vRedAjusteIndiv do Declarante deverá ser o cálculo: 
   vRedAjusteIndiv = pAquisicao * vRedAjusteImovel     (*1) 
910 Rej. 
 
Rejeição: Valor do Redutor de Ajuste Individual do Declarante difere do calculado 
U12-90 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”. 
  → Proibido preencher o Valor do Redutor de Ajuste Individual do Declarante (tag: 
vRedAjusteIndiv) 
1028 Rej. Rejeição: Não é permitido preencher o Valor do Redutor de Ajuste Individual do 
Declarante (tag: vRedAjusteIndiv) quando o Tipo de pagamento (tag: tpPagAnt) for 
igual à “1=Pagamento antecipado”. 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos

## Página 27

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 27 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
U13-30 Se: 
   Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e 
   Tipo de Documento Fiscal for “0=Simplificado” (tag: tpNF=0); e 
   Enquadramento igual a “01=Imóvel Residencial Novo” ou “03=Lote Residencial” 
(tag: enquadramento=01 ou 03); e 
   Indicador de Redutor Social igual à 1 (tag: indRedSocial = 1); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1) 
 Então, vRedSocialIndiv do Declarante deverá ser o cálculo: 
 vRedSocialIndiv = vRedSocial 
912 Rej. Rejeição: Valor do Redutor Social Individual do Declarante difere do calculado 
U13-40 Se: 
   Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e 
   Tipo de Documento Fiscal for “1=Completo” (tag: tpNF=1); e 
   Enquadramento igual a “01=Imóvel Residencial Novo” ou “03=Lote Residencial” 
(tag: enquadramento=01 ou 03); e 
   Indicador de Redutor Social igual à 1 (tag: indRedSocial = 1); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1) 
 Então, vRedSocialIndiv do Declarante deverá ser o cálculo: 
 vRedSocialIndiv = vRedSocial * pAquisicao           (*1) 
912 Rej. Rejeição: Valor do Redutor Social Individual do Declarante difere do calculado 
U13-80 Se: 
  Modalidade da operação igual a “03=Cessão ou Transmissão de direitos” (tag: 
modOper=03); ou 
  Indicador de Torna igual a 1 (tag: indTorna=1); ou 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 0 (tag: 
ind_gIBSCBS=0); ou 
  Enquadramento do Imóvel for “02=Imóvel Residencial Usado” (tag: 
enquadramento=02) ou “04=Não Residencial” (tag: enquadramento=04). 
Então: 
   Proibido informar o Valor do Redutor Social Individual do Declarante (tag: 
vRedSocialIndiv) 
913 Rej. Rejeição: Proibido informar o Valor do Redutor Social Individual do Declarante 
U13-90 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”. 
  → Proibido preencher o Valor do Redutor Social Individual do Declarante (tag: 
vRedSocialIndiv) 
1029 Rej. Rejeição: Não é permitido preencher o Valor do Redutor Social Individual do Declarante 
(tag: vRedSocialIndiv) quando o Tipo de pagamento (tag: tpPagAnt) for igual à 
“1=Pagamento antecipado”. 
U14-10 Se: 
  Modalidade da operação igual a “01=Alienação em geral” (tag: modOper=01); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e  
  Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então: 
   vBC = MAXIMO ((vOperacIndiv - vRedAjusteIndiv – vRedSocialIndiv) ; 0)    (*1) (*2) 
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos 
(*2) Função MAXIMO retorna o maior dentre dois valores

## Página 28

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 28 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
U14-20 Se: 
  Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e 
  Valor do Redutor de Ajuste do Imóvel igual a 0 ou não informado (tag: 
vRedAjusteImovel=0 ou não informado); e  
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e  
 Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então: 
  o valor da Base de Cálculo do declarante deverá ser 0 (tag: vBC = 0)   
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
U14-30 Se: 
  Modalidade da operação igual a “02=Arrematação Judicial, Adjudicação ou 
Remição” (tag: modOper=02); e 
  Valor do Redutor de Ajuste do Imóvel for diferente de 0 (tag: vRedAjusteImovel<>0) 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e  
 Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então, o valor da Base de Cálculo do Declarante deverá ser o cálculo: 
  vBC = MAXIMO ((vOperacIndiv - vRedAjusteIndiv – vRedSocialIndiv) ; 0)     (*1) (*2) 
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
U14-40 Se: 
  Modalidade da operação igual a “03=Cessão ou Transmissão de direitos” (tag: 
modOper=03); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
 Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então, o valor da Base de Cálculo do Declarante deverá ser o cálculo: 
  vBC = vOperacIndiv     (*1) 
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
U14-50 Se: 
  Modalidade da operação igual a “04=Permuta” (tag: modOper=04); e 
  Natureza da operação igual a 13 ou 14 (tag: natOper=13 ou 14); e 
  Indicador de Torna igual a 1 (tag: indTorna=1); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
 Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então, o valor da Base de Cálculo do Declarante deverá ser o cálculo: 
  vBC = vTornaIndiv     (*1) 
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos 
(*2) Função MAXIMO retorna o maior dentre dois valores

## Página 29

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 29 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
U14-60 Se: 
  Modalidade da operação igual a “04=Permuta” (tag: modOper=04); e 
  Natureza da operação igual a 15 (tag: natOper=15); e 
  Indicador "ind_gIBSCBS" da tabela de CST do IBS e da CBS for igual à 1 (tag: 
ind_gIBSCBS=1); e 
 Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente” 
Então, o valor da Base de Cálculo do Declarante deverá ser o cálculo: 
  vBC = MAXIMO ((vOperacIndiv - vRedAjusteIndiv – vRedSocialIndiv) ; 0)     (*1) (*2) 
914 Rej. 
 
Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos 
(*2) Função MAXIMO retorna o maior dentre dois valores 
 
UA. Informações da Tributação no Regime de Transição 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
UA01-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou 
“1=Completo”: 
  → Proibido preencher o grupo de Informações da Tributação no Regime de Transição 
(tag: gInfTribTransic) 
1030 Rej. Rejeição: Não é permitido preencher o grupo de Informações da Tributação no Regime 
de Transição (tag: gInfTribTransic) quando o Tipo de Documento Fiscal (tag: tpNF) for 
igual à “0=Simplificado” ou “1=Completo”. 
UA01-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Obrigatório preencher o grupo de Informações da Tributação no Regime de 
Transição (tag: gInfTribTransic) 
1031 Rej. Rejeição: É obrigatório preencher o grupo de Informações da Tributação no Regime de 
Transição (tag: gInfTribTransic) quando o Tipo de Documento Fiscal (tag: tpNF) for igual 
à “2=Transição”. 
UA15a-10 A Receita total de venda das unidades imobiliárias (tag: vRecTotal) deverá ser à soma 
das Receitas recebidas na venda das unidades imobiliárias (tag: vRecRecebRET) com as 
Receitas financeiras e variações monetárias vinculadas às vendas (tag: vRecFinRET). 
(vRecTotal = vRecRecebRET + vRecFinRET) 
1032 Rej. Rejeição: A Receita total de venda das unidades imobiliárias (tag: vRecTotal) não 
corresponde à soma das Receitas recebidas na venda das unidades imobiliárias (tag: 
vRecRecebRET) com as Receitas financeiras e variações monetárias vinculadas às 
vendas (tag: vRecFinRET). 
 
Y. Detalhes de Pagamento 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
Y01-10 Se o indicador “ind_pag_NFeABI” da tabela de cClassTrib do IBS e da CBS igual a 1 (tag: 
ind_ pag_NFeABI=0): 
  Proibido informar o grupo de pagamento inicialmente previsto (tag: pag)  
(OBS: Regra de implementação futura) 
860 Rej. 
 
Rejeição: É proibido informar o grupo de pagamento inicialmente previsto 
Y01-20 Se o indicador “ind_pag_NFeABI” da tabela de cClassTrib do IBS e da CBS igual a 1 (tag: 
ind_ pag_NFeABI=1): 
  Obrigatório informar o grupo de pagamento inicialmente previsto (tag: pag)  
(OBS: Regra de implementação futura) 
861 Rej. 
 
Rejeição: É obrigatório informar o grupo de pagamento inicialmente previsto 
Y01-30 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”: 
  → Proibido preencher o grupo de Pagamento inicialmente previsto (tag: pag) 
1033 Rej. 
 
Rejeição: Não é permitido preencher o grupo de Pagamento inicialmente previsto (tag: 
pag) quando o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição”. 
Y01-40 Se o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”: 
  → Proibido preencher o grupo de Pagamento inicialmente previsto (tag: pag) 
1034 Rej. Rejeição: Não é permitido preencher o grupo de Pagamento inicialmente previsto (tag: 
pag) quando o Tipo de pagamento (tag: tpPagAnt) for igual à “1=Pagamento 
antecipado”.

## Página 30

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 30 / 43 
1 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
Y06-20 Se o Indicador de alienação decorrente de incorporação, loteamento ou 
desmembramento for igual à 1 (tag: indIncorpLote=1): 
  Obrigatório informar o grupo de Detalhamento de Pagamento inicialmente previsto 
(tag: detPagIncorpLote) 
863 Rej. 
 
Rejeição: É obrigatório informar o grupo de Detalhamento de Pagamento inicialmente 
previsto 
Y06a-10 Número sequencial do detalhe de pagamento (atributo: nDetPag) deve ser sequencial 
e incremental 
864 Rej. Rejeição: Número sequencial do detalhe de pagamento não está sequencial e 
incremental [nDetPag: NNN] 
 
W. Total da NF-e 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
W01-10 O grupo “Total da NF-e ABI” não poderá ser informado se Indicador de alienação 
decorrente de incorporação, loteamento ou desmembramento for igual à 1 ou 2 (tag: 
indIncorpLote=1 ou 2) 
530 Rej. Rejeição: É proibido informar o grupo “Total da NF-e ABI” quando o Indicador de 
alienação decorrente de incorporação, loteamento ou desmembramento (tag: 
indIncorpLote) for igual à 1 ou 2. 
W03-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição” ou o Tipo de 
pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”: 
  → Proibido preencher o Valor Total da Operação (tag: total/vTotalOperacao) 
1039 Rej. Rejeição: Não é permitido preencher o campo Valor Total da Operação (tag: 
total/vTotalOperacao) na NF-e ABI de transição ou de pagamento antecipado. 
W03-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo” 
e o Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente”: 
  → Obrigatório preencher o Valor Total da Operação (tag: total/vTotalOperacao) 
1040 Rej. Rejeição: É obrigatório preencher o campo Valor Total da Operação (tag: 
total/vTotalOperacao). 
W04-10 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição” ou o Tipo de 
pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”: 
  → Proibido preencher o Valor da Operação Individual (tag: total/vOperacIndiv) 
1041 Rej. Rejeição: Não é permitido preencher o campo Valor da Operação Individual (tag: 
total/vOperacIndiv) na NF-e ABI de transição ou de pagamento antecipado. 
W04-20 Se o Tipo de Documento Fiscal (tag: tpNF) for igual à “0=Simplificado” ou “1=Completo” 
e o Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente”: 
  → Obrigatório preencher o Valor da Operação Individual (tag: total/vOperacIndiv) 
1042 Rej. Rejeição: É obrigatório preencher o campo Valor da Operação Individual (tag: 
total/vOperacIndiv). 
W11-10 Se: 
   o Tipo de Documento Fiscal (tag: tpNF) for “0=Simplificado” ou "1=Completo"; e  
   o Tipo de pagamento (tag: tpPagAnt) não for preenchido ou for igual à 
“2=Fornecimento com pagamento realizado anteriormente”; e 
   o Total do vNF (id:W11) diferir do somatório de:  
        (+) vOperacIndiv (id: W04) 
      (+) vIBSUF (id: W08) 
      (+) vIBSMun (id: W09)  
      (+) vCBS (id: W10) 
Ou se: 
   o Tipo de Documento Fiscal (tag: tpNF) for igual à “2=Transição" ou o Tipo de 
pagamento (tag: tpPagAnt) for igual à “1=Pagamento antecipado”; e 
   o Total do vNF (id:W11) difere do somatório de:  
        (+) vBC (id: W07) 
      (+) vIBSUF (id: W08)  
      (+) vIBSMun (id: W09)  
      (+) vCBS (id: W10) 
610 Rej. Rejeição: Total da NF difere do somatório dos Valores compõe o valor Total da NF. 
W11-20 Valor total da NF-e ABI superior ao valor limite permitido 628 Rej. Rejeição: Total da NF superior ao valor limite permitido [Limite]

## Página 31

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 31 / 43 
1 
 
ZZA. Evento de Pagamento de parcela 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
ZZA15-10 Se o Código do evento de pagamento for “01=Evento de pagamento de parcela nas 
alienações decorrentes de incorporação ou parcelamento” (tag: cdEventoPag=01), o valor 
da Base de Cálculo deverá ser o cálculo: 
  vBC = MAXIMO ((vOperacIndiv - vRedAjusteIndiv – vRedSocialIndiv) ; 0)        (*1) (*2) 
914 Rej. Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
ZZA15-20 Se o Código do evento de pagamento for “02=Evento de pagamento de parcela nas 
alienações não decorrentes de incorporação ou parcelamento” (tag: cdEventoPag=02), o 
valor da Base de Cálculo deverá ser o cálculo: 
  vBC = vAcrescParcela 
914 Rej. Rejeição: Valor da Base de Cálculo do Declarante difere do calculado 
(*1) Aceitar resultado com tolerância de 0,01 para mais ou para menos 
(*2) Função MAXIMO retorna o maior dentre dois valores 
 
ZZB. Evento de Apropriação de créditos individuais 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
ZZB01-10 A Modalidade da Operação da NF-e ABI referenciada é igual à “02=Arrematação Judicial, 
Adjudicação ou Remição” (tag: modOper=02) 
950 Rej. Rejeição: O evento de apropriação de crédito individual só poderá ser registrado 
quando a modalidade da NF-e ABI referenciada for diferente de “02=Arrematação 
Judicial, Adjudicação ou Remição”. 
ZZB06-10 O somatório dos Percentuais de Participação do Adquirente (tag: pParticip) é diferente de 
100% (tag: ∑ pParticip <> 1) 
1052 Rej. Rejeição: O somatório dos percentuais de participação dos adquirentes não resultam 
em 100% 
 
ZZC. Evento de Desfazimento da Alienação 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
ZZC01-10 O Tipo de Documento Fiscal da NF-e ABI referenciada é igual à “02=Transição” (tag: 
tpNF=02). 
1035 Rej. Rejeição: O evento de desfazimento da alienação só poderá ser registrado quando o 
Tipo de Documento Fiscal da NF-e ABI referenciada for diferente de “2=Transição”. 
ZZC02-10 Código do Tipo de desfazimento inválido (tag: tpDesfaz) 
OBS: Verificar tabela de código da NF-e ABI 
1036 Rej. Rejeição: Código do Tipo de desfazimento inválido 
ZZC04-10 Se o Tipo de desfazimento (tag: tpDesfaz) for igual a “99=Outros”: 
 → Obrigatório informar o campo Descrição do ato de desfazimento (tag: xDesfaz) 
1037 Rej. Rejeição: Obrigatório informar o campo de Descrição do ato de desfazimento (tag: 
xDesfaz) 
 
1. Banco de Dados: Emitente 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
1C17-50 Acesso ao BD de Emitentes da NF-e ABI (chave: CNPJ ou CPF do emitente – tags: 
emit/CNPJ ou emit/CPF): 
→ Emitente com bloqueio aƟvo para emissão de NF-e ABI, determinado pela 
Administração Tributária. 
1038 Rej. Rejeição: Emitente bloqueado pelo Fisco para emissão de NF-e ABI

## Página 32

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 32 / 
43 
 
 
5. QR Code da NF-e ABI 
O QR Code é um código de barras bidimensional, padronizado pela norma ISO/IEC 18004, que permite o 
acesso rápido à consulta pública da NF-e ABI a partir da leitura, com aplicativo leitor instalado em smartphone 
ou tablet, do código impresso ou apresentado no DANFE-ABI. 
O QR Code deverá constar do DANFE-ABI tanto na emissão normal quanto na emissão em contingência off-
line, seja o DANFE-ABI impresso ou apresentado em meio eletrônico. O conteúdo codificado na imagem deverá 
ser idêntico ao conteúdo da tag qrCode do grupo de informações suplementares (tag: infNFeSupl) do XML da 
NF-e ABI. 
Esta Nota Técnica altera a estrutura do QR Code definida no MOC NF-e ABI v1.00a (Anexo I – Preenchimento 
da URL do QR Code e regras de validação do grupo ZX), que adotava parâmetros posicionais separados pelo 
caractere “|”, com parâmetro de versão e identificação do adquirente, no padrão da NFC-e. Passa a ser adotada 
a estrutura de parâmetros nomeados utilizada pela DC-e e pelos demais DF-e com consulta por chave de 
acesso, com os reforços de segurança descritos neste capítulo. As regras de validação do MOC que foram 
aproveitadas, alteradas ou excluídas estão identificadas no item 5.6. 
A composição da URL do QR Code depende do tipo de emissão da NF-e ABI (tag: ide/tpEmis): 
• Emissão normal: estrutura simplificada, alinhada ao padrão dos Documentos Fiscais Eletrônicos 
autorizados de forma on-line, contendo apenas a chave de acesso e o tipo de ambiente (tpEmis=1, item 
5.2); 
• Emissão em contingência off-line: estrutura estendida, que acrescenta dados de conferência do 
documento e uma assinatura digital gerada com o certificado do emitente, garantindo autoria e integridade 
do QR Code enquanto a NF-e ABI ainda não foi recebida pela Secretaria da Fazenda (tpEmis=9, item 
5.3). 
5.1 Grupo de informações suplementares e preenchimento da URL 
O grupo de informações suplementares (tag: infNFeSupl) transporta a URL utilizada na geração do QR Code e 
o endereço de consulta pública por chave de acesso. O grupo é posicionado após o grupo de informações da 
NF-e ABI e antes da assinatura digital do documento, não sendo alcançado pela assinatura do XML. Por esse 
motivo, na emissão em contingência off-line a integridade do conteúdo do QR Code é assegurada por assinatura 
própria (parâmetro sign), conforme item 5.3. 
ID Campo Descrição Ele Pai Tipo Ocor. Tam. Observação 
ZX01 infNFeSupl Informações suplementares da 
Nota Fiscal G Raiz - 1-1  Informações suplementares da Nota Fiscal, não afetando a 
assinatura digital. 
ZX02 qrCode Texto com o QR-Code impresso 
no DANFE-ABI. E ZX01 C 1-1 100-1000 Conteúdo integral codificado na imagem do QR Code, conforme 
itens 5.2 (emissão normal) e 5.3 (contingência off-line). 
ZX03 urlChave 
Texto com a URL de consulta 
por chave de acesso a ser 
impressa no DANFE-ABI 
E ZX01 C 1-1 21-85 Informar a URL da “Consulta por chave de acesso da NF-e ABI”. 
 
O tamanho máximo da tag qrCode passa de 600 para 1.000 caracteres, para comportar a estrutura de 
contingência off-line com assinaturas geradas por chaves RSA de até 4.096 bits (com chave de 2.048 bits, a 
URL de contingência tem cerca de 530 caracteres; com chave de 4.096 bits, cerca de 870). 
A orientação de preenchimento da URL do QR Code (id ZX02: qrCode) do MOC passa a ser a seguinte: 
Versão QRCode Orientações de Preenchimento da URL do QR Code (id ZX02: qrCode) 
1.00 Informar a URL da “Consulta da NF-e ABI via QR-Code” no site da SEFAZ, compreendendo: 
• Endereço do site da UF, incluindo o protocolo de comunicação (“http://” ou “https://”); 
• Caractere separador “?”; 
• Parâmetros do QR-Code, concatenados usando o “|” como separador. 
Nota 1: Respeitar o uso de caracteres maiúsculos / minúsculos. 
1.00 Informar a URL da “Consulta da NF-e ABI via QR-Code” no site da SEFAZ, compreendendo: 
• Endereço do site da UF, incluindo o protocolo de comunicação (“https://”); 
• Caractere separador “?”; 
• Parâmetros do QR-Code no formato “nome=valor”, na ordem definida nos itens 5.2 (tpEmis=1) ou 5.3 (tpEmis=9), separados pelo 
caractere “&”. 
Nota 1: Respeitar o uso de caracteres maiúsculos / minúsculos. 
Nota 2: A estrutura não possui parâmetro de versão.

## Página 33

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 33 / 
43 
 
 
5.2 QR Code para NF-e ABI com tipo de emissão normal (tpEmis=1) 
A URL codificada no QR Code será composta por duas partes: 
Parte Conteúdo Exemplo 
1ª parte Endereço do serviço de consulta por QR Code, publicado no 
Portal da NF-e ABI, seguido do caractere “?”. https://www.fazenda.pr.gov.br/nfeabi/qrcode? 
2ª parte Parâmetros de consulta chNFeABI e tpAmb, nesta ordem, 
separados pelo caractere “&”. 
chNFeABI=41261012ABC34501DE35770010000001231012345674&t
pAmb=1  
Parâmetro Ocor. Descrição Formato / Conteúdo 
chNFeABI 1-1 Chave de acesso da NF-e ABI. 44 caracteres alfanuméricos, em letras maiúsculas, idênticos à chave de 
acesso do documento (sem o prefixo do atributo Id). 
tpAmb 1-1 Identificação do ambiente de autorização. 1=Produção; 2=Homologação. Idêntico ao conteúdo de ide/tpAmb.  
Observação: a critério da Secretaria da Fazenda, poderá ser utilizado o mesmo endereço de consulta para os 
ambientes de produção e de homologação. Nesse caso, a distinção entre os ambientes será feita pela aplicação 
de consulta, a partir do conteúdo do parâmetro tpAmb. 
Exemplo (ambiente de produção): 
https://www.fazenda.pr.gov.br/nfeabi/qrcode?chNFeABI=41261012ABC34501DE35770010000001231012345674&tpAmb=1  
5.3 QR Code para NF-e ABI com tipo de emissão em contingência off-line 
(tpEmis=9) 
A NF-e ABI emitida em contingência off-line é assinada e entregue ao interessado antes de ser recebida pela 
Secretaria da Fazenda. Durante esse intervalo a consulta pela chave de acesso não retorna o documento, 
razão pela qual o QR Code deverá conter um conjunto de informações adicionais que permita (i) comprovar a 
autoria do documento, (ii) conferir os dados essenciais apresentados no DANFE-ABI e (iii) vincular o QR Code 
ao XML que será posteriormente transmitido.  
Nesse caso, a URL do QR Code será composta por quatro partes, concatenadas na ordem abaixo: 
Parte Conteúdo 
1ª parte Endereço do serviço de consulta por QR Code, seguido do caractere “?” (idêntico ao da emissão normal). 
2ª parte Parâmetros chNFeABI e tpAmb, da mesma forma que na emissão normal, separados pelo caractere “&”. 
3ª parte Parâmetros de conferência do documento: dEmi (data de emissão), vNF (valor total) e digVal (valor de resumo da assinatura do XML). 
4ª parte Parâmetro sign: assinatura digital, com o certificado do emitente, de todo o conteúdo das partes 2 e 3.  
Parâmetro Ocor. Descrição Formato / Conteúdo 
chNFeABI 1-1 Chave de acesso da NF-e ABI. 44 caracteres alfanuméricos, em letras maiúsculas. A 35ª posição da chave (tpEmis) 
deverá ser igual a 9. 
tpAmb 1-1 Identificação do ambiente. 1=Produção; 2=Homologação. 
dEmi 1-1 Data de emissão. AAAAMMDD, correspondente à data de ide/dhEmi. 
vNF 1-1 Valor total da NF-e ABI. Valor de total/vNF com duas casas decimais, separador decimal “.” e sem separador de 
milhar (ex.: 906600.00). Informar 0.00 quando o grupo total não existir. 
digVal 1-1 Valor de resumo (DigestValue) da 
assinatura digital do XML. 
Representação hexadecimal, em letras maiúsculas, dos bytes do DigestValue 
decodificado de Base64 (40 caracteres para SHA-1; 64 para SHA-256). 
sign 1-1 Assinatura digital do QR Code. RSA (RSASSA-PKCS1-v1_5) com resumo SHA-256, codificada em Base64URL sem 
preenchimento (RFC 4648, seção 5), conforme item 5.3.1.  
A identificação do emitente não é repetida como parâmetro do QR Code, pois o CNPJ ou CPF do emitente já 
compõe a chave de acesso (posições 7 a 20). A aplicação de consulta e a validação na recepção obtêm o 
emitente diretamente do parâmetro chNFeABI, e a correspondência entre esse emitente e o titular do certificado 
que assina o XML é garantida pelas validações de assinatura do documento. 
5.3.1 Geração da assinatura (parâmetro sign) 
• Mensagem assinada: sequência de caracteres situada entre o caractere “?” e o separador “&sign=”, 
exatamente como aparece na URL, ou seja: 
chNFeABI=...&tpAmb=...&dEmi=...&vNF=...&digVal=.... 
• Codificação: a mensagem será convertida em bytes pela codificação UTF-8, sem espaços, quebras de 
linha ou caracteres de controle.

## Página 34

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 34 / 
43 
 
 
• Algoritmo: assinatura RSA no padrão RSASSA-PKCS1-v1_5 com função de resumo SHA-256 
(sha256WithRSAEncryption). 
• Certificado: deverá ser utilizada a chave privada do mesmo certificado digital que assina o XML da NF-e 
ABI, de modo que a assinatura do QR Code possa ser verificada com a chave pública contida no 
elemento X509Certificate da assinatura do documento. 
• Representação: o resultado binário será codificado em Base64URL (alfabeto “A–Z”, “a–z”, “0–9”, “-” e “_”), 
com a remoção dos caracteres de preenchimento “=”, e acrescentado ao final da URL precedido de 
“&sign=”. 
• Ordem de geração: o QR Code somente poderá ser gerado após a assinatura do XML, pois o parâmetro 
digVal depende do DigestValue produzido nessa assinatura. O conteúdo resultante deverá ser gravado na 
tag qrCode antes da transmissão. 
5.3.2 Exemplo de formação 
Mensagem a ser assinada: 
chNFeABI=41261012ABC34501DE35770010000001239076543219&tpAmb=1&dEmi=20261016&vNF=906600.00&digVal=B29B14A14DDD5
16E48D36FE3DAD1B40C2B0D89BE  
Conteúdo final da tag qrCode (mensagem + assinatura gerada com chave RSA de 2.048 bits): 
https://www.fazenda.pr.gov.br/nfeabi/qrcode?chNFeABI=41261012ABC34501DE35770010000001239076543219&tpAmb=1&dEmi
=20261016&vNF=906600.00&digVal=B29B14A14DDD516E48D36FE3DAD1B40C2B0D89BE&sign=D0ZTGA5wSrUpvIUhjICaoVNR_Dgo1AWcY
crBd5coQeFos90GFJVZRxvjGGVxeE5-cZqNCbhuzmFybwdQ1NfrnOCjYmHspCHTeSJJlC3mbCdJXePI2q4obMslk6-
aPQU_J8HTuMl7swE8iT84xluqeQYp--P1x0aBU9YwxKEXh7afYuWKn5cMA8E8qXDiELV488ui-
kEloRCHMkZjDwUL1zsGueCywepzMkFbepEJH249B3tfUBAQqyJgI3iU1-LQG7E-
mcE6X4feMqtXB4pLEhvXeVaivahnTkSYxQhXPaxAna0SOoKHJzoFrYo9brxeRAS4isE0NJz_xQnoXzzghA  
Os valores acima são meramente ilustrativos; a assinatura foi gerada com chave de teste. 
5.3.3 Validação e consulta do QR Code de contingência 
Na recepção da NF-e ABI emitida em contingência off-line, a Secretaria da Fazenda verificará a assinatura do 
parâmetro sign com a chave pública do certificado que assina o XML e a correspondência de todos os 
parâmetros com o conteúdo do documento, conforme as regras de validação do item 5.6. Divergências 
impedem a autorização do documento. 
Na consulta por QR Code realizada antes da recepção do documento pela Secretaria da Fazenda, a aplicação 
de consulta poderá informar que a NF-e ABI foi emitida em contingência e ainda não foi recebida, apresentando 
o emitente identificado na chave de acesso e os dados de conferência contidos no QR Code (data de emissão 
e valor total). Após a recepção, a consulta retornará a situação atualizada do documento autorizado. 
5.4 Regras para geração e representação 
• O conteúdo codificado na imagem do QR Code deverá corresponder integralmente ao conteúdo da tag 
qrCode do XML, sem truncamento. 
• O QR Code deverá seguir a norma ISO/IEC 18004, em modo de codificação byte, com nível de correção 
de erros mínimo “M” (15%). 
• A ordem dos parâmetros deverá ser preservada. O primeiro parâmetro é precedido pelo caractere “?” e os 
subsequentes pelo caractere “&”. Não deverão ser inseridos espaços, quebras de linha, parâmetros 
adicionais ou caracteres não previstos. 
• O QR Code deverá apontar para o endereço correspondente ao ambiente informado em tpAmb, e a chave 
do parâmetro chNFeABI deverá ser a chave de acesso do próprio documento. 
• A URL deverá ser codificada em UTF-8. Os valores dos parâmetros não deverão receber codificação 
percentual. 
• Na emissão em contingência off-line, o parâmetro sign deverá ser gerado após a assinatura do XML e com 
o mesmo certificado digital. 
• Dimensão mínima da imagem impressa: 25 mm × 25 mm na emissão normal e 35 mm × 35 mm na 
emissão em contingência off-line, em razão da maior densidade de módulos. Quando o conteúdo da tag 
qrCode ultrapassar 600 caracteres (situação decorrente de certificados com chave RSA superior a 2.048 
bits), a dimensão mínima será de 40 mm × 40 mm. Deverá ser preservada margem livre (quiet zone) de, 
no mínimo, 4 módulos ao redor do símbolo.

## Página 35

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 35 / 
43 
 
 
• O QR Code deverá ser impresso em cor escura sobre fundo claro, com contraste e resolução suficientes 
para leitura por dispositivos móveis. 
5.6 Regras de validação do QR Code 
As regras de validação do grupo ZX do MOC NF-e ABI v1.00a (Anexo I) foram revisadas em função da nova 
estrutura do QR Code. Na tabela abaixo, as regras aproveitadas sem alteração estão sem destaque; os trechos 
alterados e as regras novas estão destacados; e as regras e trechos excluídos estão tachados. 
• Aproveitadas sem alteração de conteúdo: ZX02-20 (endereço do site), com inclusão de nota. 
• Aproveitadas com ajuste: ZX02-228 (chave), ZX02-244 (ambiente), ZX02-268 (data de emissão), ZX02-
276 (valor total), ZX02-330, ZX02-334 e ZX02-338 (assinatura), ajustadas aos novos nomes, posições e 
formatos dos parâmetros. 
• Excluídas: ZX02-236, pois a nova estrutura não possui parâmetro de versão; e ZX02-328, pois a 
identificação do adquirente foi excluída (o adquirente pode não ser único, e a autoria do documento é do 
emitente, já identificado na chave de acesso). 
• Incluídas: ZX02-284 (digVal), ZX02-332 (parâmetros de contingência na emissão normal), ZX02-336 
(parâmetros obrigatórios na contingência) e ZX03-10 (URL de consulta por chave). 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
ZX02-20 Endereço do site da UF para a Consulta via QR-Code difere do previsto. 
Nota: O uso diferenciado de maiúsculas ou minúsculas não deve ser 
considerado na validação. 
Nota 2: Considera-se endereço o conteúdo anterior ao caractere “?”, que 
deve corresponder ao endereço publicado para o ambiente informado (tag: 
tpAmb). 
395 Rej. Rejeição: Endereço do site da UF da Consulta via QR-Code 
diverge do previsto 
ZX02-228 Parâmetro Chave de Acesso chNFeABI no QR-Code diverge da Chave de 
Acesso da Nota Fiscal 
Observação: NF-e ABI ONLINE ou OFFLINE é 1º parâmetro da URL do QR Code 
397 Rej. Rejeição: Parâmetro do QR-Code divergente da Nota Fiscal 
[Param: xxx]. 
ZX02-236 Parâmetro Versão informada no QR-Code diverge do previsto (“1”) 
Observação: Para NF-e ABI ONLINE ou OFFLINE é o 2º parâmetro da URL do 
QR Code 
398 Rej. Rejeição: Parâmetro Versão informada no QR-Code diverge 
do previsto (“1”) 
ZX02-244 Parâmetro Tipo de Ambiente (tpAmb) do QR-Code diverge do Tipo de 
Ambiente da Nota Fiscal (tag: tpAmb) 
Observação: Para NF-e ABI ONLINE ou OFFLINE é o 3º 2º parâmetro da URL 
do QR Code 
397 Rej. Rejeição: Parâmetro do QR-Code divergente da Nota Fiscal: 
[Param: xxx] 
ZX02-268 NF-e ABI de contingência (tpEmis=9): 
Parâmetro Dia da Data de Emissão (dEmi, formato AAAAMMDD) no QR-Code 
diverge do Dia da Data de Emissão da Nota Fiscal (tag: dhEmi) 
Observação 1: Para NF-e ABI ONLINE esse parâmetro não existe. 
Observação 2: Para NF-e ABI OFFLINE é o 4º 3º parâmetro da URL do QR Code 
397 Rej. Rejeição: Parâmetro do QR-Code divergente da Nota Fiscal: 
[Param: xxx] 
ZX02-276 NF-e ABI de contingência (tpEmis=9): 
Parâmetro Valor da Nota Fiscal (vNF) no QR-Code diverge do Valor Total da 
Nota Fiscal (tag:vNF) ou de 0.00, quando o grupo total não for informado 
Observação 1: Para NF-e ABI ONLINE esse parâmetro não existe. 
Observação 2: Para a NF-e ABI OFFLINE é o 5º 4º parâmetro da URL do QR 
397 Rej. Rejeição: Parâmetro do QR-Code divergente da Nota Fiscal: 
[Param: xxx] 
ZX02-284 NF-e ABI de contingência (tpEmis=9): 
Parâmetro digVal do QR-Code diverge do DigestValue da assinatura digital 
da NF-e ABI (tag: Signature/SignedInfo/Reference/DigestValue), convertido 
para hexadecimal 
Obs. 1: Para NF-e ABI ONLINE esse parâmetro não existe. 
Obs. 2: Para NF-e ABI OFFLINE é o 5º parâmetro da URL do QR Code 
397 Rej. Rejeição: Parâmetro do QR-Code divergente da Nota Fiscal: 
[Param: xxx] 
ZX02-328 NF-e ABI de contingência (tpEmis=9): 
Parâmetro Identificação do Adquirente do QR-Code diverge da Identificação 
do primeiro Adquirente. 
Obs. 1: Para NF-e ABI ONLINE esse parâmetro não existe. 
Obs. 2: Para NF-e ABI OFFLINE, considerar 6º e 7º parâmetros da URL do QR 
Code 
396 Rej. Rejeição: Parâmetro do QR-Code inexistente: [Param: xxx) 
ZX02-330 NF-e ABI não é de contingência (tpEmis<>9), o parâmetro “assinatura” “sign” 
não deve ser informado no qrCode. 
400 Rej. Rejeição: Parâmetro sig não deve ser informado no qrCode 
ZX02-332 NF-e ABI não é de contingência (tpEmis<>9): o qrCode deve conter somente 
os parâmetros chNFeABI e tpAmb (parâmetros dEmi, vNF e digVal não 
devem ser informados). 
1060 Rej. Rejeição: Parâmetro de contingência não deve ser 
informado no qrCode [Param: xxx] 
ZX02-334 NF-e ABI é de contingência (tpEmis=9), o parâmetro “assinatura” “sign” deve 
ser informado no qrCode. 
856 Rej. Rejeição: Parâmetro sign deve ser informado no qrCode 
ZX02-336 NF-e ABI de contingência (tpEmis=9): os parâmetros dEmi, vNF e digVal 
devem ser informados no qrCode, na ordem definida no item 5.3. 
396 Rej. Rejeição: Parâmetro do QR-Code inexistente: [Param: xxx]

## Página 36

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 36 / 
43 
 
 
Campo-Seq Regra de Validação Msg Efeito Descrição Erro 
ZX02-338 NF-e ABI de contingência (tpEmis=9): Valor da assinatura difere do valor 
calculado. 
A assinatura (parâmetro sign), decodificada de Base64URL, deve ser válida 
quando verificada com a chave pública do certificado que assina o XML (RSA-
SHA256 sobre a mensagem definida no item 5.3.1). 
857 Rej. Rejeição: Valor da assinatura do qrCode difere do valor 
calculado 
ZX03-10 URL de consulta por chave de acesso (tag: urlChave) difere do endereço 
publicado para o ambiente informado (tag: tpAmb). 
Nota: O uso diferenciado de maiúsculas ou minúsculas não deve ser 
considerado na validação. 
1061 Rej. Rejeição: URL de consulta por chave de acesso diverge da 
prevista

## Página 37

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 37 / 
43 
 
 
6. DANFE-ABI 
O DANFE-ABI – Documento Auxiliar da Nota Fiscal Eletrônica de Alienação de Bens Imóveis é a representação 
gráfica simplificada das informações constantes da NF-e ABI. O DANFE-ABI não substitui o arquivo XML da 
NF-e ABI e não possui validade autônoma em relação ao documento fiscal eletrônico autorizado. 
O leiaute deverá observar os modelos de referência dos itens 6.9 (retrato) e 6.10 (paisagem) e a especificação 
de campos do item 6.7. A disposição dos blocos poderá ser adaptada ao meio de apresentação, desde que 
sejam preservados a ordem dos blocos, a identificação dos campos, a legibilidade das informações e o 
conteúdo mínimo definido neste capítulo. 
6.1 Formato e apresentação 
• O DANFE-ABI poderá ser apresentado em meio impresso ou eletrônico (arquivo PDF). Quando impresso, 
poderá ser utilizado qualquer tipo de papel, exceto papel jornal, no tamanho A4 (210 mm × 297 mm), na 
orientação indicada no Formato de Impressão do DANFE (tag: ide/tpImp): 1=Retrato ou 2=Paisagem, 
conforme os modelos de referência dos itens 6.9 e 6.10. No formato paisagem, a ordem dos blocos e a 
identificação dos campos deverão ser mantidas, podendo blocos de listagem (transmitentes e 
adquirentes) ser apresentados lado a lado. Quando tpImp=0 (sem geração de DANFE), o DANFE-ABI não 
será gerado. 
• Todo o conteúdo deverá estar contido na área útil da folha, com margens mínimas de 5 mm em cada lado. 
Nenhum bloco, tabela ou campo poderá ultrapassar as margens. 
• Os blocos deverão ocupar a largura total da área útil e ser apresentados na seguinte ordem: Identificação 
da NF-e ABI; Transmitentes; Adquirentes; Identificação do imóvel; Informações da operação; Cálculo do 
IBS e da CBS; Dados adicionais. 
• O título de cada campo deverá ser impresso em letras maiúsculas, com fonte de, no mínimo, 5 pt, e o 
conteúdo com fonte de, no mínimo, 7 pt. O conteúdo poderá ser impresso em mais de uma linha, desde 
que a leitura seja feita de forma clara. 
• Valores monetários serão apresentados com duas casas decimais, separador de milhar “.” e separador 
decimal “,”, precedidos de “R$” nos campos de valor total. Percentuais e alíquotas serão apresentados 
com quatro casas decimais seguidas de “%”. 
• Datas serão apresentadas no formato DD/MM/AAAA e data/hora no formato DD/MM/AAAA HH:MM:SS, no 
horário informado no XML. 
• CNPJ será apresentado com a máscara 99.999.999/9999-99, admitidos caracteres alfanuméricos nas 
doze primeiras posições (ex.: 12.ABC.345/01DE-35), e CPF com a máscara 999.999.999-99. 
• Campos codificados serão apresentados no formato “código – descrição”, com a descrição da tabela 
correspondente do leiaute. 
• Campos sem conteúdo no XML serão apresentados com o sinal “—”. Blocos inteiros sem conteúdo 
poderão ser omitidos. 
6.2 Mensagens obrigatórias 
• Ambiente de homologação: o DANFE-ABI de NF-e ABI autorizada em ambiente de homologação 
(tpAmb=2) deverá conter a expressão “EMITIDA EM AMBIENTE DE HOMOLOGAÇÃO – SEM VALOR 
FISCAL” no quadro Informações complementares ou em marca d’água destacada. 
• Contingência off-line: o DANFE-ABI de NF-e ABI emitida em contingência off-line deverá conter, no 
campo Protocolo de autorização de uso, a expressão “EMITIDA EM CONTINGÊNCIA OFF-LINE – 
PENDENTE DE AUTORIZAÇÃO”, em destaque, e, no quadro Informações complementares, a data e 
hora e a justificativa da entrada em contingência (tags: gCont/dhCont e gCont/xJust). Após a autorização, 
o DANFE-ABI poderá ser novamente gerado com o número do protocolo. 
• Eventos: o DANFE-ABI representa a NF-e ABI no momento da autorização e não reflete eventos 
posteriores (como o desfazimento da alienação ou a apropriação de créditos individuais), cuja situação 
deverá ser verificada na consulta pública do documento. 
6.3 Chave de acesso e código de barras 
A chave de acesso será impressa em onze blocos de quatro caracteres, separados por espaço, com a máscara 
XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX, em posição de destaque no bloco de

## Página 38

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 38 / 
43 
 
 
identificação. 
O código de barras representará os 44 caracteres da chave de acesso no padrão Code 128 (ISO/IEC 15417), 
com seleção automática dos subconjuntos B e C, uma vez que a chave pode conter letras em razão do CNPJ 
alfanumérico. O símbolo deverá ter altura mínima de 9 mm, largura máxima de 80 mm e margem livre mínima 
de 10 módulos em cada extremidade. 
6.4 QR Code no DANFE-ABI 
O QR Code será apresentado no bloco Dados adicionais, com o título “CONSULTA VIA QR CODE”, gerado a 
partir do conteúdo integral da tag qrCode e observadas as dimensões e a margem livre definidas no item 5.5. 
Abaixo da imagem deverá constar a expressão “Consulte pela chave de acesso em:” seguida do conteúdo da 
tag urlChave. Quando o DANFE-ABI tiver mais de uma folha, o QR Code será apresentado em todas as folhas, 
no rodapé (item 6.5). 
Não deverão ser sobrepostos à área do QR Code textos, linhas, bordas ou outros elementos gráficos. A falha 
de leitura da imagem do QR Code não altera a validade da NF-e ABI autorizada, desde que seja possível 
consultar o documento pela chave de acesso e que o XML autorizado permaneça íntegro. 
6.5 DANFE-ABI com mais de uma folha 
O DANFE-ABI poderá ser emitido em mais de uma folha quando o número de transmitentes, adquirentes ou o 
volume de informações não couber em uma única folha. Nesse caso, cada folha será organizada em três áreas 
– cabeçalho, corpo e rodapé –, observadas as regras abaixo. 
• Cabeçalho (repetido em todas as folhas): o bloco Identificação da NF-e ABI será impresso 
integralmente em todas as folhas, na mesma disposição e tamanho da primeira folha, incluindo emitente, 
título, número, série, código de barras, chave de acesso, protocolo de autorização e demais campos do 
bloco. O campo Folha indicará a numeração “FOLHA n/t”, em que “n” é o número da folha e “t” o total de 
folhas. 
• Rodapé (repetido em todas as folhas): o bloco Dados adicionais, com o QR Code, a URL de consulta 
por chave de acesso, o quadro Informações complementares e o quadro Reservado ao Fisco, será 
impresso em todas as folhas, ancorado na parte inferior da área útil, com a mesma altura e o mesmo 
conteúdo. Assim, qualquer folha, ainda que separada ou digitalizada isoladamente, permite a consulta do 
documento. 
• Corpo: a área entre o cabeçalho e o rodapé receberá os demais blocos, na ordem definida no item 6.1, 
com continuidade de uma folha para a seguinte. Ao continuar em outra folha, as listagens de 
transmitentes e adquirentes repetirão o título do bloco, acrescido de “(CONTINUAÇÃO)”, e a linha de 
títulos das colunas, mantidas as mesmas colunas e larguras. 
• Quebra de folha: uma linha de listagem e um bloco de campos (Identificação do imóvel, Informações da 
operação e Cálculo do IBS e da CBS) não serão divididos entre folhas; se não couberem no espaço 
restante, serão impressos integralmente na folha seguinte. Ao final do corpo de cada folha que não seja a 
última, será impressa a expressão “CONTINUA NA FOLHA n/t”. 
• Informações complementares extensas: o quadro Informações complementares do rodapé tem altura 
fixa. Quando o conteúdo não couber no quadro (o campo infCpl admite até 5.000 caracteres), o quadro 
apresentará o início do texto seguido da expressão “CONTINUA NO CORPO DA ÚLTIMA FOLHA”, e o 
restante será impresso no corpo da última folha, no bloco “INFORMAÇÕES COMPLEMENTARES 
(CONTINUAÇÃO)”. Esse procedimento evita repetir textos longos em todas as folhas e mantém fixa a 
altura do rodapé. 
• Folhas sem conteúdo: não será gerada folha contendo apenas cabeçalho e rodapé.

## Página 39

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 39 / 
43 
 
 
A figura a seguir ilustra a organização de um DANFE-ABI com duas folhas: 
 CABEÇALHO 
Identificação da NF-e ABI (repetida) 
“FOLHA 1/2”  CABEÇALHO 
Identificação da NF-e ABI (repetida) 
“FOLHA 2/2”  
 
CORPO 
Transmitentes 
Adquirentes (início) 
 
“CONTINUA NA FOLHA 2/2” 
 
CORPO 
Adquirentes (continuação) 
Imóvel · Operação · Cálculo 
Informações complementares (continuação) 
 
 RODAPÉ 
Dados adicionais + QR Code (repetidos)  RODAPÉ 
Dados adicionais + QR Code (repetidos)  
 
6.6 Correspondência com o XML 
As informações apresentadas no DANFE-ABI deverão ser obtidas exclusivamente do XML da NF-e ABI e do 
respectivo protocolo de autorização. Não será permitida a inclusão de valores ou qualificações que não constem 
do XML ou que alterem o conteúdo fiscal do documento eletrônico. 
• A chave de acesso impressa ou exibida deverá ser idêntica à chave da NF-e ABI. 
• O número, a série, o tipo, a finalidade, a modalidade, o detalhamento e a natureza da operação deverão 
refletir os respectivos campos do XML. 
• Transmitentes, adquirentes e dados do imóvel deverão reproduzir todos os participantes e informações 
constantes do documento, na ordem do número sequencial (tags: nTransmit e nAdquir). 
• Os valores de IBS e CBS apresentados deverão corresponder aos valores constantes nos grupos de 
tributação e totalização do XML. 
• O protocolo e a data/hora de autorização deverão corresponder ao retorno da autorização da NF-e ABI. 
6.7 Especificação dos campos 
As tabelas a seguir relacionam cada campo do DANFE-ABI ao respectivo campo do leiaute da NF-e ABI, com 
o formato de apresentação e a condição de preenchimento. 
Campo no DANFE-ABI Origem no XML Formato de apresentação Condição / Observação 
Bloco: Identificação da NF-e ABI 
Título — 
“DANFE-ABI” e “Documento Auxiliar da 
Nota Fiscal Eletrônica de Alienação de 
Bens Imóveis” 
Sempre. 
Emitente – nome emit/xNome (C04) Texto, em destaque Sempre. O nome fantasia (emit/xFant) poderá 
ser apresentado abaixo. 
Emitente – CNPJ/CPF emit/CNPJ (C02) ou emit/CPF (C03) Máscara de CNPJ ou CPF (item 6.1) Sempre. 
Emitente – endereço emit/enderEmit: xLgr, nro, xCpl, xBairro, 
xMun, UF e CEP (C07 a C14) Texto; CEP 99999-999 Campos informados no XML. 
Emitente – telefone emit/enderEmit/fone (C17) (99) 9999-9999 ou (99) 99999-9999 Quando informado. 
Número ide/nNF (B06) 000.000.000 Sempre. 
Série ide/serie (B05) 000 Sempre. 
Folha — (calculado) FOLHA n/t Sempre. 
Código de barras Chave de acesso (infNFeABI/@Id sem o 
literal “NFeABI” – A03) Code 128 (item 6.3) Sempre. 
Chave de acesso infNFeABI/@Id sem o literal “NFeABI” 
(A03) 11 blocos de 4 caracteres Sempre. 
Protocolo de autorização de uso protNFeABI/infProt/nProt e dhRecbto Número do protocolo – DD/MM/AAAA 
HH:MM:SS 
Na contingência off-line antes da autorização 
(tpEmis=9): mensagem do item 6.2. 
Data e hora de emissão ide/dhEmi (B07) DD/MM/AAAA HH:MM:SS Sempre. 
Tipo do documento ide/tpNF (B08) Código – descrição Sempre. 
Finalidade ide/finNFe (B18) Código – descrição (ex.: 1 – NF-e normal) Sempre. 
Modalidade da operação ide/gModNat/modOper (B11) Código – descrição Sempre. 
Detalhamento da operação ide/gModNat/detOper (B13) Código – descrição Quando informado. 
Natureza da operação ide/gModNat/natOper (B12) Código – descrição Sempre. 
Tipo do emitente emit/tpEmit (C18) Código – descrição Sempre. 
Tipo de pagamento ide/tpPagAnt (B18a) Código – descrição Quando informado; caso contrário, “—”.

## Página 40

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 40 / 
43 
 
 
Campo no DANFE-ABI Origem no XML Formato de apresentação Condição / Observação 
NF-e ABI referenciada ide/NFref/refNFeABI (BA02) Chaves em 11 blocos de 4 caracteres, uma 
por linha 
Quando informado; apresentar no quadro 
Informações complementares, com o título “NF-
e ABI REFERENCIADA”. 
NF-e ABI de pagamento 
antecipado gPagAntecipado/chNFePagAnt (BB02) Chaves em 11 blocos de 4 caracteres, uma 
por linha 
Quando tpPagAnt=2; apresentar no quadro 
Informações complementares, com o título “NF-
e ABI DE PAGAMENTO ANTECIPADO”. 
Contingência ide/gCont/dhCont (B22) e xJust (B23) DD/MM/AAAA HH:MM:SS – justificativa Quando tpEmis=9; no quadro Informações 
complementares. 
Bloco: Transmitentes (uma linha por ocorrência do grupo transmit – E01) 
Nº transmit/@nTransmit (E01a) Numérico Sempre que houver o grupo. 
CPF/CNPJ transmit/CNPJ (E03) ou transmit/CPF 
(E04) Máscara de CPF ou CNPJ Sempre que houver o grupo. 
Nome / Razão social transmit/xNome (E05) Texto Sempre que houver o grupo. 
Proporção transmitida transmit/pTransIndiv (E18) 999,9999% Quando tpNF=1; caso contrário, “—”. 
Contribuinte IBS/CBS transmit/indContrib (E19) Código – descrição Quando informado. 
Declarante transmit/indDeclarante (E02) Sim / Não Quando informado; caso contrário, “—”. 
Bloco: Adquirentes (uma linha por ocorrência do grupo adquirente – F01) 
Nº adquirente/@nAdquir (F01a) Numérico Sempre que houver o grupo. 
CPF/CNPJ adquirente/CNPJ (F03) ou 
adquirente/CPF (F04) Máscara de CPF ou CNPJ Sempre que houver o grupo. 
Nome / Razão social adquirente/xNome (F05) Texto Sempre que houver o grupo. 
Percentual de aquisição adquirente/pAquisicao (F18) 999,9999% Quando informado (tpNF=1 e modOper=2); caso 
contrário, “—”. 
Contribuinte IBS/CBS adquirente/indContrib (F19) Código – descrição Quando informado. 
Declarante adquirente/indDeclarante (F02) Sim / Não Quando informado; caso contrário, “—”.  
Campo no DANFE-ABI Origem no XML Formato de apresentação Condição / Observação 
Bloco: Identificação do imóvel (grupo imovel – G01) 
Tipo do imóvel imovel/tipo (G02) Código – descrição (1 – Urbano; 2 – Rural) Sempre que houver o grupo. 
Espécie do imóvel imovel/espImovel (G09) Código – descrição Sempre que houver o grupo. 
Descrição (outras espécies) imovel/xOutrosEspecies (G10) Texto Quando espImovel=99. 
Enquadramento do imóvel imovel/enquadramento (G11) Código – descrição (Tabela de códigos da 
NF-e ABI) Quando informado. 
Área total do imóvel imovel/areaTotal (G24) 9.999.999,99 Quando informado. 
Unidade de medida imovel/uAreaTotal (G25) m2 – Metro quadrado; ha – Hectares Quando informado. 
Matrícula ou transcrição imovel/matricTransc (G27) Texto Quando informado. 
Cartório de Registro de Imóveis imovel/cartorioRegistro (G26) Texto Quando informado. 
CIB imovel/cadastro/cCIB (G04) Texto Quando informado. 
IPTU imovel/cadastro/nIptu (G06) Texto Quando indIPTU=1; caso contrário, “—”. 
INCRA imovel/cadastro/nIncra (G08) Texto Quando indIncra=1; caso contrário, “—”. 
RIP imovel/cadastro/nRIP (G08b) Texto Quando indRIP=1; caso contrário, “—”. 
Logradouro, número, 
complemento, bairro, 
município/UF e CEP 
imovel/enderImovel: xLgr, nro, xCpl, 
xBairro, xMun, UF e CEP (G13 a G20) Texto; CEP 99999-999 Campos informados no XML. 
Observações sobre o local imovel/obsLocalImovel (G23) Texto Quando informado, em linha adicional do bloco. 
Bloco: Informações da operação (grupo infOper – H01) 
Proporção transmitida infOper/pTransImovel (H02) 999,9999% Quando informado. 
Valor da operação infOper/vTotalOperacao (H03) R$ 9.999.999.999.999,99 Sempre que houver o grupo. 
Instrumento infOper/instrumento/tpInstrumento 
(H18) e xOutrosInst (H19) 
Código – descrição; texto quando 
tpInstrumento=99 Sempre que houver o grupo. 
Data do instrumento infOper/instrumento/dtInstrumento 
(H20) DD/MM/AAAA Sempre que houver o grupo. 
Permuta com torna infOper/indTorna (H04) Sim / Não Quando informado. 
Valor da torna infOper/gTorna/vTorna (H06) R$ 9.999,99 Quando indTorna=1. 
Imóveis transmitidos junto com a 
torna infOper/gTorna/imovelTorna (H07) Tipo, espécie, matrícula e endereço de 
cada imóvel 
Quando informado; no quadro Informações 
complementares ou em folha adicional. 
Redutor de ajuste do imóvel infOper/gRedAjusteImovel/vRedAjusteIm
ovel (H15) R$ 9.999,99 Quando houver o grupo gRedAjusteImovel. 
Redutor social infOper/indRedSocial (H16) e vRedSocial 
(H16a) Sim / Não; R$ 9.999,99 Quando informado. 
Incorporação / loteamento; CNPJ 
do empreendimento; CIB da 
obra; CNO 
infOper/gIncorpLote: indIncorpLote 
(H09), CNPJempImob (H10), cCIBObra 
(H10a) e CNO (H10b) 
Sim / Não; máscara de CNPJ; texto Quando houver o grupo gIncorpLote. 
Intermediação / corretagem 
infOper/indIntermedCorret (H21) e 
gIntermedCorret: CNPJ ou CPF, xNome e 
vCorretagem (H24 a H27) 
Sim / Não; CPF/CNPJ, nome e valor Quando informado, em linha adicional do bloco. 
Bloco: Pagamento inicialmente previsto (grupo pag – Y01)

## Página 41

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 41 / 
43 
 
 
Campo no DANFE-ABI Origem no XML Formato de apresentação Condição / Observação 
Nº; tipo; descrição; valor pag/detPagImovel: nDetPag, tPag, xPag e 
vPag (Y02a a Y05) 
Numérico; código – descrição; texto; R$ 
9.999,99 
Quando houver o grupo detPagImovel; uma 
linha por ocorrência. 
Nº; tipo de parcelas; quantidade; 
observações 
pag/detPagIncorpLote: nDetPag, tParcela, 
nParcela e xParcela (Y06a a Y09) Numérico; texto; numérico; texto Quando houver o grupo detPagIncorpLote; uma 
linha por ocorrência. 
Bloco: Cálculo do IBS e da CBS (valores do declarante – grupo gInfTrib – U01) 
CST / cClassTrib gInfTrib/IBSCBS/CST (U07) e cClassTrib 
(U08) 000 / 000000 Sempre que houver o grupo. 
Valor da operação IBSCBS/gIBSCBS/vOperacIndiv (U10) 9.999,99 Quando houver o grupo gIBSCBS. 
Valor da torna gIBSCBS/vTornaIndiv (U11) 9.999,99 Quando informado, em linha adicional. 
Redutor de ajuste / Redutor 
social 
gIBSCBS/vRedAjusteIndiv (U12) e 
vRedSocialIndiv (U13) 9.999,99 Quando informado; caso contrário, “0,00”. 
Base de cálculo gIBSCBS/vBC (U14) 9.999,99 Quando houver o grupo gIBSCBS. 
Alíquota e valor do IBS UF gIBSUF/pIBSUF (U16) e vIBSUF (U20) 999,9999% / 9.999,99 Idem. Havendo redução, apresentar a alíquota 
efetiva (gRed/pAliqEfet – U19). 
Alíquota e valor do IBS Municipal gIBSMun/pIBSMun (U22) e vIBSMun 
(U26) 999,9999% / 9.999,99 Idem (pAliqEfet – U25). 
Alíquota e valor da CBS gCBS/pCBS (U28) e vCBS (U32) 999,9999% / 9.999,99 Idem (pAliqEfet – U31). 
Compra governamental gInfTrib/gCompraGov: tpEnteGov (U03), 
pRedutor (U04) e tpOperGov (U05) Código – descrição; 999,9999% Quando houver o grupo, em linha adicional do 
bloco. 
Estorno de crédito IBSCBS/gEstornoCred: vIBSEstCred (U41) 
e vCBSEstCred (U42) 9.999,99 Quando houver o grupo, em linha adicional do 
bloco. 
Pagamento antecipado 
gInfPagAntecip: vPagAntecip, 
dtPagAntecip e CNPJempImob (U09b a 
U09e) 
R$ 9.999,99; DD/MM/AAAA; máscara de 
CNPJ 
Quando houver o grupo, em linha adicional do 
bloco. 
Valor total do IBS total/tribTot/vIBSUF (W08) + vIBSMun 
(W09) R$ 9.999,99 Quando houver o grupo total. 
Valor total da CBS total/tribTot/vCBS (W10) R$ 9.999,99 Quando houver o grupo total. 
Valor total da NF-e ABI total/vNF (W11) R$ 9.999,99, em destaque Quando houver o grupo total. vNF = 
vOperacIndiv + vIBSUF + vIBSMun + vCBS. 
Bloco: Dados adicionais 
Informações complementares infAdic/infCpl (Z03) e obsCont: xCampo e 
xTexto (Z05 e Z06) Texto livre; “xCampo: xTexto” 
Quando informado. Recebe também as 
mensagens do item 6.2 e as chaves 
referenciadas. 
Reservado ao Fisco infAdic/infAdFisco (Z02) e obsFisco: 
xCampo e xTexto (Z08 e Z09) Texto livre; “xCampo: xTexto” Quando informado. 
Consulta via QR Code infNFeSupl/qrCode (ZX02) Imagem QR Code (itens 5.5 e 6.4) Sempre. 
URL de consulta infNFeSupl/urlChave (ZX03) Texto, abaixo do QR Code Sempre.  
6.8 NF-e ABI do Tipo de Documento Fiscal “2=Transição” 
A NF-e ABI com Tipo de Documento Fiscal igual a “2=Transição” (tag: ide/tpNF=2) não é emitida por operação 
de alienação: é emitida de forma unificada sobre a receita mensal ou a receita bruta enquadrada nos regimes 
opcionais dos arts. 485 ou 486 da LC 214/2025, sem identificação de transmitentes, adquirentes ou imóvel. Por 
não se destinar a acompanhar operação nem a instruir o registro de imóvel, a NF-e ABI de transição não possui 
DANFE-ABI. 
• O Formato de Impressão do DANFE (tag: ide/tpImp) deverá ser informado obrigatoriamente com “0=Sem 
geração de DANFE” (regra de validação B09-10, código 1036). 
• O grupo de informações suplementares (tag: infNFeSupl), com as tags qrCode e urlChave, permanece 
obrigatório, e a situação do documento será verificada pela consulta pública por chave de acesso ou pelo 
arquivo XML autorizado. 
• Não será admitida a geração de representação gráfica da NF-e ABI de transição com a denominação 
“DANFE-ABI” ou em leiaute que possa ser confundido com o DANFE-ABI das operações de alienação.

## Página 42

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 42 / 
43 
 
 
6.9 Modelo de referência 
O modelo a seguir ilustra a disposição dos blocos e campos do DANFE-ABI em formato retrato (tpImp=1) de uma NF-e ABI do Tipo “1=Completo”. Os 
dados são fictícios. 
IDENTIFICAÇÃO DA NF-E ABI 
EMITENTE 
INCORPORADORA EXEMPLO ABI LTDA 
Rodovia Contorno Leste BR-116, 8849 – Costeira 
São José dos Pinhais – PR – CEP 83015-162 
Fone: (41) 3333-3333 
CNPJ: 12.ABC.345/01DE-35 
DANFE-ABI 
Documento Auxiliar da Nota Fiscal 
Eletrônica de Alienação de Bens Imóveis 
Nº 000.000.123 
SÉRIE 001 
FOLHA 1/1 
 
CHAVE DE ACESSO 
4126 1012 ABC3 4501 DE35 7700 1000 0001 2310 1234 5674 
Consulta de autenticidade no Portal da NF-e ABI, pela chave de 
acesso ou pela leitura do QR Code, em 
www.fazenda.pr.gov.br/nfeabi 
PROTOCOLO DE AUTORIZAÇÃO DE USO 
141260000012345 – 16/10/2026 10:15:32 
DATA E HORA DE EMISSÃO 
16/10/2026 10:12:05 
TIPO DO DOCUMENTO 
1 – Completo 
FINALIDADE 
1 – NF-e normal 
MODALIDADE DA OPERAÇÃO 
04 – Permuta 
DETALHAMENTO DA OPERAÇÃO 
01 – Promessa / compromisso de compra e 
venda 
TIPO DO EMITENTE 
01 – Vendedor, Transmitente ou Cedente 
NATUREZA DA OPERAÇÃO 
13 – Permuta envolvendo exclusivamente bens imóveis (com ou sem torna) 
TIPO DE PAGAMENTO 
— 
TRANSMITENTES 
Nº CPF/CNPJ NOME / RAZÃO SOCIAL PROPORÇÃO 
TRANSMITIDA 
CONTRIBUINTE IBS/CBS DECLARANTE 
1 12.ABC.345/01DE-35 INCORPORADORA EXEMPLO ABI LTDA 60,0000% 1 – Regime regular Sim 
2 123.456.789-09 JOÃO DA SILVA 30,0000% 0 – Não contribuinte Não 
3 98.XYZ.765/0001-10 PARTICIPAÇÕES EXEMPLO S.A. 10,0000% 1 – Regime regular Não 
ADQUIRENTES 
Nº CPF/CNPJ NOME / RAZÃO SOCIAL PERCENTUAL DE 
AQUISIÇÃO 
CONTRIBUINTE IBS/CBS DECLARANTE 
1 987.654.321-00 MARIA DE SOUZA 50,0000% 0 – Não contribuinte — 
2 111.222.333-96 CARLOS PEREIRA 50,0000% 0 – Não contribuinte — 
IDENTIFICAÇÃO DO IMÓVEL 
TIPO DO IMÓVEL 
2 – Rural 
ESPÉCIE DO IMÓVEL 
99 – Outros 
DESCRIÇÃO (OUTRAS ESPÉCIES) 
Gleba rural com benfeitorias 
ENQUADRAMENTO DO IMÓVEL 
01 – Imóvel residencial novo 
ÁREA TOTAL DO IMÓVEL 
1.250,50 
UNIDADE DE MEDIDA 
ha – Hectares 
MATRÍCULA OU TRANSCRIÇÃO 
123.456 
CARTÓRIO DE REGISTRO DE IMÓVEIS 
1º Serviço de Registro de Imóveis de Curitiba/PR 
CIB 
CIB123456789 
IPTU 
IPTU202600001 
INCRA 
INCRA123456 
RIP 
— 
LOGRADOURO 
Estrada Municipal Rural 
NÚMERO 
SN 
COMPLEMENTO 
Lote 12 
BAIRRO / LOCALIDADE 
Zona Rural 
MUNICÍPIO / UF 
Curitiba – PR 
CEP 
82000-000 
INFORMAÇÕES DA OPERAÇÃO 
PROPORÇÃO TRANSMITIDA 
100,0000% 
VALOR DA OPERAÇÃO 
R$ 1.500.000,00 
INSTRUMENTO 
Contrato particular 
DATA DO INSTRUMENTO 
01/10/2026 
PERMUTA COM TORNA 
Sim 
VALOR DA TORNA 
R$ 50.000,00 
REDUTOR DE AJUSTE DO IMÓVEL 
R$ 400.000,00 
REDUTOR SOCIAL 
Não 
INCORPORAÇÃO / LOTEAMENTO 
Não 
CNPJ DO EMPREENDIMENTO 
— 
CIB DA OBRA 
— 
CNO 
— 
CÁLCULO DO IBS E DA CBS (DECLARANTE) 
CST 
000 
CCLASSTRIB 
000001 
VALOR DA OPERAÇÃO 
900.000,00 
REDUTOR DE AJUSTE 
240.000,00 
REDUTOR SOCIAL 
0,00 
BASE DE CÁLCULO 
660.000,00 
ALÍQ. IBS UF 
0,1000% 
VALOR IBS UF 
660,00 
ALÍQ. IBS MUN. 
0,0000% 
VALOR IBS MUN. 
0,00 
ALÍQ. CBS 
0,9000% 
VALOR CBS 
5.940,00 
VALOR TOTAL DO IBS 
R$ 660,00 
VALOR TOTAL DA CBS 
R$ 5.940,00 
VALOR TOTAL DA NF-E ABI 
R$ 906.600,00 
DADOS ADICIONAIS 
INFORMAÇÕES COMPLEMENTARES 
Imóvel objeto da matrícula nº 123.456. 
Documento de exemplo – sem valor fiscal. 
CONSULTA VIA QR CODE 
 
Consulte pela chave de acesso em: 
www.fazenda.pr.gov.br/nfeabi/consulta 
RESERVADO AO FISCO

## Página 43

Nota Fiscal Eletrônica de Alienação de Bens Imóveis 
Nota Técnica 2026.001 - Ajustes no Leiaute e nas Regras de Validação  da NF-e ABI – versão 1.00 
 
Página 43 / 43 
1 
 
 
6.10 Modelo de referência – formato paisagem 
Modelo do DANFE-ABI em formato paisagem (tpImp=2), com as mesmas informações do item 6.9. Transmitentes e adquirentes são apresentados lado a lado, e os códigos de contribuinte do IBS/CBS são 
apresentados apenas pelo código. Os dados são fictícios. 
IDENTIFICAÇÃO DA NF-E ABI 
EMITENTE 
INCORPORADORA EXEMPLO ABI LTDA 
Rodovia Contorno Leste BR-116, 8849 – Costeira 
São José dos Pinhais – PR – CEP 83015-162 
Fone: (41) 3333-3333 
CNPJ: 12.ABC.345/01DE-35 
DANFE-ABI 
Documento Auxiliar da Nota Fiscal Eletrônica de Alienação de Bens 
Imóveis 
Nº 000.000.123 
SÉRIE 001 
FOLHA 1/1 
 
CHAVE DE ACESSO 
4126 1012 ABC3 4501 DE35 7700 1000 0001 2310 1234 5674 
Consulta de autenticidade no Portal da NF-e ABI, pela chave de acesso ou pela leitura do QR Code, em 
www.fazenda.pr.gov.br/nfeabi 
PROTOCOLO DE AUTORIZAÇÃO DE USO 
141260000012345 – 16/10/2026 10:15:32 
DATA E HORA DE EMISSÃO 
16/10/2026 10:12:05 
TIPO DO DOCUMENTO 
1 – Completo 
FINALIDADE 
1 – NF-e normal 
TIPO DO EMITENTE 
01 – Vendedor, Transmitente ou Cedente 
TIPO DE PAGAMENTO 
— 
MODALIDADE DA OPERAÇÃO 
01 – Alienação em geral 
DETALHAMENTO DA OPERAÇÃO 
01 – Promessa / compromisso de compra e venda 
NATUREZA DA OPERAÇÃO 
13 – Permuta envolvendo exclusivamente bens imóveis (com ou sem torna) 
TRANSMITENTES E ADQUIRENTES 
TRANSMITENTES ADQUIRENTES 
Nº CPF/CNPJ NOME / RAZÃO SOCIAL PROPORÇÃO 
TRANSMITIDA 
CONTRIB. DECL. Nº CPF/CNPJ NOME / RAZÃO SOCIAL PERCENTUAL DE 
AQUISIÇÃO 
CONTRIB. DECL. 
1 12.ABC.345/01DE-35 INCORPORADORA EXEMPLO ABI 
LTDA 
60,0000% 1 Sim 1 987.654.321-00 MARIA DE SOUZA 50,0000% 0 — 
2 123.456.789-09 JOÃO DA SILVA 30,0000% 0 Não 2 111.222.333-96 CARLOS PEREIRA 50,0000% 0 — 
3 98.XYZ.765/0001-10 PARTICIPAÇÕES EXEMPLO S.A. 10,0000% 1 Não       
IDENTIFICAÇÃO DO IMÓVEL 
TIPO DO IMÓVEL 
2 – Rural 
ESPÉCIE DO IMÓVEL 
99 – Outros 
DESCRIÇÃO (OUTRAS ESPÉCIES) 
Gleba rural com benfeitorias 
ENQUADRAMENTO DO IMÓVEL 
01 – Imóvel residencial novo 
ÁREA TOTAL DO IMÓVEL 
1.250,50 
UNIDADE DE MEDIDA 
ha – Hectares 
MATRÍCULA OU TRANSCRIÇÃO 
123.456 
CARTÓRIO DE REGISTRO DE IMÓVEIS 
1º Serviço de Registro de Imóveis de Curitiba/PR 
CIB 
CIB123456789 
IPTU 
IPTU202600001 
INCRA 
INCRA123456 
RIP 
— 
LOGRADOURO 
Estrada Municipal Rural 
NÚMERO 
SN 
COMPLEMENTO 
Lote 12 
BAIRRO / LOCALIDADE 
Zona Rural 
MUNICÍPIO / UF 
Curitiba – PR 
CEP 
82000-000 
INFORMAÇÕES DA OPERAÇÃO 
PROPORÇÃO TRANSMITIDA 
100,0000% 
VALOR DA OPERAÇÃO 
R$ 1.500.000,00 
INSTRUMENTO 
Contrato particular 
DATA DO INSTRUMENTO 
01/10/2026 
PERMUTA C/ TORNA 
Sim 
VALOR DA TORNA 
R$ 50.000,00 
REDUTOR DE AJUSTE DO IMÓVEL 
R$ 400.000,00 
REDUTOR SOCIAL 
Não 
INCORPORAÇÃO / LOTEAMENTO 
Não 
CNPJ DO EMPREENDIMENTO 
— 
CIB DA OBRA 
— 
CNO 
— 
INTERMEDIAÇÃO / CORRETAGEM 
Não 
CÁLCULO DO IBS E DA CBS (DECLARANTE) 
CST 
000 
CCLASSTRIB 
000001 
VALOR DA OPERAÇÃO 
900.000,00 
REDUTOR DE AJUSTE 
240.000,00 
REDUTOR SOCIAL 
0,00 
BASE DE CÁLCULO 
660.000,00 
ALÍQ. IBS UF 
0,1000% 
VALOR IBS UF 
660,00 
ALÍQ. IBS MUN. 
0,0000% 
VALOR IBS MUN. 
0,00 
ALÍQ. CBS 
0,9000% 
VALOR CBS 
5.940,00 
VALOR TOTAL DO IBS 
R$ 660,00 
VALOR TOTAL DA CBS 
R$ 5.940,00 
VALOR TOTAL DA NF-E ABI 
R$ 906.600,00 
DADOS ADICIONAIS 
INFORMAÇÕES COMPLEMENTARES 
Imóvel objeto da matrícula nº 123.456. 
Documento de exemplo – sem valor fiscal. 
CONSULTA VIA QR CODE 
 
Consulte pela chave de acesso em: www.fazenda.pr.gov.br/nfeabi/consulta 
RESERVADO AO FISCO
