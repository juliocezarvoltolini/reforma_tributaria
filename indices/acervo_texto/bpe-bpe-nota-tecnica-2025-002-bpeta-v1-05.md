---
id: bpe-bpe-nota-tecnica-2025-002-bpeta-v1-05
titulo: Nota Técnica BPe - Nota_Técnica_2025_002 - RTC_v1.05 - Publicada em 26/01/2026
tipo: nota.tecnica
versao: '1.05'
data: '2026-01-26'
documento_fiscal: BP-e
url: https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=sSiH9KMw5Wg=
arquivo_original: fontes/acervo/bpe-bpe-nota-tecnica-2025-002-bpeta-v1-05.pdf
sha256_original: a1ade875d5151a985033d9b8488a66609406e3fac8cb2f80286fd62c6e85ff5a
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 559c5d67654cb2200b990d3b5b6f9ffbf48264e14bdaac45e6000dad9b7e4c97
---

## Página 1

Projeto Bilhete de Passagem 
Eletrônico 
 
BPe Transporte Aéreo  
Nota Técnica 2025.002 
 
 
 
 
 
 
 
 
Versão 1.05 – 22 de janeiro de 2026

## Página 2

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 2 / 80  
 
Sumário 
 
1 Base Conceitual ...................................................................................... ................................................... ................................................... .. 6 
1.1  Conceitos ............................................................................................................................................................. 6 
 BPe TA (modelo 63) ................................................................................................................................................................................................... 6 
 DABPE ....................................................................................................................................................................................................................... 6 
 Chave de Acesso do BPe TA ..................................................................................................................................................................................... 6 
 Chave Natural do BPe TA .......................................................................................................................................................................................... 7 
2 Arquitetura de Comunicação com Contribuinte .......................................................... ................................................... .................................. 8 
2.1  Modelo Conceitual ............................................................................................................................................... 8 
2.2  Padrões Técnicos ................................................................................................................................................ 9 
 Padrão de documento XML ....................................................................................................................................................................................... 9 
 Padrão de Comunicação .......................................................................................................................................................................................... 10  
 Padrão de Certificado Digital ................................................................................................................................................................................... 11  
 Padrão da Assinatura Digital .................................................................................................................................................................................... 11  
 Validação da Assinatura Digital pelo Ambiente Autorizador .................................................................................................................................... 13  
 Resumo dos Padrões Técnicos ............................................................................................................................................................................... 14  
2.3  Modelo Operacional ........................................................................................................................................... 14  
2.4  Padrão de Mensagens dos Web Services ......................................................................................................... 15  
 Área de dados das mensagens ............................................................................................................................................................................... 15  
 Validação da estrutura XML das Mensagens dos Web Services ............................................................................................................................ 15  
 Schemas XML das Mensagens dos Web Services ................................................................................................................................................. 16  
2.5  Versão dos Schemas XML ................................................................................................................................ 17  
 Liberação das versões dos schemas para o BPe TA .............................................................................................................................................. 17  
 Correção de Pacote de Liberação ........................................................................................................................................................................... 17  
 Divulgação de novos Pacotes de Liberação ............................................................................................................................................................ 17  
 Controle de Versão .................................................................................................................................................................................................. 18  
2.6  Sistema de Registro de Eventos........................................................................................................................ 18 
 Relação dos Tipos de Evento .................................................................................................................................................................................. 19  
 Eventos de Marcação............................................................................................................................................................................................... 19

## Página 3

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 3 / 80  
 
2.7  Data e hora de emissão e outros horários ......................................................................................................... 20  
2.8  SEFAZ virtual .................................................................................................................................................... 20  
3 Regras de Validações Gerais do BPe ................................................................... ................................................... ..................................... 21  
 Grupo A: Validação do Certificado de Transmissão (protocolo TLS) ...................................................................................................................... 21  
 Grupo B-0: Validação da Compactação da Mensagem ........................................................................................................................................... 22  
 Grupo B: Validação Inicial da Mensagem no Web Service ..................................................................................................................................... 22  
 Grupo C: Validação da área de dados da mensagem ............................................................................................................................................. 22  
 Grupo D: Validações do Certificado de Assinatura Digital....................................................................................................................................... 23  
 Grupo E: Validações da Assinatura Digital .............................................................................................................................................................. 23  
4 Web Services ......................................................................................... ................................................... ................................................... . 24  
4.1  WebService Síncrono de Recepção BPe TA ..................................................................................................... 25  
 Leiaute Mensagem de Entrada ................................................................................................................................................................................ 25  
 Leiaute Mensagem de Retorno ................................................................................................................................................................................ 25  
 Leiaute de BPe processado ..................................................................................................................................................................................... 26  
 Regras de Validação Básicas do Serviço ................................................................................................................................................................ 27  
 Regras de Negócio do BPe TA ................................................................................................................................................................................ 27  
 Final do Processamento do BPe TA ........................................................................................................................................................................ 44 
4.2  Serviço de Consulta Situação do BPe ............................................................................................................... 45  
 Leiaute Mensagem de Entrada ................................................................................................................................................................................ 45  
 Leiaute Mensagem de Retorno ................................................................................................................................................................................ 45  
 Descrição do Processo de Web Service .................................................................................................................................................................. 46  
 Regras de Validação Básicas do Serviço ................................................................................................................................................................ 46  
 Validação das Regras de Negócio da Consulta Situação ....................................................................................................................................... 46  
 Final do Processamento .......................................................................................................................................................................................... 47  
4.3  Serviço de Consulta Status do Serviço de Autorização ..................................................................................... 48  
 Leiaute Mensagem de Entrada ................................................................................................................................................................................ 48  
 Leiaute Mensagem de Retorno ................................................................................................................................................................................ 48  
 Descrição do Processo de Web Service .................................................................................................................................................................. 49  
 Regras de Validação Básicas do Serviço ................................................................................................................................................................ 49  
 Validação das Regras de Negócio da Consulta Status Serviço .............................................................................................................................. 50  
 Final do Processamento .......................................................................................................................................................................................... 50  
5 Sistema de Registro de Eventos (Parte Geral) ......................................................... ................................................... .................................. 51  
5.1  Leiaute Mensagem de Entrada .......................................................................................................................... 51

## Página 4

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 4 / 80  
 
5.2  Leiaute Mensagem de Retorno ......................................................................................................................... 52  
5.3  Descrição do Processo de Web Service ............................................................................................................ 53  
5.4  Regras de Validação Básicas do Serviço .......................................................................................................... 53  
5.5  Validação das Regras de Negócio do Serviço de Registro de Eventos............................................................. 53  
5.6  Processamento das validações específicas de cada evento ............................................................................. 55  
5.7  Final do Processamento do Evento ................................................................................................................... 55  
6 Sistema de Registro de Eventos (Parte Específica) .................................................... ................................................... ............................... 56  
6.1  Evento de Cancelamento .................................................................................................................................. 56  
 Validação das Regras Específicas do Evento ......................................................................................................................................................... 56  
 Final do Processamento .......................................................................................................................................................................................... 57  
6.2  Evento de Não Embarque ................................................................................................................................. 58  
 Validação das Regras Específicas do Evento ......................................................................................................................................................... 58  
 Final do Processamento .......................................................................................................................................................................................... 58  
6.3  Evento de Fornecimento não realizado com pagamento antecipado ................................................................ 59  
 Validação das Regras Específicas do Evento ......................................................................................................................................................... 59  
 Final do Processamento .......................................................................................................................................................................................... 59  
6.4  Evento de Ajuste do BPe TA – PENDENTE DE ESPECICAÇÂ O ..................................................................... 60  
 Validação das Regras Específicas do Evento ......................................................................................................................................................... 60  
 Final do Processamento .......................................................................................................................................................................................... 60  
7 Alterações no Serviço de Recepção de BPe e BPeTM ..................................................... ................................................... ......................... 61  
8 Informações Adicionais ............................................................................... ................................................... ............................................... 62  
8.1  Código de Classificação Tributária do IBS/CBS ................................................................................................ 62  
8.2  Cálculo do dígito verificador do CNPJ Alfanumérico ......................................................................................... 62  
 Cálculo do primeiro dígito verificador ....................................................................................................................................................................... 63  
 Cálculo do segundo dígito verificador ...................................................................................................................................................................... 64  
8.3  Cálculo do dígito verificador da chave de acesso do BPe TA ........................................................................... 65  
8.4  Número do protocolo ......................................................................................................................................... 66  
9 Leiaute do BPe TA .................................................................................... ................................................... ................................................. 67

## Página 5

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 5 / 80  
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação Implantação Produção 
1.00 • Implantação do serviço de autorização do BPe TA  
 - - 
1.01 • Ajustes nos campos do IBS/CBS e Regras de validação   
1.02 
• Ajuste na explicação da regra de valor do tributo negativo 
• IE do Emitente passa para ser campo opcional e validado se informado e necessário quando existir o par CNPJ e IE no 
cadastro da UF 
  
1.03 • Desativação das regras de validação da IE   
1.04 • Esclarecimento do preenchimento do campo vTotDFe   
1.04 a • Excluída observação da regra F70   
1.04 b  • Correção na regra de redução de alíquota   
1.05 • Tag vTotDFe obrigatória Já implantado Já implantado

## Página 6

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 6 / 80  
 
1 Base Conceitual 
1.1 Conceitos 
 BPe TA (modelo 63) 
 
Bilhete de Passagem Eletrônico para Transporte Aére o é o documento emitido e armazenado eletronicament e, de existência apenas digital, cuja validade jurí dica é garantida 
pela assinatura digital do emitente e autorização de uso pelo ambiente nacional do BPe. 
 DABPE 
 
O DABPE (Documento Auxiliar do Bilhete de Passagem Eletrônico) é um documento auxiliar impresso em papel e sua especificação/modelos de leiaute encontram-se disponíveis 
no documento Anexo II: Manual de Orientações do Contribuinte – DABPE. 
 Chave de Acesso do BPe TA 
 
A Chave de Acesso do BPe TA é composta pelos seguintes campos que se encontram dispersos no leiaute do BPe TA: 
 Código 
da UF 
AAMM da 
emissão 
CNPJ do 
Emitente 
Modelo 
(mod) 
Série 
(serie) 
Número 
do BPe 
Forma de 
emissão  
Código 
Numérico 
DV 
Quantidade de 
caracteres  
02 04 14 02 03 09 01 08 01 
  
• cUF  - Código da UF do emitente do Documento Fiscal 
• AAMM  - Ano e Mês de emissão da NFAg 
• CNPJ  - CNPJ do emitente 
• mod  - Modelo do Documento Fiscal 
• serie  - Série do Documento Fiscal 
• nBP  - Número do Documento Fiscal 
• tpEmis - forma de emissão  
• cBP  - Código Numérico que compõe a Chave de Acesso  
• cDV  - Dígito Verificador da Chave de Acesso

## Página 7

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 7 / 80  
 
 Chave Natural do BPe TA 
 
A Chave Natural do BPe TA é composta pelos campos d e UF, CNPJ do Emitente, Série e Número do BPe TA, a lém do modelo do documento fiscal eletrônico e da f orma de 
emissão. O Sistema de Autorização de Uso validará a existência de um BPe TA previamente autorizado e rejeitará novos pedidos de autorização para BPe TA com duplicidade 
da Chave Natural, quando autorizados no mesmo ambiente de autorização. A informação da Forma de Emissão pode indicar ambientes alternativos de autorização do Ambiente 
Nacional.

## Página 8

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 8 / 80  
 
2 Arquitetura de Comunicação com Contribuinte 
2.1 Modelo Conceitual 
 
O ambiente autorizador de BPe irá disponibilizar os seguintes serviços: 
a) Recepção de BPe TA (Modelo 63) – Modelo síncrono  (uma BPe); 
b) Consulta da Situação Atual do BPe TA; 
c) Consulta do status do serviço. 
d) Registro de Eventos 
 
Para cada serviço oferecido existirá um Web Service  específico. O fluxo de comunicação é sempre inicia do pelo aplicativo do contribuinte através do envio  de uma mensagem 
ao Web Service com a solicitação do serviço desejado. 
O Web Service sempre devolve uma mensagem de resposta confirmando o recebimento da solicitação de serviço ao aplicativo do contribuinte na mesma conexão. 
O processamento da solicitação de serviço é concluído na mesma conexão, com a devolução de uma mensagem com o resultado do processamento do serviço solicitado; 
O diagrama a seguir ilustra o fluxo conceitual de comunicação entre o aplicativo do contribuinte e o Ambiente Autorizador: 
 
Contribuinte  
Ambiente Autorizador  
Cliente BPe  
( 
 ERP ou software específico ) 
BPe  
Aplicativo de Faturamento  
( 
 ERP ou software específico ) 
HTTPS  
Fluxo de  
Comunicação  
Serviços  
Síncronos  
Aplicação BPe  
BPe  
Arquitetura de Comunicação – Visão Conceitual  
Web Services  Transações

## Página 9

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 9 / 80  
 
2.2 Padrões Técnicos 
 Padrão de documento XML 
 
a) Padrão de Codificação 
A especificação do documento XML adotada é a recome ndação W3C para XML 1.0, disponível em www.w3.org/T R/REC-xml e a codificação dos caracteres será em UT F-8, 
assim todos os documentos XML serão iniciados com a seguinte declaração: 
<?xml version="1.0" encoding="UTF-8"?> 
 
OBS: Lembrando que cada arquivo XML somente poderá ter uma única declaração <?xml version="1.0" encoding="UTF-8"?>. 
b) Declaração namespace 
O documento XML deverá ter uma única declaração de namespace no elemento raiz do documento com o seguinte padrão: 
<BPeTA xmlns=”http://www.portalfiscal.inf.br/bpe” > (exemplo para o XML do BPe TA)  
 
O uso de declaração namespace diferente do padrão estabelecido para o Projeto é vedado. 
A declaração do namespace da assinatura digital deverá ser realizada na própria tag <Signature>, conforme exemplo abaixo. 
c) Prefixo de namespace 
Não é permitida a utilização de prefixos de namespace. Essa restrição visa otimizar o tamanho do arquivo XML. 
Assim, ao invés da declaração: 
<BPe:BPeTA xmlns:BPe=”http://www.portalfiscal.inf.br/bpe”>  (exemplo para o XML do BPe TA com prefixo BPe) deverá ser adotada a declaração: 
<BPeTA xmlns =”http://www.portalfiscal.inf.br/bpe” > 
 
d) Otimização na montagem do arquivo 
Na geração do arquivo XML do BPe TA, excetuados os campos identificados como obrigatórios no modelo (p rimeiro dígito da coluna de ocorrências do leiaute iniciada com 1, 
ex.: 1-1, 1-2, 1-N), não deverão ser incluídas as TAGs de campos com conteúdo zero (para campos tipo numérico) ou vazio (para campos tipo caractere). 
Na geração do arquivo XML do BPe TA, deverão ser pr eenchidas no modelo apenas as TAGs de campos identificados como obrigatórios no leiaute ou os campos obrigatórios 
por força da legislação pertinente. Os campos obrigatórios no leiaute são identificados pelo primeiro dígito da coluna ocorrência (“Ocorr”) que inicie com 1, ex.: 1-1, 1-2, 1-N. Os 
campos obrigatórios por força da legislação pertinente devem ser informados, mesmo que no leiaute seu preenchimento seja facultativo.

## Página 10

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 10  / 80  
 
A regra constante do parágrafo anterior deverá estender-se para os campos onde não há indicação de obrigatoriedade e que, no entanto, seu preenchimento torna-se obrigatório 
por estar condicionado à legislação específica ou ao negócio do contribuinte. Neste caso, deverá constar a TAG com o valor correspondente e, para os demais campos, deverão 
ser eliminadas as TAGs. 
Para reduzir o tamanho final do arquivo XML do BPe TA alguns cuidados de programação deverão ser assumidos: 
• Não incluir "zeros não significativos" para campos  numéricos; 
• Não incluir "espaços" ("line-feed", "carriage retu rn", "tab", caractere de "espaço" entre as TAGs) no início ou no final de campos numéricos e alfanuméricos; 
• Não incluir comentários no arquivo XML; 
• Não incluir anotação e documentação no arquivo XML  (TAG annotation e TAG documentation); 
• Não incluir caracteres de formatação no arquivo XM L ("line-feed", "carriage return", "tab", caractere de "espaço" entre as TAGs). 
 
e) Validação de Schema 
Para garantir minimamente a integridade das informações prestadas e a correta formação dos arquivos XML, o contribuinte deverá submeter o arquivo do BPe TA e as demais 
mensagens XML para validação pelo Schema (XSD – XML  Schema Definition), disponibilizado pelo Ambiente Autorizador, antes de seu envio. 
 Padrão de Comunicação 
 
A comunicação entre o contribuinte e o Ambiente de Autorização será baseada em Web Services disponíveis no Portal da SEFAZ Virtual. 
O meio físico de comunicação utilizado será a Internet, com o uso do protocolo TLS versão 1.2, com autenticação mútua, que além de garantir um duto de comunicação seguro 
na Internet, permite a identificação do servidor e do cliente através de certificados digitais, eliminando a necessidade de identificação do usuário através de nome ou código de 
usuário e senha. 
O modelo de comunicação segue o padrão de Web Services definido pelo WS-I Basic Profile. 
A troca de mensagens entre os Web Services do Ambiente Autorizador e o aplicativo do contribuinte será realizada no padrão SOAP versão 1.2, com troca de mensagens XML 
no padrão Style/Enconding: Document/Literal. 
A chamada dos diferentes Web Services do Projeto BPe é realizada com o envio de uma mensagem através do campo BPeDadosMsg. 
A resposta do processamento da requisição pela aplicação do ambiente autorizador será realizada através de uma mensagem XML através do campo BPeResultMsg

## Página 11

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 11  / 80  
 
 Padrão de Certificado Digital 
 
O certificado digital utilizado no Projeto do BPe TA será emitido por Autoridade Certificadora credenciada pela Infraestrutura de Chaves Públicas Brasileira – ICP-Brasil, tipo A1 
ou A3, devendo conter o CNPJ da pessoa jurídica titular do certificado digital. Os certificados digitais serão exigidos em 3 (três) momentos distintos para o projeto: 
a) Assinatura de Mensagens: O certificado digital utilizado para essa função de verá conter o CNPJ de um dos estabelecimentos da em presa emissora do BPe TA. Por 
mensagens, entenda-se: o Pedido de Autorização de U so (Arquivo BPe TA), o Registro de Eventos de BPe e  demais arquivos XML que necessitem de assinatura. O 
certificado digital deverá ter o “uso da chave” previsto para a função de assinatura digital e atributo de "não recusa" obrigatoriamente com o CNPJ no campo otherName 
OID = 2.16.76.1.3.3, respeitando a Política do Certificado. 
b) Transmissão  (durante a transmissão das mensagens entre o servi dor do contribuinte e o Ambiente Autorizador): O ce rtificado digital utilizado para identificação do 
aplicativo do contribuinte deverá conter o CNPJ do responsável pela transmissão das mensagens, mas não necessita ser o mesmo CNPJ do estabelecimento emissor 
do BPe TA, devendo ter a extensão Extended Key Usage com permissão de "Autenticação Cliente". 
c) Geração do QR Code do BPe TA: O certificado digital utilizado para a assinatura do BPe TA deverá ser utilizado para assinar a chave de acesso do BPe TA na geração 
do QR Code na hipótese de emissão off-line, conforme será descrito em item futuro deste manual. 
 Padrão da Assinatura Digital 
 
As mensagens enviadas ao Ambiente Autorizador são d ocumentos eletrônicos elaborados no padrão XML e de vem ser assinados digitalmente com um certificado d igital que 
contenha o CNPJ do estabelecimento matriz ou o CNPJ  do estabelecimento emissor do BPe TA objeto do ped ido. Os elementos abaixo estão presentes dentro do Certificado 
do contribuinte tornando desnecessária a sua representação individualizada no arquivo XML. Portanto, o arquivo XML não deve conter os elementos:  
<X509SubjectName>  
<X509IssuerSerial>  
<X509IssuerName>  
<X509SerialNumber>  
<X509SKI>  
Deve-se evitar o uso das TAGs relacionadas a seguir, pois as informações serão obtidas a partir do Certificado do emitente: 
<KeyValue> 
<RSAKeyValue>  
<Modulus>  
<Exponent>

## Página 12

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 12  / 80  
 
O Projeto BPe TA utiliza um subconjunto do padrão de assinatura XML definido pelo http://www.w3.org/TR/xmldsig-core/ , que tem o seguinte leiaute: 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
XS01  Signature Raiz - - - -  
XS02  SignedInfo G XS01 - 1-1  Grupo da Informação da ass inatura 
XS03  CanonicalizationMethod G XS02 - 1-1  Grupo do Métod o de Canonicalização 
XS04 Algorithm A XS03 C 1-1  Atributo Algorithm de Canon icalizationMethod: 
http://www.w3.org/TR/2001/REC-xml-c14n-20010315  
XS05  SignatureMethod G XS02 - 1-1  Grupo do Método de As sinatura 
XS06 Algorithm A XS05 C 1-1  Atributo Algorithm de Signe dMethod: 
http://www.w3.org/2000/09/xmldsig#rsa-sha1  
XS07  Reference G XS02 - 1-1  Grupo de Reference 
XS08  URI A XS07 C 1-1  Atributo URI da tag Reference 
XS10  Transforms G XS07 - 1-1  Grupo do algorithm de Tran sform 
XS11  unique_Transf_Alg RC XS10 - 1-1  Regra para o atrib uto Algorithm do Transform ser único. 
XS12  Transform G XS10 - 2-2  Grupo de Transform 
XS13 Algorithm A XS12 C 1-1  Atributos válidos Algorithm  do Transform: 
http://www.w3.org/TR/2001/REC-xml-c14n-20010315  
http://www.w3.org/2000/09/xmldsig#enveloped-signature 
XS14  XPath E XS12 C 0-N  XPath 
XS15  DigestMethod G XS07 - 1-1  Grupo do Método de Diges tMethod 
XS16 Algorithm A XS15 C 1-1  Atributo Algorithm de Diges tMethod: 
http://www.w3.org/2000/09/xmldsig#sha1  
XS17  DigestValue E XS07 C 1-1  Digest Value (Hash SHA-1 – Base64) 
XS18  SignatureValue G XS01 - 1-1  Grupo do Signature Val ue 
XS19  KeyInfo G XS01 - 1-1  Grupo do KeyInfo 
XS20  X509Data G XS19 - 1-1  Grupo X509 
XS21  X509Certificate E XS20 C 1-1  Certificado Digital x 509 em Base64 
 
A assinatura do Contribuinte no BPe TA será feita n a TAG <infBPe> identificada pelo atributo Id , cujo conteúdo deverá ser um identificador único ( chave de acesso) precedido 
do literal ‘BPe’ para a BPe, conforme leiaute descr ito no Anexo I. O identificador único precedido do literal ‘#BPe’ deverá ser informado no atributo URI  da TAG <Reference>. 
Para as demais mensagens a serem assinadas, o processo será o mesmo mantendo sempre um identificador único para o atributo Id  na TAG a ser assinada.  
 
