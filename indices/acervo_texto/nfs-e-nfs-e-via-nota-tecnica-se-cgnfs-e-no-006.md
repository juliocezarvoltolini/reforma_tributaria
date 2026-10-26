---
id: nfs-e-nfs-e-via-nota-tecnica-se-cgnfs-e-no-006
titulo: Nota Técnica SE/CGNFS-e nº 006
tipo: nota.tecnica
documento_fiscal: NFS-e (NFS-e Via)
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nt-006-se-cgnfse-leiaute-nfse-via.pdf
arquivo_original: fontes/acervo/nfs-e-nfs-e-via-nota-tecnica-se-cgnfs-e-no-006.pdf
sha256_original: c6b7fd8a47c15f59766d974c62edb5fc8c94f3dac4e8f9e26e16ddff6dcb944b
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 1cf0894f6aa3a500a284c1b91e12e34737b0f35404fc4607c49c40c0aa08c80d
---

## Página 1

Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica 
de Padrão Nacional (SE/CGNFS-e) 
 
 
 
 
 
Projeto Reforma Tributária do Consumo 
Leiaute Nota Fiscal de Serviço para 
Exploração de Via_NFS-e Via 
 
 Nota Técnica Nº 006 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
22 de janeiro de 2026

## Página 2

2 
 
Sumário 
 
1. Introdução ................................................................................................................................................. 3 
2. Layouts da NFS-e Via ................................................................................................................................. 4 
3. Contingência para o início da emissão .................................................................................................... 13

## Página 3

3 
 
 
 
1. Introdução 
 
Em 30 de dezembro de 2025, foi publicada, no Diário Oficial da União, a Resolução CGNFS-
E Nº 9 que institui o modelo da Nota Fiscal de Serviço eletrônica de Exploração de Via de padrão 
nacional (NFS-e Via) como parte integrante do Sistema Nacional da Nota Fiscal de Serviço eletrônica 
de padrão nacional (NFS-e) de que trata o Convênio celebrado entre as administrações tributárias da 
União, do Distrito Federal e dos Municípios, publicado n o DOU de 1º de julho de 2022, Seção 3, 
página 56. 
A presente Nota Técnica objetiva ratificar a documentação publicada em 23/12/2025 no portal 
nacional da NFS-e e tornar pública a primeira versão do layout da Nota Fiscal de Serviço eletrônica 
para Exploração de Via – NFS-e Via - padrão nacional relacionados à tributação do Imposto sobre 
Bens e Serviços – IBS, da Contribuição sobre Bens e Serviços – CBS e demais tributos incidentes 
nas operações de serviços de exploração de via , também em atendimento às alterações previstas na 
Emenda Constitucional nº 132 de, 20 de dezembro de 2023, que deu ensejo à Reforma Tributária do 
Consumo – RTC. 
 A primeira versão do layout da NFS -e Via, presente no documento “ LeiautesRN_ADN-
SNNFSeVia_V1.0_Produção”, ab as “ Leiaute_NFSeVia-ADN_NFSeVia”, “RN_NFSeVia-
ADN_NFSeVia”, “ LEIAUTE_EVENTO-ADN_NFS-e_Via” e “RN_EVENTO-ADN_NFS-e_Via” 
que consta na sessão de documentação técnica no Portal da NFS-e: https://www.gov.br/nfse/pt-br/nfs-
e-via/documentacao-tecnica. 
 O layout ora divulgado  corresponde à primeira versão  desenvolvida em parceria com as 
concessionárias de exploração de via, após estudos técnicos realizados tomando como base os textos 
das Leis Complementares – LC nº 116/2003 de 31 de julho de 2003 e LC nº 214, de 16 de janeiro de 
2025. Sua divulgação objetiva dar transparência aos Estados, aos Municípios, às empresas prestadoras 
de serviço e de Tecnologia da Informação – TI e contribuintes do novo padrão que passa a vigorar a 
partir de 1º de janeiro de 2026.  
A modelagem da NFS-e Via compreende as seguintes etapas:  
1) a concessionária deve parametrizar, no Portal de Gestão  das Concessionárias 
(https://via.nfse.gov.br/concessionarias/login), os dados de concessão, abrangendo contratos, 
trechos, praças de cobrança, municípios e alíquotas tributárias; 
2) com base neste cadastro, o sistema define a alíquota efetiva por trecho para uso no layout.

## Página 4

4 
 
