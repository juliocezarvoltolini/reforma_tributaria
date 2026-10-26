---
id: nf3e-nf3e-nota-tecnica-2026-001-rtc-vinculacaopgto-v1-01
titulo: Nota Técnica 2026.001 v.1.01 - Publicada em 02/03/2026 - Publicada em 02/03/2026
tipo: nota.tecnica
versao: '1.01'
data: '2026-03-02'
documento_fiscal: NF3e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=8jS1eZoTbbs=
arquivo_original: fontes/acervo/nf3e-nf3e-nota-tecnica-2026-001-rtc-vinculacaopgto-v1-01.pdf
sha256_original: 47a906e89dfcf31c14718bb33535e8d6808630945ea0c3e9b9819f132a3c8c90
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: d4383bac2d6c39dc4519dd39c34cd42065bee06279537c982f3cea99fdb3bb1d
---

## Página 1

Projeto Nota Fiscal de Energia 
Elétrica Eletrônica 
 
Nota Técnica 2026.001 – Vinculação com a transação de 
pagamento do DFe 
 
Versão 1.01 de 27 de fevereiro de 2026

## Página 2

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 2 / 9 
 
Sumário  
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 4 
2 Informação da vinculação da transação de pagamento no DFe ...................................... 6 
Regras de Validação...........................................................................................................6 
3 Evento de vinculação da transação de pagamento no DFe ............................................. 7 
Validação das Regras Específicas do Evento .....................................................................7 
Final do Processamento .....................................................................................................8 
4 Evento de Cancelamento da Vinculação de Pagamento ................................................. 9 
Validação das Regras Específicas do Evento .....................................................................9 
Final do Processamento .....................................................................................................9

## Página 3

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 3 / 9 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Criação do grupo de informações da vinculação da transação de 
pagamento do DFe 
 Criação do evento de informações da vinculação da transação de 
pagamento do DFe 
 Criação do evento de cancelamento da vinculação da transação de 
pagamento do DFe 
  
1.01  Equalização dos códigos de meios de pagamento conforme tabela 
utilizada na NFe 
06 abril 2026 04 maio 2026 
 
A implantação do split payment está prevista para ocorrer a partir de 2027. Dessa forma, os 
campos mencionados nesta Nota Técnica têm caráter preparatório e visam permitir que os 
sistemas das administrações tributárias, emissores de documentos fiscais e demais atores 
envolvidos possam planejar, desenvolver e testar, com a devida antecedência, as adaptações 
necessárias. 
  
Considerações importantes: 
 Não há exigência de preenchimento ou uso dos campos de split payment em 2026 no 
ambiente de produção das empresas. 
 A ativação efetiva desses campos ocorrerá somente quando o mecanismo de split 
payment entrar em vigência, prevista para 2027. 
 Orientações adicionais e cronogramas serão divulgados oportunamente por meio dos 
canais oficiais do CGIBS e da RFB.

## Página 4

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 4 / 9 
 
1 Introdução 
A vinculação entre DFe e transação financeira sujeita ao split payment é estritamente necessária para a correta 
apuração dos débitos do fornecedor e concessão de créditos ao adquirente. 
No split payment, há duas formas de o contribuinte indicar a vinculação entre o documento fiscal e a transação 
financeira sujeita ao split payment: 
i. transmitindo a chave do documento fiscal ao prestador de serviço de pagamento, no início da transação 
financeira, ou 
ii. informando os dados da transação financeira em campos ou evento de DFe. 
Esta nota técnica detalha a forma de vinculação, por meio da inserção de dados da transação financeira, em 
campos do documento fiscal ou evento vinculado a este. 
Atenção: O vínculo indicado pelo contribuinte não necessariamente representa um pagamento efetuado e 
liquidado. Indica uma expectativa de pagamento que pode ou não se concretizar. Por exemplo: um boleto pode 
ser emitido e não pago.  
Nas transações sujeitas ao procedimento padrão do split payment e originadas por fornecedor/recebedor, a 
vinculação se faz necessária antes mesmo da liquidação financeira, com o propósito de viabilizar o split payment 
superinteligente. Cumpre destacar que, quanto mais tempo o fornecedor/recebedor demorar para reportar o 
vínculo entre DFe e transação financeira, menor serão as chances de o split superinteligente ser executado. Em 
caso de impossibilidade de execução do split superinteligente, será executado o split inteligente offline, com 
posterior devolução de valores retidos a maior no prazo de 3 (três) dias úteis. 
São exemplos, não exaustivos, de possíveis cenários de vinculação por meio da inserção de dados da transação 
financeira em campos de DFe ou evento: 
Ex. 1. O fornecedor emite um boleto para uma empresa adquirente, antes da emissão do DFe. Uma vez que o 
boleto foi emitido sem chave de DFe, a vinculação fica inicialmente pendente. Após a emissão do boleto, o 
fornecedor emite o DFe preenchendo os campos relativos à transação financeira, viabilizando assim a vinculação.