Para o processo de assinatura, o contribuinte não d eve fornecer a Lista de Certificados Revogados, já que ela será montada e validada no Ambiente Autoriz ador no momento 
da conferência da assinatura digital.

## Página 13

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 13  / 80  
 
A assinatura digital do documento eletrônico deverá atender aos seguintes padrões adotados: 
• Padrão de assinatura:  “XML Digital Signature”, utilizando o formato “Env eloped”  (http://www.w3.org/TR/xmldsig-core/ ); 
• Certificado digital:  Emitido por AC credenciada no ICP-Brasil ( http://www.w3.org/2000/09/xmldsig#X509Data );  
• Cadeia de Certificação:  EndCertOnly (Incluir na assinatura apenas o certificado do usuário final);  
• Tipo do certificado:  A1 ou A3 (o uso de HSM é recomendado);  
• Tamanho da Chave Criptográfica:  Compatível com os certificados A1 e A3 (1024 bits);  
• Função criptográfica assimétrica:  RSA ( http://www.w3.org/2000/09/xmldsig#rsa-sha1 ); 
• Função de “message digest” : SHA-1 ( http://www.w3.org/2000/09/xmldsig#sha1 ); 
• Codificação : Base64 ( http://www.w3.org/2000/09/xmldsig#base64 ); 
• Transformações exigidas : Útil para realizar a canonicalização do XML enviado para realizar a validação correta da Assinatura Digital. São elas: 
(1) Enveloped ( http://www.w3.org/2000/09/xmldsig#enveloped-signature ) 
(2) C14N ( http://www.w3.org/TR/2001/REC-xml-c14n-20010315 ) 
 Validação da Assinatura Digital pelo Ambiente Autorizador 
 
Para a validação da assinatura digital, seguem as regras que serão adotadas pelo Ambiente Autorizador: 
(1) Extrair a chave pública do certificado; 
(2) Verificar o prazo de validade do certificado ut ilizado; 
(3) Montar e validar a cadeia de confiança dos cert ificados validando também a LCR (Lista de Certificados Revogados) de cada certificado da cadeia; 
(4) Validar o uso da chave utilizada (Assinatura Di gital) de tal forma a aceitar certificados somente do tipo A (não serão aceitos certificados do tipo S); 
(5) Garantir que o certificado utilizado é de um us uário final e não de uma Autoridade Certificadora; 
(6) Adotar as regras definidas pelo RFC 3280 para L CRs e cadeia de confiança; 
(7) Validar a integridade de todas as LCR utilizada s pelo sistema; 
(8) Prazo de validade de cada LCR utilizada (verifi car data inicial e final). 
A forma de conferência da LCR pode ser feita de 2 ( duas) maneiras: On-line ou Download periódico. As a ssinaturas digitais das mensagens serão verificadas  considerando a 
lista de certificados revogados disponível no momento da conferência da assinatura.

## Página 14

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 14  / 80  
 
 Resumo dos Padrões Técnicos 
 
Característica Descrição 
Web Services  Padrão definido pelo WS-I Basic Profile 1.1 ( http://www.ws-i.org/Profiles/BasicProfile-1.1-2004-08-24.html ). 
Meio lógico de comunicação  Web Services, disponibilizados pelo AMBIENTE AUTORIZADOR  
Meio físico de comunicação  Internet 
Protocolo Internet  TLS versão 1.2, com autenticação mútua através de certificados digitais. 
Padrão de troca de mensagens  SOAP versão 1.2   
Padrão da mensagem  XML no padrão Style/Encoding: Document/Literal. 
Padrão de certificado digital X.509 versão 3, emitido por Autoridade Certificadora credenciada pela Infra-estrutura de Chaves Públicas Brasileira – 
ICP-Brasil, do tipo A1 ou A3, devendo conter o CNPJ do proprietário do certificado digital. 
Para assinatura de mensagens, utilizar o certificado digital de um dos estabelecimentos da empresa emissora de BPe. 
Para transmissão, utilizar o certificado digital do responsável pela transmissão. 
Padrão de assinatura digital XML Digital Signature, Enveloped, com certificado digital X.509 versão 3, com chave privada de 1024 bits, com padrões 
de criptografia assimétrica RSA, algoritmo message digest SHA-1 e utilização das transformações Enveloped e C14N. 
Validação de assinatura digital  Será validada além da integridade e autoria, a cadeia de confiança com a validação das LCRs. 
Padrões de preenchimento XML Campos não obrigatórios do Schema que não possuam conteúdo terão suas tags suprimidas no arquivo XML. 
Máscara de números decimais e datas estão definidas no Schema XML. 
Nos campos numéricos inteiro, não incluir a vírgula ou ponto decimal. 
Nos campos numéricos com casas decimais, utilizar o “ponto decimal” na separação da parte inteira. 
2.3 Modelo Operacional 
 
As solicitações de serviços do BPe TA seguem o mode lo de implementação síncrona processadas imediatame nte e o resultado do processamento é obtido em uma única 
conexão. 
A seguir, o fluxo simplificado de funcionamento: 
 
 
 
Aplicativo 
Cliente 
 Web Service 
Processamento 
de Serviços 
(1) Solicitação de  serviço  
 (2) Solicitação de serviço 
(4) Resultado 
 (3) Resultado 
Contribuinte 
  Secretaria de Fazenda Estadual 
Serviço de Implementação Síncrona

## Página 15

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 15  / 80  
 
Etapas do processo ideal: 
 
(1) O aplicativo do contribuinte inicia a conexão e nviando uma mensagem de solicitação de serviço para o Web Service; 
(2) O Web Service recebe a mensagem de solicitação de serviço e encaminha ao aplicativo do BPe TA que irá processar o serviço solicitado; 
(3) O aplicativo do BPe TA recebe a mensagem de sol icitação de serviço e realiza o processamento, devolvendo uma mensagem de resultado do processamento ao 
Web Service ; 
(4) O Web Service recebe a mensagem de resultado do  processamento e o encaminha ao aplicativo do contribuinte; 
(5) O aplicativo do contribuinte recebe a mensagem de resultado do processamento e, caso não exista outra mensagem, encerra a conexão. 
2.4 Padrão de Mensagens dos Web Services 
 Área de dados das mensagens 
 
A informação armazenada na área de dados <Body> da mensagem SOAP é um documento que deve atender o leiaute definido na documentação do Web Service acessado.  
Para os serviços de recepção, a mensagem deverá ser  compactada no padrão GZip, onde o resultado da com pactação é convertido para Base64, reduzindo o tama nho da 
mensagem em aproximadamente 70%, conforme abaixo:  
<soap12:Body> 
<BPeDadosMsg                
   xmlns="http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoTA"> 
string </BPeDadosMsg> 
</soap12:Body> 
 
Para os demais serviços (Consulta, Recepção Eventos e Status), a mensagem deverá utilizar XML sem compactação: 
<soap12:Body> 
<BPeDadosMsg  
   xmlns="http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento"> 
xml </BPeDadosMsg> 
</soap12:Body 
 
A área referente ao SOAP Header não deverá ser informada. 
 Validação da estrutura XML das Mensagens dos Web Services 
 
As informações são enviadas ou recebidas dos Web Services através de mensagens no padrão XML definido na documentação de cada Web Service. 
As alterações de leiaute e da estrutura de dados XML realizadas nas mensagens são controladas através da atribuição de um número de versão para a mensagem.

## Página 16

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 16  / 80  
 
Um Schema XML é uma linguagem que define o conteúdo  do documento XML, descrevendo os seus elementos e a sua organização, além de estabelecer regras de 
preenchimento de conteúdo e de obrigatoriedade de cada elemento ou grupo de informação. 
A validação da estrutura XML da mensagem é realizada por um analisador sintático (parser) que verifica se a mensagem atende as definições e regras de seu Schema XML. 
Qualquer divergência da estrutura XML da mensagem em relação ao seu Schema XML provoca um erro de validação do Schema XML. 
A primeira condição para que a mensagem seja validada com sucesso é que ela seja submetida ao Schema XML correto. 
Assim, o aplicativo do contribuinte deve estar preparado para gerar as mensagens no leiaute em vigor, devendo ainda informar a versão do leiaute da estrutura XML da mensagem 
na TAG correspondente em cada mensagem. 
<BPeTA xmlns="http://www.portalfiscal.inf.br/bpe"> 
    <infBPe Id="BPe43081808467115000100750010757245731000000010" versao="1.00"> 
     …. 
   </infBPe> 
</BPeTA> 
 Schemas XML das Mensagens dos Web Services 
 
Toda mudança de leiaute das mensagens dos Web Services implica na atualização do seu respectivo Schema XML. 
A identificação da versão dos Schemas será realizada com o acréscimo do número da versão no nome do arquivo precedida da literal ‘_v’, como segue: 
BPeTA_v1.00.xsd (Schema XML do BPe TA, versão 1.00); 
tiposGeral_v1.00.xsd (Schema XML dos tipos do BPeTA, versão 1.00). 
 
A maioria dos Schemas XML do BPe TA utilizam as definições de tipos básicos ou tipos complexos que estão definidos em outros Schemas XML (ex.: tiposGeralBPe_v1.00.xsd, 
etc.), nestes casos, a modificação de versão do Schema básico será repercutida no Schema principal.  
Por exemplo, o tipo numérico de 15 posições com 2 decimais é definido no Schema tiposGeralBPe_v1.00.xsd, caso ocorra alguma modificação na definição deste tipo, todos os 
Schemas que utilizam este tipo básico devem ter a sua versão atualizada e as declarações “import” ou “include” devem ser atualizadas com o nome do Schema básico atualizado. 
As modificações de leiaute das mensagens dos Web Services podem ser causadas por necessidades técnicas ou em razão da modificação de alguma legislação. As modificações 
decorrentes de alteração da legislação deverão ser implementadas nos prazos previstos na norma que introduziu a alteração. As modificações de ordem técnica serão divulgadas 
pela Coordenação Técnica do ENCAT e poderão ocorrer sempre que se fizerem necessárias.

## Página 17

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 17  / 80  
 
2.5 Versão dos Schemas XML 
 Liberação das versões dos schemas para o BPe TA 
 
Os schemas válidos para a BPe TA serão disponibiliz ados no sítio nacional do Projeto ( 
dfe-portal.svrs.rs.gov.br/BPe ), e serão liberados após autorização da equipe de Gestão 
do Projeto formada pelos Líderes dos Projetos nos Estados e representante das Empresas. 
A cada nova liberação de schema será disponibilizad o um arquivo compactado contendo o conjunto de sche mas a ser utilizados pelas empresas para a geração dos arquivos 
XML. Este arquivo será denominado “Pacote de Libera ção” e terá a mesma numeração da versão do Manual d e Orientações que lhe é compatível. Os pacotes de l iberação 
serão identificados pelas letras “PL_BPe”, seguida do número da versão do Manual de Orientações corres pondente. Exemplificando: O pacote PL_BPe_1.00.zip representa o 
“Pacote de Liberação” de schemas do BPe TA compatíveis com o Manual de Orientações do Contribuinte – v ersão 1.00. 
Os schemas XML das mensagens XML são identificados pelo seu nome, seguido da versão do respectivo schema. 
Assim, para o schema XML de “BPe”, corresponderá um  arquivo com a extensão “.xsd”, que terá o nome de “BPe _v9.99.xsd ”, onde v9.99, corresponde a versão do respectivo 
schema. 
Para identificar quais os schemas que sofreram alteração em um determinado pacote liberado, deve-se comparar o número da versão do schema deste pacote com o do pacote 
anterior. 
 Correção de Pacote de Liberação 
 
Em alguma situação pode surgir a necessidade de correção de um Schema XML por um erro de implementação de regra de validação, obrigatoriedade de campo, nome de tag 
divergente do definido no leiaute da mensagem, que não modifica a estrutura do Schema XML e nem exige a alteração dos aplicativos da autorização ou dos contribuintes. 
Nesta situação, divulgaremos um novo pacote de liberação com o Schema XML corrigido, sem modificar o número da versão do PL para manter a compatibilidade com o Manual 
de Orientações do Contribuinte vigente. 
A identificação dos pacotes mais recentes se dará com o acréscimo de letras minúscula do alfabeto, como por exemplo: BPe_PL_1.00a.ZIP, indicando que se trata da primeira 
versão corrigida do BPe_PL_1.00.ZIP. 
 Divulgação de novos Pacotes de Liberação 
 
A divulgação de novos pacotes de liberação ou atualizações de pacote de liberação será realizada através da publicação de Notas Técnicas no Portal Nacional do BPe TA com 
as informações necessárias para a implementação dos novos pacotes de liberação.

## Página 18

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 18  / 80  
 
 Controle de Versão 
 
O controle de versão de cada um dos schemas válidos do BPe TA compreende uma definição nacional sobre: 
Qual a versão vigente (versão mais atualizada)? 
Quais são as versões anteriores ainda suportadas? 
 
Este controle de versão permite a adaptação dos sistemas de informática das empresas participantes do Projeto em diferentes datas. Ou seja, algumas empresas poderão estar 
com uma versão de leiaute mais atualizada, enquanto outras empresas poderão ainda estar operando com mensagens em um leiaute anterior. 
Não estão previstas mudanças frequentes de leiaute de mensagens e as empresas deverão ter um prazo razoável para implementar as mudanças necessárias, conforme acordo 
operacional a ser estabelecido. 
Mensagens recebidas com uma versão de leiaute não suportada serão rejeitadas com uma mensagem de erro específica na versão do leiaute de resposta mais recente em uso. 
2.6 Sistema de Registro de Eventos 
 
O Sistema de Registro de Eventos do BPe TA – SRE é o modelo genérico que permite o registro de evento de interesse do BPe TA originado a partir do próprio contribuinte ou 
da administração tributária. 
Um evento é o registro de um fato relacionado com o documento fiscal eletrônico, esse evento pode ou não modificar a situação do documento (por exemplo: cancelamento) ou 
até mesmo substituí-lo por outro (por exemplo: substituição). 
O serviço para registro de eventos será disponibilizado pelo Ambiente Autorizador através de Web Service de processamento síncrono e será propagado para os demais órgãos 
interessados pelo mecanismo de compartilhamento de documentos fiscais eletrônicos. As mensagens de evento utilizarão o padrão XML já definido para o projeto BPe contendo 
a assinatura digital do emissor do evento (seja ele contribuinte ou fisco). 
O registro do evento requer a existência do BPe TA vinculada no Ambiente Autorizador, contudo alguns tipos de eventos poderão ser registrados sem que exista a BPe na base 
de dados do autorizador em conformidade com as regras de negócio estabelecidas para este tipo de evento. 
O modelo de mensagem do evento deverá ter um conjunto mínimo de informações comuns, a saber: 
• Identificação do autor da mensagem; 
• Identificação do evento;  
• Identificação do BPe TA vinculado; 
• Informações específicas do evento; 
• Assinatura digital da mensagem;

## Página 19

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 19  / 80  
 
O Web Service será único com a funcionalidade de tratar eventos de forma genérica para facilitar a criação de novos eventos sem a necessidade de criação de novos serviços 
e com poucas alterações na aplicação de Registro de Eventos do Ambiente Autorizador. 
O leiaute da mensagem de Registro de Evento seguirá o modelo adotado para o documento BPe, contendo uma parte genérica (comum a todos os tipos de evento) e uma parte 
específica onde será inserido o XML correspondente a cada tipo de evento em uma tag do tipo any . 
As regras de validação referentes à parte genérica dos eventos estarão descritas no item 5 deste manual. 
As validações específicas de cada tipo de evento estarão descritas no item 6 deste Manual, originando um novo subitem para cada tipo de evento especificado. 
O Pacote de Liberação de schemas do BPe TA deverá conter o leiaute da parte genérica do Registro de Eventos e um schema para cada leiaute específico dos eventos definidos 
neste manual. 
 Relação dos Tipos de Evento 
 
Os eventos identificados abaixo serão construídos gradativamente pelo ambiente autorizador, assim como novos eventos poderão ser identificados e acrescentados nesta tabela 
em futuras versões deste MOC. 
Tipo de 
Evento  Descrição Evento  
Tipo de 
Autor do Evento  
Tipo de 
Meio Informação BPe deve 
existir?  
*** Evento: Empresa Emitente 
110111 Cancelamento 1-Empresa Emitente 1=via WS Eve nto Sim 
110115 Não embarque 1-Empresa Emitente 1=via WS Eve nto Sim 
112140 Não Fornecimento 1-Empresa Emitente 1=via WS  Evento Sim 
112130 Ajuste de BPe TA 1-Empresa Emitente 1=via WS  Evento Sim 
*** Evento: Fisco Emitente 
240140 Autorizado BPe de Substituição 2-Fisco Emite nte 1=via WS Evento Sim 
240170 Liberação Prazo Cancelamento 2-Fisco Emitent e 1=via WS Evento; 
2=via Extranet BPe 
Sim 
240160 Autorizado BPe Vinculado 2-Fisco Emitente 1= via WS Evento; Sim 
 Eventos de Marcação 
 
Serão criados eventos de marcação de BPe para os casos em que um documento referenciar outro. Por exemplo: Autorizado BPe Vinculado.  
Esses eventos serão gerados automaticamente pelo Fisco no momento da autorização dos documentos e serão assinados digitalmente com certificado digital da SEFAZ Virtual 
autorizadora do BPe TA. Os eventos gerados nos BPe TA referenciados deverão constar da consulta pública destes documentos.

## Página 20

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 20  / 80  
 
2.7 Data e hora de emissão e outros horários 
 
Todos os campos que representam Data e Hora no leia ute das mensagens do BPe TA seguem o formato UTC co mpleto com a informação do TimeZone. Este tipo de 
representação de dados é tecnicamente adequado para a representação do horário para um País com dimensões continentais como o Brasil.  
Serão aceitos os horários de qualquer região do mundo (faixa de horário UTC de -11 a +12) e não apenas as faixas de horário do Brasil.  
Exemplo: no formato UTC para os campos de Data-Hora, "TZD" pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, 
-02:00 e -03:00. Exemplo: "2010-08-19T13:00:15-03:00". 
2.8 SEFAZ virtual 
 
Os serviços da SEFAZ VIRTUAL compreendem os Web Ser vices descritos no Modelo Conceitual da Arquitetura de Comunicação, conforme consta no Manual de Orien tações 
do Contribuinte e nesta Nota Técnica. 
O credenciamento de contribuintes bem como a autori zação de uso dos serviços de uma determinada SEFAZ VIRTUAL é responsabilidade da Administração Tributá ria de 
circunscrição daqueles contribuintes.

## Página 21

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 21  / 80  
 
3 Regras de Validações Gerais do BPe 
Os quadros a seguir representam as regras de valida ção genéricas para os serviços do BPe TA. Os quadro s serão relacionados a cada serviço conforme a nece ssidade, além 
das regras específicas de cada Web Service. 
 Grupo A: Validação do Certificado de Transmissão (protocolo TLS) 
 
# Regra de Validação Aplic. cStat Efeito Mensagem 
A01 Certificado de Transmissor Inválido: 
- Certificado de Transmissor inexistente na mensagem 
- Versão difere "3" 
- Se informado, Basic Constraint deve ser true (não pode ser Certificado de 
AC) 
- KeyUsage não define "Autenticação Cliente" 
Obrig. 280 Rej. Rejeição: Certificado Transmissor i nválido 
A02  Validade do Certificado (data início e data fim) Ob rig. 281 Rej. Rejeição: Certificado Transmissor Dat a Validade 
A03 Verificar a Cadeia de Certificação: 
- Certificado da AC emissora não cadastrado na SEFAZ 
- Certificado de AC revogado 
- Certificado não assinado pela AC emissora do Certificado 
Obrig. 283 Rej. Rejeição: Certificado Transmissor -  erro Cadeia de 
Certificação 
A04 LCR do Certificado de Transmissor 
- Falta o endereço da LCR (CRL DistributionPoint) 
- LCR indisponível 
- LCR inválida 
Obrig. 286 Rej. Rejeição: Certificado Transmissor e rro no acesso a LCR 
A05  Certificado do Transmissor revogado Obrig. 284 Rej. Rejeição: Certificado Transmissor r evogado 
A06  Certificado Raiz difere da "ICP-Brasil" Obrig. 285 Rej. Rejeição: Certificado Transmissor d ifere ICP-Brasil 
A07  Falta a extensão de CNPJ no Certificado (OtherName - OID=2.16.76.1.3.3 Obrig. 282 Rej. Rejeição: Certi ficado Transmissor sem CNPJ 
 
As validações de A01, A02, A03, A04 e A05 são realizadas pelo protocolo TLS  e não precisam ser implementadas. A validação A06 também pode ser realizada pelo protocolo, 
mas pode falhar se existirem outros certificados di gitais de Autoridade Certificadora Raiz que não sej am “ICP-Brasil” no repositório de certificados digi tais do servidor de Web 
Service da SEFAZ.

## Página 22

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 22  / 80  
 
 Grupo B-0: Validação da Compactação da Mensagem 
 
O sistema do autorizador deverá descompactar mensagem da área de Dados. 
Todas as validações serão aplicadas sobre o XML já descompactado 
# Regra de Validação Aplic. cStat Efeito Mensagem 
B00 Verificar compactação da mensagem da área de dados Obrig. 244 Rej. Rejeição: Falha na descompactação d a área de dados 
 Grupo B: Validação Inicial da Mensagem no Web Service 
# Regra de Validação Aplic. cStat Efeito Mensagem 
B01 Tamanho do XML de Dados superior a 1024 Kbytes Obri g. 214 Rej. Rejeição: Tamanho da mensagem excedeu o  limite 
estabelecido 
B02 XML de Dados Malformado 
 
Obrig. 243 Rej. Rejeição: XML Malformado 
B03  Verificar se o Serviço de processamento está Paralisado Momentaneamente Obrig. 108 Rej. Serviço Parali sado Momentaneamente (curto prazo) 
B04  Verificar se o Serviço de processamento está Paralisado sem Previsão Obrig. 109 Rej. Serviço Paralisad o sem Previsão 
 
A mensagem será descartada se o tamanho exceder o limite previsto (1024 KB) A aplicação do contribuinte não poderá permitir a geração de mensagem com tamanho superior 
a 1024 KB. Caso isto ocorra, a conexão poderá ser i nterrompida sem mensagem de erro se o controle do t amanho da mensagem for implementado por configuraçõ es do 
ambiente de rede da SEFAZ (ex.: controle no firewall ). No caso de o controle de tamanho ser implementado por aplicativo teremos a devolução da mensagem de erro 214. 
O Ambiente Autorizador que mantêm o Web Service disponível, mesmo quando o serviço estiver paralisa do, deverá implementar as verificações 108 e 109. E stas validações 
poderão ser dispensadas se o Web Service não ficar disponível quando o serviço estiver paralisado. 
 Grupo C: Validação da área de dados da mensagem 
# Regra de Validação Aplic. cStat Efeito Mensagem 
C01 Verificar Schema XML da Área de Dados  
 
Obrig. 215 
 
Rej. Rejeição: Falha no schema XML 
 
C02 Verificar a existência de qualquer namespace diverso do namespace padrão 
do projeto (http://www.portalfiscal.inf.br/bpe) 
Obrig. 598 Rej. Rejeição: Usar somente o namespace padrão do BPe 
C03 Verificar a existência de caracteres de edição no início ou fim da mensagem 
ou entre as tags 
Obrig. 599 Rej. Rejeição: Não é permitida a presenç a de caracteres de 
edição no início/fim da mensagem ou entre as tags da 
mensagem

## Página 23

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 23  / 80  
 
C04 Verificar o uso de prefixo no namespace Obrig. 404  Rej. Rejeição: Uso de prefixo de namesp ace não permitido 
C05 Verificar se XML utiliza codificação diferente de UTF-8 Obrig. 402  Rej. Rejeição: XML da área de dado s com codificação diferente 
de UTF-8 
C06 Verificar se a versão do XML é suportada 
 
Obrig. 239  Rej. Rejeição: Versão informada para a BPe não suportada 
 Grupo D: Validações do Certificado de Assinatura Digital 
# Regra de Validação Aplic. cStat Efeito Mensagem 
D01 Certificado de Assinatura Inválido: 
- Certificado de Assinatura inexistente na mensagem 
- Versão difere “3” 
- Basic Constraint = true (não pode ser Certificado de AC) 
- KeyUsage não define “Autenticação Cliente” 
Obrig. 290 Rej. Rejeição: Certificado Assinatura in válido 
D02 Validade do Certificado (data início e data fim) Ob rig. 291 Rej. Rejeição: Certificado Assinatura Data  Validade 
D03  Falta a extensão de CNPJ no Certificado (OtherName – OID=2.16.76.1.3.3) Obrig. 292 Rej. Rejeição: Cert ificado Assinatura sem CNPJ 
D04 Verificar a Cadeia de Certificação: 
- Certificado da AC emissora não cadastrado na SEFAZ 
- Certificado de AC revogado 
- Certificado não assinado pela AC emissora do Certificado 
Obrig. 293 Rej. Rejeição: Certificado Assinatura - erro Cadeia de 
Certificação 
D05 LCR do Certificado de Assinatura 
- Falta o endereço da LCR (CRL DistributionPoint) 
- Erro no acesso à LCR 
Obrig. 296 Rej. Rejeição: Certificado Assinatura er ro no acesso a LCR 
D06  Certificado de Assinatura revogado Obrig. 294 Rej. Rejeição: Certificado Assinatura re vogado 
D07 Certificado Raiz difere da “ICP-Brasil” Obrig. 295 Rej Rejeição: Certificado Assinatura dif ere ICP-Brasil 
 Grupo E: Validações da Assinatura Digital 
# Regra de Validação Aplic. cStat Efeito Mensagem 
E01 Assinatura difere do padrão do Projeto: 
- Não assinado o atributo “ID” (falta “Reference UR I” na assinatura) 
(*validado também pelo Schema) 
 - Faltam os “Transform Algorithm” previstos na assinatura (“C14N” e 
“Enveloped”) 
Estas validações são implementadas pelo Schema XML da Signature  
Obrig. 298 Rej. Rejeição: Assinatura difere do padr ão do Projeto 
E02  Valor da assinatura (SignatureValue) difere do valor calculado Obrig. 297 Rej. Rejeição: Assinatura di fere do calculado 
E03 CNPJ-Base do Emitente difere do CNPJ-Base do Certificado Digital 
 
Obrig. 213 Rej. Rejeição: CNPJ-Base do Emitente dif ere do CNPJ-Base do 
Certificado Digital

## Página 24

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 24  / 80  
 
4 Web Services 
Os Web Services disponibilizam os serviços que serão utilizados pelos aplicativos dos contribuintes. O mecanismo de utilização dos Web Services segue as seguintes premissas: 
a) Será disponibilizado um Web Service por serviço,  existindo um método para cada tipo de serviço; 
b) O envio da solicitação e a obtenção do retorno s erão realizados na mesma conexão através de um único método. 
c) As URLs dos Web Services encontram-se no Portal Nacional do BPe (dfe-portal.svrs.rs.gov.br/BPe). Ac essando a URL pode ser obtido o WSDL (Web Services 
Description Language) de cada Web Service. 
d) O processo de utilização dos Web Services sempre  é iniciado pelo contribuinte enviando uma mensagem nos padrões XML e SOAP, através do protocolo TLS com 
autenticação mútua. 
e) A ocorrência de qualquer erro na validação dos d ados recebidos interrompe o processo com a disponibilização de uma mensagem contendo o código e a descrição 
do erro.

## Página 25

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 25  / 80  
 
4.1 WebService Síncrono de Recepção BPe TA 
 
O Serviço de Recepção de BPe Transporte Aéreo é o s erviço oferecido pelos Portais das Secretarias da F azenda dos Estados para recepção dos BPe TA emitido s pelos 
contribuintes credenciados em sua unidade federada. 
A forma de processamento do serviço de recepção de BPe TA é síncrona sem a formação de lotes. O contribuinte deve transmitir BPe TA através do Web Service de recepção 
de BPe TA e receberá o resultado do processamento na mesma conexão. 
O BPe Transporte Aéreo será emitido por contribuint es que possuírem credenciamento específico para ess a modalidade de BPe identificada pelo modal de tran sporte aéreo 
(tag: modal = 2), portanto, não serão necessariamente os mesmos que já emitem o BPe normal. 
Função : serviço destinado à recepção de mensagens de envio de BPe Transporte Aéreo. 
 
Processo : síncrono. 
 
Método: bpeRecepcaoTA 
 
Parâmetro da Mensagem da área de dados: Compactada utilizando GZip (Base64) 
 Leiaute Mensagem de Entrada 
 
Entrada:  Estrutura XML com o Bilhete de Passagem Transporte Aéreo está definida no documento último capítulo desta Nota Técnica. 
Schema XML: BPeTA_v9.99.xsd 
 Leiaute Mensagem de Retorno 
 
Retorno: Estrutura XML com a mensagem do resultado do envio do BPe TA usará o mesmo schema de retorno do BPe Normal 
Schema XML: retBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
AR01 retBPe Raiz - - - - TAG raiz da Resposta 
AR02  versao A AR01 N 1-1 1-4 Versão do leiaute 
AR03 tpAmb E AR01 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 – Homologação

## Página 26

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 26  / 80  
 
AR04  cUF E AR01 N 1-1 2 Código da UF que atendeu à solic itação. 
AR05  verAplic E AR01 C 1-1 1-20 Versão do Aplicativo que  recebeu o BPe. 
AR06  cStat E AR01 N 1-1 4 Código do status da resposta  
AR07  xMotivo E AR01 C 1-1 1-255 Descrição literal do sta tus da resposta 
AR08  protBPe G AR01 - 0-1 - Resposta ao processamento do  BPe 
 Leiaute de BPe processado 
 
O BPe TA usará o mesmo layout de BPe Processado Normal. 
 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
PR01 protBPe Raiz - - - - TAG raiz da resposta processamento 
PR02 versao A PR01 N 1-1 2v2 Versão do leiaute 
PR03  infProt G PR01 - 1-1 - Informações do protocolo de resposta 
PR04 Id A PR03 C 0-1 - Identificador da TAG a ser assina da, somente precisa ser informado se a UF 
assinar a resposta. Em caso de assinatura da resposta pela SEFAZ preencher o 
campo com o Nro do Protocolo, precedido com o literal “ID” 
PR05 tpAmb E PR03 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 – Homologação 
PR06  verAplic E PR03 C 1-1 1-20 Versão do Aplicativo que  recebeu o BPe. 
PR07  chBPe E PR03 N 1-1 44 Chave de acesso do BPe 
PR08 dhRecbto E PR03 D 1-1 - Data e Hora do Processament o 
Formato = AAAA-MM-DDTHH:MM:SS TZD 
Preenchido com data e hora da gravação do BPe no Banco de Dados. 
Em caso de Rejeição, com data e hora do recebimento do Arquivo do BPe 
enviado. 
PR09  nProt E PR03 N 0-1 15 Número do protocolo de autori zação do BPe 
PR10 digVal E PR03 C 0-1 28 Digest Value do BPe processa do, utilizada para conferir a integridade com o 
BPe original 
PR11  cStat E PR03 N 1-1 3 Código do status da resposta p ara o BPe 
PR12  xMotivo E PR03 C 1-1 1-255 Descrição literal do sta tus da resposta para o BPe 
PR13  infFisco G PR01 - 0-1 - Grupo reservado para envio de mensagem do Fisco para o contribuinte 
PR14  cMsg E PR13 N 1-1 3 Código de status da mensagem do  fisco 
PR15  xMsg E PR13 C 1-1 1-255 Mensagem do Fisco para o co ntribuinte 
PR16 Signature G PR01 XML 0-1 - Assinatura XML do grupo identificado pelo atributo “ID” 
A decisão de assinar a mensagem fica a critério da UF interessada.

## Página 27

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 27  / 80  
 
 Regras de Validação Básicas do Serviço 
 
Deverão ser aplicadas as validações gerais conforme quadro abaixo: 
 
Grupo Descrição 
A Validação do Certificado de Transmissão (protocolo  TLS) 
B-0 Validação da Compactação da Mensagem 
B Validação Inicial da Mensagem no Web Service  
C Validação da Área de Dados da mensagem 
D Validação do Certificado de Assinatura 
E Validações da Assinatura Digital 
 Regras de Negócio do BPe TA 
 
# Regra de Validação 
 Aplic. cStat Efeito Mensagem 
Validações Gerais 
F01 Tipo do ambiente do BPe difere do ambiente do Web Service   Obrig. 252 Rej. Rejeição: Ambiente informado diverge do Ambiente de 
recebimento 
F02 Código da UF do Emitente difere da UF Autorizadora Obrig. 226 Rej. Rejeição: Código da UF do Emitente diverge da UF 
autorizadora 
F03 Sigla da UF do Emitente difere da UF Autorizadora O brig. 247 Rej. Rejeição: Sigla da UF do Emitente di verge da UF 
autorizadora 
F04 Código da UF do emitente difere da Sigla da UF do emitente Obrig, 233 Rej. Rejeição: Código da UF do e mitente difere da Sigla da UF 
do Emitente 
F05 
Se forma de emissão do BPe = 1 (Normal):  
dhCont e xJust não devem ser informados 
Obrig. 415 Rej. Rejeição: Data e Justificativa de e ntrada em contingência 
não devem ser informadas para tipo de emissão igual a 
Normal. 
F06 Se forma de emissão do BPe = 2 (Contingência Off-Line): 
dhCont e xJust devem ser informados 
Obrig. 416 Rej. Rejeição: Data e Justificativa de e ntrada em contingência 
devem ser informadas 
F07 
Se Data de entrada em contingência estiver informada, esta deve ser 
menor ou igual à data de emissão 
 
Obrig 417 Rej. Rejeição: Data de entrada em conting ência posterior ou 
igual a data de emissão. 
F08 
Se forma de emissão do BPe = 2 (Contingência Off-Line): 
Rejeitar se UF do emitente estiver configurada para não aceitar este tipo 
de contingência. 
Obrig. 418 Rej. Rejeição: UF do Emitente não permit e emissão Off-line

## Página 28

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 28  / 80  
 
F09 
Campo "ID" inválido: 
- Falta literal "BPe" 
- Chave de acesso do campo ID difere da concatenação dos campos 
correspondentes 
Obrig. 227 Rej. 
Rejeição: Erro na composição do Campo ID 
F10 Verificar se Ano da chave de acesso é inferior a 2025 Obrig. 421 Rej. Rejeição: Ano do BPe informado na chave de acesso 
inválido 
F11 Dígito Verificador inválido da Chave de acesso resultante da concatenação 
dos campos correspondentes Obrig. 253 Rej. Rejeição: Digito Verificador da chave de acesso composta 
inválido 
Validações da Viagem 
F12 Município de Início da viagem do BPe diverge da UF (verificar se as 2 
posições da esquerda do código de município que identifica o código da 
UF estão de acordo com a sigla da UF informada) 
Obrig. 409 Rej. Rejeição: Código de Município diver ge da UF de início da 
viagem do BPe 
F13 Rejeitar se UF de início da viajem for diferente da UF do emitente Obrig. 505 Rej. Rejeição: UF de iní cio da viagem deve ser igual a UF do 
emitente do BPe 
F14 Código do Município de início da viagem deve existir (Tabela Municípios do 
IBGE) 
Obrig. 405 Rej. Rejeição: Município de início da vi agem inexistente 
F15 Município de fim da viagem do BPe diverge da UF (verificar se as 2 
posições da esquerda do código de município que identifica o código da 
UF estão de acordo com a sigla da UF informada)  
Obrig. 410 Rej. Rejeição: Código de Município diver ge da UF de fim da 
viagem do BPe 
F16 Se UF de fim da viagem for diferente de exterior (tag:ide/UFFim <> “EX”): 
Código do Município de fim da viagem deve existir (Tabela Municípios do 
IBGE) 
Obrig. 406 Rej. Rejeição: Município de fim da viage m inexistente 
F17 Se UF de fim da viagem for igual a exterior (tag:ide/UFFim = “EX”): 
- Código do Município de fim da viagem deve ser 9999999 
Obrig. 411 Rej. Rejeição: Código de Município invál ido para viagem ao 
exterior 
F18 Se informado CPF do passageiro: 
- Validar CPF do passageiro (dígito de controle, zeros) 
Obrig. 497 Rej. Rejeição: CPF do passageiro inválid o 
F19 Se o grupo de informações da viagem (grupo:infViagem) NÃO for múltiplo: 
- Deve existir apenas uma viagem com tipo de trecho Normal (tag:tpTrecho 
= 1) 
Obrig. 419 Rej. Rejeição: Viagem sem conexão com tr echo inválido 
F20 Se o grupo de informações da viagem (grupo:infViagem) for múltiplo: 
- Deve existir obrigatoriamente uma viagem com tipo de trecho inicial 
(tag:tpTrecho = 2) e as demais devem ser obrigatoriamente do tipo de 
trecho conexão (tag:tpTrecho = 3) 
Obrig, 420 Rej. Rejeição: Viagem com conexão com um  dos trechos 
inválidos 
F21 Se informado tipo de trecho Conexão (tag:tpTrecho = 3): 
- A data-hora da conexão deve ser informada no trecho Conexão 
Obrig. 484 Rej. Rejeição: A data-hora da conexão de ve ser informada para 
viagem conexão

## Página 29

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 29  / 80  
 
F22 Se informado tipo de trecho diferente de Conexão (tag:tpTrecho = 1 ou 2): 
- A data-hora da conexão NÃO deve ser informada no trecho 
Obrig. 485 Rej. Rejeição: A data-hora da conexão nã o deve ser informada 
para viagem normal ou trecho inicial 
F23 Se informada data-hora da conexão, esta deve ser maior que a data-hora 
do embarque 
Obrig, 486 Rej. Rejeição: A data-hora da conexão de ve ser maior que a 
data-hora do embarque 
Validações do Emitente 
F24 Validar CNPJ Emitente (dígito controle, zeros ou nulo) Obrig. 207 Rej. Rejeição: CNPJ do emitente invá lido 
F26 Se IE emitente informada: 
Validar IE Emitente (erro no dígito de controle) 
Obs.: Antes da validação, a IE deverá ser normalizada, na aplicação da 
SEFAZ, com o acréscimo de zeros não significativos previstos na definição 
do formato da IE se necessário.  
Ex.: IE informada 130000019, formato da IE: NNNNNNNNNND, a IE deve 
ser padronizada para 00130000019, com o acréscimo dos zeros não 
significativos necessários para a validação do dígito verificador. 
Obrig. 209 Rej. Rejeição: IE do emitente inválida 
F27 Emitente não credenciado para emissão de BPe Aéreo  Obrig. 203 Rej. Rejeição: Emissor não habilitado p ara emissão do BPe 
F32 Município do Emitente diverge da UF (verificar se as 2 posições da 
esquerda do código de município que identifica o código da UF é 
compatível com a sigla da UF informada) 
Obrig. 407 Rej Rejeição: Código de Município diverg e da UF do Emitente 
do BPe 
F33 Código do Município Emitente inexistente (Tabela Municípios do IBGE) Obrig. 408 Rej. Rejeição: Municíp io do Emitente inexistente 
Validações do Comprador 
F34 Se CNPJ Comprador informado:  
- Validar CNPJ Comprador (dígito de controle, zeros)  
Obrig. 422 Rej. Rejeição: CNPJ do comprador inválid o 
F35 Se CPF Comprador informado:  
- Validar CPF Comprador (dígito de controle, zeros) 
Obrig. 423 Rej. Rejeição: CPF do comprador inválido  
F36 Se informado Comprador:  
- Município do Comprador deve pertencer à UF (verificar se as 2 posições 
da esquerda do código de município que identifica o código da UF é 
compatível com a sigla da UF informada) 
Obrig. 424 Rej Rejeição: Código de Município diverg e da UF de localização 
comprador 
 
F37 Se informado Comprador e endereço do Comprador não for exterior 
(tag:enderComp/UF <> “EX”) 
- Código do Município do Comprador deve existir (Tabela Municípios do 
IBGE) 
Obrig. 425 Rej. Rejeição: Município do comprador in existente 
 
F38 Se informado Comprador e endereço do Comprador for exterior 
(tag:enderComp/UF = “EX”) 
- Código do Município do Comprador deve ser 9999999 
 
Obrig. 426 Rej. Rejeição: Código de Município invál ido para comprador 
residente no exterior

## Página 30

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 30  / 80  
 
F39 Se IE Comprador informada: 
- Validar IE do Comprador (erro no dígito de controle) 
 
Observação .: Antes da validação, a IE deverá ser normalizada, na 
aplicação da SEFAZ, com o acréscimo de zeros não significativos 
previstos na definição do formato da IE se necessário.  
 
Ex. : IE informada 130000019, formato da IE: NNNNNNNNNND, a IE deve 
ser padronizada para 00130000019, com o acréscimo dos zeros não 
significativos necessários para a validação do dígito verificador. 
Obrig. 427 Rej. Rejeição: IE do comprador inválida 
Validações da Agência 
F43 Se informada Agência (grupo:agencia): 
Validar CNPJ Agência (dígito de controle, zeros)  
 
Observação : Para agência do exterior aceitar zeros 
Obrig. 431 Rej. Rejeição: CNPJ da Agência inválido 
F44 Se informada Agência (grupo:agencia): 
Município da Agência deve pertencer à UF (verificar se as 2 posições da 
esquerda do código de município que identifica o código da UF é 
compatível com a sigla da UF informada) 
Obrig. 432 Rej Rejeição: Código de Município diverg e da UF de localização 
da Agência 
F45 Se informada Agência (grupo:agencia) e endereço não for exterior 
(tag:enderAgencia/UF <> “EX”): 
Código do Município da Agência deve existir (Tabela Municípios do IBGE) 
Obrig. 433 Rej. Rejeição: Município da Agência inex istente 
F46 Se informado Agência e endereço da Agência for exterior 
(tag:enderAgencia/UF = “EX”):  
Código do Município da Agência deve ser 9999999 
Obrig. 503 Rej. Rejeição: Código do Município invál ido para Agência do 
exterior 
Validações da Data de Emissão 
F47 Data/Hora de Emissão posterior a Data/Hora de Recebimento (o Ambiente 
Autorizador deve considerar a hora local do emissor para a validação). A 
SEFAZ deve tolerar uma diferença máxima de 5 minutos quando a 
data/hora de emissão for maior que a data de recebimento, em função da 
sincronização de horário de servidores. 
Obrig. 212 Rej. Rejeição: Data/hora de emissão BPe posterior a data/hora 
de recebimento 
F48 Se tipo de emissão for Normal (tag:tpEmis=1): 
Data-Hora de Emissão com atraso superior a 5 minutos em relação ao 
horário de recepção na SEFAZ Autorizadora. 
 
Exceção 1:  A critério da UF, a rejeição acima pode ser efetuada para 
qualquer Tipo de Emissão.  
 
Obrig. 228 Rej. Rejeição: BPe com Data-Hora de Emis são muito atrasada

## Página 31

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 31  / 80  
 
Exceção 2 : A critério da UF, pode ser aceito BPe com Data de Emissão 
muito atrasada, desde que tenha sido emitido em contingência Off-Line 
(tag:tpEmis=2). O BPe transmitido para a SEFAZ Autorizadora após o 
prazo de 24 horas deve retornar: cStat=”150- Autorizado Uso do BPe, 
autorização fora de prazo”.  
 
Observação : A emissão do BPe deve ocorrer de forma on-line, real-time, 
com uma tolerância de até 5 minutos, devido ao sincronismo de horário do 
Servidor da Empresa e o servidor da SEFAZ Autorizadora 
F49 Data-hora do embarque deve ser igual ou superior a data de emissão Obrig. 254 Rej. Rejeição: Data-hora  do embarque deve ser maior ou igual 
data de emissão 
Validações do Tipo da Compra 
 
F50 
Se tipo de compra for Normal (tag: tpCompra = 0) ou Vinculado a BPe 
Múltiplo (tag: tpCompra =2): 
Os dados do passageiro devem ser informados (grupo: infPassageiro) 
Obrig. 441 Rej. Rejeição: Passageiro deve ser infor mado para o tipo de 
compra informado 
F51 
Se tipo de compra for múltiplo (tag: tpCompra = 1)  
Os dados do passageiro NÃO devem ser informados (grupo: 
infPassageiro) 
Obrig. 442 Rej. Rejeição: Dados do passageiro não d evem ser informados 
para BPe Múltiplo 
F52 Se tipo de compra for múltiplo (tag: tpCompra = 1): 
Os dados do comprador DEVEM ser informados (grupo: comp) 
Obrig. 443 Rej. Rejeição: Comprador deve ser inform ado para BPe Múltiplo 
F53 
Se tipo de compra for Normal (tag: tpCompra = 0) ou múltiplo (tag: 
tpCompra = 1): 
O grupo de informações de Valor do BPe e Impostos devem ser 
informados (grupos: infValorBPe e imp) 
Obrig. 444 Rej. Rejeição: BPe Normal e Múltiplo exi gem informação de 
valores e destaque de imposto 
F54 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
O grupo de informações do BPe Vinculado deve ser informado (grupo: 
infBPeVinculado) 
Obrig. 445 Rej. Rejeição: BPe vincula a BPe Múltipl o exige a informação da 
chave de acesso do BPe Múltiplo 
F55 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- Validar chave de acesso do BPe Múltiplo.  
Retornar motivo da rejeição da Chave de Acesso: CNPJ zerado ou 
inválido, Ano < 2017 ou maior que atual, Mês inválido (0 ou > 12), Modelo 
diferente de 63, Número zerado, Tipo de emissão inválido, UF inválida ou 
DV inválido) 
[Motivo: XXXXXXXXXXXX] 
Obrig. 446 Rej. Rejeição: Chave de acesso do BPe mú ltiplo inválida 
F56 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- O BPe Múltiplo deve existir 
Acesso BD BPE (Chave: CNPJ Emit, Modelo, Série, Nro) 
 
Obrig 447 Rej Rejeição: BPe múltiplo inexistente

## Página 32

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 32  / 80  
 
F57 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- BPe múltiplo não pode existir com diferença na Chave de Acesso 
Retornar a chave de acesso já autorizada, o número do protocolo e data 
de autorização do BPe 
[chBPe: 99999999999999999999999999999999999999999999] 
[nProt:999999999999999][dhAut: AAAA-MM-DDTHH:MM:SS TZD] 
Obrig. 448 Rej. Rejeição: BPe múltiplo com diferenç a de Chave de Acesso 
F58 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- O BPe múltiplo não pode estar cancelado  
Obrig. 471 Rej Rejeição: BPe múltiplo deve estar na  situação Autorizado o 
Uso 
F59 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- O BPe múltiplo não pode estar substituído 
Obrig. 472 Rej Rejeição: BPe múltiplo não pode ter sido substituído 
anteriormente 
F60 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- O BPe múltiplo deve ser do modal aéreo 
Obrig 473 Rej Rejeição: O BPe múltiplo deve ser do modal aéreo 
F61 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- CNPJ do emitente do BPe múltiplo deve ser igual ao informado no BPe 
vinculado a múltiplo 
Obrig. 474 Rej. Rejeição: CNPJ do emitente do BPe m últiplo deve ser igual 
ao informado no BPe vinculado a BPe múltiplo 
F62 Se tipo de compra for Vinculado a BPe Múltiplo (tag: tpCompra = 2): 
- IE do emitente do BPe múltiplo deve ser igual ao informado no BPe 
vinculado a BPe múltiplo 
Obrig, 476 Rej. Rejeição: IE do emitente do BPe sub stituto deve ser igual à 
informada no BPe substituído 
Validações de Valores 
F63 Verificar se valor total do bilhete (tag:vBP) não ultrapassa limite de R$ 
9.999.999,99 
 
OBS: A SEFAZ poderá aumentar o limite para contribuintes que operam 
com valores acima desse teto. 
Obrig. 434 Rej. Rejeição: Valor total do bilhete su perior ao limite permitido 
(R$ 9.999.999,99) 
F64 Verificar se o valor da soma dos componentes do valor do BPe 
(tag:Comp/vComp) corresponde ao valor total do bilhete de passagem 
(tag:vBP) 
* Considerar uma tolerância de R$ 1,00 para mais ou para menos  
Obrig. 436 Rej. Rejeição: Valor da soma dos compone ntes não corresponde 
ao valor total do bilhete 
F65 Se informado o Tipo de Desconto (tag:tpDesconto), a descrição do tipo de 
desconto deve ser informada (tag:xDesconto) 
Obrig. 437 Rej. Rejeição: Descrição do Tipo do desc onto deve ser informada 
F66 Se informado o tipo de desconto, o valor do desconto (tag:vDesconto) deve 
ser maior que zero 
Obrig. 401 Rej. Rejeição: Valor de desconto deve se r informado quando 
indicado o tipo de benefício 
F67 Se informado valor do desconto (tag:vDesconto) maior que zero e/ou 
informado conteúdo em xDesconto 
- O campo tpDesconto deverá estar preenchido 
Obrig. 500 Rej. Rejeição: O tipo do desconto deve s er informado 
F68 Se NÃO estiver informado campo tpDesconto: 
- Rejeitar se valor do BPe for igual a zero 
Obrig. 501 Rej. Rejeição: Valor do BPe sem desconto  deve ser maior que 
zero

## Página 33

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 33  / 80  
 
F69 Validar se o somatório das formas de pagamento (tag:pag/vPag) é 
diferente do valor pago do BPe (tag:vPgto) + Troco (tag:vTroco)  
* Considerar uma tolerância de R$ 1,00 para mais ou para menos 
 
Observação : a partir de 2027 deverá considerar vIBS e vCBS para 
consolidar a soma 
Obrig. 438 Rej. Rejeição: BPe com somatório dos pag amentos diferente do 
total pago 
F70 Validar se o valor pago pelo BPe (tag:vPgto) corresponde ao valor total do 
bilhete (tag: vBP) menos o valor do desconto (tag:vDesconto) 
Obrig. 403 Rej. Rejeição: Valor pago difere do Valo r Total menos o desconto 
concedido 
F71 Se a forma de pagamento for cartão (tag:tPag=03 ou 04): 
O grupo de informações do cartão (tag:card) deve ser informado 
Obrig. 475 Rej. Rejeição: Não informados os dados d o cartão de 
crédito/débito nas formas de pagamento 
F72 Se informado o tipo de integração como pagamento não integrado com o 
sistema de automação da empresa (tag: tpIntegra=2) para UF que não 
aceita esse tipo de integração.  
 
Observação : Regra de Validação opcional a critério da UF. 
Facult. 477 Rej. Rejeição: Pagamento com cartão de crédito em sistema de 
automação não integrado 
F73 Se informado CNPJ da credenciadora do cartão de crédito/débito 
(tag:card/CNPJ): 
- Validar CNPJ da credenciadora (dígito de controle, zeros) 
Obrig. 502 Rej. Rejeição: CNPJ da credenciadora do cartão inválido 
F74 Se informado o grupo de Cartão de Crédito / Débito (tag:card):  
- Se o pagamento com cartão for integrado ao sistema de automação da 
empresa (tag:tpIntegra=1) devem ser informados os campos de CNPJ da 
Credenciadora e o código de autenticação da operação (tag:card/CNPJ e 
card/cAut)  
 
Observação : Implementação por padrão, opcional a critério da UF 
Facult. 478 Rej. Rejeição: Não informados os dados da operação de 
pagamento por cartão de crédito / débito 
Validações do IBS / CBS 
F76 Se CST do IBS/CBS for informado, este deve existir na tabela de Código 
de Situação Tributária (tag: IBSCBS/CST) 
Obrig. 311 Rej. Rejeição: CST informado inexistente  
F77 Se cClassTrib for informado, este deve existir na tabela de Classificação 
Tributária do IBS/CBS (tag: IBSCBS/cClassTrib) 
Obrig. 312 Rej. Rejeição: Classificação Tributária informada inexistente 
F78 Verificar se o CST informado é compatível com o cClassTrib Obrig. 313 Rej. Rejeição: Classificação Tri butária incompatível com o CST 
informado 
F79 Verificar se o cClassTrib informado (tag: IBSCBS/cClassTrib) possui 
indicador que não permite ser informado nesse modelo de DFe 
Obrig. 388 Rej. Rejeição: Classificação Tributária do IBS/CBS não permitida 
neste modelo de DFe. 
F80 Se o CST informado possuir indicador que VEDA preenchimento do grupo 
de informações específicas do IBS/CBS, este grupo NÂO DEVE estar 
informado (grupo: gIBSCBS) 
Obrig 314 Rej. Rejeição: Grupo IBS/CBS não deve ser  preenchido para o 
CST informado

## Página 34

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 34  / 80  
 
F81 Se o CST informado possuir indicador que EXIGE preenchimento do grupo 
de informações específicas do IBS/CBS, este grupo DEVE estar informado 
(grupo: gIBSCBS) 
Exceção : Se o CRT informado pelo emitente for 1-Simples Nacional, 2- 
Simples Nacional, excesso sublimite de receita bruta ou 4 -MEI, o grupo 
gIBSCBS NÃO será exigido 
Obrig 315 Rej. Rejeição: Grupo IBS/CBS deve ser pre enchido para o CST 
informado 
F82 Se informado grupo IBS de competência das Unidades Federadas 
(gIBSUF): 
 
A alíquota de IBS da UF (pIBSUF) deverá ser: 
• 0,1% para documento com data de emissão no ano de 2026. (Art. 
343 da LC 214/25) 
• 0,05% para documento com data de emissão no ano de  2027 e 
2028. (Art. 344 da LC 214/25) 
• Alíquota de referência ou específica da UF a ser p ublicada para 
anos posteriores a 2028. 
 
Exceção : Se o cClassTrib possuir indicador de tributação regular o 
pIBSUF deve ser igual a zero 
Obrig. 316 Rej. Rejeição: Alíquota do IBS da UF inv álida  
F83 Se CST informado possuir indicador que EXIGE informação de redução de 
alíquota para o IBS Estadual ou informado grupo de compra 
governamental, o grupo gRed DEVE estar informado 
 
Exceção:  A regra não se aplica para CST do IBS/CBS (tag: IBSCBS/CST)  
que possui indicador que não permite a informação do IBS/CBS 
Obrig. 366 Rej. Rejeição: CST informado ou compras governamentais 
obriga informação de redução de alíquota estadual 
F84 Se informado grupo de Redução de Alíquota para IBS Estadual 
(gIBSUF/gRed): 
Verificar se percentual de Redução de Alíquota (pRedAliq) é válido para o 
cClassTrib informado (gIBSCBS/cClassTrib) 
Obrig. 389 Rej. Rejeição: Percentual de redução de alíquota da UF não é 
válido para este cClassTrib 
F85 Se informado grupo de Redução de Alíquota para IBS Estadual 
(gIBSUF/gRed), a Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado de: 
Se NÃO houver compra governamental (grupo gCompraGov não 
informado):  
pAliqEfet = pIBSUF × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo gCompraGov informado): 
pAliqEfet = pIBSUF × (1 - pRedAliq /100) × (1 - pRedutor/100). 
 
Observação : pRedutor é obtido no grupo gCompraGov 
 
Obrig. 390 Rej. Rejeição: Valor da Alíquota Efetiva  do IBS da UF calculado 
incorretamente

## Página 35

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 35  / 80  
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E):  
E = A × (1 – R/100) × (1 – RG/100) = 5,7. 
F86 Se CST informado possuir indicador que VEDA a informação de redução 
de alíquota para o IBS Estadual, o grupo gRed NÃO DEVE estar informado 
 
Exceção : Se Percentual de redução de alíquota em compra 
governamental (tag:gCompraGov/pRedutor) informado, este grupo é 
exigido e pRed deve ser igual a 0. 
Obrig. 367 Rej. Rejeição: CST informado não permite  informação de 
redução de alíquota estadual 
F87 Se CST informado possuir indicador que EXIGE informação de Diferimento 
para o IBS Estadual, o grupo gDif DEVE estar informado 
Obrig. 319 Rej. Rejeição: CST informado obriga info rmação de diferimento 
Estadual 
F88 Se CST informado possuir indicador que VEDA informação de Diferimento 
para o IBS Estadual, o grupo gDif NÃO DEVE estar informado 
Obrig. 368 Rej. Rejeição: CST informado não permite  informação de 
diferimento Estadual 
F89 Se informado grupo do Diferimento (gIBSUF/gDif): 
 
O valor do Diferimento (vDif) deverá ser resultante de: 
vDif = vBC x (pIBSUF/100) x (pDif/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 320 Rej. Rejeição: Valor do Diferimento da U F difere do calculado 
F90 Se informado grupo IBS de competência das Unidades Federadas 
(gIBSUF): 
O valor resultante da soma do diferimento (vDif) e Devolução (DevTrib) 
QUANDO INFORMADOS, NÃO  pode ser superior a vBC x (pIBSUF/100) 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a alíquota 
utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet)  
Obrig. 395 Rej. Rejeição: Valor do IBS UF não pode resultar negativo 
F91 Se informado grupo IBS de competência das Unidades Federadas 
(gIBSUF): 
O valor do IBS (vIBSUF) deverá ser resultante de: 
vIBSUF = vBC x (pIBSUF/100) – vDif - vDevTrib 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação 2 : Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 318 Rej. Rejeição: Valor do IBS UF difere do  calculado

## Página 36

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 36  / 80  
 
F92 Se informado grupo IBS de competência dos Municípios (gIBSMun): 
A alíquota de IBS Municipal deverá ser: 
• 0% para documento com data de emissão no ano de 20 26. (Art. 
343 da LC 214/25) 
• 0,05% para documento com data de emissão no ano de  2027 e 
2028. (Art. 344 da LC 214/25) 
• Alíquota de referência ou específica do Município a ser publicada 
para anos posteriores a 2028 
 
Exceção : Se o cClassTrib possuir indicador de tributação regular o 
pIBSMun deve ser igual a zero 
Obrig. 321 Rej. Rejeição: Alíquota do IBS do Municí pio inválida  
F93 Se CST informado possuir indicador que EXIGE informação de redução de 
alíquota para o IBS Municipal ou informado grupo de compra 
governamental, o grupo gRed DEVE estar informado 
Exceção:  A regra não se aplica para CST do IBS/CBS (tag: IBSCBS/CST)  
que possui indicador que não permite a informação do IBS/CBS 
Obrig. 369 Rej. Rejeição: CST informado ou compras governamentais 
obriga informação de redução de alíquota municipal 
F94 Se informado grupo de Redução de Alíquota para IBS Municipal 
(gIBSMun/gRed): 
Verificar se percentual de Redução de Alíquota (pRedAliq) é válido 
para o cClassTrib informado (gIBSCBS/cClassTrib)  
Obrig. 391 Rej. Rejeição: Percentual de redução de alíquota do Município 
não é válido para este cClassTrib 
F95 Se informado grupo de Redução de Alíquota para IBS Municipal 
(gIBSMun/gRed), a Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado 
de: 
Se NÃO houver compra governamental (grupo gCompraGov não 
informado):  
pAliqEfet = pIBSMun × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo gCompraGov informado): 
pAliqEfet = pIBSMun × (1 - pRedAliq /100) × (1 - pRedutor/100). 
 
Observação : pRedutor é obtido no grupo gCompraGov 
 
 
Exemplo : Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E):  
E = A × (1 – R/100) × (1 – RG/100) = 5,7. 
Obrig. 392 Rej. Rejeição: Valor da Alíquota Efetiva  do IBS do Município 
calculado incorretamente

