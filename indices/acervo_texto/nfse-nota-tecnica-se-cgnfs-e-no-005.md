---
id: nfse-nota-tecnica-se-cgnfs-e-no-005
titulo: Nota Técnica SE/CGNFS-e nº 005
tipo: nota.tecnica
versao: '1.1'
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nt-005-se-cgnfse-novo-layout-rtc.pdf
arquivo_original: fontes/acervo/nfse-nota-tecnica-se-cgnfs-e-no-005.pdf
sha256_original: c4edd43536dd69b370704532f64c1bdb2a754ac89dd5eb84b16ad9efb3d4d8fb
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 12547ea748f3a268def1a5b9176a83994fb7e1dd26d7e1ed9a137e7b627f1c69
---

## Página 1

Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica 
de Padrão Nacional (SE/CGNFS-e) 
 
 
 
 
 
Projeto Reforma Tributária do Consumo – 
Adequações NFS-e 
 
 Nota Técnica Nº 005 – Versão 1.1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
19 de novembro de 2025

## Página 2

2 
 
Sumário 
 
1. Introdução ................................................................................................................................................. 3 
2. Layout NFS-e: Novos Grupos no Contexto da EC nº 132/2023 .................................................................. 4 
2.1 Novos Grupos na DPS da NFS-e ........................................................................................................ 6 
2.1.2 Grupo de Informações de Operações Relacionadas a Bens Imóveis, Exceto Obras .................... 8 
2.1.3 Grupo de Informações de Operações de Locação de Bens Móveis ............................................. 8 
2.1.4 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS ....................................... 10 
2.2 Novos Grupos na NFS-e .................................................................................................................. 12 
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS .......................................................... 13 
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS ........................................... 13 
2.2.3 Grupos Totalizadores ................................................................................................................. 14 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS ........................................................ 15 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS ....................................................... 15

## Página 3

3 
 
1. Introdução 
 
 Este documento contempla a quinta versão dos novos agrupamentos e campos opcionais do 
layout da Nota Fiscal de Serviço eletrônica – NFS-e padrão nacional relacionados à tributação do 
Imposto sobre Bens e Serviços – IBS e da Contribuição sobre Bens e Serviços – CBS incidentes nas 
operações de serviços, em atendimento às alterações previstas na Emenda Constitucional nº 132 de, 
20 de dezembro de 2023, que deu ensejo à Reforma Tributária do Consumo – RTC. Importante 
observar que esta nota técnica substitui as versões anteriores. 
 Os novos agrupamentos de campos foram inseridos a partir do layout atual da NFS-e, presente 
no documento “ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe.xlsx”, aba “LEIAUTE NFS -e 
ADN” que consta na sessão de documentação técnica no Portal da NFS-e: https://www.gov.br/nfse/pt-
br/biblioteca/documentacao-tecnica/documentacao-atual. 
 Importante esclarecer que o conjunto de campos apresentados neste documento é uma quinta 
versão, resultado de estudos técnicos realizados tomando como base o texto da Lei Complementar – 
LC nº 214, de 16 de janeiro de 2025 , e sua divulgação objetiva dar transparência aos  Estados, aos 
Municípios, às empresas prestadoras de serviço e de Tecnologia da Informação – TI e contribuintes 
para que possam se familiarizar com o novo padrão que deve rá vigorar a partir de janeiro de 2026. 
Os estudos técnicos permanecem e novas versões deverão ser publicadas nas próximas semanas com 
atualizações do layout proposto. Mesmo com a publicação desta Nota Técnica - NT, os novos 
campos e grupos de informações que estarão presentes no layout da NFS-e nos ambientes de 
Produção e de Produção Restrita (homologação/testes) em janeiro de 2026 serão aqueles 
publicados na NT 004, de 19 de agosto de 2025. As evoluções/atualizações aqui publicadas serão 
disponibilizadas nesses ambientes em data futura, a ser divulgada no Portal da NFS-e. 
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
• AnexoVI-LeiautesRN_RTC_IBSCBS-V1.02.01.xlsx 
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
• CAMPO 
Nome do campo/informação que deve constar no XML. 
• ELE 
Elemento ou valor do campo que deve ser informado. Pode ser dos tipos:

## Página 5

5 
 
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

## Página 6