3) o emissor gera a nota em formato XML e transmite para o Ambiente Nacional da NFS-e; 
4) o Ambiente Nacional valida as regras de arquivo e conteúdo de forma síncrona, fornecendo a 
resposta da validação imediatamente ao emitente.  
Junto a esta nota técnica, foi também publicado o anexo na seção de documentação técnica do 
portal da NFS-e (https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica): 
 
LeiautesRN_ADN-SNNFSeVia_V1.00.02- o documento é  composto por 4 planilhas: 
“LeiauteRN_ADN-SNNFSeVia_V1.00.02-”, “Leiaute_NFSeVia-ADN_NFSeVia”, “RN_NFSeVia-
ADN_NFSeVia”, “LEIAUTE_EVENTO-ADN_NFS-e_Via” e “RN_EVENTO-ADN_NFS-e_Via” 
 
2. Layouts da NFS-e Via 
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
 
 
 
Layout da NFS-e Via – Versão 1.00 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
- NFS-e Via Raiz - - - - 
NFSeVia/ versao A C 1-1 1-4V2 Versão do leiaute da NFS-e Via. 
NFSeVia/ infNFSeVia G - 1-1 - Grupo de informações da NFS-e Via 
NFSeVia/infNFSeVia/ y ID C 1-1 53 
Informar o identificador precedido do literal ‘ID’. 
 
A formação do identificador de 53 posições da NFS-e 
Via é: 
 
"VIA" + 
Cód.da localidade/trecho (7) + 
Amb.Ger. (1) + 
Inscrição Federal (14) + 
nNFS-e Via (13) + 
serie (3) + 
AnoMes Emis. da NFS-e Via (4) + 
Cód.Num. (7) + 
DV (1) 
 
Código numérico de 7 Posições numérico, 
possivelmente aleatório, gerado pelo emitente. 
NFSeVia/infNFSeVia/ tpAmb E N 1-1 1 
Identificação do tipo de ambiente no Sistema Nacional 
NFS-e Via: 
1 - Produção; 
2 - Homologação; 
NFSeVia/infNFSeVia/ verAplic E C 1-1 1-20 Versão da aplicação que gerou a NFS-e Via 
NFSeVia/infNFSeVia/ cStat E N 1-1 3 
Situações possíveis: 
 
100 - NFS-e Via Gerada; 
101 - NFS-e Via de Substituição Gerada; 
102 - NFS-e Via de Decisão Judicial; 
NFSeVia/infNFSeVia dhEmi E D 1-1 8 
Data e hora da emissão da NFS-e Via. 
Data e hora no formato UTC (Universal Coordinated 
Time): 
AAAA-MM-DDThh:mm:ssTZD 
NFSeVia/infNFSeVia dhCompet E D 1-1 8 
Data e hora de competência da prestação do serviço: 
passagem veicular. 
Data e hora no formato UTC (Universal Coordinated 
Time): 
AAAA-MM-DDThh:mm:ssTZD 
NFSeVia/infNFSeVia/ subst G - 0-1 - Grupo de informações relativas à NFS-e Via a ser 
substituída 
NFSeVia/infNFSeVia/subst
/ chSubstda E C 1-1 50 Chave de Acesso da NFS-e Via a ser substituída.

## Página 7

7 
 
NFSeVia/infNFSeVia/subst
/ cMotivo E N 1-1 2 
Código de justificativa para substituição de NFS-e Via: 
 