## Página 5

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 5 / 9 
 
Ex. 2. O fornecedor emite um DFe. Em seguida, o fornecedor emite QR code Pix dinâmico para a empresa 
adquirente, informando valores de IBS e CBS, mas sem a chave do DFe previamente emitido (nos termos do § 2º-
A do Art. 32 da LC 214/2025, com redação dada pela LC 227/2026). O vínculo fica inicialmente pendente, em 
razão da ausência da chave DFe na transação de pagamento. Para finalmente efetivar a vinculação, o fornecedor 
emite evento atrelado ao DFe, com os dados do Pix dinâmico. 
  
Ex. 3. O fornecedor emite um DFe antes do início da transação financeira. A empresa adquirente efetua o 
pagamento via TED informando a chave do DFe, porém comete um erro neste preenchimento, o que impede a 
correta vinculação entre transação financeira e DFe. A fim de resolver o problema, o fornecedor emite um evento 
atrelado ao DFe com os dados da transação financeira.

## Página 6

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 6 / 9 
 
2 Informação da vinculação da transação de pagamento no DFe 
Este grupo de informações deverá ser informado sempre que a transação de pagamento for iniciada antes da 
emissão do DFe. Exemplos: boleto gerado antes da emissão do DFe; QR Code dinâmico Pix gerado antes da 
emissão do DFe. Neste caso, o DFe deverá reportar os dados das transações financeiras previamente iniciadas, 
ainda que estejam pendentes de efetivo pagamento e liquidação. 
  #  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# pgtoVinc G infNF3e - 0-1 - Grupo de informações da vínculação com a 
transação de pagamento 
1 pgto E pgtoVinc G 1-99 - Dados de cada pagamento previsto para o DFe 
2 nPag A pgto N 1-1 3 Atributo numerador único de cada ocorrência de 
pagamento 
3 idTransacao A pgto C 1-1 2-35 Atributo Identificador específico da transação 
financeira, de acordo com a transação de 
pagamento. O próprio schema impede que se repita 
dentro do grupo 
4 tpMeioPgto E pgto N 1-1 2 Código do meio de pagamento utilizado 
Ver IT DFe 2026.001 que divulgará códigos que 
serão aceitos (conforme tabela nacional de Meios 
de Pagamento da NFe) 
5 CNPJReceb E pgto C 1-1 14 CNPJ completo do recebedor do pagamento 
(fornecedor, plataforma, ou outra entidade que 
receba o pagamento do adquirente).  
Observação: indicar o CNPJ responsável por 
receber dinheiro do adquirente na transação de 
pagamento. É possível que o CNPJ do recebedor 
seja diferente do CNPJ do fornecedor constante no 
documento fiscal. 
6 CNPJBasePSP E pgto C 1-1 8 CNPJ base da instituição financeira ou de 
pagamento utilizada pelo recebedor do pagamento 
(fornecedor, plataforma, ou outra entidade que 
receba o pagamento do adquirente). 
 
 
Regras de Validação 
# Regra de Validação Aplic. cStat Efeito Mensagem 
01 Se informado grupo de informações de vinculação com 
a transação de pagamento (grupo: gPgtoVinc), para 
cada ocorrência de pagamento vinculado: 
 
Validar o CNPJ do Recebedor do Pagamento (dígito de 
controle, zeros, validação CNPJ Alfanumérico) 
 