## Página 37

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 37  / 80  
 
F96 Se CST informado possuir indicador que VEDA a informação de redução 
de alíquota para o IBS Municipal, o grupo gRed NÃO DEVE estar 
informado 
 
Exceção : Se Percentual de redução de alíquota em compra 
governamental (tag:gCompraGov/pRedutor) informado, este grupo é 
exigido e pRed deve ser igual a 0. 
Obrig. 381 Rej. Rejeição: CST informado não permite  informação de 
redução de alíquota municipal 
F97 Se CST informado possuir indicador que EXIGE informação de Diferimento 
para o IBS Municipal, o grupo gDif DEVE estar informado 
Obrig. 324 Rej. Rejeição: CST informado obriga info rmação de diferimento 
Municipal 
F98 Se CST informado possuir indicador que VEDA informação de Diferimento 
para o IBS Municipal, o grupo gDif NÃO DEVE estar informado 
Obrig. 382 Rej. Rejeição: CST informado não permite  informação de 
diferimento Municipal 
F99 Se informado grupo do Diferimento (gIBSMun/gDif): 
O valor do Diferimento (vDif) deverá ser resultante de  
vDif = vBC x (pIBSMun/100) x (pDif/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 325 Rej. Rejeição: Valor do Diferimento do M unicípio difere do 
calculado 
F100 Se informado grupo IBS de competência dos Municípios (gIBSMun): 
O valor do IBS (vIBSMun) deverá ser resultante de: 
vIBSMun = vBC x (pIBSMun/100) – vDif - vDevTrib 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação 2 : Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 323 Rej. Rejeição: Valor do IBS Municipal di fere do calculado 
F101 Se informado grupo IBS de competência dos Municípios (gIBSMun): 
O valor resultante da soma do diferimento (vDif) e Devolução (DevTrib) 
QUANDO INFORMADOS, NÃO  pode ser superior a vBC x (pIBSMun/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 396 Rej. Rejeição: Valor do IBS Municipal nã o pode resultar negativo 
F102 Se informados grupos IBS de competência dos Estados (gIBSUF) e 
Municípios (gIBSMun): 
O valor do total de IBS (vIBS) deverá ser a soma do vIBSUF e do 
vIBSMUn 
vIBS = vIBSUF + vIBSMun 
 
Obrig. 317 Rej. Rejeição: Total de IBS difere do ca lculado

## Página 38

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 38  / 80  
 
F103 Se informado grupo CBS (gCBS): 
A alíquota de CBS deverá ser: 
• 0,90 % para documento com data de emissão no ano d e 2026. 
(Art. 346 da LC 214/25) 
• Alíquota de referência a ser publicada para anos p osteriores a 
2026 
 
Exceção : Se o cClassTrib possuir indicador de tributação regular o pCBS 
deve ser igual a zero 
Obrig. 326 Rej. Rejeição: Alíquota da CBS inválida 
F104 Se CST informado possuir indicador que EXIGE informação de redução de 
alíquota para o CBS ou informado grupo de compra governamental, o 
grupo gRed DEVE estar informado 
Exceção:  A regra não se aplica para CST do IBS/CBS (tag: IBSCBS/CST)  
que possui indicador que não permite a informação do IBS/CBS 
Obrig. 383 Rej. Rejeição: CST informado ou compras governamentais 
obriga informação de redução de alíquota do CBS 
F105 Se informado grupo de Redução de Alíquota para CBS (gCBS/gRed): 
Verificar se percentual de Redução de Alíquota (pRedAliq) é válido para o 
cClassTrib informado (gIBSCBS/cClassTrib) 
Obrig. 393 Rej. Rejeição: Percentual de redução de alíquota da CBS não é 
válido para este cClassTrib 
F106 Se informado grupo de Redução de Alíquota para CBS (gCBS/gRed), a 
Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado de: 
Se NÃO houver compra governamental (grupo gCompraGov não 
informado):  
pAliqEfet = pCBS × (1 - pRedAliq /100). 
 
Se houver compra governamental (grupo gCompraGov informado): 
pAliqEfet = pCBS × (1 - pRedAliq /100) × (1 - pRedutor/100). 
 
Observação : pRedutor é obtido no grupo gCompraGov 
 
Exemplo: Redução de 40% na alíquota: 
Alíquota vigente (A): 10% 
Redução na alíquota (R): 40% 
Redutor de compras governamentais (RG): 5% 
Alíquota Efetiva (E):  
E = A × (1 – R/100) × (1 – RG/100) = 5,7. 
Obrig. 394 Rej. Rejeição: Valor da Alíquota Efetiva  da CBS calculado 
incorretamente 
F107 Se CST informado possuir indicador que VEDA a informação de redução 
de alíquota para o CBS, o grupo gRed NÃO DEVE estar informado 
 
Exceção : Se Percentual de redução de alíquota em compra 
governamental (tag:gCompraGov/pRedutor) informado, este grupo é 
exigido e pRed deve ser igual a 0. 
Obrig. 384 Rej. Rejeição: CST informado não permite  informação de 
redução de alíquota do CBS

## Página 39

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 39  / 80  
 
F108 Se CST informado possuir indicador que EXIGE informação de Diferimento 
para o CBS, o grupo gDif DEVE estar informado 
Obrig. 328 Rej. Rejeição: CST informado obriga info rmação de diferimento 
do CBS 
F109 Se CST informado possuir indicador que VEDA informação de Diferimento 
para o CBS, o grupo gDif NÃO DEVE estar informado 
Obrig. 385 Rej. Rejeição: CST informado não permite  informação de 
diferimento do CBS 
F110 Se informado grupo do Diferimento (gCBS/gDif): 
O valor do Diferimento (vDif) deverá ser resultante de: 
vDif = vBC x (pCBS/100) x (pDif/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet) 
Obrig. 329 Rej. Rejeição: Valor do Diferimento do C BS difere do calculado 
F111 Se informado grupo CBS (gCBS): 
O valor resultante da soma do diferimento (vDif) e Devolução (DevTrib) 
QUANDO INFORMADOS, NÃO pode ser superior a vBC x (pCBS/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a alíquota 
utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet)  
Obrig. 397 Rej. Rejeição: Valor do CBS não pode res ultar negativo 
F112 Se informado grupo CBS (gCBS): 
O valor da CBS (vCBS) deverá ser resultante de: 
vCBS = vBC x (pCBS/100) – vDif – vDevTrib 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Observação  2: Em caso de preenchimento do grupo de redução (gRed) a 
alíquota utilizada deverá ser a tag Alíquota Efetiva (pAliqEfet). 
Obrig. 327 Rej. Rejeição: Valor do CBS difere do ca lculado 
F113 Se cClassTrib informado possuir indicador que EXIGE informação de 
tributação regular, o grupo gTribRegular DEVE estar informado 
Obrig. 330 Rej. Rejeição: Classificação Tributária informada obriga 
informação da tributação regular  
F114 Se cClassTrib informado NÃO POSSUIR indicador de informação de 
tributação regular, o grupo gTribRegular NÃO DEVE estar informado 
Obrig. 322 Rej. Rejeição: Classificação Tributária não permite informação da 
tributação regular 
F115 Se informado grupo da tributação regular (gTribRegular): 
O CST Regular informado no grupo gTribRegular deve existir na tabela de 
Código de Situação Tributária (gTribRegular/CSTReg) 
Obrig. 331 Rej. Rejeição: CST informado no grupo de  tributação regular 
inexistente 
F116 Se informado grupo da tributação regular (gTribRegular): 
O cClassTrib regular for informado, este deve existir na tabela de 
Classificação Tributária do IBS/CBS (tag: gTribRegular/cClassTribReg) 
Obrig. 332 Rej. Rejeição: Classificação Tributária informada no grupo de 
tributação regular inexistente 
F117 Se informado grupo da tributação regular (gTribRegular): 
O valor do tributo regular de IBS dos Estados (vTribRegIBSUF) deverá ser 
resultante de: 
vTribRegIBSUF = vBC x (pAliqEfetRegIBSUF/100) 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos  
Obrig. 333 Rej. Rejeição: Valor da tributação regul ar da UF difere do 
calculado

## Página 40

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 40  / 80  
 
F118 Se informado grupo da tributação regular (gTribRegular): 
O valor do tributo regular de IBS dos Municípios (vTribRegIBSMun) deverá 
ser resultante de: 
vTribRegIBSMun = vBC x (pAliqEfetRegIBSMun/100) 
 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Obrig. 334 Rej. Rejeição: Valor da tributação regul ar do Município difere do 
calculado 
F119 Se informado grupo da tributação regular (gTribRegular): 
O valor do tributo regular de CBS (vTribRegCBS) deverá ser resultante de: 
vTribRegularCBS = vBC x (pAliqEfetRegCBS/100) 
Observação : Aceitar uma tolerância de 0,01 a mais ou a menos 
Obrig. 335 Rej. Rejeição: Valor da tributação regul ar da CBS difere do 
calculado 
F136 Se grupo compra governamental (grupo: gCompraGov) estiver informado, 
o Grupo de informações da composição do valor do IBS e da CBS em 
compras governamentais (grupo: gTribCompraGov) DEVE ser informado. 
 
Exceção:  A regra não se aplica para CST do IBS/CBS (tag: IBSCBS/CST)  
que possui indicador que não permite a informação do IBS/CBS 
Obrig. 398 Rej. Rejeição: Grupo de informações da c omposição do valor do 
IBS e da CBS em compras governamentais deve ser 
informado 
F137 Se grupo compra governamental (grupo: gCompraGov) NÃO estiver 
informado, o Grupo de informações da composição do valor do IBS e da 
CBS em compras governamentais (grupo: gTribCompraGov) NÃO DEVE 
ser informado. 
Obrig. 399 Rej, Rejeição: Grupo de informações da c omposição do valor do 
IBS e da CBS em compras governamentais não deve ser 
informado 
F138 Verificar se a soma dos valores de IBS e CBS do grupo gTribCompraGov 
(vTribIBSUF + vTribIBSMun + vTribCBS) é diferente do resultado de 
gIBSUF/vIBSUF + gIBSMun/vIBSMun + gCBS/vCBS. 
 
Obrig. 400 Rej. Rejeição: Somas dos valores de IBS e CBS em compras 
governamentais divergente 
F138a Se o cClassTrib informado possuir indicador que VEDA  preenchimento do 
grupo de informações do estorno de crédito (grupo:gEstornoCred) 
Obrig 303 Rej. Rejeição: Grupo Estorno de Crédito n ão deve ser 
preenchido para o cClassTrib informado 
F138b Se o cClassTrib informado possuir indicador que EXIGE  preenchimento do 
grupo de informações do estorno de crédito (grupo:gEstornoCred) 
Obrig 304 Rej. Rejeição: Grupo Estorno de Crédito d eve ser preenchido 
para o cClassTrib informado 
Validações de Compras Governamentais 
F139 Se informado o grupo de informações de compra governamental 
(grupo:ide\gCompraGov), o DFe de compra governamental deve ter 
alíquota de outros entes igual a zero. 
Se 2027 até 2032 
Para compra da união (tag: tpEnteGov = 1): 
• Alíquota do IBS da UF (tag: pIBSUF) deve ser igual  a zero. 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
 
Obrig. 347 Rej. Rejeição: DFe de compra governament al e alíquota dos 
outros entes diferentes de zero.

## Página 41

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 41  / 80  
 
Para compra estadual (tag: tpEnteGov = 2): 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
Para compra do DF (tag: tpEnteGov = 3) 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
Para compra municipal (tag: tpEnte = 4) 
• Alíquota do IBS da UF (tag: pIBSUF) deve ser igual  a zero. 
 
A partir de 2033: 
Para compra da união (tag: tpEnteGov = 1): 
• Alíquota do IBS da UF (tag: pIBSUF) deve ser igual  a zero. 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
Para compra estadual (tag: tpEnteGov = 2): 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
• Alíquota do CBS (tag: pCBS) deve ser igual a zero.  
Para compra do DF (tag: tpEnteGov = 3) 
• Alíquota do IBS do Município (tag: pIBSMun) deve s er igual a 
zero. 
• Alíquota do CBS (tag: pCBS) deve ser igual a zero.  
Para compra municipal (tag: tpEnte = 4) 
• Alíquota do IBS da UF (tag: pIBSUF) deve ser igual  a zero. 
• Alíquota do CBS (tag: pCBS) deve ser igual a zero.  
 
Observação : Conforme Art. 473, § 1o e seus Incisos I, II, III e IV da LC 
214/2025. 
Validações do total do DFe 
F140 O total geral do DFe deverá ser INFORMADO com a soma do total do BPe 
+ IBS + CBS: 
vTotDFe = infValorBPe/vBP + gIBSCBS/vIBS + gCBS/vCBS 
 
Exceção: Em 2026 não somar IBS e CBS, usar a fórmula:  
vTotDFe = infValorBPe/vBP  
Obrig. 365 Rej. Rejeição: Total do DFe inválido 
 
Validações da Substituição 
F141 Se o Tipo do BPe = 3 (Substituição): 
 - O grupo de informações da substituição (grupo: infBPeSub) deve ser 
Obrig. 439 Rej. Rejeição: Grupo BPe de Substituição  deve ser informado 
para o BPe de Substituição

## Página 42

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 42  / 80  
 
informado 
F142 Se o Tipo do BPe = 0 (Normal): 
- O grupo de informações da substituição (grupo: infBPeSub) NÃO deve 
ser informado 
Obrig. 440 Rej. Rejeição: Grupo BPe de Substituição  não deve informado 
para o BPe Normal 
F143 Se tipo do BPe = 3 (Substituição): 
- Validar chave de acesso do BPe substituído.  
Retornar motivo da rejeição da Chave de Acesso: CNPJ zerado ou 
inválido, Ano < 2017 ou maior que atual, Mês inválido (0 ou > 12), Modelo 
diferente de 63, Número zerado, Tipo de emissão inválido, UF inválida ou 
DV inválido) 
[Motivo: XXXXXXXXXXXX] 
Obrig. 508 Rej. Rejeição: Chave de acesso do BPe su bstituído inválida 
F144 Se Tipo do BPe = 3 (Substituição):  
- O BPe substituído deve existir 
Acesso BD BPE (Chave: CNPJ Emit, Modelo, Série, Nro) 
Obrig 449 Rej Rejeição: BPe a ser substituído inexi stente 
F145 Se Tipo do BPe = 3 (Substituição):  
- BPe substituído não pode existir com diferença na Chave de Acesso 
Retornar a chave de acesso já autorizada, o número do protocolo e data 
de autorização do BPe 
[chBPe: 99999999999999999999999999999999999999999999] 
[nProt:999999999999999][dhAut: AAAA-MM-DDTHH:MM:SS TZD] 
Obrig. 450 Rej. Rejeição: BPe substituído com difer ença de Chave de 
Acesso 
F146 Se Tipo do BPe = 3 (Substituição): 
- O BPe substituído não pode estar cancelado  
Obrig. 451 Rej Rejeição: BPe a ser substituído deve  estar na situação 
Autorizado o Uso 
F147 Se Tipo do BPe = 3 (Substituição):  
- O BPe substituído não pode estar substituído 
Obrig. 452 Rej Rejeição: BPe a ser substituído não pode ter sido substituído 
anteriormente 
F148 Se Tipo do BPe = 3 (Substituição):  
- O BPe substituído deve ser do modal aéreo 
Obrig 469 Rej Rejeição: O BPe substituído deve ser do modal aéreo 
F149 Se Tipo do BPe = 3 (Substituição) e data-hora do embarque do BPe 
substituído for menor ou igual a data-hora do ambiente autorizador: 
Acesso BD Eventos BPe (Chave: Chave de Acesso do BPe substituído): 
- O BPe substituído deve possuir evento de não embarque associado 
Obrig. 453 Rej Rejeição: BPe a ser substituído com data/hora de embarque 
anterior a data-hora atual sem evento de Não Embarque 
associado 
F150 Se Tipo do BPe = 3 (Substituição): 
- CNPJ do emitente do BPe substituto deve ser igual ao informado no BPe 
substituído 
Obrig. 454 Rej. Rejeição: CNPJ do emitente do BPe s ubstituto deve ser 
igual ao informado no BPe substituído 
F151 Se Tipo do BPe = 3 (Substituição): 
- IE do emitente do BPe substituto deve ser igual ao informado no BPe 
substituído 
Obrig, 455 Rej. Rejeição: IE do emitente do BPe sub stituto deve ser igual à 
informada no BPe substituído 
F152 Se Tipo do BPe = 3 (Substituição):  
- O CNPJ/CPF do comprador do BPe substituto deve ser igual ao 
Obrig. 456 Rej. Rejeição: CNPJ/CPF do comprador do BPe substituto deve 
ser igual ao informado no BPe substituído

## Página 43

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 43  / 80  
 
informado no BPe substituído 
 
Observação : Rejeitar caso não exista identificação do comprador no BPe 
original e informado no substituto (ou vice-versa) 
F154 Se Tipo do BPe = 3 (Substituição): 
- UF e Município de início e fim da viagem devem ser iguais aos 
informados no BPe substituído  
Obrig. 458 Rej. Rejeição: UF e Município de início e fim da viagem do BPe 
substituto devem ser iguais aos informados no BPe 
substituído 
Validações de Banco de Dados 
F155 Acessar BD BPe (Chave: CNPJ Emit, Modelo, Série, Nro): 
 - Verificar Duplicidade de BPe com diferença na Chave de Acesso 
(Campo de Código Numérico difere) 
Retornar a chave de acesso já autorizada, o número do protocolo e data 
de autorização 
[chBPe: 99999999999999999999999999999999999999999999] 
[nProt:999999999999999][dhAut: AAAA-MM-DDTHH:MM:SS TZD] 
Obrig 539 Rej. Rejeição: Duplicidade de BPe, com di ferença na Chave de 
Acesso 
 
 
  
F156 Acessar BD BPe (Chave: CNPJ Emit, Modelo, Série, Nro): 
Verificar Duplicidade de BPe 
Retornar Protocolo e data de autorização. 
[nProt:999999999999999][dhAut: AAAA-MM-DDTHH:MM:SS TZD]. 
Observação : Esta validação leva em consideração o ambiente de 
autorização do DFe 
Obrig. 204 Rej. Rejeição: Duplicidade de BPe  
 
F157 Verificar se BPe está cancelado 
Retornar Protocolo e data de autorização do evento de cancelamento.  
[nProt:999999999999999][dhCanc: AAAA-MM-DDTHH:MM:SS TZD] 
Obrig. 218 Rej. Rejeição: BPe já está cancelado na base de dados da SEFAZ 
 
F158 Verificar se BPe está substituído: 
Retornar Protocolo e data de autorização do evento de substituição.  
[nProt:999999999999999][dhSubst: AAAA-MM-DDTHH:MM:SS TZD] 
Obrig. 224 Rej. Rejeição: BPe já está substituído n a base de dados da 
SEFAZ. 
 
Validações de Autorizados ao XML 
F159 Se informada autorização download XML com CNPJ: 
CNPJ com zeros ou dígito inválido 
Obrig. 466 Rej. Rejeição: CNPJ autorizado para down load inválido 
F160 Se informada autorização download do XML com CPF:  
CPF com zeros, nulo, números repetidos (111, 222, etc.), ou dígito de 
controle inválido. 
Obrig. 467 Rej. Rejeição: CPF autorizado para downl oad inválido 
F161 Se informada autorização download XML: 
- Verificar se existe duplicidade de CPF/CNPJ informado no grupo autXML  
 
Obrig. 412 Rej Rejeição: Documento autorizado ao XM L duplicado no BPe 
 
Validações do QR Code

## Página 44

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 44  / 80  
 
F162 Endereço do site da UF para a Consulta via QR Code difere do previsto.  
Nota: O uso diferenciado de maiúsculas ou minúsculas não deve ser 
considerado na validação.  
Observação : Para consultar as URLs por UF utilizadas no QR Code, 
acesse: 
https://dfe-portal.svrs.rs.gov.br/BPE/Servicos  
Obrig. 479 Rej. Rejeição: Endereço do site da UF da  Consulta via QR Code 
diverge do previsto 
 
F163 Parâmetro Chave de Acesso no QR Code diverge da Chave de Acesso do 
BPe 
Obrig. 481 Rej. Rejeição: Parâmetro do QR Code dive rgente do BPe 
F164 Se tipo de emissão for igual a Contingência Off-line: 
O parâmetro sign deve informado no QR-Code 
Obrig. 482 Rej. Rejeição: Parâmetro sign não inform ado no QR Code para 
emissão em contingência 
F165 Se tipo de emissão for igual a Normal: 
O parâmetro sign não deve ser informado no QR-Code 
Obrig. 488 Rej. Rejeição: Parâmetro sign não deve s er informado no QR 
Code para emissão Normal 
F166 Se tipo de emissão for igual a Contingência Off-line: 
Valor da assinatura (sign) do QR-Code difere do valor calculado 
Obrig. 496 Rej. Rejeição: Assinatura do QR-Code dif ere do calculado 
Validações do Responsável Técnico 
F167 Não informado o grupo de informações do responsável técnico 
 
Observação: Implementação à critério da UF  
Facul. 679 Rej. 
Rejeição: Obrigatória as informações do responsável técnico 
F168 Se informado grupo do responsável técnico (grupo: infRespTec): 
- Validar CNPJ (dígito controle, zeros ou nulo).  
Facul. 510 Rej. Rejeição: CNPJ do responsável técni co inválido (zerado ou 
dígito inválido) 
F169 
Obrigatória a informação do identificador do CSRT (tag:idCSRT) e Hash do 
CSRT (tag: hashCSRT) 
 
Observação: Implementação futura  
Facul. 680 Rej. 
Rejeição: Obrigatória a informação do identificador do CSRT 
e do Hash do CSRT 
 Final do Processamento do BPe TA 
 
A validação do BPe TA poderá resultar em: 
• Rejeição  – o BPe TA será descartado, não sendo armazenado n o Banco de Dados podendo ser corrigido e novamente transmitido; 
• Autorização de uso  – o BPe TA será armazenado no Banco de Dados; 
Ou seja: 
 
 
Validação Consequência 
De forma do BPe TA Situação do BPe TA Para o contribuinte Banco de Dados

## Página 45

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 45  / 80  
 
Inválida Rejeição Corrigir BPe TA Não gravar 
Válida Autorização de uso Autorizado Gravar 
 
Para cada BPe TA será atribuído um número de protocolo do Ambiente Autorizador. 
4.2 Serviço de Consulta Situação do BPe 
 
Função : serviço destinado ao atendimento de solicitações de consulta da situação atual do BPe na Base de Dados do Ambiente Autorizador. 
 
Processo : síncrono. 
 
Método: bpeConsultaBP 
 
Parâmetro da Mensagem da área de dados: XML sem compactação 
 Leiaute Mensagem de Entrada 
 
Entrada: Estrutura XML contendo a chave de acesso do BPe. 
Schema XML: consSitBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
BP01 consSitBPe Raiz - - - - TAG raiz  
BP02 versao A BP01 N 1-1 2v2 Versão do leiaute 
BP03 tpAmb E BP01 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 - Homologação 
BP04 xServ E BP01 C 1-1 9 Serviço solicitado: ‘CONSULTAR ’ 
BP05 chBPe E BP01 N 1-1 44 Chave de acesso do BPe 
 Leiaute Mensagem de Retorno 
 
Retorno: Estrutura XML com o resultado da consulta situação. 
Schema XML: retConsSitBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação

## Página 46

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 46  / 80  
 
BR01 retConsSitBPe Raiz - - - - TAG raiz da Resposta 
BR02 versao A BR01 N 1-1 2v2 Versão do leiaute 
BR03 tpAmb E BR01 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 - Homologação 
BR04  verAplic E BR01 C 1-1 1-20 Versão do Aplicativo que  processou a consulta 
BR05  cStat E BR01 N 1-1 4 Código do status da resposta 
BR06  xMotivo E BR01 C 1-1 1-255 Descrição literal do sta tus da resposta 
BR07  cUF E BR01 N 1-1 2 Código da UF que atendeu à solic itação 
BR08  protBPe G BR01 XML 0-1 - Protocolo de autorização d e uso do BPe 
BR09  procEventoBPe G BR01 XML 0-N - Informações dos even tos e respectivo protocolo de registro de evento. 
 Descrição do Processo de Web Service 
 
Este método será responsável por receber as solicitações referentes à consulta do status do serviço do Ambiente Autorizador. 
O aplicativo do contribuinte envia a solicitação para o Web Service do Ambiente Autorizador. Ao receber a solicitação a aplicação do Ambiente Autorizador processará a solicitação 
de consulta, e retornará mensagem contendo o status do serviço. 
A empresa que construir aplicativo que se mantenha em permanente "loop" de consulta a este Web Service, deverá aguardar um tempo mínimo de 3 minutos entre uma consulta 
e outra, evitando sobrecarga desnecessária dos servidores do Ambiente Autorizador. 
 Regras de Validação Básicas do Serviço 
 
Deverão ser aplicadas as validações gerais conforme quadro abaixo: 
Grupo Descrição 
A Validação do Certificado de Transmissão (protocolo  TLS) 
B Validação Inicial da Mensagem no Web Service  
C Validação da Área de Dados da mensagem 
 Validação das Regras de Negócio da Consulta Situação 
 
# Regra de Validação Aplic cStat. Efeito Mensagem 
G01  Tipo do ambiente informado difere do ambiente do Web Service Obrig. 252 Rej. Rejeição: Ambiente inform ado diverge do Ambiente de

## Página 47

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 47  / 80  
 
recebimento 
G02  UF da chave de acesso difere da UF do Web Service O brig. 226 Rej. Rejeição: Código da UF do Emitente d iverge da UF autorizadora 
G03 Verificar se o ano – mês da chave de acesso está co m atraso superior a 6 
meses em relação ao ano – mês atual 
Obrig 413 Rej. Rejeição: Consulta a uma Chave de Ac esso muito antiga 
G04 - Validar chave de acesso  
Retornar motivo da rejeição da Chave de Acesso: CNPJ zerado ou 
inválido, Ano < 2017 ou maior que atual, Mês inválido (0 ou > 12), Modelo 
diferente de 63, Número zerado, Tipo de emissão inválido, Site de 
Autorização inválido, UF inválida ou DV inválido) 
[Motivo: XXXXXXXXXXXX] 
Obrig. 236 Rej. Rejeição: Chave de Acesso inválida 
[Motivo: XXXXXXXXX] 
G05 Acesso BD BPe (Chave: CNPJ Emit, Modelo, Série, Nro): 
- Verificar se BPe não existe 
Obrig. 217 Rej. Rejeição: BPe não consta na base de  dados da SEFAZ 
G06 Verificar se campo “Código Numérico” informado na Chave de Acesso é 
diferente do existente no BD 
Obrig. 216 Rej. Rejeição: Chave de Acesso difere da  cadastrada 
G07 Chave de Acesso difere da existente em BD (opcionalmente a descrição 
do erro, campo xMotivo, tem concatenada a Chave de Acesso, quando o 
autor da consulta for o emissor) 
Obrig. 600 Rej. Rejeição: Chave de Acesso difere da  existente em BD 
 Final do Processamento  
 
