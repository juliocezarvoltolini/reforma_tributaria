---
id: nfse-nota-tecnica-se-cgnfs-e-no-003
titulo: Nota Técnica SE/CGNFS-e nº 003
tipo: nota.tecnica
versao: '1.2'
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nt-003-1-2-se-cgnfse-novo-layout-rtc.pdf
arquivo_original: fontes/acervo/nfse-nota-tecnica-se-cgnfs-e-no-003.pdf
sha256_original: 2b88fd94638cb9a4dedcc8374220f013bd7a1131990364257a1e4e96be7812d7
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: d07f2b04235b3f582010443a6eb9d9c5fe23f908bcf59eb61d5ae7e687a25b3f
---

## Página 1

Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica 
de Padrão Nacional (SE/CGNFS-e) 
 
 
 
 
 
Projeto Reforma Tributária do Consumo – 
Adequações NFS-e 
 
 Nota Técnica Nº 003 – Versão 1.2 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
04 de julho de 2025

## Página 2

2 
 
Sumário 
 
1. Introdução ................................................................................................................................................. 3 
2. Layout NFS-e: Novos Grupos no Contexto da EC nº 132/2023 .................................................................. 4 
2.1 Novos Grupos na DPS da NFS-e ........................................................................................................ 6 
2.1.1 Grupo de Informações Relativas ao Destinatário ........................................................................ 7 
2.1.2 Grupo de Informações Relativas ao Adquirente .......................................................................... 8 
2.1.3 Grupo de Informações de Operações Relacionadas a Bens Imóveis, Exceto Obras .................... 9 
2.1.4 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS ......................................... 9 
2.1.4.1 (REMOVIDO)Grupo de Informações Específicas Relativas ao IBS Estadual ........................... 11 
2.1.4.2 (REMOVIDO)Grupo de Informações Específicas Relativas ao IBS Municipal ......................... 12 
2.1.4.3 (REMOVIDO)Grupo de Informações Específicas Relativas à CBS........................................... 12 
2.2 Novos Grupos na NFS-e .................................................................................................................. 13 
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS .......................................................... 13 
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS ........................................... 14 
2.2.3 Grupos Totalizadores ................................................................................................................. 15 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS ........................................................ 16 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS ....................................................... 16

## Página 3

3 
 
 
 
 
1. Introdução 
 
 Este documento contempla a terceira versão dos novos agrupamentos e campos opcionais do 
layout da Nota Fiscal de Serviço eletrônica – NFS-e padrão nacional relacionados à tributação do 
Imposto sobre Bens e Serviços – IBS e da Contribuição sobre Bens e Serviços – CBS incidentes nas 
operações de serviços, em atendimento às alterações previstas na Emenda Constitucional nº 132 de, 
20 de dezembro de 2023, que deu ensejo à Reforma Tributária do Consumo – RTC. Importante 
observar que esta nota técnica substitui as versões anteriores. 
 Os novos agrupamentos de campos foram inseridos a partir do layout atual da NFS-e, presente 
no documento “AnexoIV -LeiautesRN_ADN-SNNFSe_V1.00.02-Produção.xlsx”, aba “LEIAUTE 
NFS-e ADN” que consta na sessão de documentação técnica no Portal da NFS -e: 
https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica. 
 
 Importante esclarecer que o conjunto de campos apresentados neste documento é uma terceira 
versão, resultado de estudos técnicos realizados tomando como base o texto da Lei Complementar – 
LC nº 214, de 16 de janeiro de 2025 , e sua divulgação objetiva dar transparência aos  Estados, aos 
Municípios, às empresas prestadoras de serviço e de Tecnologia da Informação – TI e contribuintes 
para que possam se familiarizar com o novo padrão que deve rá vigorar a partir de janeiro de 2026. 
Os estudos técnicos permanecem e novas versões deverão ser publicadas nas próximas semanas com 
atualizações do layout proposto. 
 Para melhor compreensão dos agrupamentos que serão apresentados no próximo tópico desta 
Nota Técnica, a seguir é apresentada a modelagem do processo de emissão  da NFS-e. O emissor 
(prestador de serviços ) preenche a Declaração de Prestação de Serviço  (DPS) que será enviada à 
“Sefin Nacional”, responsável pela validação das informações, cálculo dos tributos e autorização da 
NFS-e. Caso as informações atendam aos requisitos, será gerada a NFS-e em formato XML com o 
destaque dos tributos devidos e que poderá ser acessada pelo emissor  e demais envolvidos na 
operação. É importante observar que a DPS é assinada e encapsulada no interior da nota gerada e que, 
dessa forma, há dois grupos de informações apresentados neste documento: um relativo à DPS com 
campos que serão informados pelo contribuinte e outro que, a partir dessas informações, terá campos 
calculados pela plataforma.

## Página 4

4 
 
 
 
 
 
Junto a esta nota técnica, foram também publicados dois anexos  na seção de documentação 
técnica do portal da NFS-e (https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica): 
 