Observação: Informar na mensagem de rejeição qual 
o numerador do pagamento que ocorreu a rejeição 
Obrig. 1001 Rej. Rejeição: CNPJ do recebedor do pagamento 
inválido [nPag: XXX] 
02 Verificar se o código informado em tpMeioPgto é válido 
 
Observação: Os códigos válidos estarão publicados em 
Informe Técnico dos DFe de número 2006.001 e 
correspondem a codificação padronizada com a tabela 
de Meios de Pagamento da NFe publicada no Ambiente 
Nacional  
Obrig. 1003 Rej. Rejeição: Meio de pagamento inválido [nPag: XXX]

## Página 7

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 7 / 9 
 
3 Evento de vinculação da transação de pagamento no DFe 
Este evento deverá ser gerado pelo emitente do DFe sempre que se for vincular uma ou mais transações 
financeiras a um documento fiscal previamente autorizado. 
Obs.: É possível que a transação financeira vinculada esteja em situação iniciada, ainda pendente de pagamento 
e/ou liquidação (ex. boleto emitido ou QR code Pix gerado) 
 
Função: evento destinado ao atendimento de solicitações vinculação do pagamento do DFe. 
 
Autor do Evento: O autor do evento é o emissor do DFe. A mensagem XML do evento será assinada com o 
certificado digital que tenha o CNPJ base do Emissor  
 
Código do Tipo de Evento: 110300 
 
Schema XML: evVincPgto_v9.99.xsd 
  #  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
# evVincPgto Raiz detEvento G 1-1  Schema XML de validação do evento de 
vinculação da transação de pagamento com o 
DFe  - 110300 
1 descEvento E evVincPgto E 1-1 20 Descrição do Evento - “Vinculação Pagamento” 
2 nProt E evVincPgto E 1-1 15 Número do protocolo de autorização do DFe 
3 pgto E pgtoVinc G 1-1 - Dados de cada pagamento previsto para o DFe 
4 nPag A pgto N 1-1 3 Atributo numerador único de cada ocorrência de 
pagamento 
5 idTransacao A pgto C 1-1 2-35 Atributo Identificador específico da transação 
financeira, de acordo com a transação de 
pagamento. O próprio schema impede que se repita 
dentro do grupo 
6 tpMeioPgto E pgto N 1-1 2 Código do meio de pagamento utilizado 
Ver IT DFe 2026.001 que divulgará códigos que 
serão aceitos (conforme tabela nacional de Meios 
de Pagamento da NFe) 
7 CNPJReceb E pgto C 1-1 14 CNPJ completo do recebedor do pagamento 
(fornecedor, plataforma, ou outra entidade que 
receba o pagamento do adquirente).  
Observação: indicar o CNPJ responsável por 
receber dinheiro do adquirente na transação de 
pagamento. É possível que o CNPJ do recebedor 
seja diferente do CNPJ do fornecedor constante no 
documento fiscal. 
8 CNPJBasePSP E pgto C 1-1 8 CNPJ base da instituição financeira ou de 
pagamento utilizada pelo recebedor do pagamento 
(fornecedor, plataforma, ou outra entidade que 
receba o pagamento do adquirente). 
Validação das Regras Específicas do Evento 
# Regra de Validação Aplic. cStat Efeito Mensagem 
L01 Verificar se a UF da Chave de Acesso difere da 
UF do Web Service 
 
Obrig
. 
249 Rej. Rejeição: UF da Chave de Acesso diverge da UF 
autorizadora 
L02 Verificar se o nSeqEvento é maior que o valor 
permitido (1 a 999) 
Obrig
. 
636 Rej. Rejeição: O número sequencial do evento é 
maior que o permitido 
L03 Emitente deve estar habilitado na base de dados 
para emissão do DFe 
Obrig
. 
203 Rej. Rejeição: Emissor não habilitado para emissão 
de NF3e 
L04 Verificar se DFe já está cancelado. Obrig
. 
218 Rej. Rejeição: NF3e já está cancelado na base de 
dados da SEFAZ. 
[nProt:999999999999999][dhCanc: AAAA-MM-
DDTHH:MM:SS TZD]. 
L06 Verificar se DFe foi substituído 
 