6 
 
 
• DESCRIÇÃO 
Descrição sucinta do que representa cada campo e como deve ser preenchido. 
 
 
2.1 Novos Grupos na DPS da NFS-e 
 
 Na DPS, foi criado o grupo IBSCBS (caminho NFSe/infNFSe/DPS/infDPS/). Neste grupo 
serão dispostos todos os subgrupos e informações relativas aos novos tributos: IBS  e CBS; e que 
deverão ser informados pelo contribuinte na emissão. Importante observar que os campos/tags/células 
listados abaixo em verde se referem a campos que foram modificados , excluídos ou inseridos  em 
relação à versão anterior, publicada na NT SE/CGNFS-e nº 004, de 19 de agosto de 2025. 
 
 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/ IBSCBS G - 0-1 - Grupo de informações declaradas pelo emitente 
referentes ao IBS e à CBS 
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
NFSe/infNFSe/DPS/infDPS/IBSCBS/ tpOper E N 0-1 1 
Tipo de Operação com Entes Governanementais ou outros 
serviços sobre bens imóveis: 
 
1 – Fornecimento com pagamento posterior; 
2 - Recebimento do pagamento com fornecimento já realizado; 
3 – Fornecimento com pagamento já realizado; 
4 – Recebimento do pagamento com fornecimento posterior; 
5 – Fornecimento e recebimento do pagamento concomitantes.  
NFSe/infNFSe/DPS/infDPS/IBSCBS/ gRefNFSe G - 0-1 - Grupo de NFS-e referenciadas. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/gRefNFSe/ refNFSe E C 1-99 50 Chave da NFS-e referenciada. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ tpEnteGov E N 0-1 1 
Tipo de ente governamental 
 
Para administração pública direta e suas autarquias e 
fundações:  
1 = União  
2 = Estado  
3 = Distrito Federal  
4 = Município 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ indDoacao E N 0-1 1 Indica uma Operação de Doação 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ indDest E N 1-1 1 
A respeito do Destinatário dos serviços: 
 
0 – o destinatário é o próprio tomador/adquirente identificado 
na NFS-e (tomador=adquirente=destinatário); 
1 – o destinatário não é o próprio adquirente, podendo ser 
outra pessoa, física ou jurídica (ou equiparada), ou um 
estabelecimento diferente do indicado como tomador 
(tomador=adquirente≠destinatário);

## Página 7

7 
 
Algumas observações importantes acerca dos campos acima: 
1. O campo “cIndOp” se refere à tabela de indicador da operação publicada no ANEXO 
AnexoVII-IndOp_IBSCBS_V1.00.00-.xlsx; 
2. As notas de ajuste, de crédito e de débito, estão em processo de estudos e atualizações 
serão publicadas na próxima nota técnica. Portanto, a menção a essas notas de ajuste na 
descrição d o campo  “finNFSe” tem, por enquanto,  o único objetivo de  esclarecer a 
necessidade da criação desse campo. 
3. O campo “ indDoacao” possuirá critérios de preenchimento a depender da operação, 
inclusive se relacionando ao novo grupo de informações “ gEstornoCred” e ao código 
cClassTrib informado. Importante observar a coluna “NOTAS EXPLICATIV AS” no 
AnexoVI e as regras de negócio correspondentes para uma melhor compreensão. 
 
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

## Página 8

8 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ fone E N 0-1 6-20 
Número do telefone do destinatário. 
 (Preencher com o Código DDD + número do 
telefone.  Nas operações com exterior é permitido 
informar o código do país + código da localidade + 
número do telefone) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/dest/ email E C 0-1 1-80 E-mail do destinatário. 
 
 
 
2.1.2 Grupo de Informações de Operações Relacionadas a Bens Imóveis, Exceto 
Obras 
 
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
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/ endExt CG - 1-1 - Grupo de informações descritivas do endereço do 
imóvel no exterior. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/imovel/end/endExt/ cEndPost E C 1-1 1-11 Código de Endereçamento Postal alfanumérico do 
endereço do imóvel no exterior. 
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
 
2.1.3 Grupo de Informações de Operações de Locação de Bens Móveis 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ gLocBensMoveis G - 0-99 - Grupo de informações relativas aos bens 
móveis objetos de locação 
NFSe/infNFSe/DPS/infDPS/IBSCBS/gLocBensMoveis/ cNCMBemMovel E N 1-1 8 Código da Nomenclatura Comum do Mercosul 
(NCM) do bem móvel objeto da locação. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/gLocBensMoveis / xNCMBemMovel E C 1-1 1-150 Descrição do Bem Móvel objeto de locação. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/gLocBensMoveis / qtdNCMBemMovel E N 1-1 3 Quantidade de Bem Móvel objeto de locação.