• AnexoVI-LeiautesRN_RTC_IBSCBS-V1.00.01.xlsx 
Composto por três tabelas, este anexo possui o layout da NFS-e com os novos grupos 
referentes ao IBS e à CBS (“Leiaute DPS_NFS -e - RT”) e as primeiras regras de 
negócio do grupo “IBSCBS” da DPS (“RN DPS - RTC_IBSCBS”) e da NFS-e (“RN 
NFS-e - RTC_IBSCBS”); 
 
• AnexoVII-IndOp_IBSCBS_V1.00.00-.xlsx 
Composto por uma tabela com os códigos indicadores da operação que serão 
referenciados no campo “cIndOp” da DPS. A tabela foi baseada no art. 11 da Lei 
Complementar – LC Nº 214, de 16 de janeiro de 2025. 
 
2. Layout NFS-e: Novos Grupos no Contexto da EC nº 132/2023 
 
 Para melhor compreensão das informações disponibilizadas  nos layouts dispostos 
neste tópico, segue um breve glossário. 
• CAMINHO NO XML 
O XML (Extensible Markup Language) é uma linguagem de marcação utilizada para 
estruturar e armazenar dados em um formato legível por máquina  que obedece aos 
layouts dispostos neste documento e que possui regras a serem seguidas, em uma 
sequência pré-definida e ordenada. Esta coluna informa o path, ou caminho, ordenado 
em que as informações devem ser dispostas na formatação do XML.

## Página 5

5 
 
• CAMPO 
Nome do campo/informação que deve constar no XML. 
 
 
• ELE 
Elemento ou valor do campo que deve ser informado. Pode ser dos tipos: 
o ID: Campo identificador do documento; 
o E: Element (Elemento), atributo deve ser informado no campo; 
o G: Group (Grupo), tag que identifica um grupo de informações que será 
formado por elements (E), choice elements (CE) ou outros grupos; 
o CG: Choice Group (Grupo de Escolha), tag que identifica um grupo que deverá 
ser informado a depender da escolha do emitente; 
o CE: Choice Element  (Elemento de Escolha), elemento de uma lista pré -
determinada, a ser preenchida pelo emitente. 
 
• TIPO 
Tipo do campo que deve ser informado para a tag específica. Pode ser dos tipos: 
o N: Numérico; 
o C: Caractere; 
o D: Data. 
 
Nas tags G ou CG ( Group ou Choice Group ), como são apenas informações de 
agrupamento de campos, não há um tipo relacionado. 
 
• OCOR. 
Quantidade de ocorrências possíveis para o campo/tag. 
Por exemplo: 
o 0-1: A informação não é obrigatória e, caso seja informada, só será possível de 
ser informada uma única vez no documento; 
o 1-1: Informação obrigatória e que deverá ser informada apenas uma vez no 
documento; 
o 1-60: Informação obrigatória que deverá ser informada até, no máximo, 60 
vezes no documento.

## Página 6

6 
 
• TAM. 
  Tamanho da informação para o campo/tag. 
  Por exemplo: 
o 14: Campo de tamanho fixo com 14 caracteres ou números; 
o 1-150: Campo de tamanho variável, podendo possuir de 1 a 150 caracteres  ou 
números; 
o 1-3V2: Campo de tamanho variável, podendo possuir de 1 a 3 números mais duas 
casas decimais. 
 
Nas tags G ou CG ( Group ou Choice Group ), como são apenas informações de 
agrupamento de campos, não há um tamanho relacionado. 
 
• DESCRIÇÃO 
Descrição sucinta do que representa cada campo e como deve ser preenchido. 
 
 
2.1 Novos Grupos na DPS da NFS-e 
 
 Na DPS, foi criado o grupo IBSCBS (caminho NFSe/infNFSe/DPS/infDPS/). Neste grupo 
serão dispostos todos os subgrupos e informações relativas aos novos tributos: IBS  e CBS; e que 
deverão ser informados pelo contribuinte na emissão. Importante observar que os campos/tags/células 
listados abaixo em amarelo se referem a campos que foram modificados em relação à versão anterior, 
publicada na Nota Técnica SE/CGNFS-e nº 002, de 28 de fevereiro de 2025. 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/ IBSCBS G - 1-1 - Grupo de informações declaradas pelo emitente referentes ao 
IBS e à CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ finNFSe E N 1-1 1 
Indicador da finalidade da emissão de NFS-e  
 
0 = NFS-e regular 
1 = NFS-e de crédito 
2 = NFS-e de débito 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ indFinal  E N 1-1 1 
Indica operação de uso ou consumo pessoal.  
 
0=Não 
1=Sim 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ cIndOp E N 1-1 6 Código indicador da operação de fornecimento, conforme tabela 
“código indicador de operação” 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ tpEnteGov E N 0-1 1 
Tipo de ente governamental 
 
