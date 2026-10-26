---
id: nfse-nota-tecnica-se-cgnfs-e-no-002
titulo: Nota Técnica SE/CGNFS-e nº 002
tipo: nota.tecnica
versao: '1.0'
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nota-tecnica-se-cgnfs-e-no-002-de-28-de-fevereiro-de-2025
arquivo_original: fontes/acervo/nfse-nota-tecnica-se-cgnfs-e-no-002.pdf
sha256_original: 725593f48bb8c33cec5213e59c5585c2e3c2dcd62eae4fdd70880fd8a476f550
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 43dc39bc52738112d683d4d24041dbc5a77ef166a03682e3b00978777f04ed1f
---

## Página 1

Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica 
de Padrão Nacional (SE/CGNFS-e) 
 
 
 
 
 
 
Projeto Reforma Tributária do Consumo – 
Adequações NFS-e 
 
 Nota Técnica Nº 002 – Versão 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
28 de fevereiro de 2025

## Página 2

2 
 
Sumário 
 
1. Introdução ................................................................................................................................................. 3 
2. Layout NFS-e: Novos Grupos no Contexto da EC nº 132/2023 .................................................................. 4 
2.1 Novos Grupos na DPS da NFS-e ........................................................................................................ 6 
2.1.1 Grupo de Informações Relativas ao Destinatário ........................................................................ 6 
2.1.2 Grupo de Informações Relativas ao Adquirente .......................................................................... 7 
2.1.3 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS ......................................... 8 
2.1.4 Grupo de Informações Relativas aos Valores do Serviço Prestado para IBS e CBS ...................... 8 
2.1.4.1 Grupo de Informações Específicas Relativas ao IBS Estadual .................................................. 9 
2.1.4.2 Grupo de Informações Específicas Relativas ao IBS Municipal................................................ 9 
2.1.4.3 Grupo de Informações Específicas Relativas à CBS ............................................................... 10 
2.2 Novos Grupos na NFS-e .................................................................................................................. 10 
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS .......................................................... 11 
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS ........................................... 11 
2.2.3 Grupos Totalizadores ................................................................................................................. 12 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS ........................................................ 12 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS ....................................................... 12

## Página 3

3 
 
 
1. Introdução 
 
 Este documento contempla a segunda versão dos novos agrupamentos e campos opcionais do 
layout da Nota Fiscal de Serviço eletrônica – NFS-e padrão nacional relacionados à tributação do 
Imposto sobre Bens e Serviços – IBS e da Contribuição sobre Bens e Serviços – CBS incidentes nas 
operações de serviços, em atendimento às alterações previstas na Emenda Constitucional nº 132 de, 
20 de dezembro de 2023, que deu ensejo à Reforma Tributária do Consumo – RTC. 
 Os novos agrupamentos de campos foram inseridos a partir do layout atual da NFS-e, presente 
no documento “ AnexoIV-LeiautesRN_ADN-SNNFSe_V1.00.02-Produção.xlsx”, aba “LEIAUTE 
NFS-e ADN” que consta na sessão de documentação técnica no Portal da NFS -e: 
https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica. 
 Importante esclarecer que o conjunto de campos apresentados neste documento é uma segunda 
versão, resultado de estudos técnicos realizados tomando como base o texto da Lei Complementar – 
LC nº 214, de 16 de janeiro de 2025, e sua divulgação objetiva dar transparência aos Municípios, às 
empresas prestadoras de serviço e de Tecnologia da Informação – TI e contribuintes para que possam 
se familiarizar com o novo padrão que deverá vigorar a partir de janeiro de 2026. Os estudos técnicos 
permanecem e novas versões deverão ser publicadas nos próximos meses com atualizações do layout 
proposto. 
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
 
 
 
2. Layout NFS-e: Novos Grupos no Contexto da EC nº 132/2023 
 
 Para melhor compreensão das informações disponibilizadas nos layouts dispostos 
neste tópico, segue um breve glossário. 
• CAMINHO NO XML 
O XML (Extensible Markup Language) é uma linguagem de marcação utilizada para 
estruturar e armazenar dados em um formato legível por máquina  que obedece aos 
layouts dispostos neste documento e que possui regras a serem seguidas, em uma 
sequência pré-definida e ordenada. Esta coluna informa o path, ou caminho, ordenado 
em que as informações devem ser dispostas na formatação do XML. 
 
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

## Página 5

5 
 
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

## Página 6

6 
 