## Página 9

9 
 
Observação importante acerca dos campos acima: 
1. O grupo acima só deverá ser informado para os casos de prestação de serviço de locação 
de bens móveis; 
2. A locação de bens móveis, por se tratar de um fato gerador do IBS/CBS, mas não do 
Imposto Sobre Serviço de Qualquer Natureza – ISSQN, será autorizada em ambiente 
nacional independente do status da adesão municipal e de sua opção pela utilização dos 
emissores públicos nacionais; 
3. Em razão das regras de negócio presentes no AnexoVI, esse grupo de informações só 
poderá ser fornecido nos casos em que o código de serviço informado (“cTribNac”) for 
99.04.01 “Locação de Bens Móveis”.; 
É importante mencionar que o item 99 do código de serviços será desmembrado para 
comportar as informações dos novos fatos gerados que serão formalizados pela NFS-e: 
 
Código Descrição 
99.01.01 
Outros serviços sem a incidência de ISSQN 
e ICMS. 
99.02.01 
Operações com Bens Imateriais Não 
Classificados em Itens Anteriores 
99.03.01 Locação de Bens Imóveis 
99.03.02 Cessão Onerosa de Bens Imóveis 
99.03.03 Arrendamento de Bens Imóveis 
99.03.04 
Servidão, Cessão de Uso ou de Espaço de 
Bens Imóveis (quando não caracterizem 
operações tributáveis pelo ISSQN) 
99.03.05 
Permissão de Uso ou Direito de Passagem 
de Bens Imóveis (quando não caracterizem 
operações tributáveis pelo ISSQN) 
99.04.01 Locação de Bens Móveis 
 
OBS:  
• Por padrão da plataforma NFS -e, os itens de serviço 99 não destacam ISSQN no 
documento fiscal;

## Página 10

10 
 
• Para os serviços do subitem “99.03”, d eve-se utilizar o código NBS  (cNBS) 
1.1002.10.00 quando o objeto da operação for um imóvel residencial ou 1.1002.20.00 
quando for não residencial. 
 
 
4. Nas próximas semanas, manuais relacionados aos novos fatos geradores serão 
publicados no portal da NFS-e. 
 
 
2.1.4 Grupo de Informações Relativas ao Serviço Prestado para IBS e CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/DPS/infDPS/IBSCBS/ valores G - 1-1 - Grupo de informações relativas aos valores 
do serviço prestado para IBS e CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/ gReeRepRes G - 0-1 - 
Grupo de informações relativas a valores 
incluídos neste documento e recebidos por 
motivo de estarem relacionadas a operações 
de terceiros, objeto de reembolso, repasse 
ou ressarcimento pelo recebedor, já 
tributados e aqui referenciados 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/gReeRepRes/ documentos G - 1-
1000 - 
Grupo relativo aos documentos 
referenciados nos casos de reembolso, 
repasse e ressarcimento que serão 
considerados na base de cálculo do ISSQN, 
do IBS e da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/gReeRepRes/documentos/ dFeNacional CG - 1-1 - 
Grupo de informações de documentos fiscais 
eletrônicos que se encontram no repositório 
nacional. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/dFeNacional/ tipoChaveDFe E N 1-1 1 
Documento fiscal a que se refere a chaveDfe que 
seja um dos documentos do Repositório Nacional: 
1 = NFS-e 
2 = NF-e 
3 = CT-e 
9 = Outro 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/dFeNacional/ xTipoChaveDFe E C 0-1 1-255 
Descrição da DF-e a que se refere a chaveDfe que 
seja um dos documentos do Repositório Nacional. 
Deve ser preenchido apenas quando 
tipoChaveDFe = 9 (Outro). 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/dFeNacional/ chaveDFe E C 1-1 1-50 
Chave do Documento Fiscal eletrônico do 
repositório nacional referenciado para os casos de 
operações já tributadas. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/gReeRepRes/documentos/ docFiscalOutro CG - 1-1 - 
Grupo de informações de documento fiscais, 
eletrônicos ou não, que não se encontram no 
repositório nacional. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/docFiscalOutro/ cMunDocFiscal E N 1-1 7 Código do município emissor do documento fiscal 
que não se encontra no repositório nacional 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/docFiscalOutro/ nDocFiscal E C 1-1 1-255 Número do documento fiscal que não se encontra 
no repositório nacional 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/docFiscalOutro/ xDocFiscal E C 1-1 1-255 Descrição do documento fiscal 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/gReeRepRes/documentos/ docOutro CG - 1-1 - Grupo de informações de documento não 
fiscal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/docOutro/ nDoc E C 1-1 1-255 Número do documento não fiscal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/docOutro/ xDoc E C 1-1 1-255 Descrição do documento não fiscal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/gReeRepRes/documentos/ fornec G - 0-1 - Grupo de informações do fornecedor do 
documento referenciado 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/fornec/ CNPJ CE N 1-1 14 Número da inscrição federal (CNPJ) do 
fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/fornec/ CPF CE N 1-1 11 Número da inscrição federal (CPF) do fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/fornec/ NIF CE C 1-1 40 Este elemento só deverá ser preenchido para 
fornecedores não residentes no Brasil.