Para administração pública direta e suas autarquias e fundações:  
1 = União  
2 = Estado  
3 = Distrito Federal  
4 = Município 
9 = Outro 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ xTpEnteGov E C 0-1 100 Se tpEnteGov informado for igual a 9 = outro, este campo deve 
informar qual a descrição do ente. Exemplo: "Comitê Gestor do IBS".

## Página 7

7 
 
 
 
Algumas observações importantes acerca dos campos acima: 
1. O campo “cIndOp” se refere à tabela de indicador da operação publicada no ANEXO 
AnexoVII-IndOp_IBSCBS_V1.00.00-.xlsx; 
2. As notas de ajuste, de crédito e de débito, estão em processo de estudos e atualizações 
serão publicadas nas próximas notas técnicas. Portanto, a menção a essas notas de ajuste 
na descrição do campo “finNFSe” tem, por enquanto, o único objetivo de esclarecer a 
necessidade da criação desse campo. 
 
2.1.1 Grupo de Informações Relativas ao Destinatário 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ dest G - 0-1 - Grupo de informações relativas ao Destinatário 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ CNPJ CE N 1-1 14 Número da inscrição no Cadastro Nacional de 
Pessoa Jurídica (CNPJ) do destinatário de serviço 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ CPF CE N 1-1 11 Número da inscrição no Cadastro Nacional de 
Pessoa Física (CPF) do destinatário do serviço 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ NIF CE C 1-1 40 Número de identificação fiscal fornecido por órgão 
de administração tributária no exterior 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ cNaoNIF CE N 1-1 1 
Motivo para não informação do NIF: 
  
 0 - Não informado na nota de origem; 
 1 - Dispensado do NIF; 
 2 - Não exigência do NIF; 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ CAEPF E N 0-1 14 Número do Cadastro de Atividade Econômica da 
Pessoa Física (CAEPF) do destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ xNome E C 1-1 150 Nome / Nome Empresarial do destinatário 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ end G - 0-1 - Grupo de informações do endereço do destinatário 
do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ endNac CG - 1-1 - Grupo de informações do endereço nacional. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endNac/ cMun E N 1-1 7 
Código do município do endereço do destinatário do 
serviço. 
  (Tabela do IBGE)  
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endNac/ CEP E C 1-1 8 
Código numérico do Endereçamento Postal nacional 
(CEP)  
  do endereço do destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ endExt CG - 1-1 - Grupo de informações do endereço no exterior. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endExt/ cPais E C 1-1 2 
Código do país do endereço do destinatário do 
serviço. 
  (Tabela de Países ISO) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endExt/ cEndPost E C 1-1 1-11 Código alfanumérico do Endereçamento Postal no 
exterior do destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ indPessoas E N 1-1 1 
A respeito do Destinatário dos serviços: 
 
0 – O tomador identificado na NFS-e é o adquirente e o destinatário do 
fornecimento (tomador = adquirente = destinatário); 
1 – O tomador e o adquirente são a mesma pessoa, mas o destinatário 
é uma pessoa física ou jurídica ou equiparada diversa do indicado 
como tomador/adquirente ou se trata de um estabelecimento do 
adquirente diferente do indicado no campo “tomador” (tomador = 
adquirente ≠ destinatário); 
2 - O adquirente e o destinatário são a mesma pessoa, mas diferente 
do tomador de serviços; (tomador  ≠ adquirente = destinatário) 
3 - O tomador e o destinatário são a mesma pessoa, diferente do 
adquirente; (tomador =  destinatário ≠ adquirente) 
4 - O tomador, o adquirente e o destinatário são pessoas distintas que 
devem ser identificadas. (tomador ≠ adquirente ≠ destinatário)

## Página 8

8 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endExt/ xCidade E C 1-1 1-60 Nome da cidade no exterior do destinatário do 
serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/endExt/ xEstProvReg E C 1-1 1-60 Estado, província ou região da cidade no exterior do 
destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ xLgr E C 1-1 1-
255 
Tipo e nome do logradouro do endereço do 
destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ nro E C 1-1 1-60 Número no logradouro do endereço do destinatário 
do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ xCpl E C 0-1 1-
156 
Complemento do endereço do destinatário do 
serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/end/ xBairro E C 1-1 1-60 Bairro do endereço do destinatário do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ fone E N 0-1 6-20 
Número do telefone do destinatário. 
 (Preencher com o Código DDD + número do 
telefone.  Nas operações com exterior é permitido 
informar o código do país + código da localidade + 
número do telefone) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ email E C 0-1 1-80 E-mail do destinatário. 
 
 
 
2.1.2 Grupo de Informações Relativas ao Adquirente 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ adq G - 0-1 - Grupo de informações relativas ao Adquirente 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ CNPJ CE N 1-1 14 Número da inscrição no Cadastro Nacional de Pessoa 
Jurídica (CNPJ) do adquirente de serviço 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ CPF CE N 1-1 11 Número da inscrição no Cadastro de Pessoa Física 
(CPF) do adquirente do serviço 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ NIF CE C 1-1 40 Número de identificação fiscal fornecido por órgão de 
administração tributária no exterior 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ cNaoNIF CE N 1-1 1 
Motivo para não informação do NIF: 
  
 0 - Não informado na nota de origem; 
 1 - Dispensado do NIF; 
 2 - Não exigência do NIF; 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ CAEPF E N 0-1 14 Número do Cadastro de Atividade Econômica da 