03 - Inclusão Retroativa de Imunidade/Isenção para 
NFS-e Via; 
04 - Exclusão Retroativa de Imunidade/Isenção para 
NFS-e Via; 
05 - Rejeição de NFS-e Via pelo tomador ou pelo 
intermediário se responsável pelo recolhimento do 
tributo; 
06 - Alteração de parâmetros de cadastro do trecho da 
concessão; 
07 - Erro na identificação do veículo; 
99 - Outros; 
NFSeVia/infNFSeVia/subst
/ xMotivo E C 0-1 15-255 
Descrição do motivo da substituição da NFS-e Via 
quando o emitente deve descrever o motivo da 
substituição para outros motivos (cMotivo = 99). 
NFSeVia/infNFSeVia fornec G - 1-1 - Grupo de informações relativas ao 
fornecedor(prestador) do serviço 
NFSeVia/infNFSeVia/forne
c/ CNPJ CE C 1-1 14 Número da inscrição federal (CNPJ) do 
fornecedor(prestador) do serviço: concessionária 
NFSeVia/infNFSeVia/forne
c/ xNome E C 0-1 150 Nome / Nome Empresarial do fornecedor. 
NFSeVia/infNFSeVia/forne
c/ cMun E N 1-1 7 
Código do município do endereço do fornecedor do 
serviço. 
(Tabela do IBGE) 
NFSeVia/infNFSeVia/ serv G G 1-1 - Grupo de informações relativas ao serviço 
prestado. 
NFSeVia/infNFSeVia/serv/ cLocOper E N 1-1 7 
Código da localidade da operação (prestação) do 
serviço. 
Obs: Para a exploração de via, o local da operação 
(prestação) é o trecho de concessão de exploração de 
via para a qual a NFS-e Via foi emitida. Também é o 
local de incidência. O local da operação, para o IBS e 
para a CBS, será o mesmo local de incidência para o 
ISSQN. 
NFSeVia/infNFSeVia/serv/ xLocOper E C 1-1 150 
Descrição do código de 7 dígitos referente ao local da 
Operação(prestação) do serviço: nome dado ao trecho 
no cadastro pela concessionária. 
NFSeVia/infNFSeVia/ cPracaEmi E N 1-1 7 
Código da Praça de Pedágio, gerado no portal da 
Concessionária no momento do cadastro do trecho, 
onde a NFS-e Via foi emitida. 
NFSeVia/infNFSeVia/ xPracaEmi E C 1-1 150 Nome da Praça de Pedágio onde a NFS-e Via foi 
emitida. 
NFSeVia/infNFSeVia/ kmPracaEmi E N 1-1 7 Quilômetro da via onde está localizada a praça de 
pedágio. 
NFSeVia/infNFSeVia/ cLocEmi E N 1-1 7 Código de 7 dígitos do município (IBGE) onde está 
localizada a praça de pedágio.

## Página 8

8 
 
NFSeVia/infNFSeVia/ xLocEmi E C 1-1 150 Descrição do código de 7 dígitos do município (IBGE) 
onde está localizada a praça de pedágio. 
NFSeVia/infNFSeVia/ nNFSeVia E N 1-1 1-13 
Número sequencial, por praça e por equipamento, de 
pedágio, da NFS-eVIA gerado pelo emitente e tipo de 
emitente da NFS-eVIA. 
NFSeVia/infNFSeVia/ serie E C 1-1 3 
 
Uma série para cada praça e/ou equipamento ou 
número da pista de cobrança. 
NFSeVia/infNFSeVia/serv/ cTribNac E N 1-1 6 Código de tributação nacional do ISSQN. Valor fixo 
[220101] 
NFSeVia/infNFSeVia/serv/ cNBS E N 1-1 9 Código NBS correspondente ao serviço prestado. Valor 
Fixo [106042100] 
NFSeVia/infNFSeVia/se
rv/ explVia G - 1-1 - Grupo de informações relativas a atividades de 
Exploração de Rodovia 
NFSeVia/infNFSeVia/serv/
explVia/ categVeic E N 1-1 2 
Categorias de veículos para cobrança: 
 
00 - Categoria de Veículos (tipo não informado na nota 
de origem); 
01 - Automóvel, caminhonete e furgão - (2 eixos); 
02 - Caminhão leve, ônibus, caminhão trator e furgão - 
(2 eixos); 
03 - Automóvel e caminhonete com semireboque - (3 
eixos); 
04 - Caminhão, caminhão-trator, caminhão-trator com 
semi-reboque e ônibus - (3 eixos); 
05 - Automóvel e caminhonete com reboque - (4 
eixos); 
06 - Caminhão com reboque e caminhãotrator com 
semi-reboque - (4 eixos); 
07 - Caminhão com reboque e caminhãotrator com 
semi-reboque - (5 eixos); 
08 - Caminhão com reboque e caminhãotrator com 
semi-reboque - (6 eixos); 
09 - Caminhão com reboque e caminhãotrator com 
semi-reboque - (7 eixos); 
10 - Caminhão com reboque e caminhãotrator com 
semi-reboque - (8 eixos); 
11 - Motocicletas, motonetas e bicicletas motorizadas; 
12 - Veículo com gratuidade;  
99 - Cobrança Especial. 
NFSeVia/infNFSeVia/serv/
explVia/ sentido E C 1-1 1-3 
Orientação de passagem do veículo: 
 