No processamento do pedido de consulta de status de BP-e pode resultar em uma mensagem de erro, caso o BP-e não seja localizado. Ou, caso localizado, retornar a situação 
atual do BP-e consultado, retornando o cStat com um  dos valores, 100 ("Autorizado o Uso do BP-e"), 101  ("Cancelamento de BP-e homologado"), 102 ("Substit uição do BP-e 
homologada"), 150 ("Autorizado o Uso do BP-e, autorização fora de prazo") e o respectivo protocolo de autorização de uso e registro de eventos.

## Página 48

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 48  / 80  
 
4.3 Serviço de Consulta Status do Serviço de Autori zação 
 
Função : serviço destinado à consulta do status do serviço prestado pelo Ambiente Autorizador. 
 
Processo : síncrono. 
 
Método: bpeStatusServicoBP 
 
Parâmetro da Mensagem da área de dados: XML sem compactação 
 Leiaute Mensagem de Entrada 
 
Entrada: Estrutura XML para a consulta do status do serviço. 
Schema XML: consStatServBPe_v99.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
CP01 consStatServBPe Raiz - - - - TAG raiz  
CP02 versao A CP01 N 1-1 2v2 Versão do leiaute 
CP03 tpAmb E CP01 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 - Homologação 
CP04 xServ E CP01 C 1-1 6 Serviço solicitado: ‘STATUS’ 
 Leiaute Mensagem de Retorno 
 
Retorno: Estrutura XML com o resultado da consulta status serviço. 
Schema XML: retConsStatServBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
CR01 retConsStatServBPe Raiz - - - - TAG raiz da Resposta 
CR02 versao A CR01 N 1-1 2v2 Versão do leiaute 
CR03 tpAmb E CR01 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 - Homologação 
CR04  verAplic E CR01 C 1-1 1-20 Versão do Aplicativo que  processou a consulta 
CR05  cStat E CR01 N 1-1 4 Código do status da resposta 
CR06  xMotivo E CR01 C 1-1 1-255 Descrição literal do sta tus da resposta 
CR07  cUF E CR01 N 1-1 2 Código da UF que atendeu à solic itação

## Página 49

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 49  / 80  
 
CR08 dhRecbto E CR01 D 1-1 - Data e hora de recebimento do pedido 
Formato = AAAA-MM-DDTHH:MM:SS TZD 
CR09 tMed E CR01 N 0-1 1-4 Tempo médio de resposta do se rviço (em segundos) dos últimos 5 
minutos 
CR10 dhRetorno E CR01 D 0-1 - Preencher com data e hora previstas para o retorno do Web Service, 
no formato AAA-MM-DDTHH:MM:SS 
CR11  xObs E CR01 C 0-1 1-255 Informações adicionais ao c ontribuinte 
 Descrição do Processo de Web Service 
 
Este método será responsável por receber as solicitações referentes à consulta do status do serviço do Ambiente Autorizador. 
O aplicativo do contribuinte envia a solicitação para o Web Service do Ambiente Autorizador. Ao receber a solicitação a aplicação do Ambiente Autorizador processará a solicitação 
de consulta, e retornará mensagem contendo o status do serviço. 
A empresa que construir aplicativo que se mantenha em permanente "loop" de consulta a este Web Service, deverá aguardar um tempo mínimo de 3 minutos entre uma consulta 
e outra, evitando sobrecarga desnecessária dos servidores do Ambiente Autorizador. 
Deverão ser realizadas as validações e procedimentos que seguem: 
 Regras de Validação Básicas do Serviço 
 
Deverão ser aplicadas as validações gerais conforme quadro abaixo: 
 
Grupo Descrição 
A Validação do Certificado de Transmissão (protocolo  TLS) 
B Validação Inicial da Mensagem no Web Service  
C Validação da Área de Dados da mensagem

## Página 50

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 50  / 80  
 
 Validação das Regras de Negócio da Consulta Status Serviço 
 
# Regra de Validação Aplic cStat. Efeito Mensagem 
J01 Tipo do ambiente informado difere do ambiente do Web Service Obrig. 252 Rej. Rejeição: Ambiente inform ado diverge do Ambiente de 
recebimento 
J02 Verifica se o Servidor de Processamento está Paralisado 
Momentaneamente 
Obrig. 108 - Serviço Paralisado Momentaneamente (cu rto prazo) 
J03  Verifica se o Servidor de Processamento está Paralisado sem Previsão Obrig. 109 - Serviço Paralisado s em Previsão 
 Final do Processamento  
 
O processamento do pedido de consulta de status de Serviço pode resultar em uma mensagem de erro ou retornar a situação atual do Servidor de Processamento, códigos de 
situação 107 (“Serviço em Operação”), 108 (“Serviço  Paralisado Momentaneamente”) e 109 (“Serviço Paralisado sem Previsão”).

## Página 51

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 51  / 80  
 
5 Sistema de Registro de Eventos (Parte Geral) 
Função : serviço destinado à recepção de mensagem de evento de BPe. 
 
Processo : síncrono. 
 
Método: bpeRecepcaoEvento 
 
Parâmetro da Mensagem da área de dados: XML sem compactação 
5.1 Leiaute Mensagem de Entrada 
 
Entrada: Estrutura XML contendo a consulta do status do serviço 
Schema XML: eventoBPe_v9.99.xsd 
# Campo  Ele  Pai  Tipo  Ocor.  Tam.  Descrição /Observação  
DP01  eventoBPe Raiz - - - - TAG raiz  
DP02  versao A FP01 N 1-1 2v2 Versão do leiaute 
DP03 infEvento G FP01 - 1-1  Grupo de informações do reg istro de eventos 
DP04 Id ID FP03 C 1-1 54 Identificador da TAG a ser assi nada, a regra de formação do Id é: 
“ID” + tpEvento+ chave do BPe + nSeqEvento 
DP05 cOrgao E FP03 N 1-1 2 Código do órgão de recepção d o Evento. Utilizar a Tabela do IBGE 
estendida 
DP06 tpAmb E FP03 N 1-1 1 Identificação do Ambiente: 
1 – Produção 2 – Homologação 
DP07  CNPJ E FP03 C 1-1 14 Informar o CNPJ do autor do Ev ento 
DP08  chBPe E FP03 N 1-1 44 Chave de Acesso do BPe vincul ado ao Evento 
DP09 dhEvento E FP03 D 1-1 - Data e Hora do Evento  
Formato = AAAA-MM-DDTHH:MM:SS TZD. 
DP10  tpEvento E FP03 N 1-1 6 Tipo do Evento (ver tabela de tipos de evento) 
DP11 nSeqEvento E FP03 N 1-1 1-2 Sequencial do evento pa ra o mesmo tipo de evento.  Para maioria dos 
eventos será 1, nos casos em que possa existir mais de um evento o 
autor do evento deve numerar de forma sequencial. 
DP12  detEvento G FP03 - 1-1 - Informações do evento espe cífico. 
DP13  versaoEvento A FP12 N 1-1 2v2 Versão do leiaute esp ecífico do evento. 
DP14 any E FP12 XML 1-1 - XML do evento: Insira neste lo cal o XML específico do tipo de evento 
(cancelamento, não embarque)  
DP15  Signature G FP01 XML 1-1 - Assinatura XML do grupo identificado pelo atributo “Id”

## Página 52

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 52  / 80  
 
5.2 Leiaute Mensagem de Retorno 
 
Retorno: Estrutura XML com o resultado do pedido de evento. 
Schema XML: retEventoBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
DR01 retEventoBPe Raiz - - - - TAG raiz do Resultado do Envio do Evento 
DR02 versao A DR01 N 1-1 1-4 Versão do leiaute 
DR03  infEvento G DR01  1-1  Grupo de informações do regi stro do Evento 
DR04 Id ID DR03 C 0-1 17 Identificador da TAG a ser assi nada, somente deve ser informado se o órgão 
de registro assinar a resposta. 
Em caso de assinatura da resposta pelo órgão de registro, preencher com o 
número do protocolo, precedido pela literal “ID” 
DR05 tpAmb E DR03 N 1-1 1 Identificação do Ambiente: 
1 – Produção / 2 – Homologação 
DR06 verAplic E DR03 C 1-1 1-20 Versão da aplicação que registrou o Evento, utilizar literal que permita a 
identificação do órgão, como a sigla da UF ou do órgão. 
DR07  cOrgao E DR03 N 1-1 2 Código da UF que registrou o Evento.  
DR08  cStat E DR03 N 1-1 4 Código do status da resposta  
DR09  xMotivo E DR03 C 1-1 1-255 Descrição do status da r esposta  
Os campos a seguir são obrigatórios no caso de homologação do evento cStat=135, 134 ou cStat=136. 
Os campos de dhRegEvento  e nProt  não serão preenchidos em caso de erro  
DR10  chBPe E DR03 N 0-1 44 Chave de Acesso do BPe vincul ado ao evento 
DR11  tpEvento E DR03 N 0-1  6 Código do Tipo do Evento 
DR12  xEvento E DR03 C 0-1 5-60 Descrição do Evento 
DR13 nSeqEvento E DR03 N 0-1 1-2 Sequencial do evento pa ra o mesmo tipo de evento.  Para maioria dos 
eventos será 1, nos casos em que possa existir mais de um evento o autor do 
evento deve numerar de forma sequencial. 
DR14  dhRegEvento E DR03 D 0-1  Data e Hora do Evento For mato = AAAA-MM-DDTHH:MM:SS TZD 
DR15  nProt E DR15 N 0-1 15 Número do protocolo de regist ro do evento 
DR16 Signature G DR01 XML 0-1  Assinatura Digital do doc umento XML, a assinatura deverá ser aplicada no 
elemento infEvento. A decisão de assinar a mensagem fica a critério do 
Ambiente Autorizador

## Página 53

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 53  / 80  
 
5.3 Descrição do Processo de Web Service 
 
Este método é responsável por receber as solicitações referentes ao registro de eventos de BPe. Ao receber a solicitação do transmissor, a aplicação do Ambiente Autorizador 
realiza o processamento da solicitação e devolve o resultado do processamento para o aplicativo dele.  
5.4 Regras de Validação Básicas do Serviço 
 
Deverão ser aplicadas as validações gerais conforme quadro abaixo: 
 
Grupo Descrição 
A Validação do Certificado de Transmissão (protocolo  TLS) 
B Validação Inicial da Mensagem no Web Service  
C Validação da Área de Dados da mensagem 
D Validação do Certificado de Assinatura 
E Validações da Assinatura Digital 
5.5 Validação das Regras de Negócio do Serviço de R egistro de Eventos 
 
# Regra de Validação 
 Aplic. cStat Efeito Mensagem 
I01 Tipo do ambiente difere do ambiente do Web Service   
 Obrig. 252 Rej. Rejeição: Ambiente informado diverge do Ambiente de 
recebimento 
I02 Verificar se o código do órgão de recepção do Evento diverge do solicitado Obrig. 226 Rej. Rejeição: Código da UF do Emitente diverge da UF 
autorizadora 
I04 Validar CNPJ do autor do evento (DV ou zeros)  
 
 
Obrig. 627 Rej. Rejeição: CNPJ do autor do evento inválido 
I05 Validar se atributo Id corresponde à concatenação dos campos evento 
(“ID” + tpEvento + chBPe + nSeqEvento) Obrig. 628 Rej. 
Rejeição: Erro Atributo ID do evento não corresponde à 
concatenação dos campos (“ID” + tpEvento + chBPe + 
nSeqEvento) 
I06 Verificar se o tpEvento é válido Obrig. 629 Rej. Rejeição: O tpEvento informado inválido 
I07 
Verificar Schema da parte específica do Evento 
OBS: Utilizar o tpEvento + o atributo versaoEvento para identificar qual 
schema deve ser validado. 
Obrig. 630 Rej. 
Rejeição: Falha no Schema XML específico para o evento 
I08 
- Validar chave de acesso 
Retornar motivo da rejeição da Chave de Acesso: CNPJ zerado ou 
inválido, Ano < 2017 ou maior que atual, Mês inválido (0 ou > 12), Modelo 
Obrig. 236 Rej. 
Rejeição: Chave de Acesso inválida 
[Motivo: XXXXXXXXX]

## Página 54

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 54  / 80  
 
diferente de 63, Número zerado, Tipo de emissão inválido, UF inválida ou 
DV inválido) 
[Motivo: XXXXXXXXXXXX] 
I16 Verificar duplicidade do evento (cOrgao + tpEvento + chBPe + 
nSeqEvento) Obrig. 631 Rej. 
Rejeição: Duplicidade de evento 
 [nProt:999999999999999][ dhRegEvento: AAAA-MM-
DDTHH:MM:SS TZD] 
I17 Se evento do emissor verificar se CNPJ do Autor diferente do CNPJ da 
chave de acesso do BPe Obrig. 632 Rej. 
Rejeição: O autor do evento diverge do emissor do BPe 
I18 Se evento do Fisco/RFB/Outros órgãos, verificar se CNPJ do Autor consta 
da tabela de órgãos autorizados a gerar evento. Obrig. 633 Rej. 
Rejeição: O autor do evento não é um órgão autorizado a 
gerar o evento 
I19 
Se evento exige BPe: 
Acesso BD BPe (Chave: CNPJ Emit, Modelo, Série, Nº):  
- Verificar se BPe não existe 
Obrig. 217 Rej. 
Rejeição: BPe não consta na base de dados da SEFAZ 
I20 
Se existir o BPe: (Independente do evento exigir) 
Verificar se a Chave de Acesso difere da existente em BD (opcionalmente 
a descrição do erro, campo xMotivo, tem concatenada a Chave de Acesso) 
Obrig. 600 Rej. 
Rejeição: Chave de Acesso difere da existente em BD 
I20a 
Se o BPe for do tipo = 4 (Transporte Metropolitano) não deve aceitar 
eventos dos tipos: Não Embarque, Substituição e Excesso de Bagagem, 
Fornecimento não realizado e Ajuste de BPe TA. 
Obrig. 703 Rej. 
Rejeição: Tipo de evento inválido para BPe TM 
I20b Se o modal do BP-e for do tipo = 2 (Transporte Aéreo) não deve aceitar 
eventos dos tipos: Excesso de Bagagem e Alteração de Poltrona. Obrig, 708 Rej. 
Rejeição: Tipo de evento inválido para BPe TA 
I20c Se o modal do BP-e for DIFERENTE de 2 (Transporte Aéreo) não deve 
aceitar eventos dos tipos: Fornecimento não realizado e Ajuste de BPe TA Obrig, 709 Rej. 
Rejeição: Tipo de evento inválido para BPe e BPe TM 
I21 
Data do evento não pode ser menor que a data de emissão do BPe, se 
existir. 
A SEFAZ deve tolerar uma diferença máxima de 5 minutos em função da 
sincronização de horário de servidores. 
Obrig. 634 Rej. 
Rejeição: A data do evento não pode ser menor que a data de 
emissão do BPe 
I22 
Data do evento não pode ser menor que a data de autorização do BPe, se 
existir 
A SEFAZ deve tolerar uma diferença máxima de 5 minutos em função da 
sincronização de horário de servidores. 
Obrig. 637 Rej. 
Rejeição: A data do evento não pode ser menor que a data de 
autorização do BPe 
I23 
Data do evento não pode ser maior que a data de processamento. (O 
Ambiente Autorizador deve considerar a hora local do emissor para a 
validação). A SEFAZ deve tolerar uma diferença máxima de 5 minutos em 
função da sincronização de horário de servidores. 
Obrig. 635 Rej. 
Rejeição: A data do evento não pode ser maior que a data do 
processamento