Pessoa Física (CAEPF) do adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ xNome E C 1-1 150 Nome / Nome Empresarial do adquirente 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ end G - 0-1 - Grupo de informações do endereço do adquirente do 
serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ endNac CG - 1-1 - Grupo de informações do endereço nacional. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endNac/ cMun E N 1-1 7 
Código do município do endereço do adquirente do 
serviço. 
  (Tabela do IBGE) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endNac/ CEP E C 1-1 8 
Código numérico do Endereçamento Postal nacional 
(CEP)  
  do endereço do adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ endExt CG - 1-1 - Grupo de informações do endereço no exterior. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endExt/ cPais E C 1-1 2 
Código do país do endereço do adquirente do 
serviço. 
  (Tabela de Países ISO) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endExt/ cEndPost E C 1-1 1-11 Código alfanumérico do Endereçamento Postal no 
exterior do adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endExt/ xCidade E C 1-1 1-60 Nome da cidade no exterior do adquirente do 
serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/endExt/ xEstProvReg E C 1-1 1-60 Estado, província ou região da cidade no exterior do 
adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ xLgr E C 1-1 1-
255 
Tipo e nome do logradouro do endereço do 
adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ nro E C 1-1 1-60 Número no logradouro do endereço do adquirente do 
serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ xCpl E C 0-1 1-
156 Complemento do endereço do adquirente do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/end/ xBairro E C 1-1 1-60 Bairro do endereço do adquirente do serviço.

## Página 9

9 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ fone E N 0-1 6-20 
Número do telefone do adquirente do serviço. 
 (Preencher com o Código DDD + número do 
telefone. Nas operações com exterior é permitido 
informar o código do país + código da localidade + 
número do telefone) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ email E C 0-1 1-80 E-mail do adquirente. 
 
 
 
2.1.3 Grupo de Informações de Operações Relacionadas a Bens Imóveis, Exceto Obras 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ imovel G - 0-1 - Grupo de informações de operações 
relacionadas a bens imóveis, exceto obras. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/ inscImobFisc E C 0-1 1-30 
Inscrição imobiliária fiscal  
 (código fornecido pela prefeitura para a 
identificação da obra ou para fins de recolhimento 
do IPTU) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/ cCIB CE C 1-1 8 Código do Cadastro Imobiliário Brasileiro - CIB 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/ end CG - 1-1 - Grupo de informações do endereço do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ CEP CE C 1-1 8 Código de Endereçamento Postal numérico do 
endereço nacional do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ endExt CG - 1-1 - Grupo de informações descritivas do endereço no 
exterior do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/endExt/ cEndPost E C 1-1 1-11 Código de Endereçamento Postal alfanumérico do 
endereço no exterior do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/endExt/ xCidade E C 1-1 1-60 Nome da cidade no exterior, local do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/endExt/ xEstProvReg E C 1-1 1-60 Estado, província ou região da cidade no exterior, 
local do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ xLgr E C 1-1 1-
255 Tipo e nome do logradouro do endereço do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ nro E C 1-1 1-60 Número no logradouro do endereço do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ xCpl E C 0-1 1-
156 Complemento do endereço do imóvel. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ xBairro E C 1-1 1-60 Bairro do endereço do imóvel. 
 
Observação importante acerca dos campos acima: 
1. O grupo “obra” em “ NFSe/infNFSe/DPS/infDPS/serv” deverá ser utilizado quando se 
tratar de um serviço de obra.  
 
2.1.4 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS 
 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCO
R. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/ valores G - 1-1 - Grupo de informações relativas aos valores do 
serviço prestado para IBS e CBS 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/ gReeRepRes G - 0-1 - 
Grupo de informações relativas a valores 
incluídos neste documento e recebidos por 
motivo de estarem relacionadas a operações de 
terceiros, objeto de reembolso, repasse ou 
ressarcimento pelo recebedor, já tributados e 
aqui referenciados 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/gReeRepRe
s/ 
documentos G - 
1-
100
0 
- 
Grupo relativo aos documentos referenciados 
nos casos de reembolso, repasse e 
ressarcimento que serão considerados na base 
de cálculo do ISSQN, do IBS e da CBS.

## Página 10

10 
 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/gReeRepRe