## Página 11

11 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/fornec/ cNaoNIF CE N 1-1 1 
Motivo para não informação do NIF: 
 
0 - Não informado na nota de origem; 
1 - Dispensado do NIF; 
2 - Não exigência do NIF; 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/fornec/ xNome E C 1-1 1-150 Nome / Razão Social do fornecedor. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/ dtEmiDoc E D 1-1 - Data da emissão do documento dedutível. 
Ano, mês e dia (AAAA-MM-DD) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/ dtCompDoc E D 1-1 - Data da competência do documento dedutível. 
Ano, mês e dia (AAAA-MM-DD) 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/ tpReeRepRes E N 1-1 2 
Tipo de valor incluído neste documento, recebido 
por motivo de estarem relacionadas a operações 
de terceiros, objeto de reembolso, repasse ou 
ressarcimento pelo recebedor, já tributados e aqui 
referenciados 
 
  01 = Repasse de remuneração por 
intermediação de imóveis a demais corretores  
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
agência de propaganda e  
           publicidade por valores pagos relativos a 
serviços de mídia por conta                            
           e ordem de terceiro 
  99 = Outros reembolsos ou ressarcimentos 
recebidos por valores pagos relativos a  
           operações por conta e ordem de terceiro 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/ xTpReeRepRes E C 0-1 0-150 
Descrição do reembolso ou ressarcimento quando 
a opção é "99 – Outros reembolsos ou 
ressarcimentos recebidos por valores pagos 
relativos a operações por conta e ordem de 
terceiro". 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gReeRepRes/documentos/ vlrReeRepRes E N 1-1 1-15V2 
Valor monetário (total ou parcial, conforme 
documento informado) utilizado para não inclusão 
na base de cálculo do ISS e do IBS e da CBS da 
NFS-e que está sendo emitida (R$). 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/ gDedRedIBSCBS G - 0-
1000 - 
Grupo de informações relativas a valores de 
dedução e redução da Base de Cálculo do 
IBS e da CBS referentes às operações de 
locação, cessão onerosa ou arrendamento 
de bens imóveis, e serviços médicos. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gDedRedIBSCBS/ tpDedRedIBSCBS E N 1-1 2 
Tipo de parcela não integrante da base de cálculo 
do IBS e da CBS  
 
  01 = Tributos inclusos no aluguel ou equivalente 
(Ex.: IPTU, Contribuição de melhoria) - apenas 
para NBS 1.1002.10.00 ou 1.1002.20.00 
  02 = Emolumento incluso no aluguel ou 
equivalente - apenas para NBS 1.1002.10.00 ou 
1.1002.20.00 
  03 = Condomínio incluso no aluguel ou 
equivalente - apenas para NBS 1.1002.10.00 ou 
1.1002.20.00 
04 = Redutor Social - apenas para a NBS 
1.1002.10.00 
  05 = Glosa de Serviços Médicos 
  99 = Outras parcelas inclusas no aluguel ou 
equivalente 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gDedRedIBSCBS/ xTpDedRedIBSCBS E C 0-1 0-150 
Descrição do tipo de parcela não integrante da 
base de cálculo do IBS e da CBS quando a opção 
for “99  = Outras parcelas inclusas no aluguel ou 
equivalente". 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/gDedRedIBSCBS/ vlrDedRedIBSCBS E N 1-1 1-15V2 
Valor monetário (total ou parcial) utilizado para 
não inclusão na base de cálculo do IBS e da CBS 
da NFS-e que está sendo emitida (R$). 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/ trib G - 1-1 - Grupo de informações relacionados aos 
tributos IBS e CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/trib/ gIBSCBS G - 1-1 - Grupo de informações relacionadas ao IBS e 
à CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/ CST E N 1-1 3 Código de Situação Tributária do  
IBS e da CBS