Ângulo em graus a partir do norte geográfico em 
sentido horário, número inteiro de 0 a 359, onde 0º 
seria o norte, 90º o leste, 180º o sul, 270º o oeste. 
Precisão mínima de 10. 
NFSeVia/infNFSeVia/serv/
explVia/ placa E C 1-1 1 - 10 Placa do veículo até 10 caracteres. 
NFSeVia/infNFSeVia/serv/
explVia/ codAcessoPed E C 1-1 17 Código de acesso gerado automaticamente pelo 
sistema emissor da concessionária. 
NFSeVia/infNFSeVia/serv/
explVia/ 
modPassage
m E C 1-1 1 
Modalidade da Passagem: 
 
1 - Fluxo Livre 
2 - Manual 
3 - Automático 
4 - Semi-Automático 
5 - Outros

## Página 9

9 
 
NFSeVia/infNFSeVia/serv/
explVia/ codContrato E C 1-1 4 Código de contrato do cadastro da concessionária. 
NFSeVia/infNFSeVia/serv/
explVia/ xInfComp E C 0-1 2000 Campo livre para preenchimento pelo contribuinte. 
NFSeVia/infNFSeVia/ valores G - 1-1 - Grupo de informações relativas à valores do 
serviço prestado 
NFSeVia/infNFSeVia/valor
es/ vServ E N 1-1 1-15V2 Valor monetário do serviço (R$). 
NFSeVia/infNFSeVia/valor
es/ 
modPagamen
to E C 1-1 1 
Modalidade de pagamento: 
 
1. Débito ou pix 
2. Crédito 
3. Dinheiro 
4. Eletrônico 
5. Pagamento posterior 
NFSeVia/infNFSeVia/va
lores/ 
vDescCondI
ncond G - 0-1 - Grupo de informações relativas aos descontos 
condicionados e incondicionados 
NFSeVia/infNFSeVia/valor
es/vDescCondIncond/ vDescIncond E N 0-1 1-15V2 Valor monetário do desconto incondicionado (R$). 
NFSeVia/infNFSeVia/valor
es/vDescCondIncond/ vDescCond E N 0-1 1-15V2 Valor monetário do desconto condicionado (R$). 
NFSeVia/infNFSeVia/va
lores/ trib G - 1-1 - Grupo de informações relacionados aos tributos 
relacionados ao serviço prestado 
NFSeVia/infNFSeVia/va
lores/trib/ issqn G - 1-1 - Grupo de valores para o ISSQN 
NFSeVia/infNFSeVia/valor
es/trib/issqn/ vBC E N 1-1 1-15V2 
Valor da Base de Cálculo do ISSQN (R$) = Valor do 
Serviço - Desconto Incondicionado 
 
vBC = vServ - descIncond 
NFSeVia/infNFSeVia/valor
es/trib/issqn/ pAliq E N 1-1 1V2 Valor da alíquota efetiva (%) do serviço prestado 
resultante do cadastro do trecho pela concessionária. 
NFSeVia/infNFSeVia/valor
es/trib/issqn/ vISSQN E N 1-1 1-15V2 
Valor do ISSQN (R$) = Valor da Base de Cálculo x 
Alíquota 
 
vISSQN = vBC x pAliq 
NFSeVia/infNFSeVia/va
lores/trib/ tribFed G - 0-1 - Grupo de informações de outros tributos 
relacionados ao serviço prestado 
NFSeVia/infNFSeVia/va
lores/trib/tribFed/ piscofins G - 0-1 - Grupo de informações dos tributos PIS/COFINS

## Página 10

10 
 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ CST E N 1-1 2 
"Código de Situação Tributária do PIS/COFINS (CST): 
 