s/documentos/ 
dFeNacional CG - 1-1 - 
Grupo de informações de documentos fiscais 
eletrônicos que se encontram no repositório 
nacional. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/dFeNacional/ 
tipoChaveDFe E N 1-1 1 
Documento fiscal a que se refere a chaveDfe que seja 
um dos documentos do Repositório Nacional: 
1 = NFS-e 
2 = NF-e 
3 = CT-e 
9 = Outro 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/dFeNacional/ 
xTipoChaveDFe E C 0-1 255 
Descrição da DF-e a que se refere a chaveDfe que 
seja um dos documentos do Repositório Nacional. 
Deve ser preenchido apenas quando tipoChaveDFe = 
9 (Outro). 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/dFeNacional/ 
chaveDFe E C 1-1 1-50 
Chave do Documento Fiscal eletrônico do repositório 
nacional referenciado para os casos de operações já 
tributadas. 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/gReeRepRe
s/documentos/ 
docFiscalOutro CG - 1-1 - 
Grupo de informações de documento fiscais, 
eletrônicos ou não, que não se encontram no 
repositório nacional. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/docFiscalOutro/ 
cMunDocFiscal E N 1-1 7 Código do município emissor do documento fiscal que 
não se encontra no repositório nacional 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/docFiscalOutro/ 
nDocFiscal E C 1-1 255 Número do documento fiscal que não se encontra no 
repositório nacional 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/docFiscalOutro/ 
xDocFiscal E C 1-1 255 Descrição do documento fiscal 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/gReeRepRe
s/documentos/ 
docOutro CG - 1-1 - Grupo de informações de documento não fiscal. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/docOutro/ 
nDoc E C 1-1 255 Número do documento não fiscal. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/docOutro/ 
xDoc E C 1-1 255 Descrição do documento não fiscal. 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/gReeRepRe
s/documentos/ 
fornec G - 0-1 - Grupo de informações do fornecedor do 
documento referenciado 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/fornec/ 
CNPJ CE N 1-1 14 Número da inscrição federal (CNPJ) do fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/fornec/ 
CPF CE N 1-1 11 Número da inscrição federal (CPF) do fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/fornec/ 
NIF CE C 1-1 40 Este elemento só deverá ser preenchido para 
fornecedores não residentes no Brasil. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/fornec/ 
cNaoNIF CE N 1-1 1 
Motivo para não informação do NIF: 
 
0 - Não informado na nota de origem; 
1 - Dispensado do NIF; 
2 - Não exigência do NIF; 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/fornec/ 
xNome E C 1-1 150 Nome / Razão Social do fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/ 
dtEmiDoc E D 1-1 - Data da emissão do documento dedutível. 
Ano, mês e dia (AAAA-MM-DD) 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/ 
dtCompDoc E D 1-1 - Data da competência do documento dedutível. 
Ano, mês e dia (AAAA-MM-DD) 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/ 
tpReeRepRes E N 1-1 2 
Tipo de valor incluído neste documento, recebido por 
motivo de estarem relacionadas a operações de 
terceiros, objeto de reembolso, repasse ou 
ressarcimento pelo recebedor, já tributados e aqui 
referenciados 
 
  01 = Repasse de remuneração por intermediação de 
imóveis a demais corretores  
           envolvidos na operação 
  02 = Repasse de valores a fornecedor relativo a 
fornecimento intermediado por  
           agência de turismo 
  03 = Reembolso ou ressarcimento recebido por 
agência de propaganda e  
           publicidade por valores pagos relativos a 
serviços de produção externa por conta                            
           e ordem de terceiro 
  04 = Reembolso ou ressarcimento recebido por

## Página 11

11 
 
agência de propaganda e  
           publicidade por valores pagos relativos a 
serviços de mídia por conta                            
           e ordem de terceiro 
  99 = Outros reembolsos ou ressarcimentos 
recebidos por valores pagos relativos a  
           operações por conta e ordem de terceiro 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/ 
xTpReeRepRes E C 0-1 0-
150 
Descrição do reembolso ou ressarcimento quando a 
opção é "99 – Outros reembolsos ou ressarcimentos 
recebidos por valores pagos relativos a operações por 
conta e ordem de terceiro". 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/gReeRepRes/docume
ntos/ 
vlrReeRepRes E N 1-1 1-
15V2 
Valor monetário (total ou parcial, conforme 
documento informado) utilizado para não inclusão na 
base de cálculo do ISS e do IBS e da CBS da NFS-e 
que está sendo emitida (R$). 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/ trib G - 1-1 - Grupo de informações relacionados aos tributos 
IBS e CBS 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/trib/ gIBSCBS G - 1-1 - Grupo de informações relacionadas ao IBS e à 
CBS 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/ CST E N 1-1 3 Código de Situação Tributária do  
IBS e da CBS 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/ cClassTrib E N 1-1 6 Código de Classificação Tributária  
do IBS e da CBS 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/ cCredPres E N 0-1 2 Código e classificação do crédito presumido: IBS e 
CBS. 
NFSe/infNFSe/DPS/infDPS/
IBSCBSSEL/valores/trib/gIB
SCBS/ 
gTribRegular G - 0-1 - Grupo de informações da Tributação Regular 
NFSe/infNFSe/DPS/infDPS/IBSC
BSSEL/valores/trib/gIBSCBS/gTr
ibRegular/ 
CSTReg E N 1-1 3 Código de Situação Tributária do  
IBS e da CBS de tributação regular 
NFSe/infNFSe/DPS/infDPS/IBSC
BSSEL/valores/trib/gIBSCBS/gTr
ibRegular/ 
cClassTribReg E N 1-1 6 Código da Classificação Tributária do  
IBS e da CBS de tributação regular 
NFSe/infNFSe/DPS/infDPS/
IBSCBS/valores/trib/gIBSC
BS/ 
gDif G - 0-1 - Grupo de informações relacionadas ao 
diferimento para IBS e CBS 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/gDif/ pDifUF E N 1-1 1-
3V2 Percentual de diferimento para o IBS estadual. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/gDif/ pDifMun E N 1-1 1-
3V2 Percentual de diferimento para o IBS municipal. 
NFSe/infNFSe/DPS/infDPS/IBSC
BS/valores/trib/gIBSCBS/gDif/ pDifCBS E N 1-1 1-
3V2 Percentual de diferimento para a CBS. 
 
 
 
 
 
 
 