2.1 Novos Grupos na DPS da NFS-e 
 
 Na DPS, foi criado o grupo IBSCBS (caminho NFSe/infNFSe/DPS/infDPS/). Neste grupo 
serão dispostos todos os subgrupos e informações relativas aos novos tributos: IBS  e CBS; e que 
deverão ser informados pelo contribuinte  na emissão . Importante observar que os  campos/tags 
listados abaixo em vermelho se referem a campos que foram modificados em relação à versão 
anterior, publicada na Nota Técnica SE/CGNFS-e nº 001, de 01 de agosto de 2024. 
 
 
 
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
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/ IBSCBS G - 1-1 - Grupo de informações declaradas pelo emitente referentes ao 
IBS e à CBS

## Página 7

7 
 
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
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ fone E N 0-1 6-20 
Número do telefone do adquirente do serviço. 
 (Preencher com o Código DDD + número do 
telefone. Nas operações com exterior é permitido 
informar o código do país + código da localidade + 
número do telefone) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/adq/ email E C 0-1 1-80 E-mail do adquirente.

## Página 8

8 
 
 
2.1.3 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ serv G G 1-1 - Grupo de informações relativas ao serviço 
prestado para IBS/CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/ modoPrestServ E C 1-1 1 
Modo de prestação do serviço: 
 
1 - Presencial; 
2 - Não presencial; 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/ clocalPrestServ CE N 1-1 7 Código da localidade da prestação do serviço. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/ cPaisPrestServ CE C 1-1 2 
Código do país onde ocorreu a prestação do 
serviço. 
 (Tabela de Países ISO) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/ cCIB E C 0-1 8 Cadastro de imóveis. Obrigatório para construção 
civil. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/ gCompraGov G - 0-1 - 
Grupo de informações de compras 
governamentais relacionadas aos tributos 
IBS / CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/serv/gCompraGov/ indCompGov E N 0-1 1 
Indicador de compra governamental 
0 - Não; 
1 - Sim; 
 
 
 
2.1.4 Grupo de Informações Relativas aos Valores do Serviço Prestado para IBS e 
CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ valores G - 1-1 - 
Grupo de informações relativas 
aos valores do serviço prestado 
para IBS e CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/ trib G - 1-1 - 
Grupo de informações 
relacionados aos tributos IBS e 
CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/ gIBSCBS G - 1-1 - Grupo de informações 
relacionadas ao IBS e à CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ cstIBSCBS E N 1-1 3 Código de Situação Tributária do 
IBS e da CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ cClassTribIBSCBS E N 1-1 6 Código de Classificação Tributária 
do IBS e da CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ gIBSCredPres G - 1-1 - 
Grupo de Informações do 
Crédito Presumido  
referente ao IBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSCredPres/ cCredPresIBS E N 1-1 2 Código de Classificação do Crédito 
Presumido do IBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSCredPres/ pCredPresIBS E N 1-1 1-
2V2 
Percentual do Crédito Presumido do 
IBS.

## Página 9

9 
 
2.1.4.1 Grupo de Informações Específicas Relativas ao IBS Estadual 
 
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
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/ gDevTrib G - 0-1 - 
Grupo de informações 
relacionados à devolução 
tributária para o Estado 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/gDevol/ vDevTribUF E N 1-1 1-
15V2 
Devolução personalizada do 
IBS estadual. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gIBSUF/ gDeson G - 0-1 - 
Grupo de informações 
relacionados à desoneração 
para o Estado 
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
 
 
2.1.4.2 Grupo de Informações Específicas Relativas ao IBS Municipal 
 
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

## Página 10

10 
 
2.1.4.3 Grupo de Informações Específicas Relativas à CBS 
 
 
 
 
 
2.2 Novos Grupos na NFS-e 
 
  Nos novos grupos que constam na NFS -e, fora dos limites da  DPS, os campos aqui 
apresentados são os que deverão ser  parametrizados pelos Estados, pelos Municípios e pela 
União ou aqueles que a própria plataforma, dadas as suas regras e cálculos, fornecerá de forma 
automatizada a partir dos dados emitidos pelos contribuintes na DPS, listados no tópico 
anterior.  
  De forma análoga ao novo grupo criado na DPS, aqui também foi criado o grupo IBSCBS 