00 - Nenhum; 
01 - Operação Tributável com Alíquota Básica; 
02 - Operação Tributável com Alíquota Diferenciada; 
03 - Operação Tributável com Alíquota por Unidade de 
Medida de Produto; 
04 - Operação Tributável monofásica - Revenda a 
Alíquota Zero; 
05 - Operação Tributável por Substituição Tributária; 
06 - Operação Tributável a Alíquota Zero; 
07 - Operação Tributável da Contribuição; 
08 - Operação sem Incidência da Contribuição; 
09 - Operação com Suspensão da Contribuição;" 
49 - Operação sem cobrança; 
98 - Anulação; 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ vBCPisCofins E N 0-1 1-15V2 Valor da Base de Cálculo do PIS/COFINS (R$). 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ pAliqPis E N 0-1 1-2V2 Valor da Alíquota do PIS (%). 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ pAliqCofins E N 0-1 1-2V2 Valor da Alíquota da COFINS (%). 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ vPis E N 0-1 1-15V2 Valor monetário do PIS (R$). 
NFSeVia/infNFSeVia/valor
es/trib/tribFed/piscofins/ vCofins E N 0-1 1-15V2 Valor monetário do COFINS (R$). 
NFSeVia/infNFSeVia/va
lores/trib/ ibscbs G - 0-1 - Grupo de informações declaradas pelo emitente 
referentes ao IBS e à CBS 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ CST E N 1-1 3 Tabela da Código de Situação Tributária do IBS. Valor 
Fixo [000] 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ cClassTrib E N 1-1 6 Tabela de Código de classificação Tributária do IBS. 
Valor fixo [[000002] 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ cindOp E C 1-1 6 Tabela de Classificação do indicador da operação 
(AnexoVII-IndOp_IBSCBS). Valor fixo [080101] 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ vBC E N 1-1 1-15V2 
Valor da base de cálculo (BC) do IBS/CBS antes das 
reduções para cálculo do tributo bruto. 
 
vBC = vServ - descIncond – vISSQN – vPIS - vCOFINS 
(2026) 
 
ou 
 
vBC = vServ - descIncond – vISSQN (2027 até 2032) 
 
Utilizada a data de competência. 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ vLiq E N 1-1 1-15V2 
Valor líquido (R$) = Valor do serviço - Desconto 
condicionado - Desconto incondicionado - Valores, se 
retidos (ISSQN, PIS, COFINS)** 
 
VLiq = vServ – vDescIncond – vDescCond – (vISSQN + 
vPIS + vCOFINS)** 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/ vTotNF E N 1-1 1-15V2 
Valor Total da NF considerando os impostos por fora 
IBS e CBS. 
O IBS e a CBS são por fora, por isso seus valores 
devem ser adicionados ao valor total da NF. 
 
vTotNF = VLiq + vCBS + vIBSTot 
NFSeVia/infNFSeVia/va
lores/trib/ibscbs/ gIBS G - 1-1 - Grupo de Informações relativas aos valores do 
IBS Estadual

## Página 11

11 
 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gIBS/ vIBSTot E N 1-1 1-15V2 
Total Valor do IBS Total. 
 
vIBSTot = vIBSUF + vIBSMun 
NFSeVia/infNFSeVia/va
lores/trib/ibscbs/gIBS
/ 
uf G - 1-1 - Grupo de Informações relativas aos valores do 
IBS Estadual 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gIBS/uf/ pAliqEfetUF E N 1-1 1-2V2 
Alíquota efetiva para IBS das UFs da localidade de 
incidência/operação cadastrada: trecho. 
 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gIBS/uf/ vIBSUF E N 1-1 1-15V2 
Total valor do IBS estadual. 
 
vIBSUF = vBC x pAliqEfetUF 
NFSeVia/infNFSeVia/va
lores/trib/ibscbs/gIBS
/ 
mun G    Grupo de Informações relativas aos valores do 
IBS Municipal 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gIBS/mun/ pAliqEfetMun E N 1-1 1-2V2 
Alíquota efetiva para IBS dos Municípios da localidade 
de incidência/operação cadastrada: trecho. 
 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gIBS/mun/ vIBSMun E N 1-1 1-15V2 
Total valor do IBS municipal. 
 
vIBSMun = vBC x pAliqEfetMun 
NFSeVia/infNFSeVia/va
lores/trib/ibscbs/ gCBS G - 1-1 - Grupo de Informações relativas aos valores da 
CBS 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gCBS/ pAliq E N 1-1 1-2V2 Alíquota da União para a CBS Cadastrada 
 
NFSeVia/infNFSeVia/valor
es/trib/ibscbs/gCBS/ vCBS E N 1-1 1-15V2 
Total valor da CBS da União. 
 
vCBS = vBC x pAliq 
NFSeVia/ Signature G - 1-1 - Assinatura XML da NFS-e Via segundo o padrão 
XML digital signature 
 dhReg     
Data/Hora da recepção da NFS-e Via. 
Data e hora no formato UTC (Universal Coordinated 
Time): 
AAAA-MM-DDThh:mm:ssTZD 
 nReg     "Número do Registro" da NFS-e Via

## Página 12

12 
 
Layout do Evento de cancelamento da NFS-e Via – Versão 1.00 
 
CAMINHO NO XML CAMPO ELE TIPO OCOR. TAM. DESCRIÇÃO 
 evento Raiz - - - TAG raiz 
evento/ versao A C 1-1 1-4V2 Versão do leiaute do evento 
evento/ infEvento G - 1-1 - c 
evento/infEvento/ id ID C 1-1 62 O identificador do evento é composto pela 
concatenação de campos que constam no leiaute. 
 
A formação deste identificador considera o literal 
"EVT" associado a outras 59 posições numéricas, 
conforme descrito abaixo: 
 
"EVT" + 
Chave de acesso da NFS-e Via (50) + Código do 
Evento (06) + 
Número sequencial do evento (nSeqEvento) (03) 
 
O código do evento corresponde ao valor informado 
na tag infEvento sem a primeira posição: 
Cancelamento de NFS-e Via - tag e101101 - código do 
evento 101101 
Cancelamento de NFS-e Via por substituição - tag 
e105102 - código do evento 105102 
evento/infEvento/ verAplic E C 0-1 1-20 Versão do aplicativo que gerou o evento. 
evento/infEvento/ nSeqEvento E N 1-1 3 Número sequencial do evento para o mesmo tipo de 
evento. 
 
Para os eventos que ocorrem somente uma vez, como 
é o caso do cancelamento, o nSeqEvento = 001. 
 
Para os eventos que possam existir mais de um 
evento do mesmo tipo o ambiente gerador deverá 
numerar de forma sequencial. 
evento/infEvento/ chNFSeVia CE N 1-1 50 Identificador da NFS-e a qual o evento será vinculada. 
evento/infEvento/ dhEvento E D 1-1 - Data e hora do evento no formato AAAA-MM-
DDThh:mm:ssTZD (UTC - Universal Coordinated 
Time, onde TZD pode ser -02:00 (Fernando de 
Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no 
horário de verão serão -01:00, -02:00 e -03:00. Ex.: 
2010-08-19T13:00:15-03:00. 
evento/infEvento/ tpAmb E N 1-1 1 
Tipo de ambiente: 
 
1 - Produção; 
2 - Homologação; 
evento/infEvento/ e101101 CG - 1-1 - Parte Específica do Registro de Evento 
Evento Cancelamento de NFS-e 
evento/infEvento/e101
101/ 
xDesc E C 1-1 5-60 Descrição do evento: 
"Cancelamento de NFS-e" 
evento/infEvento/e101
101/ 
cMotivo E N 1-1 1 Código de justificativa de cancelamento: 
 
2 - Serviço não Prestado; 
evento/infEvento/e101
101/ 
xMotivo E C 1-1 15-255 Descrição para explicitar o motivo indicado neste 
evento. 
evento/infEvento/ e105102 CG - 1-1 - Parte Específica do Registro de Evento 
Cancelamento de NFS-e por Substituição 
evento/infEvento/e105
102/ 
xDesc E C 1-1 5-60 Descrição do evento: 
"Cancelamento de NFS-e por Substituição"

## Página 13

13 
 
evento/infEvento/e105
102/ 
cMotivo E N 1-1 1 Código de justificativa de cancelamento substituição: 
 
1 - Erro na Emissão 
evento/infEvento/e105
102/ 
xMotivo E C 0-1 15-255 Descrição para explicitar o motivo indicado neste 
evento. 
 
 
evento/infEvento/e105
102/ 
chSubstituta E C 1-1 50 Chave de Acesso da NFS-e substituta. 
evento/ Signature G - 1-1 - Assinatura do registro segundo o Padrão XML 
Digital Signature. 
 dhReg     Data/Hora da recepção do Evento de NFS-e Via. 
Data e hora no formato UTC (Universal Coordinated 
Time): 
AAAA-MM-DDThh:mm:ssTZD 
 nReg     "Número do Registro" do Evento da NFS-e Via 
 
3. Contingência para o início da emissão  
 Em caráter excepcional, a emissão das Notas Fiscais de Serviço eletrônicas de 
Exploração de Via (NFS -e Via) relativas às operações realizadas no mês de janeiro de 2026 será 
admitida até o dia 31 de janeiro de 2026, como medida de contingência para o início da 
obrigatoriedade. 
 
 
 
Carlos Eduardo Burkle 
Auditor-Fiscal de Tributos – Londrina (PR) 
Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço 
Eletrônica de Padrão Nacional (SE/CGNFS-e)