2.1.4.1 (REMOVIDO)Grupo de Informações Específicas Relativas ao IBS 
Estadual 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ gIBSUF G - 1-1 - 
Grupo de informações 
relacionados ao IBS para o 
Estado 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/ gDif G - 0-1 - 
Grupo de informações 
relacionadas ao diferimento 
para o Estado 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDif/ pDifUF E N 1-1 1-
3V2 
Percentual de diferimento 
estadual. 
NFSe/infNFSe/DPS/infDPS/IBSCBSSEL/valores/trib/gIBSCBS/gIBSUF/  gDevTrib G - 0-1 - 
Grupo de informações 
relacionados à devolução 
tributária para o Estado 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDevTrib/ vDevTribUF E N 1-1 1-
15V2 
Devolução personalizada do 
IBS estadual. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/ gDeson G - 0-1 - 
Grupo de informações 
relacionados à desoneração 
para o Estado

## Página 12

12 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDeson/ cstUFDeson E N 1-1 3 
Código de Situação tributária 
estadual de Desoneração do 
IBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDeson/ cClassTribUFDeson E N 1-1 6 
Código de Classificação 
estadual de Desoneração do 
IBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDeson/ pAliqUFDeson E N 1-1 1-
2V2 
Valor da alíquota estadual de 
Desoneração do IBS. 
 
 
 
2.1.4.2 (REMOVIDO)Grupo de Informações Específicas Relativas ao IBS 
Municipal 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ gIBSMun G - 1-1 - 
Grupo de informações 
relacionados ao IBS para 
o Município 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/ gDif G - 0-1 - 
Grupo de informações 
relacionadas ao 
diferimento para o 
Município 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/gDif/ pDifMun E N 1-1 1-
3V2 
Percentual de diferimento 
municipal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/ gDevTrib G - 0-1 - 
Grupo de informações 
relacionadas à devolução 
tributária para o 
Município 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/gDevol/ vDevTribMun E N 1-1 1-
15V2 
Devolução personalizada do 
IBS municipal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/ gDeson G - 0-1 - 
Grupo de informações 
relacionadas à 
desoneração para o 
Município 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/gDeson/ cstMunDeson E N 1-1 3 
Código de Situação 
tributária municipal de 
desoneração do IBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/gDeson/ cClassTribMunDeson E N 1-1 6 
Código de Classificação 
municipal de desoneração 
do IBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSMun/gDeson/ pAliqMunDeson E N 1-1 1-
2V2 
Valor da alíquota municipal 
de desoneração do IBS. 
 
 
2.1.4.3 (REMOVIDO)Grupo de Informações Específicas Relativas à CBS 
 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/  gCBS G - 1-1 - Grupo de informações 
relacionadas à CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/  gCBSCredPres G - 0-1 - 
Grupo de informações 
relacionadas ao crédito 
presumido para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gCBSCredPres/  cCredPresCBS E N 1-1 2 Código de Classificação do 
Crédito Presumido da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gCBSCredPres/  pCredPresCBS E N 1-1 1-
2V2 
Percentual do Crédito 
Presumido da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/  gDif G - 0-1 - 
Grupo de informações 
relacionadas ao 
diferimento para a CBS

## Página 13

13 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDif/  pDifCBS E N 1-1 1-
3V2 
Percentual de diferimento 
da 
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/  gDevTrib G - 0-1 - 
Grupo de informações 
relacionadas à devolução 
tributária para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDevol/  vDevTribCBS E N 1-1 1-
15V2 
Devolução personalizada da 
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/  gDeson G - 0-1 - Grupo de informações da 
desoneração para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/  cstCBSDeson E N 1-1 3 
Código de Situação 
tributária de Desoneração 
da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/  cClassTribCBSDeson E N 1-1 6 
Código de Classificação 
Tributária de Desoneração 
da 
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/  pAliqCBSDeson E N 1-1 1-
2V2 
Valor da alíquota 
Desoneração 
da CBS. 
 
 
2.2 Novos Grupos na NFS-e 
 
  Nos novos grupos que constam na NFS -e, fora dos limites da  DPS, os campos aqui 