## Página 12

12 
 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/ cClassTrib E N 1-1 6 Código de Classificação Tributária  
do IBS e da CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/ cCredPres E N 0-1 2 Código e classificação do crédito presumido: IBS 
e CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBSS
EL/valores/trib/gIBSCBS/ gTribRegular G - 0-1 - Grupo de informações da Tributação Regular 
NFSe/infNFSe/DPS/infDPS/IBSCBSSEL/val
ores/trib/gIBSCBS/gTribRegular/ CSTReg E N 1-1 3 Código de Situação Tributária do  
IBS e da CBS de tributação regular 
NFSe/infNFSe/DPS/infDPS/IBSCBSSEL/val
ores/trib/gIBSCBS/gTribRegular/ cClassTribReg E N 1-1 6 Código da Classificação Tributária do  
IBS e da CBS de tributação regular 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/trib/gIBSCBS/ gDif G - 0-1 - Grupo de informações relacionadas ao 
diferimento para IBS e CBS 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gDif/ pDifUF E N 1-1 1-3V2 Percentual de diferimento para o IBS estadual. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gDif/ pDifMun E N 1-1 1-3V2 Percentual de diferimento para o IBS municipal. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gDif/ pDifCBS E N 1-1 1-3V2 Percentual de diferimento para a CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/trib/gIBSCBS/ gEstornoCred G - 0-1 - Grupo de informações relacionadas aos 
estornos de créditos do IBS e da CBS. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gEstornoCred/ vIBSEstCred E N 1-1 1-15V2 Valor do IBS a ser estornado. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gEstornoCred/ vCBSEstCred E N 1-1 1-15V2 Valor da CBS a ser estornado. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/v
alores/trib/gIBSCBS/ gPagAntecipado G - 0-1 - Grupo de referenciamento das NFS-e de 
pagamento antecipado para abatimento. 
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores
/trib/gIBSCBS/gPagAntecipado/ refNFSe E C 1-99 50 Chave da NFS-e de pagamento antecipado 
referenciada. 
 
 
 
2.2 Novos Grupos na NFS-e 
 
  Nos novos grupos que constam na NFS -e, fora dos limites da  DPS, os campos aqui 
apresentados são os que deverão ser  parametrizados pelos Estados, pelos Municípios e pela 
União ou aqueles que a própria plataforma, dadas as suas regras e cálculos, fornecerá de forma 
automatizada a partir dos dados emitidos pelos contribuintes na DPS, listados no tópico 
anterior.  
  De forma análoga ao novo grupo criado na DPS, aqui também foi criado o grupo IBSCBS 
(caminho NFSe/infNFSe/). Neste grupo serão dispostos todos os subgrupos e informações relativas 
aos novos tributos: IBS  e CBS. Importante observar que os campos/tags/células listados abaixo 
em verde se referem a campos que foram modificados em relação à versão anterior, publicada 
na NT SE/CGNFS-e nº 004, de 19 de agosto de 2025. 
 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G - 0-1 - Grupo de informações geradas pelo sistema 
referentes ao IBS e à CBS

## Página 13

13 
 
2.2.1 Grupo de Informações Comuns Relativas ao IBS e à CBS 
 
CAMINHO NO XML CAMPO ELE  TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/ IBSCBS G  - 0-1 - Grupo de informações geradas pelo sistema referentes ao  
IBS e à CBS 
NFSe/infNFSe/IBSCBS/ cLocalidadeIncid E  N 1-1 7 Código IBGE da localidade de incidência do IBS/CBS (local da  
operação). 
NFSe/infNFSe/IBSCBS/ xLocalidadeIncid E  C 1-1 600 Nome da localidade de incidência do IBS/CBS. 
NFSe/infNFSe/IBSCBS/ pRedutor E  C 0-1 1-2V2 Percentual de redução de aliquota em compra governamental. 
 
 
2.2.2 Grupo de Informações de Valores Brutos Relativos ao IBS e à CBS 
 