Obrig
. 
224 Rej. Rejeição: NF3e já está substituído na base de 
dados da SEFAZ. 
[nProt:999999999999999][dhSubst: AAAA-MM-
DDTHH:MM:SS TZD]. 
L10 Verificar se número do Protocolo informado 
difere do número do Protocolo do DFe 
Obrig
. 
222 Rej. Rejeição: Protocolo de Autorização de Uso difere 
do cadastrado

## Página 8

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 8 / 9 
 
L11 Se informado grupo de informações de 
vinculação com a transação de pagamento 
(grupo: gPgtoVinc), para cada ocorrência de 
pagamento vinculado: 
 
Validar o CNPJ do Recebedor do Pagamento 
(dígito de controle, zeros, validação CNPJ 
Alfanumérico) 
 
Observação: Informar na mensagem de 
rejeição qual o numerador do pagamento que 
ocorreu a rejeição 
Obrig
. 
1001 Rej. Rejeição: CNPJ do recebedor do pagamento 
inválido [nPag: XXX] 
      
L12 Verificar se o código informado em tpMeioPgto é 
válido 
 
Observação: Os códigos válidos estarão 
publicados em Informe Técnico dos DFe de 
número 2006.001 e correspondem a codificação 
padronizada com a tabela de Meios de 
Pagamento da NFe publicada no Ambiente 
Nacional  
Obrig 1003 Rej. Rejeição: Meio de pagamento inválido 
[nPag: XXX] 
Final do Processamento 
 
Se o evento de vinculação de pagamento do DFe for homologado o status de retorno deverá ser cStat=135.

## Página 9

Projeto 
Projeto Nota Fiscal de Energia Elétrica Eletrônica 
NT 2026.001 v1.01 
 
 
Página 9 / 9 
 
4 Evento de Cancelamento da Vinculação de Pagamento 
Função: Evento para indicar o cancelamento de um evento de vinculação de pagamento do DFe nas ocasiões em que ocorrer 
erro na geração do evento. 
Autor do Evento: O autor do evento é o emissor do DFe. A mensagem XML do evento será assinada com o certificado digital 
que tenha o CNPJ base do Emissor. 
 
Código do Tipo de Evento: 110301 (Este evento exige existência do DFe em situação autorizado) 
 
Schema XML: evCancVincPGto_v9.99.xsd 
 
#  Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
IP01 evCancVincPgto G - - - - TAG raiz  
IP02 descEvento E IP01 C 1-1 44 Descrição do Evento: “Cancelamento da 
Vinculação do Pagamento”  
IP03 nProt E IP01 N 1-1 15 Informar o número do protocolo de autorização do 
DFe  
IP04 nProtVincPgto E IP01 N 1-1 15 Informar o número do protocolo de autorização do 
evento de vinculação de pagamento que será 
cancelado  
Validação das Regras Específicas do Evento 
# Regra de Validação Aplic. cStat Efeito Mensagem 
Q01 Verificar se a UF da Chave de Acesso difere da 
UF do Web Service 
 
Obrig
. 
249 Rej. Rejeição: UF da Chave de Acesso diverge da UF 
autorizadora 
Q02 Verificar se o nSeqEvento é maior que o valor 
permitido (1 a 999) 
Obrig
. 
636 Rej. Rejeição: O número sequencial do evento é 
maior que o permitido 
Q03 Emitente deve estar habilitado na base de 
dados para emissão do DFe 
Obrig
. 
203 Rej. Rejeição: Emissor não habilitado para emissão 
de NF3e 
Q04 Verificar se número do Protocolo informado 
difere do número do Protocolo do DFe 
Obrig
. 
222 Rej. Rejeição: Protocolo de Autorização de Uso difere 
do cadastrado 
Q05 Verificar se número do Protocolo do evento de 
vinculação de pgto a ser cancelado existe para 
o DFe e encontra-se na situação autorizado 
Obrig
. 
1002 Rej. Rejeição: Protocolo do evento a ser cancelado 
não existe, não está associado ao DFe ou já está 
cancelado 
Final do Processamento 
 
Se o evento de Cancelamento da vinculação do pagamento do DFe for homologado o status de retorno deverá ser cStat=135 e 
o evento cancelado passará a condição de anulado.