(caminho NFSe/infNFSe/). Neste grupo serão dispostos todos os subgrupos e informações relativas aos novos 
tributos: IBS e CBS. Importante observar que os campos/tags listados abaixo em vermelho se referem a 
campos que foram modificados em relação à versão anterior, publicada na Nota Técnica SE/CGNFS-
e nº 001, de 01 de agosto de 2024. 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G - 1-1 - Grupo de informações geradas pelo sistema referentes ao  
IBS e à CBS 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/ gCBS G - 1-1 - Grupo de informações 
relacionadas à CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/ gCBSCredPres G - 0-1 - 
Grupo de informações 
relacionadas ao crédito 
presumido para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gCBSCredPres/ cCredPresCBS E N 1-1 2 Código de Classificação do  
Crédito Presumido da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gCBSCredPres/ pCredPresCBS E N 1-1 1-
2V2 
Percentual do Crédito Presumido da 
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/ gDif G - 0-1 - 
Grupo de informações 
relacionadas ao diferimento 
para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDif/ pDifCBS E N 1-1 1-
3V2 
Percentual de diferimento da  
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/ gDevTrib G - 0-1 - 
Grupo de informações 
relacionadas à devolução 
tributária para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDevol/ vDevTribCBS E N 1-1 1-
15V2 Devolução personalizada da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/ gDeson G - 0-1 - Grupo de informações da 
desoneração para a CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/ cstCBSDeson E N 1-1 3 Código de Situação tributária de 
Desoneração da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/ cClassTribCBSDeson E N 1-1 6 
Código de Classificação  
Tributária de Desoneração da  
CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gCBS/gDeson/ pAliqCBSDeson E N 1-1 1-
2V2 
Valor da alíquota Desoneração  
da CBS.

## Página 11

11 
 
 
  
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G - 1-1 - Grupo de informações geradas pelo sistema referentes ao  
IBS e à CBS 
NFSe/infNFSe/IBSCBS/ xLocalidadeIncid E C 1-1 600 Nome da localidade de incidência do IBS/CBS. 
NFSe/infNFSe/IBSCBS/ xCSTIBSCBS E C 1-1 600 Descrição do Código de Situação Tributária do IBS/CBS. 
NFSe/infNFSe/IBSCBS/ xClassTribIBSCBS E C 1-1 600 Descrição do Código de Classificação Tributária do IBS/CBS 
NFSe/infNFSe/IBSCBS/ compGov G - 0-1 - Grupo referente a compras governamentais. 
NFSe/infNFSe/IBSCBS/compGov/ tpCompraGov E C 1-1 1 
Tipo do ente da compra governamental: 
 
1 - União; 
2 - Estados; 
3 - Distrito Federal; 
4 - Municípios; 
NFSe/infNFSe/IBSCBS/compGov/ pRedutor E C 1-1 1-2V2 Percentual de redução de alíquota em compra governamental. 
   
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/ valores G - 1-1 - Grupo de valores brutos referentes ao IBS e à CBS  
NFSe/infNFSe/IBSCBS/valores/ vBC E N 1-1 1-
15V2 
Valor da base de cálculo (BC) do IBS/CBS antes das reduções para 
cálculo do tributo bruto. 
NFSe/infNFSe/IBSCBS/valores/ uf         Grupo de Informações relativas aos valores do IBS Estadual  
NFSe/infNFSe/IBSCBS/valores/uf/ pIBSUF E N 1-1 1-2V2 Alíquota da UF para IBS da localidade de incidência parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/uf/ pRedAliqUF E N 1-1 1-3V2 Percentual de redução de alíquota estadual. 
NFSe/infNFSe/IBSCBS/valores/uf/ pAliqEfetUF E N 1-1 1-2V2 
pAliqEfetUF = pIBSUF x pRedAliqUF 
 
Se pRedAliqUF não for informado na DPS, então pAliqEfetUF é a  
própria pIBSUF. 
NFSe/infNFSe/IBSCBS/valores/uf/ vTribOpUF E N 1-1 1-
15V2 
Valor do tributo bruto da Operação para IBS Estadual. 
 
vTribOpUF = vBC x pIBSUF. 
NFSe/infNFSe/IBSCBS/valores/ mun         Grupo de Informações relativas aos valores do IBS Municipal  
NFSe/infNFSe/IBSCBS/valores/mun/ pIBSMun E N 1-1 1-2V2 Alíquota da UF para IBS da localidade de incidência parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/mun/ pRedAliqMun E N 1-1 1-3V2 Percentual de redução de alíquota estadual. 
NFSe/infNFSe/IBSCBS/valores/mun/ pAliqEfetMun E N 1-1 1-2V2 
pAliqEfetMun = pIBSMun x pRedAliqMun 
 