CAMINHO NO XML CAMPO ELE TIP
O 
OCO
R. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/ valores G - 1-1 - Grupo de valores brutos referentes ao IBS e à 
CBS 
NFSe/infNFSe/IBSCBS/valores/ vBC E N 1-1 1-15V2 
Valor da base de cálculo (BC) do IBS/CBS antes das 
reduções para cálculo do tributo bruto.  
 
vBC = vServ - descIncond – vCalcReeRepRes - 
vCalcDedRedIBSCBS – vISSQN – vPIS - vCOFINS (até 
2026) 
 
ou 
 
vBC = vServ - descIncond – vCalcReeRepRes – 
vCalcDedRedIBSCBS - vISSQN (até 2032) 
 
NFSe/infNFSe/IBSCBS/valores/ vCalcReeRepRes E N 0-1 1-15V2 
Valor monetário (R$) total relativo ao fornecimento 
próprio de bens materiais ou relacionados a operações 
de terceiros, objeto de reembolso, repasse ou 
ressarcimento pelo recebedor, já tributados e aqui 
referenciados e que não integram da base de cálculo 
(BC) do ISSQN, do IBS e da CBS. 
NFSe/infNFSe/IBSCBS/valores/ vCalcDedRedIBSCBS E N 0-1 1-15V2 
Valor monetário (R$) total relativo aos valores de 
dedução e redução da Base de Cálculo do IBS e da 
CBS referentes às operações de locação, cessão 
onerosa ou arrendamento de bens imóveis, e serviços 
médicos. 
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

## Página 14

14 
 
NFSe/infNFSe/IBSCBS/valores/fed/ pAliqEfetCBS E N 1-1 1-2V2 
pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - 
pRedutor) 
 
Se pRedAliqCBS não for informado na DPS, então 
pAliqEfetCBS é a própria pCBS. 
 
 
 
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

## Página 15

15 
 
 
2.2.3.1 Grupo de Informações Relativas às Totalizações do IBS 
 
 
2.2.3.2 Grupo de Informações Relativas às Totalizações da CBS 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBS/ gCBS G - 1-1 - Grupo de valores referentes à CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ gCBSCredPres G - 0-1 - Grupo de valores referentes ao crédito 
presumido para CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/ pCredPresCBS E N 1-1 1-2V2 Alíquota do crédito presumido para a CBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/ vCredPresCBS E N 1-1 1-
15V2 
Valor do Crédito Presumido da CBS. 
 
vCredPresCBS = vBC x pCredPresCBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vDifCBS E N 0-1 1-
15V2 
Total do Diferimento CBS. 
 
vDifCBS = vCBS x pDifCBS 
NFSe/infNFSe/IBSCBS/totCIBS/gCBS/ vCBS E N 1-1 1-
15V2 
Total valor da CBS da União. 
 
vCBS = vBC x (pCBS ou pAliqEfetCBS) 
 
 
 
 
CARLOS EDUARDO BURKLE 
Auditor Fiscal de Tributos – Londrina/PR 
Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço 
Eletrônica de Padrão Nacional (SE/CGNFS-e) 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
NFSe/infNFSe/IBSCBS/totCIBS/ gIBS G - 1-1 - Grupo de totalizadores referentes ao IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ vIBSTot E N 1-1 1-
15V2 
Valor total do IBS. 
 
vIBSTot = vIBSUF + vIBSMun 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSCredPres G - 0-1 - Grupo de valores referentes ao crédito 
presumido para IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/ pCredPresIBS E N 1-1 1-
2V2 Alíquota do crédito presumido para o IBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/ vCredPresIBS E N 1-1 1-
15V2 
Valor do Crédito Presumido para o IBS 
 
vCredPresIBS = vBC x pCredPresIBS 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSUFTot G - 1-1 - Grupo de valores referentes ao IBS Estadual 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vDifUF E N 0-1 1-
15V2 
Total do Diferimento do IBS estadual. 
 
vDifUF = vIBSUF x pDifUF 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/ vIBSUF E N 1-1 1-
15V2 
Total valor do IBS estadual. 
 
vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/ gIBSMunTot G - 1-1 - Grupo de valores referentes ao IBS Municipal 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vDifMun E N 0-1 1-
15V2 
Total do Diferimento do IBS municipal. 
 
vDifMun = vIBSMun x pDifMun 
NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/ vIBSMun E N 1-1 1-
15V2 
Total valor do IBS municipal. 
 
vIBSMun = vBC x (pIBSMun ou pAliqEfetMun)