apresentados são os que deverão ser  parametrizados pelos Estados, pelos Municípios e pela 
União ou aqueles que a própria plataforma, dadas as suas regras e cálculos, fornecerá de forma 
automatizada a partir dos dados emitidos pelos contribuintes na DPS, listados no tópico 
anterior.  
  De forma análoga ao novo grupo criado na DPS, aqui também foi criado o grupo IBSCBS 
(caminho NFSe/infNFSe/). Neste grupo serão dispostos todos os subgrupos e informações relativas 
aos novos tributos: IBS  e CBS. Importante observar que os campos/tags/células listados abaixo 
em amarelo se referem a campos que foram modificados em relação à versão anterior, 
publicada na Nota Técnica SE/CGNFS-e nº 002, de 28 de fevereiro de 2025. 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G - 1-1 - Grupo de informações geradas pelo sistema 
referentes ao IBS e à CBS 
 
  
 
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS 
 
CAMINHO NO XML CAMPO ELE  TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G  - 1-1 - Grupo de informações geradas pelo sistema referentes ao  
IBS e à CBS 
NFSe/infNFSe/IBSCBS/ cLocalidadeIncid E  N 1-1 7 Código IBGE da localidade de incidência do IBS/CBS (local da 
operação). 
NFSe/infNFSe/IBSCBS/ xLocalidadeIncid E  C 1-1 600 Nome da localidade de incidência do IBS/CBS. 
NFSe/infNFSe/IBSCBS/ xIndOp E  C 1-1 500 Descrição do código indicador da operação de fornecimento, 
conforme tabela “código indicador de operação”

## Página 14

14 
 
NFSe/infNFSe/IBSCBS/ xCST E  C 1-1 600 Descrição do Código de Situação Tributária do IBS/CBS.  
NFSe/infNFSe/IBSCBS/ xCClassTrib E  C 1-1 600 Descrição do Código de Classificação Tributária do IBS/CBS  
NFSe/infNFSe/IBSCBS/ pRedutor E  C 1-1 1-2V2 Percentual de redução de aliquota em compra governamental. 
 
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/ valores G - 1-1 - Grupo de valores brutos referentes ao IBS e à 
CBS 
NFSe/infNFSe/IBSCBS/valores/ vBC E N 1-1 1-15V2 
Valor da base de cálculo (BC) do IBS/CBS antes das 
reduções para cálculo do tributo bruto.  
 
vBC = vServ - descIncond – vCalcReeRepRes – vISSQN – 
vPIS - vCOFINS (até 2026) 
 
ou 
 
vBC = vServ - descIncond – vCalcReeRepRes – vISSQN 
(até 2032) 
 
NFSe/infNFSe/IBSCBS/valores/ vCalcReeRepRes E N 0-1 1-15V2 
Valor monetário (R$) total relativo ao fornecimento 
próprio de bens materiais ou relacionados a operações 
de terceiros, objeto de reembolso, repasse ou 
ressarcimento pelo recebedor, já tributados e aqui 
referenciados e que não integram da base de cálculo 
(BC) do ISSQN, do IBS e da CBS. 
NFSe/infNFSe/IBSCBS/valores/ uf         Grupo de Informações relativas aos valores do 
IBS Estadual 
NFSe/infNFSe/IBSCBS/valores/uf/ pIBSUF E N 1-1 1-2V2 
Alíquota da UF para IBS da localidade de incidência 
parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/uf/ pRedAliqUF E N 1-1 1-3V2 Percentual de redução de alíquota estadual. 
NFSe/infNFSe/IBSCBS/valores/uf/ pAliqEfetUF E N 1-1 1-2V2 
pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 - pRedutor) 
 
Se pRedAliqUF não for informado na DPS, então 
pAliqEfetUF é a própria pIBSUF. 
 
NFSe/infNFSe/IBSCBS/valores/ mun         Grupo de Informações relativas aos valores do 
IBS Municipal 
NFSe/infNFSe/IBSCBS/valores/mun/ pIBSMun E N 1-1 1-2V2 
Alíquota da UF para IBS da localidade de incidência 
parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/mun/ pRedAliqMun E N 1-1 1-3V2 Percentual de redução de alíquota municipal. 
NFSe/infNFSe/IBSCBS/valores/mun/ pAliqEfetMun E N 1-1 1-2V2 
pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x (1 - 
pRedutor) 
 
Se pRedAliqMun não for informado na DPS, então 
pAliqEfetMun é a própria pIBSMun. 
 
NFSe/infNFSe/IBSCBS/valores/ fed         Grupo de Informações relativas aos valores da 
CBS 
NFSe/infNFSe/IBSCBS/valores/fed/ pCBS E N 1-1 1-2V2 
Alíquota da UF para IBS da localidade de incidência 
parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/fed/ pRedAliqCBS E N 1-1 1-3V2 Percentual da redução de alíquota. 
NFSe/infNFSe/IBSCBS/valores/fed/ pAliqEfetCBS E N 1-1 1-2V2 
pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - 
pRedutor) 
 