Se pRedAliqMun não for informado na DPS, então pAliqEfetMun é a 
própria pIBSMun. 
NFSe/infNFSe/IBSCBS/valores/mun/ vTribOpMun E N 1-1 1-
15V2 
Valor do tributo bruto da Operação para o IBS Municipal. 
 
vTribOpMun = vBC x pIBSMun. 
NFSe/infNFSe/IBSCBS/valores/ fed         Grupo de Informações relativas aos valores da CBS  
NFSe/infNFSe/IBSCBS/valores/fed/ pCBS E N 1-1 1-2V2 Alíquota da UF para IBS da localidade de incidência parametrizada  
no sistema. 
NFSe/infNFSe/IBSCBS/valores/fed/ pRedAliqCBS E N 1-1 1-3V2 Percentual da redução de alíquota. 
NFSe/infNFSe/IBSCBS/valores/fed/ pAliqEfetCBS E N 1-1 1-2V2 
pAliqEfetCBS = pCBS x pRedAliqCBS 
 
Se pRedAliqCBS não for informado na DPS, então pAliqEfetCBS é a 
própria pCBS. 
NFSe/infNFSe/IBSCBS/valores/fed/ vTribOpCBS E N 1-1 1-
15V2 
Valor do tributo bruto da Operação para a CBS. 
 
vTribOpCBS =  vBC x pCBS.

## Página 12

12 
 
 
2.2.3 Grupos Totalizadores 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/ totCIBS G - 1-1 - Grupo de Totalizadores 
NFSe/infNFSe/IBSCBS/totCIBS/ vTotNF E N 1-1 1-
15V2 
Valor Total da NF considerando os impostos por fora IBS e CBS.  
O IBS e a CBS são por fora, por isso seus valores devem ser 
adicionados ao valor total da NF. 
 
vTotNF = VLiq + vCBS + vIBSTot 
 
 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS 
 
 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBSSel/ gCBS G - 1-1 - Grupo de totalizadores referentes à CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vCredPresCBS E N 1-1 1-
15V2 
Valor do Crédito Presumido da CBS. 
 
vCredPresCBS = vBC x pCredPresCBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vDifCBS E N 1-1 1-
15V2 
Total do Diferimento CBS. 
 
vDifCBS = (vBC x pDifCBS) 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vDesonCBS E N 1-1 1-
15V2 
Total do valor desonerado CBS. 
 
vDesonCBS = (vBC x pAliqCBS) - (vBC x pAliqEfetCBS) 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vCBS E N 1-1 1-
15V2 
Total valor da CBS da União. 
 
vCBS = vBC x (pCBS ou pAliqEfetCBS) - (vCredPresCBS + vDifCBS + 
vDevTribCBS) 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBS/ gIBS G - 1-1 - Grupo de totalizadores referentes ao IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ vCredPresIBS E N 1-1 1-
15V2 
Valor do Crédito Presumido. 
 
vCredPresIBS = vBC x pCredPresIBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSUFTot G - 1-1 - Grupo de valores referentes ao IBS Estadual 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vDifUF E N 1-1 1-
15V2 
Total do Diferimento estadual. 
 
vDifUF = (vBC x pDifUF) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vDesonUF E N 1-1 1-
15V2 
Total valor desonerado estadual. 
 
vDesonUF = (vBC x pAliqUF) - (vBC x pAliqEfetUF) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vIBSUF E N 1-1 1-
15V2 
Total valor do IBS estadual. 
 
vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) - (vCredPresIBS  
+ vDifUF + vDevTribUF) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSMunTot G - 1-1 - Grupo de valores referentes ao IBS Municipal 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vDifMun E N 1-1 1-
15V2 
Total do Diferimento municipal. 
 
vDifMun = (vBC x pDifMun) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vDesonMun E N 1-1 1-
15V2 
Total valor desonerado municipal. 
 
vDesonMun = (vBC x pAliqMun) - (vBC x pAliqEfetMun) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vIBSMun E N 1-1 1-
15V2 
Total valor do IBS municipal. 
 
vIBSMun = vBC x (pIBSMun ou pAliqEfetMun) - 
(vCredPresIBS + vDifMun + vDevTribMun) 
NFSe/infNFSe/IBSCBS/totCIBSSel/gIBS/ vIBSTot E N 1-1 1-
15V2 
Total Valor do IBS Total. 
 
vIBSTot = vIBSUF + vIBSMun

## Página 13

13 
 
 
 
SAMUEL KRUGER 
Auditor-Fiscal da Receita Federal do Brasil 
Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço 
Eletrônica de Padrão Nacional (SE/CGNFS-e)