## Página 55

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 55  / 80  
 
5.6 Processamento das validações específicas de cad a evento 
 
Serão definidas no item 6 desta Nota Técnica correspondentes a cada evento. 
5.7 Final do Processamento do Evento 
 
O processamento do evento pode resultar em: 
• Rejeição  – o Evento será descartado, com retorno do código do status do motivo da rejeição; 
• Recebido pelo Sistema de Registro de Eventos, com v inculação do evento no respetivo BPe , o Evento será armazenado no repositório do Sistem a de Registro 
de Eventos com a vinculação do Evento no respectivo BPe (cStat=135); 
• Recebido pelo Sistema de Registro de Eventos – vinc ulação do evento ao respectivo BPe prejudicado – o Evento será armazenado no repositório do Sistem a 
de Registro de Eventos, a vinculação do evento ao respectivo BPe fica prejudicada face a inexistência do BPe no momento do recebimento do Evento (cStat=136); 
• Recebido pelo Sistema de Registro de Eventos, com vinculação do evento no respectiva BPe com situação diferente de Autorizado , o Evento será armazenado 
no repositório do Sistema de Registro de Eventos com a vinculação do Evento no respectivo BPe retornando um alerta com a situação de BPe (cStat=134) ; 
O Ambiente Autorizador deverá compartilhar os eventos autorizados no Sistema de Registro de Eventos com os órgãos interessados.