Se pRedAliqCBS não for informado na DPS, então 
pAliqEfetCBS é a própria pCBS.

## Página 15

15 
 
2.2.3 Grupos Totalizadores 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/ totCIBS G - 1-1 - Grupo de Totalizadores 
NFSe/infNFSe/IBSCBS/totCIBS/ vTotNF E N 1-1 1-15V2 
Valor Total da NF considerando os impostos 
por fora: IBS e CBS. 
O IBS e a CBS são por fora, por isso seus 
valores devem ser adicionados ao valor 
total da NF. 
 
 vTotNF = vLiq (em 2026) 
 
 vTotNF = vLiq + vCBS + vIBSTot (a partir 
de 2027) 
NFSe/infNFSe/IBSCBS/totCIBS/ gTribRegular G - 0-1 - 
Grupo de informações de tributação 
regular 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ pAliqEfeRegIBSUF E N 1-1 1-2V2 
Alíquota efetiva de tributação regular do 
IBS estadual 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ vTribRegIBSUF E N 1-1 1-15V2 
Valor da tributação regular do IBS estadual. 
 
vTribRegIBSUF = vBC x pAliqEfeRegIBSUF 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ pAliqEfeRegIBSMun E N 1-1 1-2V2 
Alíquota efetiva de tributação regular do 
IBS municipal 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ vTribRegIBSMun E N 1-1 1-15V2 
Valor da tributação regular do IBS 
municipal. 
 
vTribRegIBSMun = vBC x 
pAliqEfeRegIBSMun 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ pAliqEfeRegCBS E N 1-1 1-2V2 
Alíquota efetiva de tributação regular da 
CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/ vTribRegCBS E N 1-1 1-15V2 
Valor da tributação regular da CBS. 
 
vTribRegCBS = vBC x pAliqEfeRegCBS 
NFSe/infNFSe/IBSCBS/totCIBS/ gTribCompraGov G - 0-1 - 
Grupo de informações da composição 
do valor do IBS e da CBS em compras 
governamentais 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov pIBSUF E N 1-1 1-2V2 Alíquota do IBS de competência do Estado 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov vIBSUF E N 1-1 1-15V2 Valor do Tributo do IBS da UF calculado 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov pIBSMun E N 1-1 1-2V2 
Alíquota do IBS de competência do 
Município 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov vIBSMun E N 1-1 1-15V2 
Valor do Tributo do IBS do Município 
calculado 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov pCBS E N 1-1 1-2V2 Alíquota da CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov vCBS E N 1-1 1-15V2 Valor do Tributo da CBS calculado

## Página 16

16 
 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS 
 
 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBS/ gCBS G - 1-1 - Grupo de valores referentes à CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ gCBSCredPres G - 1-1 - Grupo de valores referentes ao crédito 
presumido para CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/ pCredPresCBS E N 0-1 1-2V2 Alíquota do crédito presumido para a CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/ vCredPresCBS E N 1-1 1-
15V2 
Valor do Crédito Presumido da CBS. 
 
vCredPresCBS = vBC x pCredPresCBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vDifCBS E N 1-1 1-
15V2 
Total do Diferimento CBS. 
 
vDifCBS = vCBS x pDifCBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vCBS E N 1-1 1-
15V2 
Total valor da CBS da União. 
 
vCBS = vBC x (pCBS ou pAliqEfetCBS) 
 
 
 
SAMUEL KRUGER 
Auditor-Fiscal da Receita Federal do Brasil 
Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço 
Eletrônica de Padrão Nacional (SE/CGNFS-e) 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBS/ gIBS G - 1-1 - Grupo de totalizadores referentes ao IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ vIBSTot E N 1-1 1-
15V2 
Valor total do IBS. 
 
vIBSTot = vIBSUF + vIBSMun 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSCredPres G - 1-1 - Grupo de valores referentes ao crédito 
presumido para IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/ pCredPresIBS E N 0-1 1-
2V2 Alíquota do crédito presumido para o IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/ vCredPresIBS E N 1-1 1-
15V2 
Valor do Crédito Presumido para o IBS 
 
vCredPresIBS = vBC x pCredPresIBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSUFTot G - 1-1 - Grupo de valores referentes ao IBS Estadual 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vDifUF E N 1-1 1-
15V2 
Total do Diferimento do IBS estadual. 
 
vDifUF = vIBSUF x pDifUF 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vIBSUF E N 1-1 1-
15V2 
Total valor do IBS estadual. 
 
vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSMunTot G - 1-1 - Grupo de valores referentes ao IBS Municipal 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vDifMun E N 1-1 1-
15V2 
Total do Diferimento do IBS municipal. 
 
vDifMun = vIBSMun x pDifMun 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vIBSMun E N 1-1 1-
15V2 
Total valor do IBS municipal. 
 
vIBSMun = vBC x (pIBSMun ou pAliqEfetMun)