## Página 56

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 56  / 80  
 
6 Sistema de Registro de Eventos (Parte Específica)  
6.1 Evento de Cancelamento 
 
Função : evento destinado ao atendimento de solicitações de cancelamento de BPe. 
 
Autor do Evento : O autor do evento é o emissor do BPe TA. A mensag em XML do evento será assinada com o certificado di gital que tenha o CNPJ base do Emissor do BPe 
TA. 
 
Código do Tipo de Evento: 110111 
Schema XML: evCancBPe_v9.99.xsd 
 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
EP01 evCancBPe G - - - - TAG raiz  
EP02 descEvento E EP01 C 1-1 12 Descrição do Evento: ‘Ca ncelamento’ 
EP03 nProt E EP01 N 1-1 15 Informar o número do protocol o de autorização do BPe TA a ser 
cancelado 
EP04  xJust E EP01 C 1-1 1-255 Informar a justificativa d o cancelamento 
 Validação das Regras Específicas do Evento 
 
# Regra de Validação 
 
Aplic. cStat Efeito Mensagem 
J0 1 Verificar se o nSeqEvento é maior que o valor permitido (=1) Obrig. 636 Rej. Rejeição: O número sequen cial do evento é maior que o permitido 
J02 Emitente deve estar habilitado na base de dados para emissão do BPe 
 
Obrig. 203 Rej. Rejeição: Emissor não habilitado pa ra emissão do BPe 
J03 Verificar se BPe já está cancelado. Obrig. 218 Rej. Rejeição: BPe já está cancelado na base de dados da SEFAZ.  
[nProt:999999999999999][dhCanc: AAAA-MM-DDTHH:MM:SS 
TZD]. 
J04 Verificar se BPe já está substituído Obrig. 224 Rej. Rejeição: BPe já está substituído n a base de dados da SEFAZ.  
[nProt:999999999999999][dhSubst:  AAAA-MM-DDTHH:MM:SS 
TZD]. 
J05 Vedar cancelamento se data/hora de autorização do evento for superior 
à data/hora do embarque. 
 
Obrig. 220 Rej. Rejeição: Vedado cancelamento de BP e com data/hora de 
embarque maior que data/hora atual

## Página 57

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 57  / 80  
 
Observação : Na comparação dos horários acima, aceitar uma 
tolerância de 5 minutos, devido ao sincronismo de horário entre 
servidor da Empresa e o servidor da SEFAZ Autorizadora 
 
Exceção: Em caso de BPe emitido em contingência deve ser tolerado 
um prazo de 24 horas após a data do embarque 
 
J06 Verificar se o número do Protocolo informado difere do número do 
Protocolo do BPe 
Obrig. 222 Rej. Rejeição: Protocolo de Autorização de Uso difere do cadastrado 
J07 Verificar se existe evento de Não Embarque associado ao BPe Obrig. 504 Rej. Rejeição: Cancelamento não  permitido, BPe possui evento de não 
embarque 
J07a Se tipo do BP-e = 4 (Transporte Metropolitano): 
Verificar BP-e TM autorizado há mais de 168 horas (7 dias) 
 
Observação : Exceto se existir evento de Manifestação do Fisco do tipo 
“Liberação do Prazo de Cancelamento” 
Obrig. 704 Rej. Rejeição: Vedado cancelamento de BP e com data/hora maior que 
168 horas da autorização 
 
O Fisco poderá liberar o cancelamento fora de prazo através do evento de Manifestação do Fisco do tipo “Liberação do Prazo de Cancelamento” 
 Final do Processamento 
 
Se o evento de cancelamento for homologado, a situação do BPe para efeito de consulta situação passará para “101 – Cancelamento homologado”

## Página 58

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 58  / 80  
 
6.2 Evento de Não Embarque 
 
Função : evento destinado ao atendimento de solicitações de comunicação do não embarque do BPe. 
 
Autor do Evento : O autor do evento é o emissor do BPe TA. A mensagem do evento será assinada com o certificado digital que tenha o CNPJ base do Emissor do BPe TA. 
 
Código do Tipo de Evento: 110115 
 
Schema XML: evNaoEmbBPe_v9.99.xsd 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
EP01  evNaoEmbBPe G - - - - TAG raiz  
EP02 descEvento E EP01 C 1-1 12 Descrição do Evento: ‘Nã o Embarque’ 
EP03 nProt E EP01 N 1-1 15 Informar o número do protocol o de autorização do BPe TA a receber o 
evento 
EP04  xJust E EP01 C 1-1 1-255 Informar a justificativa d o não embarque 
 Validação das Regras Específicas do Evento 
# Regra de Validação 
 
Aplic. cStat Efeito Mensagem 
J01 Verificar se o nSeqEvento é maior que o valor permitido (=1) Obrig. 636 Rej. Rejeição: O número sequen cial do evento é maior que o permitido 
J02 Emitente deve estar habilitado na base de dados para emissão do BPe Obrig. 203 Rej. Rejeição: Emissor não habilitado para emissão do BPe 
J03 Verificar se BPe já está cancelado. Obrig. 218 Rej. Rejeição: BPe já está cancelado na base de dados da SEFAZ.  
[nProt:999999999999999][dhCanc:  AAAA-MM-DDTHH:MM:SS TZD]. 
J04  Verificar se o BPe está substituído Obrig. 224 Rej. Rejeição: BPe já está substituído n a base de dados da SEFAZ.  
[nProt:999999999999999][dhSubst:  AAAA-MM-DDTHH:MM:SS 
TZD]. 
J05 Verificar se data-hora do evento não ultrapassa 24 horas da data-hora 
de embarque informada no BPe. 
Obrig, 221 Rej. Rejeição: Prazo para geração do eve nto de não embarque 
superior ao limite tolerado em relação a data-hora do embarque 
J06 Verificar se a data-hora de embarque do BPe é anterior à data de 
processamento do evento 
Obrig. 234 Rej. Rejeição: Evento de não embarque de ve ser posterior a data-hora 
do embarque 
J07 Verificar se o número Protocolo informado difere do número Protocolo 
do BPe 
Obrig. 222 Rej. Rejeição: Protocolo de Autorização de Uso difere do cadastrado 
 Final do Processamento 
 
Se o evento de não embarque for homologado o status de retorno deverá ser cStat=135

## Página 59

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 59  / 80  
 
6.3 Evento de Fornecimento não realizado com pagame nto antecipado 
 
Função : Permitir ao fornecedor informar que um pagamento antecipado não teve o respectivo fornecimento realizado 
 
Autor do Evento : O autor do evento é o emissor do BPe TA. A mensagem do evento será assinada com o certificado digital que tenha o CNPJ base do Emissor do BPe TA. 
 
Código do Tipo de Evento: 112140 
 
Schema XML: evFornecNaoRealizBPe_v9.99.xsd 
 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
EP01 evFornNaoRealizBPe G - - - - TAG raiz  
EP02 descEvento E EP01 C 1-1 12 Descrição do Evento: ‘Fo rnecimento Não Realizado’ 
EP03 nProt E EP01 N 1-1 15 Informar o número do protocol o de autorização do BPe TA a receber o 
evento 
EP04  vIBS E EP01 N 1-1 13v2 Valor do IBS correspondente ao serviço que não foi fornecido 
EP05  vCBS E EP01 N 1-1 13v2 Valor da CBS correspondente ao serviço que não foi fornecido 
 Validação das Regras Específicas do Evento 
# Regra de Validação Aplic. cStat Efeito Mensagem 
J01 Verificar se o nSeqEvento é maior que o valor permitido (=1) Obrig. 636 Rej. Rejeição: O número sequen cial do evento é maior que o permitido 
J02 Emitente deve estar habilitado na base de dados para emissão do BPe Obrig. 203 Rej. Rejeição: Emissor não habilitado para emissão do BPe 
J03 Verificar se BPe já está cancelado. Obrig. 218 Rej. Rejeição: BPe já está cancelado na base de dados da SEFAZ.  
[nProt:999999999999999][dhCanc:  AAAA-MM-DDTHH:MM:SS TZD]. 
J04  Verificar se o BPe está substituído Obrig. 224 Rej. Rejeição: BPe já está substituído n a base de dados da SEFAZ.  
[nProt:999999999999999][dhSubst:  AAAA-MM-DDTHH:MM:SS 
TZD]. 
J05 Verificar se o número Protocolo informado difere do número Protocolo 
do BPe 
Obrig. 222 Rej. Rejeição: Protocolo de Autorização de Uso difere do cadastrado 
 Final do Processamento 
 
Se o evento de fornecimento não realizado for homologado o status de retorno deverá ser cStat=135

## Página 60

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 60  / 80  
 
6.4 Evento de Ajuste do BPe TA – PENDENTE DE ESPECI CAÇÂO 
 
Função : evento destinado alterações de valores referentes a crédito ou débitos adicionais do BPè TA 
 
Autor do Evento : O autor do evento é o emissor do BPe TA. A mensagem do evento será assinada com o certificado digital que tenha o CNPJ base do Emissor do BPe TA. 
 
Código do Tipo de Evento: 112130 
 
Schema XML: evAjusteBPeTA_v9.99.xsd 
 
# Campo Ele Pai Tipo Ocor. Tam. Descrição/Observação 
EP01 evAjusteBPeTA G - - - - TAG raiz  
EP02 descEvento E EP01 C 1-1 12 Descrição do Evento: ‘Aj uste de BPe TA’ 
EP03 nProt E EP01 N 1-1 15 Informar o número do protocol o de autorização do BPeTA a receber o 
evento 
EP04  -- definir campos       
 Validação das Regras Específicas do Evento 
# Regra de Validação Aplic. cStat Efeito Mensagem 
J01 Verificar se o nSeqEvento é maior que o valor permitido (=1) Obrig. 636 Rej. Rejeição: O número sequen cial do evento é maior que o permitido 
J02 Emitente deve estar habilitado na base de dados para emissão do 
BPe 
Obrig. 203 Rej. Rejeição: Emissor não habilitado pa ra emissão do BPe 
J03 Verificar se BPe já está cancelado. Obrig. 218 Rej. Rejeição: BPe já está cancelado na base de dados da SEFAZ.  
[nProt:999999999999999][dhCanc:  AAAA-MM-DDTHH:MM:SS TZD]. 
J04  Verificar se o BPe está substituído Obrig. 224 Rej. Rejeição: BPe já está substituído n a base de dados da SEFAZ.  
[nProt:999999999999999][dhSubst:  AAAA-MM-DDTHH:MM:SS TZD]. 
 Final do Processamento 
 
Se o evento de não embarque for homologado o status de retorno deverá ser cStat=135

## Página 61

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 61  / 80  
 
7 Alterações no Serviço de Recepção de BPe e BPeTM 
Regra de Validação Aplic. cStat Efeito Mensagem 
Se Tipo do BPe = 3 (Substituição): 
- O BPe substituído NÃO PODE ser do modal = 2 (Transporte Aéreo) Obrig. 470 Rej. Rejeição: O BPe substituído não pode ser do modal aéreo

## Página 62

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 62  / 80  
 
8 Informações Adicionais 
8.1 Código de Classificação Tributária do IBS/CBS 
 
O grupo de informações do IBS e CBS associado ao documento fiscal contém o Código de Situação Tributária (CST) e Código de Classificação Tributária (cClassTrib) do IBS e 
CBS.  
A publicação da tabela contendo esta codificação está disponível no Portal Nacional da NF-e (www.nfe.fazenda.gov.br), na aba “Documentos”, opção “Diverso s” e no portal dos 
Documentos Fiscais Eletrônicos (dfe-portal.svrs.rs.gov.br).  
Cada código “cClassTrib” corresponde a um dispositi vo específico da Lei Complementar nº 214/2025, tornando objetiva a informação prestada pelo contribuinte quanto à forma 
como interpreta a tributação do IBS e da CBS para cada DFe. 
A tabela também contém indicadores que vinculam de forma dinâmica códigos “CST-IBS/CBS” e “cClassTrib”  com as Regras de Validação descritas nesta NT, ou que contêm 
informações necessárias para a preparação das apurações assistidas do IBS e da CBS, em atendimento ao disposto na Legislação vigente.  
Vale ressaltar que a tabela poderá sofrer alteraçõe s em virtude de aperfeiçoamentos, novidades introdu zidas em sede de Regulamento, ou para atender a nec essidades 
relacionadas à apuração assistida do IBS e da CBS. 
 
8.2 Cálculo do dígito verificador do CNPJ Alfanumér ico 
 
O CNPJ alfanumérico é composto por doze caracteres alfanuméricos e dois dígitos verificadores  numéricos. 
Os dígitos verificadores (DV) são calculados a partir dos doze primeiros caracteres em duas etapas, utilizando o módulo de divisão 11 e pesos distribuídos de 2 a 9.

## Página 63

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 63  / 80  
 
 Cálculo do primeiro dígito verificador 
 
Para cada um dos caracteres do CNPJ, atribuir o valor da coluna “Valor para cálculo do DV”, 
conforme a tabela abaixo (ou subtrair 48 do “Valor ASCII”):

## Página 64

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 64  / 80  
 
 
 
Obter o resto da divisão do somatório por 11. 
Se o resto da divisão for igual a 1 ou 0, o primeiro dígito será igual a 0 (zero). 
Senão, o primeiro dígito será igual ao resultado de 11 – resto. 
No exemplo: 
Resto da divisão 459/11 = 8. 
  1º DV = 3 (resultado de 11-8) 
 Cálculo do segundo dígito verificador 
 
Para o cálculo do segundo dígito é necessário acres centar o primeiro DV ao final do CNPJ, formando ass im treze caracteres, e repetir os passos realizados  para o primeiro 
dígito. Assim, no exemplo, temos:

## Página 65

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 65  / 80  
 
8.3 Cálculo do dígito verificador da chave de acess o do BPe TA 
 
O dígito verificador da chave de acesso do BPe TA é  baseado em um cálculo do módulo 11. O módulo 11 de  um número é calculado multiplicando-se cada algari smo pela 
sequência de multiplicadores 2,3,4,5,6,7,8,9,2,3, ... posicionados da direita para a esquerda. 
A somatória dos resultados das ponderações dos algarismos é dividida por 11 e o DV (dígito verificador) será a diferença entre o divisor (11) e o resto da divisão: 
DV = 11 - (resto da divisão) 
Quando o resto da divisão for 0 (zero) ou 1 (um), o DV deverá ser igual a 0 (zero).  
Exemplo: consideremos que a chave de acesso tem a seguinte sequência de caracteres: 
 
Somatória das ponderações = 644 
Dividindo a somatória das ponderações por 11 teremos, 644 /11 = 58 restando 6. 
Como o dígito verificador DV = 11 - (resto da divisão), portando 11 - 6 = 5 
Neste caso o DV da chave de acesso do BPe TA é igual a " 5", valor este que deverá compor a chave de acesso totalizando a uma sequência de 44 caracteres. 
IMPORTANTE : O cálculo do DV da chave de acesso deverá aplicar a mesma lógica da validação do CNPJ Alfanumérico, trocando todos os caracteres (44) que compõe a chave 
(números e letras) pelos números correspondentes da tabela ASCII subtraindo 48 . 
Posteriormente à substituição, deverá ser aplicado o cálculo do Modulo 11 para a totalidade dos dígitos resultantes da chave de acesso.  
 
 
A CH A VE DE A CESSO 5 2 0 6 0 4 3 3 0 0 9 9 1 1 0 0 2 5 0 6 5 5 0 1 2 0 0 0 0 0 0 7 8 0 0 2 6 7 3 0 1 6 1
B P ESO S 4 3 2 9 8 7 6 5 4 3 2 9 8 7 6 5 4 3 2 9 8 7 6 5 4 3 2 9 8 7 6 5 4 3 2 9 8 7 6 5 4 3 2
C P O N D ERA ÇÃO  (A *B) 20 6 0 54 0 28 18 15 0 0 18 81 8 7 0 0 8 15 0 54 40 35 0 5 8 0 0 0 0 0 0 35 32 0 0 18 4 8 49 18 0 4 18 2

## Página 66

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 66  / 80  
 
8.4 Número do protocolo 
 
O número do protocolo é gerado pelo Ambiente Autorizador para identificar univocamente as transações realizadas de autorização de uso e registro de eventos do BPe TA.  
A regra de formação do número do protocolo é: 
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
Tipo de 
Autorizador 
Código da 
UF Ano Sequencial de 10 posições 
• 1 posição com o Tipo de Autorizador (3 = SEFAZ Vir tual RS, 2 = Site Alternativo de Autorização do Ambiente Nacional); 
• 2 posições para o código da UF do IBGE; 
• 2 posições para o ano; 
• 10 posições numéricas sequenciais no ano. 
 
A geração do número de protocolo deverá ser única, sendo utilizada por todos os Web Services  que precisam atribuir um número de protocolo para o resultado do processamento. 
Juntamente ao protocolo, no DABPE aparecerá a data (DD/MM/AAAA) e hora (hh:mm:ss).  
O protocolo iniciado em 2 ocorrerá somente quando o ambiente de autorização possuir um site alternativo para situações de contingência e seguirá numeração sequencial própria 
enquanto estiver em utilização de forma transparente para a empresa emitente. 
O projeto utiliza a codificação da UF definida pelo IBGE: 
Região Norte Região Nordeste Região Sudeste Região Sul Região Centro-Oeste 
11-Rondônia 
12-Acre 
13-Amazonas 
14-Roraima 
15-Pará 
16-Amapá 
17-Tocantins 
21-Maranhão 
22-Piauí 
23-Ceará 
24-Rio Grande do Norte 
25-Paraíba 
26-Pernambuco 
27-Alagoas 
28-Sergipe 
29-Bahia 
31-Minas Gerais 
32-Espírito 
Santo 
33-Rio de 
Janeiro 
35-São Paulo 
 
41-Paraná 
42-Santa Catarina 
43-Rio Grande do 
Sul 
50-Mato Grosso do 
Sul 
51-Mato Grosso 
52-Goiás 
53-Distrito Federal

## Página 67

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 67  / 80  
 
9 Leiaute do BPe TA 
# Campo Nível Descrição Ele Tipo Ocorr. Tamanho Domínio Exp.Reg. Observações 
0 BPeTA Raíz Tag raiz do BPe TA       Raíz do XML do BPe Transporte Aéreo 
1 infBPe 0 Informações do BPe Aéreo G 
 
1 - 1 
    
2 versao 1 Versão do leiaute A C 1 - 1 
  
ER52 Ex: "1.00" 
3 Id 1 Identificador da tag a ser assinada A C 1 - 1 47 
 
ER45 Informar a chave de acesso do BPe e precedida do literal 
"BPe" 
4 ide 1 Identificação do BPe G 
 
1 - 1 
    
5 cUF 2 Código da UF do emitente do BPe E N 1 - 1 2 D1 
 
Código da UF do emitente do Documento Fiscal. Utilizar a 
Tabela do IBGE de código de unidades da federação. 
6 tpAmb 2 Tipo do Ambiente E N 1 - 1 1 D7 
 
1 - Produção 
2 - Homologação 
7 mod 2 Modelo do Bilhete de Passagem E N 1 - 1 2 D4 
 
Utilizar o código 63 para identificação do BPe 
8 serie 2 Série do documento fiscal E N 1 - 1 1 - 3 
 
ER31 Informar a série do documento fiscal (informar zero se 
inexistente). 
9 nBP 2 Número do bilhete de passagem E N 1 - 1 1 - 9 
 
ER30 Número que identifica o bilhete 1 a 999999999. 
10 cBP 2 Código numérico que compõe a Chave de 
Acesso. 
E N 1 - 1 8 
 
ER40 Código aleatório gerado pelo emitente, com o objetivo de 
evitar acessos indevidos ao documento. 
11 cDV 2 Digito verificador da chave de acesso E N 1 - 1 1 
 
ER41 Informar o dígito de controle da chave de acesso do BPe, 
que deve ser calculado com a aplicação do algoritmo 
módulo 11 (base 2,9) da chave de acesso. 
12 modal 2 Modalidade de transporte E N 1 - 1 1 D9 
 
2 - Aéreo 
13 dhEmi 2 Data e hora de emissão do Bilhete de 
Passagem 
E D 1 - 1 21 
 
ER1 Formato AAAA-MM-DDTHH:MM:DD TZD 
14 tpEmis 2 Forma de emissão do Bilhete (Normal ou 
Contingência Off-Line) 
E N 1 - 1 1 D7 
 
1 - Normal 
2 - Contingência Off-Line 
15 verProc 2 Versão do processo de emissão E C 1 - 1 1 - 20 
 
ER34 Informar a versão do aplicativo emissor de BPe. 
16 tpBPe 2 Tipo do BPe E N 1 - 1 1 D27 
 
0 - BPe normal 
3 - BPe substituição 
17 tpCompra 2 Tipo de compra do BPe Aéreo E N 1 - 1 1 D28 
 
0 - Normal 
1 - BPe múltiplo (fretamento) 
2 - Vinculado a BPe múltiplo

## Página 68

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 68  / 80  
 
18 indPres 2 Indicador de presença do comprador no 
estabelecimento comercial no momento da 
operação 
E N 1 - 1 1 D31 
 
1=Operação presencial não embarcado; 
2=Operação não presencial, pela Internet; 
3=Operação não presencial, Teleatendimento; 
4=BPe em operação com entrega a domicílio; 
5=Operação presencial embarcada; 
9=Operação não presencial, outros. 
19 UFIni 2 Sigla da UF Início da Viagem E N 1 - 1 2 D6 
 
Utilizar a Tabela do IBGE de código de unidades da 
federação 
20 cMunIni 2 Código do município do início da viagem E N 1 - 1 7 
 
ER2 
 
21 UFFim 2 Sigla da UF do Fim da Viagem E N 1 - 1 2 D5 
 
Utilizar a Tabela do IBGE de código de unidades da 
federação. 
Informar 'EX' para operações com o exterior. 
22 cMunFim 2 Código do município do fim da viagem E N 1 - 1 7 
 
ER2 
 
# --- x --- 2 Sequência XML - - 0 - 1 
   
As tags dhCont e xJust são filhas dessa sequência opcional, 
se informar uma delas, deverá informar as outra, mas o 
conjunto é opcional e exigido apenas quando emissão em 
contingência 
24 dhCont 2 Data e Hora da entrada em contingência ES D 1 - 1 21 
 
ER1 Informar a data e hora no formato AAAA-MM-
DDTHH:MM:SS 
25 xJust 2 Justificativa da entrada em contingência ES C 1 - 1 15 - 256 
 
ER34 
 
26 nroBPIATA 2 Informação do número do bilhete de 
passagem conforme definido pela IATA 
E C 0 - 1 1 - 20 
 
ER34 Número que identifica o bilhete 1 a 999999999. 
27 gCompraGov 2 Grupo de Compras Governamentais G - 0 - 1 
    
27 a tpEnteGov 3 Para administração pública direta e suas 
autarquias e fundações: 
1=União 
2=Estados 
3=Distrito Federal 
4=Municípios 
E N 1 - 1 1 D8 
  
27 b pRedutor 3 Percentual de redução de alíquota em 
compra governamental 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
27 c tpOperGov 3 Tipo da operação com ente governamental:  
1 - Fornecimento 
2 - Recebimento do Pagamento 
E N 1 - 1 1 D7 
  
28 emit 1 Identificação do Emitente do BPe G 
 
1 - 1 
    
29 CNPJ 2 CNPJ do emitente E C 1 - 1 2 
 
ER7 Informar zeros não significativos 
31 IE 2 Inscrição Estadual do emitente E N 0 - 1 2 - 14 
 
ER29

## Página 69

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 69  / 80  
 
32 xNome 2 Razão social ou Nome do emitente E C 1 - 1 2 - 60 
 
ER34 
 
33 xFant 2 Nome fantasia do emitente E C 0 - 1 1 - 60 
 
ER34 
 
34 CRT 2 Código de Regime Tributário. E N 1 - 1 1 D10 
 
Este campo será obrigatoriamente preenchido com: 
1 – Simples Nacional; 
2 – Simples Nacional – excesso de sublimite de receita bruta;  
3 – Regime Normal. 
35 enderEmit 2 Endereço do emitente G 
 
1 - 1 
    
36 xLgr 3 Logradouro E C 1 - 1 2 - 60 
 
ER34 
 
37 nro 3 Número E C 1 - 1 1 - 60 
 
ER34 
 
38 xCpl 3 Complemento E C 0 - 1 1 - 60 
 
ER34 
 
39 xBairro 3 Bairro E C 1 - 1 2 - 60 
 
ER34 
 
40 cMun 3 Código do município (utilizar a tabela do 
IBGE) 
E N 1 - 1 7 
 
ER2 
 
41 xMun 3 Nome do município E C 1 - 1 2 - 60 
 
ER34 
 
42 CEP 3 CEP E N 0 - 1 8 
 
ER40 Informar zeros não significativos 
43 UF 3 Sigla da UF E C 1 - 1 2 D6 
  
44 fone 3 Telefone E N 0 - 1 7 - 12 
 
ER43 
 
45 email 3 Endereço de E-mail E C 0 - 1 1 - 60 
 
ER54 
 
46 comp 1 Identificação do Comprador do BPe 
 
Informar quando diferente do passageiro 
G 
 
0 - 1 
    
47 xNome 2 Razão social ou Nome do comprador E C 1 - 1 2 - 60 
 
ER34 
 
# --- x --- 2 Choice XML - - 1 - 1 
   
Esta é uma escolha XML, que sinaliza que APENAS uma das 
tags CNPJ, CPF ou idEstrangeiro deve ser informado 
48 CNPJ 2 Número do CNPJ CE C 1 - 1 2 
 
ER8 Em caso de empresa não estabelecida no Brasil, será 
informado o CNPJ com zeros. 
Informar os zeros não significativos. 
49 CPF 2 Número do CPF CE N 1 - 1 11 
 
ER9 Informar os zeros não significativos. 
50 idEstrangeiro 2 Identificador do comprador em caso de 
comprador estrangeiro 
CE C 1 - 1 
  
ER42 
 
51 IE 2 Inscrição Estadual E N 0 - 1 0 - 14 
 
ER28 Informar a IE do remetente ou ISENTO se remetente é 
contribuinte do ICMS isento de inscrição no cadastro de 
contribuintes do ICMS. Caso o remetente não seja 
contribuinte do ICMS não informar a tag. 
52 enderComp 2 Endereço do comprador G 
 
1 - 1 
    
53 xLgr 3 Logradouro E C 1 - 1 1 - 255 
 
ER34

## Página 70

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 70  / 80  
 
54 nro 3 Número E C 1 - 1 1 - 60 
 
ER34 
 
55 xCpl 3 Complemento E C 0 - 1 1 - 60 
 
ER34 
 
56 xBairro 3 Bairro E C 1 - 1 1 - 60 
 
ER34 
 
57 cMun 3 Código do município (utilizar a tabela do 
IBGE), informar 9999999 para operações com 
o exterior. 
E N 1 - 1 7 
 
ER2 
 
58 xMun 3 Nome do município, informar EXTERIOR para 
operações com o exterior. 
E C 1 - 1 1 - 60 
 
ER34 
 
59 CEP 3 CEP E N 0 - 1 8 
 
ER40 Informar os zeros não significativos 
60 UF 3 Sigla da UF, informar EX para operações com 
o exterior. 
E C 1 - 1 2 D5 
  
61 cPais 3 Código do país E N 0 - 1 1 - 4 
 
ER33 Utilizar a tabela do BACEN 
62 xPais 3 Nome do país E C 0 - 1 1 - 60 
 
ER34 
 
63 fone 3 Telefone E N 0 - 1 7 - 12 
 
ER43 
 
64 email 3 Endereço de E-mail E C 0 - 1 1 - 60 
 
ER54 
 
65 agencia 1 Identificação da agência/preposto/terceiro 
que comercializou o BPe 
G 
 
0 - 1 
    
66 xNome 2 Razão social ou Nome da Agência E C 1 - 1 2 - 60 
 
ER34 
 
67 CNPJ 2 Número do CNPJ E C 1 - 1 2 
 
ER8 Em caso de empresa não estabelecida no Brasil, será 
informado o CNPJ com zeros. 
Informar os zeros não significativos. 
68 enderAgencia 2 Endereço da agência G 
 
1 - 1 
    
69 xLgr 3 Logradouro E C 1 - 1 1 - 255 
 
ER34 
 
70 nro 3 Número E C 1 - 1 1 - 60 
 
ER34 
 
71 xCpl 3 Complemento E C 0 - 1 1 - 60 
 
ER34 
 
72 xBairro 3 Bairro E C 1 - 1 1 - 60 
 
ER34 
 
73 cMun 3 Código do município (utilizar a tabela do 
IBGE), informar 9999999 para operações com 
o exterior. 
E N 1 - 1 7 
 
ER2 
 
74 xMun 3 Nome do município, informar EXTERIOR para 
operações com o exterior. 
E C 1 - 1 1 - 60 
 
ER34 
 
75 CEP 3 CEP E N 0 - 1 8 
 
ER40 Informar os zeros não significativos 
76 UF 3 Sigla da UF, informar EX para operações com 
o exterior. 
E C 1 - 1 2 D5 
  
77 cPais 3 Código do país E N 0 - 1 1 - 4 
 
ER33 Utilizar a tabela do BACEN 
78 xPais 3 Nome do país E C 0 - 1 1 - 60 
 
ER34

## Página 71

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 71  / 80  
 
79 fone 3 Telefone E N 0 - 1 7 - 12 
 
ER43 
 
80 email 3 Endereço de E-mail E C 0 - 1 1 - 60 
 
ER54 
 
81 infBPeSub 1 Informações dos BPe de Substituição para 
remarcação e/ou transferência 
G 
 
0 - 1 
    
82 chBPe 2 Chave do Bilhete de Passagem Substituído E C 1 - 1 44 
 
ER3 Informar os zeros não significativos. 
83 tpSub 2 Tipo de Substituição E N 1 - 1 1 D32 
 
1 - Remarcação 
2 - Transferência 
3 - Transferência e Remarcação 
4 – Erro de Tarifa 
5 – Erro de Tributação 
6 – Decisão judicial 
7 – Erro Cadastral 
9 - Outros  
84 infPassagem 1 Informações do detalhamento da Passagem  G 
 
1 - 1 
    
85 dhEmb 2 Data e hora de embarque E D 1 - 1 21 
 
ER1 Formato AAAA-MM-DDTHH:MM:DD TZD 
86 dhValidade 2 Data e hora de validade do bilhete E D 1 - 1 21 
 
ER1 Formato AAAA-MM-DDTHH:MM:DD TZD 
87 infPassageiro 2 Informações do passageiro G 
 
0 - 1 
    
88 xNome 3 Nome do Passageiro E C 1 - 1 2 - 60 
 
ER34 
 
89 CPF 3 Número do CPF E N 0 - 1 11 
 
ER9 Informar os zeros não significativos. 
90 tpDoc 3 Tipo do Documento de identificação E N 1 - 1 1 D19 
 
1-RG 
2-Título de Eleitor 
3-Passaporte 
4-CNH 
5-Outros 
91 nDoc 3 Número do Documento do passageiro E C 1 - 1 2 - 20 
 
ER34 
 
92 xDoc 3 Descrição do tipo de documento "outros" E C 0 - 1 2 - 100 
 
ER34 
 
93 dNasc 3 Data de Nascimento E D 0 - 1 10 
 
ER35 Formato AAAA-MM-DD 
94 fone 3 Telefone E N 0 - 1 7 - 12 
 
ER43 
 
95 email 3 Endereço de E-mail E C 0 - 1 1 - 60 
 
ER54 
 
96 infViagem 1 Grupo de informações da viagem do BPe G 
 
1 - n 
    
97 nroVoo 2 Código voo viagem E C 1 - 1 1 - 20 
   
97 a SiglaCiaOperVoo 2 Sigla IATA da Companhia que opera o voo E C 1 - 1 1 - 3 
 
ER4 
 
98 tpViagem 2 Tipo de Viagem E N 1 - 1 2 D11 
 
Informa o código do tipo da viagem 
00- Regular Doméstico; 
01- Regular Internacional; 
02- Não Regular Doméstico; e 
03- Não Regular Internacional.

## Página 72

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 72  / 80  
 
99 cAeroOrig 2 Código IATA do Aeroporto de origem E C 1 - 1 3-4 
 
ER34 
 
100 cAeroDest 2 Código IATA do Aeroporto de destino E C 1 - 1 3-4 
 
ER34 
 
101 tpServ 2 Tipo de Serviço E N 1 - 1 2 D12 
 
Informar o código do tipo de serviço (12 - Comercial, 13 - 
Executivo) 
102 tpAcomodacao 2 Tipo de Acomodação E N 1 - 1 1 D13 
 
Informar o código do tipo de acomodação (6-Comum, 7-
Conforto) 
103 tpTrecho 2 Tipo de trecho da viagem E N 1 - 1 1 D10 
 
Informar do tipo de trecho (1-Normal, 2-Trecho Inicial, 3-
Conexão) 
104 dhViagem 2 Data e hora de referência para a viagem E D 1 - 1 21 
 
ER1 Formato AAAA-MM-DDTHH:MM:DD TZD 
105 dhConexao 2 Data e hora da conexão 
Informar se tpTrecho = 3 
E D 0 - 1 21 
 
ER1 Formato AAAA-MM-DDTHH:MM:DD TZD 
106 infValorBPe 1 Informações dos valores do Bilhete de 
Passagem 
G 
 
1 - 1 
    
107 vBP 2 Valor do Bilhete de Passagem E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
Pode conter zeros quando o BPe for de complemento de 
ICMS 
108 vDesconto 2 Valor do desconto concedido ao comprador E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
Indicar o valor total concedido em função dos benefícios 
concedidos ou política de desconto da empresa 
Informar 0.00 em caso de passagem comercializada sem 
nenhum desconto 
109 vPgto 2 Valor pago pelo BPe (vBP - vDesconto) E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
110 vTroco 2 Valor do troco E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
111 tpDesconto 2 Tipo de desconto/benefício para o BPe E N 0 - 1 2 D14 
 
03 - Crianças 
09 - Profissional da Empresa (empregados ou tripulantes da 
cia aérea) 
10 - Programas de fidelidade (Milhagem); 
11 - Acordos Corporativos 
12- Acordos com Grupos de Passageiros; 
13 - Acompanhante passageiro PNE 
99 - Outros 
112 xDesconto 2 Descrição do tipo de desconto/benefício 
concedido 
E C 0 - 1 2 - 100 
 
ER34 
 
113 cDesconto 2 Código do desconto quando informado com 
tipo 99 - Outros 
E C 0 - 1 2 - 20 
 
ER34 
 
114 Comp 2 Componentes do Valor do Bilhete G 
 
1 - n

## Página 73

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 73  / 80  
 
115 tpComp 3 Tipo do Componente E N 1 - 1 2 D15 
 
01 - TARIFA; 
03 - TAXA EMBARQUE; 
06 - BAGAGEM 
07 - RESERVA DE ASSENTOS 
08 - TRANSPORTE DE ANIMAIS 
99 - OUTROS 
116 vComp 3 Valor do componente E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
117 imp 1 Informações relativas aos Impostos G 
 
1 - 1 
    
118 IBSCBS 2 Grupo de informações do IBS e CBS E C 1 - 1 
    
120 CST 3 Código Situação Tributária do IBS/CBS E N 1 - 1 
  
ER54 Utilizar tabela CST do IBS/CBS 
121 cClassTrib 3 Código de Classificação Tributária do IBS e 
CBS 
E N 1 - 1 
  
ER55 Utilizar tabela cClassTrib 
121 a indDoacao 3 Informar quando doação E N 0 - 1    Informar em caso de doação 
122 gIBSCBS 3 
 
G 
 
0 - 1 
    
123 vBC 4 Valor do BC E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
# --- x --- 4 Sequência XML - - 1 - 1 
    
125 gIBSUF 4 Grupo de informações do IBS na UF GS 
 
1 - 1 
    
126 pIBSUF 5 Alíquota do IBS de competência das UF E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
127 gDif 5 Grupo de campos do Diferimento G 
 
0 - 1 
    
128 pDif 6 Percentual do diferimento E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
129 vDif 7 Valor do diferimento E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
130 gDevTrib 5 Grupo de Informações da devolução de 
tributos 
G 
 
0 - 1 
    
131 vDevTrib 6 Valor do tributo devolvido. No fornecimento 
de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas 
no regulamento 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
132 gRed 5 Grupo de campos da redução de alíquota G 
 
0 - 1 
    
133 pRedAliq 6 Percentual de redução de alíquota do 
cClassTrib 
E N 1 - 1 3, 2 
3, 4  
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
134 pAliqEfet 6 Alíquota Efetiva que será aplicada a Base de 
Cálculo 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a4 casas decimais. 
135 vIBSUF 5 Valor do IBS de competência das UF E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
136 gIBSMun 4 Grupo de Informações do IBS no Município GS 
 
1 - 1

## Página 74

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 74  / 80  
 
137 pIBSMun 5 Alíquota do IBS Municipal E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
138 gDif 5 Grupo de campos do Diferimento G 
 
0 - 1 
    
139 pDif 6 Percentual do diferimento E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
140 vDif 6 Valor do diferimento E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
141 gDevTrib 5 Grupo de Informações da devolução de 
tributos 
G 
 
0 - 1 
    
142 vDevTrib 6 Valor do tributo devolvido. No fornecimento 
de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas 
no regulamento 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
143 gRed 5 Grupo de campos da redução de alíquota G 
 
0 - 1 
    
144 pRedAliq 6 Percentual de redução de alíquota do 
cClassTrib 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
145 pAliqEfet 5 Alíquota Efetiva que será aplicada a Base de 
Cálculo 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
146 vIBSMun 5 Valor do IBS Municipal E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
147 vIBS 4 Valor do IBS (soma de vIBSUF e vIBSMun) ES N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
148 gCBS 4 Grupo de Tributação da CBS G 
 
1 - 1 
    
149 pCBS 5 Alíquota da CBS E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
150 gDif 5 Grupo de campos do Diferimento G 
 
0 - 1 
    
151 pDif 6 Percentual do diferimento E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
152 vDif 6 Valor do diferimento E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
153 gDevTrib 5 Grupo de Informações da devolução de 
tributos 
G 
 
0 - 1 
    
154 vDevTrib 6 Valor do tributo devolvido. No fornecimento 
de energia elétrica, água, esgoto e 
gás natural e em outras hipóteses definidas 
no regulamento 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
155 gRed 5 Grupo de campos da redução de alíquota G 
 
0 - 1 
    
156 pRedAliq 6 Percentual de redução de alíquota do 
cClassTrib 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
157 pAliqEfet 6 Alíquota Efetiva que será aplicada a Base de 
Cálculo 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais.

## Página 75

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 75  / 80  
 
158 vCBS 5 Valor da CBS E C 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
159 gTribRegular 4 Grupo de informações da Tributação Regular. 
Informar como seria a tributação caso não 
cumprida a condição resolutória/suspensiva. 
Exemplo 1: Art. 442, §4. Operações com ZFM 
e ALC. Exemplo 2: Operações com suspensão 
do tributo. 
G 
 
0 - 1 
    
160 CSTReg 5 Código da Situação Tributária do IBS e CBS E N 1 - 1 
  
ER54 Informar qual seria o CST caso não cumprida a condição 
resolutória/suspensiva 
161 cClassTribReg 5 Informar qual seria o cClassTrib caso não 
cumprida a condição resolutória/suspensiva 
E N 1 - 1 
  
ER55 
 
175 pAliqEfetRegIBSUF 5 Alíquota do IBS da UF E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
Informar como seria a Alíquota caso não cumprida a 
condição resolutória/suspensiva 
163 vTribRegIBSUF 5 Valor do IBS da UF E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
Informar como seria o valor do Tributo caso não cumprida a 
condição resolutória/suspensiva 
164 pAliqEfetRegIBSMun 5 Alíquota do IBS do Município E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
Informar como seria a Alíquota caso não cumprida a 
condição resolutória/suspensiva 
165 vTribRegIBSMun 5 Valor do IBS do Município E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
Informar como seria o valor do Tributo caso não cumprida a 
condição resolutória/suspensiva 
166 pAliqEfetRegCBS 5 Alíquota da CBS E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
Informar como seria a Alíquota caso não cumprida a 
condição resolutória/suspensiva 
167 vTribRegCBS 5 Valor da CBS E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
Informar como seria o valor do Tributo caso não cumprida a 
condição resolutória/suspensiva 
178 gTribCompraGov 4 Grupo de informações da composição do 
valor do IBS e da CBS em compras 
governamentais 
G 
 
0 - 1 
    
179 pAliqIBSUF 5 
 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
180 vTribIBSUF 5 Valor que seria devido a UF, sem aplicação 
do Art. 473. da LC 214/2025 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais.

## Página 76

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 76  / 80  
 
181 pAliqIBSMun 5 
 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
182 vTribIBSMun 5 Valor que seria devido ao município, sem 
aplicação do Art. 473. da LC 214/2025 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
183 pAliqCBS 5 
 
E N 1 - 1 3, 2 
3, 4 
 
ER16 5 posições, sendo 3 inteiras e 2 a 4 casas decimais. 
184 vTribCBS 5 Valor que seria devido a CBS, sem aplicação 
do Art. 473. da LC 214/2025 
E N 1 - 1 13. 2 
 
ER36 15 posições, sendo 13 inteiras e 2 casas decimais. 
184 a gEstornoCred 3 Grupo de informações do estorno de crédito  G  0 - 1    Informado conforme indicador no cClassTrib  
184 b vIBSEstCred 4 Valor do IBS a ser estornado E N 1 – 1 13,2  ER36  
184 c vCBSEstCred 4 Valor da CBS a ser estornada E N 1 – 1 13,2  ER36  
185 vINSSRet 2 Valor retido de contribuição previdenciária 
(informar apenas no múltiplo) 
E N 0 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
186 vTotTrib 2 Valor Total dos Tributos E N 0 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
187 infAdFisco 2 Informações adicionais de interesse do Fisco  E C 0 - 1 1 - 2000 
 
ER34 Norma referenciada, informações complementares etc. 
188 vTotDFe 2 Valor total do documento fiscal 
(vBP + total do IBS + total da CBS)  
E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
189 infBPeVinculado 1 Informações do Serviço Vinculado a BPe 
múltiplo 
CG 
 
1 - 1 
    
190 chBPeMultiplo 2 Chave de acesso do BPe Múltiplo E C 1 - 1 44 
 
ER3 
 
191 pag 1 Dados de Pagamento. G 
 
1 - 10 
    
192 tPag 2 Forma de Pagamento:01-Dinheiro;02-
Cheque;03-Cartão de Crédito;04-Cartão de 
Débito;05-Vale Transportel;06 - PIX; 99 - 
Outros 
E N 1 - 1 2 D16 
  
193 xPag 2 Descrição da forma de pagamento 99 - 
Outros 
E C 0 - 1 2 - 100 
 
ER34 
 
194 nDocPag 2 Número do documento ou carteira 
apresentada nas formas de pagamento 
diferentes de 03 e 04 
E C 0 - 1 2 - 20 
 
ER34 
 
195 vPag 2 Valor do Pagamento E N 1 - 1 13, 2 
 
ER26 15 posições, sendo 13 inteiras e 2 casas decimais. 
196 card 2 Grupo de Cartões G 
 
0 - 1 
    
197 tpIntegra 3 Tipo de Integração para pagamento E N 1 - 1 1 D7 
 
Tipo de Integração do processo de pagamento com o 
sistema de automação da empresa: 
1=Pagamento integrado com o sistema de automação da 
empresa (Ex.: equipamento TEF, Comércio Eletrônico, POS

## Página 77

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 77  / 80  
 
Integrado) 
2= Pagamento não integrado com o sistema de automação 
da empresa (Ex.: equipamento POS Simples) 
198 CNPJ 3 CNPJ da credenciadora de cartão de 
crédito/débito 
E C 0 - 1 2 
 
ER7 
 
199 tBand 3 Bandeira da operadora de cartão de 
crédito/débito 
E N 0 - 1 2 D16 
 
01–Visa; 02–Mastercard; 03–American Express; 04–
Sorocred; 05 - Elo; 06 - Diners; 99–Outros 
200 xBand 3 Descrição do operador de cartão para 99 - 
Outros 
E C 0 - 1 2 - 100 
 
ER34 
 
201 cAut 3 Número de autorização da operação cartão 
de crédito/débito 
E C 0 - 1 1 - 20 
 
ER34 
 
202 nsuTrans 3 Número sequencial único da transação E C 0 - 1 1 - 20 
 
ER34 
 
203 nsuHost 3 Número sequencial único do Host E C 0 - 1 1 - 20 
 
ER34 
 
204 nParcelas 3 Número de parcelas E N 0 - 1 1 - 3 
 
ER44 
 
205 infAdCard 3 Informações adicionais operacionais para 
integração do cartão de crédito 
E C 0 - 1 1 - 2000 
 
ER34 Norma referenciada, informações complementares etc. 
206 autXML 1 Autorizados para download do XML do DFe G 
 
0 - 10 
   
Informar CNPJ ou CPF. Preencher os zeros não 
significativos. 
207 CNPJ 2 CNPJ do autorizado CE C 1 - 1 2 
 
ER7 Informar zeros não significativos 
208 CPF 2 CPF do autorizado CE N 1 - 1 11 
 
ER9 Informar zeros não significativos 
209 infAdic 1 Informações Adicionais G 
 
0 - 1 
    
210 infAdFisco 2 Informações adicionais de interesse do Fisco  E C 0 - 1 1 - 2000 
 
ER34 Norma referenciada, informações complementares, etc 
211 infCpl 2 Informações complementares de interesse 
do Contribuinte 
E C 0 - 1 1 - 5000 
 
ER34 
 
212 infRespTec 1 Informações do Responsável Técnico pela 
emissão do DFe 
G 
 
0 - 1 
    
213 CNPJ 2 CNPJ da pessoa jurídica responsável técnica 
pelo sistema utilizado na emissão do 
documento fiscal eletrônico 
E C 1 - 1 2 
 
ER7 Informar o CNPJ da pessoa jurídica desenvolvedora do 
sistema utilizado na emissão do documento fiscal eletrônico.  
214 xContato 2 Nome da pessoa a ser contatada E C 1 - 1 2 - 60 
 
ER34 Informar o nome da pessoa a ser contatada na empresa 
desenvolvedora do sistema utilizado na emissão do 
documento fiscal eletrônico. No caso de pessoa física, 
informar o respectivo nome. 
215 email 2 Email da pessoa jurídica a ser contatada E C 1 - 1 1 - 60 
 
ER54 
 
216 fone 2 Telefone da pessoa jurídica a ser contatada E N 1 - 1 7 - 12 
 
ER43 Preencher com o Código DDD + número do telefone. 
# --- x --- 0 Sequência XML - - 0 - 1 
   
As tags idCRT e hashCRT são filhas desta sequência opcional, 
se informada uma das tags a outra deverá ser informada

## Página 78

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 78  / 80  
 
217 idCSRT 2 Identificador do código de segurança do 
responsável técnico 
ES C 1 - 1 3 
 
ER44 Identificador do CSRT utilizado para geração do hash 
218 hashCSRT 2 Hash do token do código de segurança do 
responsável técnico 
ES C 1 - 1 20 
  
O hashCSRT é o resultado das funções SHA-1 e base64 do 
token CSRT fornecido pelo fisco + chave de acesso do DFe. 
(Implementação em futura NT) 
 
 
Observação: 28 caracteres são representados no schema 
como 20 bytes do tipo base64Binary 
219 infBPeSupl 0 Informações suplementares do BPe G 
 
1 - 1 
    
220 qrCodBPe 1 Texto com o QR-Code impresso no DABPE E C 1 - 1 50 - 1000 
 
ER46 
 
221 
 
0 ds:Signature E C 1 - 1 
    
 
 
 
 
 
 
Expressões Regulares 
ER1 (((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-
(29|30)))))T(20|21|22|23|[0 -1] \d):[0 -5] \d:[0 -5] \d([ \-,\+](0[0 -9]|10|11):00|([ \+](12):00))  
ER2  [0 -9]{7}  
ER3  [0 -9]{6}[A -Z0 -9]{12}[0 -9]{26}  
ER4  [0 -9]{36}  
ER5  [0 -9]{15}  
ER6  [0 -9]{3,4}  
ER7  [A -Z0 -9]{12}[0 -9]{2}  
ER8  [0 -9]{0}|[A -Z0 -9]{12}[0 -9]{2}  
ER9  [0 -9]{11}  
ER10  [0 -9]{3,11}  
ER11  0|0 \.[0 -9]{2}|[1 -9]{1}[0 -9]{0,2}( \.[0 -9]{2})?  
ER12  0|0 \.[ 0-9]{2}|[1 -9]{1}[0 -9]{0,2}( \.[0 -9]{3})?  
ER13  0\.[0 -9]{1}[1 -9]{1}|0 \.[1 -9]{1}[0 -9]{1}|[1 -9]{1}[0 -9]{0,2}( \.[0 -9]{2})?  
ER14  [0 -9]{1,3}( \.[0 -9]{2,3})?  
ER15  0|0 \.[0 -9]{3}|[1 -9]{1}[0 -9]{0,7}( \.[0 -9]{3})?  
ER16  0\.[1 -9]{1}[0 -9]{2}|0 \.[0 -9]{2}[1 -9]{1}|0 \.[ 0-9]{1}[1 -9]{1}[0 -9]{1}|[1 -9]{1}[0 -9]{0,7}( \.[0 -9]{3})?  
ER17  0|0 \.[0 -9]{4}|[1 -9]{1}[0 -9]{0,7}( \.[0 -9]{4})?  
ER18  0\.[1 -9]{1}[0 -9]{3}|0 \.[0 -9]{3}[1 -9]{1}|0 \.[0 -9]{2}[1 -9]{1}[0 -9]{1}|0 \.[0 -9]{1}[1 -9]{1}[0 -9]{2}|[1 -9]{1}[0 -9]{0,7}( \.[0 -9]{4})?

## Página 79

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 79  / 80  
 
ER19 0\.[1-9]{1}[0-9]{5}|0\.[0-9]{1}[1-9]{1}[0-9]{4}|0\.[0-9]{2}[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}[0-9]{2}|0\.[0-9]{4}[1-9]{1}[0-9]{1}|0\.[0-9]{5}[1-9]{1}|[1-9]{1}[0-
9]{0,8}( \.[0 -9]{6})?  
ER20  0|0 \.[0 -9]{4}|[1 -9]{1}[0 -9]{0,10}( \.[0 -9]{4})?  
ER21  0\.[1 -9]{1}[ 0-9]{3}|0 \.[0 -9]{3}[1 -9]{1}|0 \.[0 -9]{2}[1 -9]{1}[0 -9]{1}|0 \.[0 -9]{1}[1 -9]{1}[0 -9]{2}|[1 -9]{1}[0 -9]{0,10}( \.[0 -9]{4})?  
ER22  0|0 \.[0 -9]{3}|[1 -9]{1}[0 -9]{0,11}( \.[0 -9]{3})?  
ER23  0\.[1 -9]{1}[0 -9]{2}|0 \.[0 -9]{2}[1 -9]{1}|0 \.[0 -9]{1}[1 -9]{1}[0 -9]{1}|[1 -9]{1}[0 -9]{0,11}( \.[0 -9]{3})?  
ER24  0|0 \.[0 -9]{4}|[1 -9]{1}[0 -9]{0,11}( \.[0 -9]{4})?  
ER25  0\.[1 -9]{1}[0 -9]{3}|0 \.[0 -9]{3}[1 -9]{1}|0 \.[0 -9]{2}[1 -9]{1}[0 -9]{1}|0 \.[0 -9]{1}[1 -9]{1}[0 -9]{2}|[1 -9]{1}[0 -9]{0,11}( \.[0 -9]{4})?  
ER26  0|0 \.[0 -9]{2}|[1 -9]{1}[0 -9]{0, 12}( \.[0 -9]{2})?  
ER27  0\.[0 -9]{1}[1 -9]{1}|0 \.[1 -9]{1}[0 -9]{1}|[1 -9]{1}[0 -9]{0,12}( \.[0 -9]{2})?  
ER28  [0 -9]{0,14}|ISENTO|PR[0 -9]{4,8}  
ER29  [0 -9]{2,14}  
ER30  [1 -9]{1}[0 -9]{0,8}  
ER31  0|[1 -9]{1}[0 -9]{0,2}  
ER32  [0 -9]{2}  
ER33  [0 -9]{1,4}  
ER34  [! -ÿ]{1}[ -ÿ]{0,}[! -ÿ]{1}|[! -ÿ]{1}  
ER35 ((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-
(29|30)))))  
ER36  [0 -9] \.[0 -9]{6}|[1 -8][0 -9] \.[0 -9]{6}|90 \.[0 -9]{6}| -[0 -9] \.[0 -9]{6}| -[1 -8][0 -9] \.[0 -9]{6}| -90 \.[0 -9]{6}  
ER37  [0 -9] \.[0 -9]{6}|[1 -9][0 -9] \.[0 -9]{6}|1[0 -7][0 -9] \.[0 -9]{6}|180 \.[0 -9]{6}| -[0 -9] \.[0 -9]{6}| -[1 -9][0 -9] \.[0 -9]{6}| -1[0 -7][0 -9] \.[0 -9]{6}| -180 \.[0 -9]{6}  
ER38  (([0 -9]|[1 -9][0 -9]|1[0 -9]{2}|2[0 -4][0 -9]|25[0 -5]) \.){3}([0 -9]|[1 -9][0 -9]|1[0 -9]{2}|2[0 -4][0 -9]|25[0 -5])  
ER39  [A -Z]{2,3}[0 -9]{4}|[A -Z]{3,4}[0 -9]{3}|[A -Z0 -9]{7}  
ER40  [0 -9]{8}  
ER41  [0 -9]{1}  
ER42  ([! -ÿ]{0}|[! -ÿ]{5,20})?  
ER43  [0 -9]{7,12}  
ER44  [0 -9]{3}  
ER45  BPe[0 -9]{44}  
ER46  ((HTTPS?|https?)://.* \?chBPe=[0 -9]{6}[A -Z0 -9]{12}[0 -9]{26}&amp;tpAmb=[1 -2](&amp;sign=[! -ÿ]{1}[ -ÿ]{0,}[! -ÿ]{1}|[! -ÿ]{1})?)  
ER47  [0 -9]{5}  
ER48  [1 -9]{1}[0 -9]{0,1}|[1 -8]{1}[0 -9]{2}|[9]{1}[0 -8]{1}[0 -9]{1}|[9]{1}[9]{1}[0]{1}  
ER49  [0 -9]{1,6}  
ER50  BPe[0 -9]{6}[A -Z0 -9]{12}[0 -9]{26}  
ER51  [0 -9]{1,15}  
ER52  1\.00  
ER53  (([0 -1][0 -9])|([2][0 -3])):([0 -5][0 -9]):([0 -5][0 -9])  
ER54  [^@]+@[^ \.]+ \..+

## Página 80

Projeto 
Bilhete de Passagem Eletrônico 
Nota Técnica 2025.002 v1.05 – Transporte Aéreo  
 
 
 
Página 80  / 80  
 
ER55  [123567][0 -9]([0 -9][1 -9]|[1 -9][0 -9])  
 
Domínio 
D1  11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53  
D2  11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53, 90, 91, 92, 93, 8 0, 81  
D3  11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53, 99  
D4  63  
D5  AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO, EX  
D6  AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO  
D7  1, 2  
D8  4 
D9  2 
D10  1, 2, 3  
D11  00, 01, 02, 03  
D12  12, 13  
D13  6, 7  
D14  03, 09, 10, 11, 12, 13, 99  
D15  01, 03, 06, 07, 08, 99  
D16  01, 02, 03, 04, 05, 06, 99  
D17  00, 01  
D18  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11  
D19  1, 2, 3, 4, 5  
D20  01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 99  
D21  01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 99  
D22  00  
D23  20  
D24  40, 41, 51  
D25  90  
D26  1 
D27  0, 3  
D28  0, 1, 2  
D29  1, 3, 4  
D30  1, 2, 0  
D31  1, 2, 3, 4, 5, 9  
D32  1, 2, 3, 4, 5, 6, 7, 9
