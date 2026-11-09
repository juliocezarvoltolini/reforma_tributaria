---
id: nfse-via-anexo-iv-leiautesrn-adn-snnfsevia-v1-00-05
titulo: Anexo IV - Leiautes RN ADN - versão 1.00.05
tipo: leiaute
versao: 1.00.05
data: '2026-10-13'
documento_fiscal: NFS-e Via
url: https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica/manuais-e-anexos/anexo-iv-leiautesrn_adn-snnfsevia_v1-00-05.xlsx
arquivo_original: fontes/acervo/nfse-via-anexo-iv-leiautesrn-adn-snnfsevia-v1-00-05.xlsx
sha256_original: ab37255cd235695e46007488d42c87290854d081a48ab5761828e471c816cb07
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
sha256_corpo: dd35b441f0efedc8880f56d1351dd5ffba44937c0d327b964c5c407beb7d2501
---

## Planilha: Leiaute_NFSeVia-ADN_NFSeVia

| # | CAMINHO NO XML | CAMPO | ELE | TIPO | OCOR. | TAM. | DESCRIÇÃO | OBSERVAÇÕES DE NEGÓCIO | - | - |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | - | NFS-e Via | Raiz | - | - | - | - | - |  |  |
| 2 | NFSeVia/ | versao | A | C | 1-1 | 1-4V2 | Versão do leiaute da NFS-e Via. | - |  |  |
| 3 | NFSeVia/ | infNFSeVia | G | - | 1-1 | - | Grupo de informações da NFS-e Via | - |  |  |
| 4 | NFSeVia/infNFSeVia/ | y | ID | C | 1-1 | 53 | Informar o identificador precedido do literal ‘ID’. A formação do identificador de 53 posições da NFS-e Via é: "VIA" + Cód.da localidade/trecho (7) + Amb.Ger. (1) + Inscrição Federal (14) + nNFS-e Via (13) + serie (3) + AnoMes Emis. da NFS-e Via (4) + Cód.Num. (7) + DV (1) Código numérico de 7 Posições numérico, possivelmente aleatório, gerado pelo emitente. |  |  |  |
| 5 | NFSeVia/infNFSeVia/ | tpAmb | E | N | 1-1 | 1 | Identificação do tipo de ambiente no Sistema Nacional NFS-e Via: 1 - Produção; 2 - Homologação; | - |  |  |
| 6 | NFSeVia/infNFSeVia/ | verAplic | E | C | 1-1 | 1-20 | Versão da aplicação que gerou a NFS-e Via | - |  |  |
| 8 | NFSeVia/infNFSeVia/ | cStat | E | N | 1-1 | 3 | Situações possíveis: 100 - NFS-e Via Gerada; 101 - NFS-e Via de Substituição Gerada; 102 - NFS-e Via de Decisão Judicial; | - |  |  |
| 9 | NFSeVia/infNFSeVia | dhEmi | E | D | 1-1 | 8 | Data e hora da emissão da NFS-e Via. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD | - |  |  |
| 10 | NFSeVia/infNFSeVia | dhCompet | E | D | 1-1 | 8 | Data e hora de competência da prestação do serviço: passagem veicular. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD | - |  |  |
| 11 | NFSeVia/infNFSeVia/ | subst | G | - | 0-1 | - | Grupo de informações relativas à NFS-e Via a ser substituída | - |  |  |
| 12 | NFSeVia/infNFSeVia/subst/ | chSubstda | E | C | 1-1 | 50 | Chave de Acesso da NFS-e Via a ser substituída. | - |  |  |
| 13 | NFSeVia/infNFSeVia/subst/ | cMotivo | E | N | 1-1 | 2 | Código de justificativa para substituição de NFS-e Via: 03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e Via; 04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e Via; 05 - Rejeição de NFS-e Via pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo; 06 - Alteração de parâmetros de cadastro do trecho da concessão; 07 - Erro na identificação do veículo; 99 - Outros; |  |  |  |
| 14 | NFSeVia/infNFSeVia/subst/ | xMotivo | E | C | 0-1 | 15-255 | Descrição do motivo da substituição da NFS-e Via quando o emitente deve descrever o motivo da substituição para outros motivos (cMotivo = 99). | - |  |  |
| 15 | NFSeVia/infNFSeVia | fornec | G | - | 1-1 | - | Grupo de informações relativas ao fornecedor(prestador) do serviço | - |  |  |
| 16 | NFSeVia/infNFSeVia/fornec/ | CNPJ | CE | C | 1-1 | 14 | Número da inscrição federal (CNPJ) do fornecedor(prestador) do serviço: concessionária |  |  |  |
| 17 | NFSeVia/infNFSeVia/fornec/ | xNome | E | C | 0-1 | 150 | Nome / Nome Empresarial do fornecedor. | - |  |  |
| 18 | NFSeVia/infNFSeVia/fornec/ | cMun | E | N | 1-1 | 7 | Código do município do endereço do fornecedor do serviço. (Tabela do IBGE) | - |  |  |
| 19 | NFSeVia/infNFSeVia/ | serv | G | G | 1-1 | - | Grupo de informações relativas ao serviço prestado. | - |  |  |
| 20 | NFSeVia/infNFSeVia/serv/ | cLocOper | E | N | 1-1 | 7 | Código da localidade da operação (prestação) do serviço. Obs: Para a exploração de via, o local da operação (prestação) é o trecho de concessão de exploração de via para a qual a NFS-e Via foi emitida. Também é o local de incidência. O local da operação, para o IBS e para a CBS, será o mesmo local de incidência para o ISSQN. |  |  |  |
| 21 | NFSeVia/infNFSeVia/serv/ | xLocOper | E | C | 1-1 | 150 | Descrição do código de 7 dígitos referente ao local da Operação(prestação) do serviço: nome dado ao trecho no cadastro pela concessionária. |  |  |  |
| 22 | NFSeVia/infNFSeVia/ | cPracaEmi | E | N | 1-1 | 7 | Código da Praça de Pedágio, gerado no portal da Concessionária no momento do cadastro do trecho, onde a NFS-e Via foi emitida. |  |  |  |
| 23 | NFSeVia/infNFSeVia/ | xPracaEmi | E | C | 1-1 | 150 | Nome da Praça de Pedágio onde a NFS-e Via foi emitida. |  |  |  |
| 24 | NFSeVia/infNFSeVia/ | kmPracaEmi | E | N | 1-1 | 7 | Quilômetro da via onde está localizada a praça de pedágio. |  |  |  |
| 25 | NFSeVia/infNFSeVia/ | cLocEmi | E | N | 1-1 | 7 | Código de 7 dígitos do município (IBGE) onde está localizada a praça de pedágio. | - |  |  |
| 26 | NFSeVia/infNFSeVia/ | xLocEmi | E | C | 1-1 | 150 | Descrição do código de 7 dígitos do município (IBGE) onde está localizada a praça de pedágio. | - |  |  |
| 27 | NFSeVia/infNFSeVia/ | nNFSeVia | E | N | 1-1 | 1-13 | Número sequencial, por praça e por equipamento, de pedágio, da NFS-eVIA gerado pelo emitente e tipo de emitente da NFS-eVIA. | - |  |  |
| 28 | NFSeVia/infNFSeVia/ | serie | E | C | 1-1 | 3 | Uma série para cada praça e/ou equipamento ou número da pista de cobrança. | - |  |  |
| 29 | NFSeVia/infNFSeVia/serv/ | cTribNac | E | N | 1-1 | 6 | Código de tributação nacional do ISSQN. Valor fixo [220101] |  |  |  |
| 30 | NFSeVia/infNFSeVia/serv/ | cNBS | E | N | 1-1 | 9 | Código NBS correspondente ao serviço prestado. Valor Fixo [106042100] |  |  |  |
| 31 | NFSeVia/infNFSeVia/serv/ | explVia | G | - | 1-1 | - | Grupo de informações relativas a atividades de Exploração de Rodovia | - |  |  |
| 32 | NFSeVia/infNFSeVia/serv/explVia/ | categVeic | E | N | 1-1 | 2 | Categorias de veículos para cobrança: 00 - Categoria de Veículos (tipo não informado na nota de origem); 01 - Automóvel, caminhonete e furgão - (2 eixos); 02 - Caminhão leve, ônibus, caminhão trator e furgão - (2 eixos); 03 - Automóvel e caminhonete com semireboque - (3 eixos); 04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus - (3 eixos); 05 - Automóvel e caminhonete com reboque - (4 eixos); 06 - Caminhão com reboque e caminhãotrator com semi-reboque - (4 eixos); 07 - Caminhão com reboque e caminhãotrator com semi-reboque - (5 eixos); 08 - Caminhão com reboque e caminhãotrator com semi-reboque - (6 eixos); 09 - Caminhão com reboque e caminhãotrator com semi-reboque - (7 eixos); 10 - Caminhão com reboque e caminhãotrator com semi-reboque - (8 eixos); 11 - Motocicletas, motonetas e bicicletas motorizadas; 12 - Veículo com gratuidade; 99 - Cobrança Especial. |  |  |  |
| 34 | NFSeVia/infNFSeVia/serv/explVia/ | sentido | E | C | 1-1 | 1-3 | Orientação de passagem do veículo: Ângulo em graus a partir do norte geográfico em sentido horário, número inteiro de 0 a 359, onde 0º seria o norte, 90º o leste, 180º o sul, 270º o oeste. Precisão mínima de 10. |  |  |  |
| 35 | NFSeVia/infNFSeVia/serv/explVia/ | placa | E | C | 1-1 | 1-10 | Placa do veículo até 10 caracteres. |  |  |  |
| 36 | NFSeVia/infNFSeVia/serv/explVia/ | codAcessoPed | E | C | 1-1 | 17 | Código de acesso gerado automaticamente pelo sistema emissor da concessionária. |  |  |  |
| 37 | NFSeVia/infNFSeVia/serv/explVia/ | modPassagem | E | C | 1-1 | 1 | Modalidade da Passagem: 1 - Fluxo Livre 2 - Manual 3 - Automático 4 - Semi-Automático 5 - Outros |  |  |  |
| 38 | NFSeVia/infNFSeVia/serv/explVia/ | codContrato | E | C | 1-1 | 4 | Código de contrato do cadastro da concessionária. |  |  |  |
| 39 | NFSeVia/infNFSeVia/serv/explVia/ | xInfComp | E | C | 0-1 | 2000 | Campo livre para preenchimento pelo contribuinte. |  |  |  |
| 40 | NFSeVia/infNFSeVia/ | valores | G | - | 1-1 | - | Grupo de informações relativas à valores do serviço prestado | - |  |  |
| 41 | NFSeVia/infNFSeVia/valores/ | vServ | E | N | 1-1 | 1-15V2 | Valor monetário do serviço (R$). | - |  |  |
| 42 | NFSeVia/infNFSeVia/valores/ | modPagamento | E | C | 1-1 | 1 | Modalidade de pagamento: 1. Débito 2. Crédito 3. Dinheiro 4. Eletrônico 5. Pagamento posterior 6. Sem cobrança |  |  |  |
| 43 | NFSeVia/infNFSeVia/valores/ | vDescCondIncond | G | - | 0-1 | - | Grupo de informações relativas aos descontos condicionados e incondicionados | - |  |  |
| 44 | NFSeVia/infNFSeVia/valores/vDescCondIncond/ | vDescIncond | E | N | 0-1 | 1-15V2 | Valor monetário do desconto incondicionado (R$). |  |  |  |
| 45 | NFSeVia/infNFSeVia/valores/vDescCondIncond/ | vDescCond | E | N | 0-1 | 1-15V2 | Valor monetário do desconto condicionado (R$). |  |  |  |
| 46 | NFSeVia/infNFSeVia/valores/ | trib | G | - | 1-1 | - | Grupo de informações relacionados aos tributos relacionados ao serviço prestado | - |  |  |
| 47 | NFSeVia/infNFSeVia/valores/trib/ | issqn | G | - | 1-1 | - | Grupo de valores para o ISSQN | - |  |  |
| 48 | NFSeVia/infNFSeVia/valores/trib/issqn/ | vBC | E | N | 1-1 | 1-15V2 | Valor da Base de Cálculo do ISSQN (R$) = Valor do Serviço - Desconto Incondicionado vBC = vServ - descIncond |  |  |  |
| 49 | NFSeVia/infNFSeVia/valores/trib/issqn/ | pAliq | E | N | 1-1 | 1V2 | Valor da alíquota efetiva (%) do serviço prestado resultante do cadastro do trecho pela concessionária. |  |  |  |
| 50 | NFSeVia/infNFSeVia/valores/trib/issqn/ | vISSQN | E | N | 1-1 | 1-15V2 | Valor do ISSQN (R$) = Valor da Base de Cálculo x Alíquota vISSQN = vBC x pAliq |  |  |  |
| 51 | NFSeVia/infNFSeVia/valores/trib/ | tribFed | G | - | 0-1 | - | Grupo de informações de outros tributos relacionados ao serviço prestado | - |  |  |
| 52 | NFSeVia/infNFSeVia/valores/trib/tribFed/ | piscofins | G | - | 0-1 | - | Grupo de informações dos tributos PIS/COFINS | - |  |  |
| 53 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | CST | E | N | 1-1 | 2 | "Código de Situação Tributária do PIS/COFINS (CST): 00 - Nenhum; 01 - Operação Tributável com Alíquota Básica; 02 - Operação Tributável com Alíquota Diferenciada; 03 - Operação Tributável com Alíquota por Unidade de Medida de Produto; 04 - Operação Tributável monofásica - Revenda a Alíquota Zero; 05 - Operação Tributável por Substituição Tributária; 06 - Operação Tributável a Alíquota Zero; 07 - Operação Tributável da Contribuição; 08 - Operação sem Incidência da Contribuição; 09 - Operação com Suspensão da Contribuição;" 49 - Operação sem cobrança; 98 - Anulação; | - |  |  |
| 54 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vBCPisCofins | E | N | 0-1 | 1-15V2 | Valor da Base de Cálculo do PIS/COFINS (R$). | - |  |  |
| 55 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | pAliqPis | E | N | 0-1 | 1-2V2 | Valor da Alíquota do PIS (%). | - |  |  |
| 56 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | pAliqCofins | E | N | 0-1 | 1-2V2 | Valor da Alíquota da COFINS (%). | - |  |  |
| 57 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vPis | E | N | 0-1 | 1-15V2 | Valor monetário do PIS (R$). | - |  |  |
| 58 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vCofins | E | N | 0-1 | 1-15V2 | Valor monetário do COFINS (R$). | - |  |  |
| 60 | NFSeVia/infNFSeVia/valores/trib/ | ibscbs | G | - | 0-1 | - | Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS | - |  |  |
| 62 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | CST | E | N | 1-1 | 3 | Tabela da Código de Situação Tributária do IBS. Valor Fixo [000] |  |  |  |
| 63 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | cClassTrib | E | N | 1-1 | 6 | Tabela de Código de classificação Tributária do IBS. Valor fixo [[000002] |  |  |  |
| 64 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | cindOp | E | C | 1-1 | 6 | Tabela de Classificação do indicador da operação (AnexoVII-IndOp_IBSCBS). Valor fixo [080101] |  |  |  |
| 65 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vBC | E | N | 1-1 | 1-15V2 | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto. vBC = vServ - descIncond – vISSQN – vPIS - vCOFINS (2026) ou vBC = vServ - descIncond – vISSQN (2027 até 2032) Utilizada a data de competência. |  |  |  |
| 66 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vLiq | E | N | 1-1 | 1-15V2 | Valor líquido (R$) = Valor do serviço - Desconto condicionado - Desconto incondicionado - Valores (ISSQN, PIS, COFINS)** VLiq = vServ – vDescIncond – vDescCond – (vISSQN + vPIS + vCOFINS)** |  |  |  |
| 67 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vTotNF | E | N | 1-1 | 1-15V2 | Valor Total da NF considerando os impostos por fora IBS e CBS. O IBS e a CBS são por fora, por isso seus valores devem ser adicionados ao valor total da NF. vTotNF = VLiq + vCBS + vIBSTot |  |  |  |
| 68 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | gIBS | G | - | 1-1 | - | Grupo de Informações relativas aos valores do IBS Estadual | - |  |  |
| 69 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | vIBSTot | E | N | 1-1 | 1-15V2 | Total Valor do IBS Total. vIBSTot = vIBSUF + vIBSMun |  |  |  |
| 70 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | uf | G | - | 1-1 | - | Grupo de Informações relativas aos valores do IBS Estadual | - |  |  |
| 71 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/ | pAliqEfetUF | E | N | 1-1 | 1-2V2 | Alíquota efetiva para IBS das UFs da localidade de incidência/operação cadastrada: trecho. |  |  |  |
| 72 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/ | vIBSUF | E | N | 1-1 | 1-15V2 | Total valor do IBS estadual. vIBSUF = vBC x pAliqEfetUF |  |  |  |
| 73 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | mun | G |  |  |  | Grupo de Informações relativas aos valores do IBS Municipal | - |  |  |
| 74 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/ | pAliqEfetMun | E | N | 1-1 | 1-2V2 | Alíquota efetiva para IBS dos Municípios da localidade de incidência/operação cadastrada: trecho. |  |  |  |
| 75 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/ | vIBSMun | E | N | 1-1 | 1-15V2 | Total valor do IBS municipal. vIBSMun = vBC x pAliqEfetMun |  |  |  |
| 76 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | gCBS | G | - | 1-1 | - | Grupo de Informações relativas aos valores da CBS | - |  |  |
| 77 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/ | pAliq | E | N | 1-1 | 1-2V2 | Alíquota da União cpara a CBS Cadastrada |  |  |  |
| 78 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/ | vCBS | E | N | 1-1 | 1-15V2 | Total valor da CBS da União. vCBS = vBC x pAliq |  |  |  |
| 79 | NFSeVia/ | Signature | G | - | 1-1 | - | Assinatura XML da NFS-e Via segundo o padrão XML digital signature | - |  |  |
|  |  | dhReg |  |  |  |  | Data/Hora da recepção da NFS-e Via. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD |  |  |  |
|  |  | nReg |  |  |  |  | "Número do Registro" da NFS-e Via |  |  |  |

## Planilha: RN_NFSeVia-ADN_NFSeVia

| # | CAMINHO NO XML | CAMPO | REGRAS DE NEGÓCIO | - | APLIC. | EFEITO | CÓD. ERRO | MSG. ERRO | NOTAS EXPLICATIVAS |
|---|---|---|---|---|---|---|---|---|---|
| 1 | - | NFS-e | - |  | - | - | - | - | - |
| 2 | NFSeVia/ | versao | - |  | - | - | - | - | - |
| 3 | NFSeVia/ | infNFSeVia | - |  | - | - | - | - | - |
| 4 | NFSeVia/infNFSeVia/ | id | O identificador da NFS-e Via é formado conforme a concatenação dos seguintes campos: "VIA" + Cód.da localidade/trecho (7) + Amb.Ger. (1) + Inscrição Federal (14) + nNFS-e Via (13) + serie (3) + AnoMes Emis. da NFS-e Via (4) + Cód.Num. (7) + DV (1) Código numérico de 7 Posições numérico, possivelmente aleatório, gerado pelo emitente. |  | Obrig. | Rej. | 1100 | Falha na composição da chave de acesso. | Aplicação da Regra de Módulo 11 para Cálculo do Dígito Verificador da NFS-e Via: Entrada: Chave alfanumérica com 49 caracteres (números e letras). Conversão de letras: Cada letra é convertida em número aplicando: valor = código ASCII da letra − 48 Pesos: Atribuem-se pesos de 2 a 9, repetindo-se ciclicamente, da direita para a esquerda. Cálculo: Multiplica-se cada valor pelo respectivo peso e soma-se o resultado. S = somatórido (valor×peso) Resto módulo 11: R = S mod 11 Dígito verificador (DV): se R=0 ou R=1 então o DV é igual a 0 Caso contrário DV = 11 - R Resultado: O dígito verificador é concatenado ao final da série original. |
|  |  |  | Chave a acesso da NFS-e Via enviada já existe no ADN |  | Obrig. | Rej. | 1117 | Chave de acesso duplicada: Código do Trecho de Concessão + Ambiente Gerador + Inscrição Federal + Número da NFS-e Via + Série | - |
|  |  |  | Quando o campo cStat for igual a 101, a chave de acesso da NFS-e Via informada deve ser igual a chave da NFS-e Via Substituta informada no Cancelamento por Substituição vinculado. |  | Obrig. | Rej. | 1142 | Chave de acesso da NFS-e Via Substituta informada no cancelamento por substituição é diferente da chave de acesso da NFS-e Via substituta vinculada. |  |
| 5 | NFSeVia/infNFSeVia/ | tpAmb | Tipo do ambiente informado difere do ambiente utilizado. |  | Obrig. | Rej. | 1133 | Ambiente inválido. |  |
| 6 | NFSeVia/infNFSeVia/ | verAplic | - |  | - | - | - | - | - |
| 7 | NFSeVia/infNFSeVia/ | tpTrans | - |  | - | - | - | - |  |
| 8 | NFSeVia/infNFSeVia/ | cStat | Se o campo for diferente de 101 - NFS-e Via de Substituição Gerada não é permitido que seja informadoo grupo de informações de substituição. |  | Obrig. | Rej. | 1147 | Dados de substituição informados na NFS-e Via. |  |
|  |  |  | Se o campo for igual a 101 - NFS-e Via de Substituição Gerada é obrigatório que seja informado grupo de informações de substituição. |  | Obrig. | Rej. | 1148 | Dados de substituição não informados na NFS-e Via de substituição. |  |
| 9 | NFSeVia/infNFSeVia | dhEmi | A data de emissão do documento deve ser maior ou igual a data da competência. |  | Obrig. | Rej. | 1105 | A data de emissão é menor que a data de competência. |  |
|  |  |  | A data de emissão do documento deve ser maior ou igual que a data de início de cobrança do trecho de sob concessão. |  | Obrig. | Rej. | 1103 | A data de emissão é menor que a data de inicio de concessão. |  |
|  |  |  | A data de emissão deve ser menor ou igual a data atual. |  | Obrig. | Rej. | 1132 | A data de emissão é futura. |  |
| 10 | NFSeVia/infNFSeVia | dCompet | A data de competência do documento deve ser maior ou igual que a data de início de cobrança do trecho de sob concessão. |  | Obrig. | Rej. | 1104 | A data de competência é menor que a data de inicio de cobrança. |  |
| 11 | NFSeVia/infNFSeVia/ | subst | - |  | - | - | - | - | - |
| 12 | NFSeVia/infNFSeVia/subst/ | chSubstda | A chave de acesso da NFS-e Substituída deve ser válida e ser formada pelo CNPJ e o Código do Trecho informados na NFS-e de Substituição. |  | Obrig. | Rej. | 1106 | Falha na composição da chave de acesso substituida. | - |
|  |  |  | O CNPJ da concessionária informado na chave de acesso da NFS-e Substituída deve possuir um CNPJ válido. |  | Obrig. | Rej. | 1107 | Dígito verificador do CNPJ da chave de acesso substituída inválido. |  |
|  |  |  | NFS-e Via de Substituição não pode ser recepcionada pelo Ambiente Nacional se referencia uma NFS-e inexistente. (Chave da NFS-e Via a ser substituída não encontrada). |  | Obrig. | Rej. | 1139 | Chave de acesso inexistente para substituição. |  |
|  |  |  | NFS-e Via de Substituição não pode ser recepcionada pelo Ambiente Nacional para NFS-e Via que possui Evento de Cancelamento (Chave da NFS-e a ser substituída possui evento de cancelamento). |  | Obrig. | Rej. | 1137 | Evento de cancelamento para substituição já existente para a chave de acesso. |  |
|  |  |  | A chave de acesso da nota substituída deve ser igual a chave de acesso informada no cancelamento por substituição (campo chNFSeVia) vinculado a essa NFS-e Via. |  | Obrig. | Rej. | 1170 | Chave de acesso informada no evento de cancelamento diferente da nota informada como substituída. |  |
|  |  |  | A NF-S e substituta deve ter as mesmas informações nos seguintes campos em relação a substituída. |  | Obrig. | Rej. | 1143 | Campo da nota substituta é diferente da nota original. Campo código (Série/Ambiente/Praça/Techo/CNPJ/Data de Competência/Codigo de Acesso ao Pedágio) da nota substituta é diferente da nota original |  |
| 13 | NFSeVia/infNFSeVia/subst/ | cMotivo | - |  | - | - | - | - | - |
| 14 | NFSeVia/infNFSeVia/subst/ | xMotivo | Quando o campo cMotivo for igual a 99 então o campo cMotivo passa a ser obrigatório. |  | Obrig. | Rej. | 1172 | Para o código de substituição 99 a descrição deve ser preenchida. | - |
| 15 | NFSeVia/infNFSeVia | fornec | - |  | - | - | - | - | - |
| 16 | NFSeVia/infNFSeVia/fornec/ | CNPJ | CNPJ informado deve ser uma CNPJ válido. |  | Obrig. | Rej. | 1108 | CNPJ do Fornecedor Inválido.. | - |
|  |  |  | O CNPJ deve estar cadastrado como um CNPJ de uma Concessinária no cadastro do portal Nacional da NFS-e. |  | Obrig. | Rej. | 1171 | O CNPJ informado não está cadastrado como um CNPJ de uma Concessionária no cadastro do portal Nacional da NFS-e. Enviar e-mail para concessionarias.nfs-evia@rfb.gov.br. | - |
| 17 | NFSeVia/infNFSeVia/fornec/ | xNome | - |  | - | - | - | - | - |
| 18 | NFSeVia/infNFSeVia/fornec/ | cMun | O Código do Município informado deve existir na Tabela de Códigos de Municípios do IBGE. |  | Obrig. | Rej. | 1110 | Municipio do fornecedor inválido. | - |
| 19 | NFSeVia/infNFSeVia/ | serv | - |  | - | - | - | - | - |
| 20 | NFSeVia/infNFSeVia/serv/ | cLocOper | O código do trecho sob concessão informado deve existir no cadastro da Concessionária. |  | Obrig. | Rej. | 1109 | Não encontrado trecho ativo para o CNPJ e código. | - |
|  |  |  | O código do trecho sob concessão informado deve ativo no cadastro da Concessionária. |  | Obrig. | Rej. | 1120 | Código de concessão {0} inativo na data de competência {1} | - |
|  |  |  | O código do trecho sob concessão deve estar associonado ao código do contrato informado. |  | Obrig. | Rej. | 1121 | Código do contrato {0} não encontrado na concessão {1} | - |
| 22 | NFSeVia/infNFSeVia/ | cPracaEmi | O código da praça que pertence ao trecho sob concessão informado deve existir no cadastro da Concessionária. |  | Obrig. | Rej. | 1161 | Código da praça não encontrado para o trecho informado. | - |
|  |  |  | O código da praça que pertence ao trecho sob concessão informado deve estar ativo no cadastro da Concessionária na data da competência da NFS-e Via. |  | Obrig. | Rej. | 1119 | Código da praça inativo na data de competência. | - |
| 24 | NFSeVia/infNFSeVia/ | kmPracaEmi | Quilômetro da via onde está localizada a praça de pedágio. |  | Obrig. | Rej. | 1164 | Quilometro informado não confere com o cadastro. | - |
| 25 | NFSeVia/infNFSeVia/ | cLocEmi | O código do município sob concessão informado deve existir e estar ativo no cadastro de trechos da Concessionária. |  | Obrig. | Rej. | 1134 | O código do município não corresponde à praça de pedágio. | - |
| 27 | NFSeVia/infNFSeVia/ | nNFSeVia | - |  | - | - | - | - | - |
| 28 | NFSeVia/infNFSeVia/ | serie | - |  | - | - | - | - | - |
| 29 | NFSeVia/infNFSeVia/serv/ | cTribNac | - |  | - | - | - | - | - |
| 30 | NFSeVia/infNFSeVia/serv/ | cNBS | - |  | - | - | - | - | - |
| 31 | NFSeVia/infNFSeVia/serv/ | explVia | - |  | - | - | - | - | - |
| 32 | NFSeVia/infNFSeVia/serv/explVia/ | categVeic | - |  | - | - | - | - | - |
| 34 | NFSeVia/infNFSeVia/serv/explVia/ | sentido | - |  | - | - | - | - | - |
| 35 | NFSeVia/infNFSeVia/serv/explVia/ | placa | - |  | - | - | - | - |  |
| 36 | NFSeVia/infNFSeVia/serv/explVia/ | codAcessoPed | - |  | - | - | - | - | - |
| 37 | NFSeVia/infNFSeVia/serv/explVia/ | modPassagem | - |  | - | - | - | - | - |
| 38 | NFSeVia/infNFSeVia/serv/explVia/ | codContrato | O código do Contrato informado deve existir no cadastro da Concessionária. |  | Obrig. | Rej. | 1111 | Não encontrado código válido para o código de contrato e CNPJ. | - |
|  |  |  | O código do Contrato informado deve estar ativo no cadastro da Concessionária. |  | Obrig. | Rej. | 1118 | Código do contrato inativo na data de competência. | - |
| 39 | NFSeVia/infNFSeVia/serv/explVia/ | xInfComp | - |  | - | - | - | - | - |
| 40 | NFSeVia/infNFSeVia/ | valores | - |  | - | - | - | - | - |
| 41 | NFSeVia/infNFSeVia/valores/ | vServ | O valor do serviço somente pode ser igual a zero se o campo categoria do veículo for igual a 12 - Veículo com Gratuidade. |  | Obrig. | Rej. | 1163 | Para veículos sem gratuidade não pode ser informado o valor R$0,00 no campo Valor do Serviço. | - |
| 42 | NFSeVia/infNFSeVia/valores/ | modPagamento | - |  | - | - | - | - |  |
| 43 | NFSeVia/infNFSeVia/valores/ | vDescCondIncond | - |  | - | - | - | - | - |
| 44 | NFSeVia/infNFSeVia/valores/vDescCondIncond/ | vDescIncond | - |  | - | - | - | - | - |
| 45 | NFSeVia/infNFSeVia/valores/vDescCondIncond/ | vDescCond | - |  | - | - | - | - | - |
| 46 | NFSeVia/infNFSeVia/valores/ | trib | - |  | - | - | - | - | - |
| 47 | NFSeVia/infNFSeVia/valores/trib/ | issqn | - |  | - | - | - | - | - |
| 48 | NFSeVia/infNFSeVia/valores/trib/issqn/ | vBC | O valor do campo vBC deve ser igual ao campo vServ subtraído o campo vdescIncond. |  | Obrig. | Rej. | 1122 | Valor base de cálculo inválido. | - |
| 49 | NFSeVia/infNFSeVia/valores/trib/issqn/ | pAliq | O valor da Alíquota efetiva do Trecho deve ser igual a Alíquota calculada no cadastro do trecho na data da competência do documento. |  | Obrig. | Rej. | 1116 | Aliquota informada inválida. | - |
| 50 | NFSeVia/infNFSeVia/valores/trib/issqn/ | vISSQN | O valor informado nesse campo vISSQN deve ser igual a multiplicação do campo vBC pelo campo pAliq. |  | Obrig. | Rej. | 1112 | Valor ISSQN inválido. | - |
| 51 | NFSeVia/infNFSeVia/valores/trib/ | tribFed | - |  | - | - | - | - | - |
| 52 | NFSeVia/infNFSeVia/valores/trib/tribFed/ | piscofins | - |  | - | - | - | - |  |
| 53 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | CST | - |  | - | - | - | - | - |
| 54 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vBCPisCofins | - |  | - | - | - | - | - |
| 55 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | pAliqPis | - |  | - | - | - | - | - |
| 56 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | pAliqCofins | - |  | - | - | - | - | - |
| 57 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vPis | - |  | - | - | - | - | - |
| 58 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | vCofins | - |  | - | - | - | - | - |
| 59 | NFSeVia/infNFSeVia/valores/trib/tribFed/piscofins/ | tpRetPisCofins | - |  | - | - | - | - | - |
| 60 | NFSeVia/infNFSeVia/valores/trib/ | ibscbs | - |  | - | - | - | - | - |
| 61 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | dest | - |  | - | - | - | - | - |
| 62 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | CST | - |  | - | - | - | - | - |
| 63 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | cClassTrib | - |  | - | - | - | - | - |
| 64 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | cindOp | - |  | - | - | - | - | - |
| 65 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vBC | O valor informado nesse campo vBC deve ser igual a vServ - descIncond – vISSQN – vPIS - vCOFINS até 31 de dezembro de 2026 ou O valor informado nesse campo vBC deve ser igual a vServ - descIncond – vISSQN de 01 de janeiro de 2027 até 31 de dezembro de 2032 Verificar pela data de competência desse documento. |  | Obrig. | Rej. | 1123 | Valor base de cálculo do IBS/CBS inválido. | - |
| 66 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vLiq | O valor informado nesse campo VLiq deve ser igual a vServ – vDescIncond – vDescCond – (vISSQN + vPIS + vCOFINS) |  | Obrig. | Rej. | 1125 | Valor líquido do IBS/CBS inválido. | - |
| 67 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | vTotNF | O valor informado nesse campo vTotNF deve ser igual a VLiq + vCBS + vIBSTot |  | Obrig. | Rej. | 1126 | Valor total da NFS-e Via inválido. | - |
| 68 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | gIBS | - |  | - | - | - | - | - |
| 69 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | vIBSTot | - |  | - | - | - | - | - |
| 70 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | uf | - |  | - | - | - | - | - |
| 71 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/ | pAliqEfetUF | - |  | - | - | - | - | - |
| 72 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/uf/ | vIBSUF | O valor informado nesse campo vIBSUF deve ser igual a vBC x pAliqEfetUF. |  | Obrig. | Rej. | 1128 | Valor do IBS/CBS UF inválido. | - |
| 73 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/ | mun | - |  | - | - | - | - | - |
| 74 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/ | pAliqEfetMun | - |  | - | - | - | - | - |
| 75 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gIBS/mun/ | vIBSMun | O valor informado nesse campo vIBSMun deve ser igual a vBC x pAliqEfetMun. |  | Obrig. | Rej. | 1129 | Valor do IBS/CBS Município inválido. | - |
| 76 | NFSeVia/infNFSeVia/valores/trib/ibscbs/ | gCBS | - |  | - | - | - | - | - |
| 77 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/ | pAliqEfetCBS | - |  | - | - | - | - | - |
| 78 | NFSeVia/infNFSeVia/valores/trib/ibscbs/gCBS/ | vCBS | O valor informado nesse campo vCBS deve ser igual a vBC x pAliq. |  | Obrig. | Rej. | 1130 | Valor do CBS inválido. | - |
| 79 | NFSeVia/ | Signature | A assinatura da NFS-e Via deve ser válida. |  | Obrig. | Rej. | 1114 | Assinatura do xml difere do calculado. | - |
|  |  |  | Certificado Digital da assintura inválido: - Validade do Certificado (data início e data fim); - Verifica a Cadeia de Certificação; - Certificado do Transmissor revogado; - LCR indisponível ou inválida. |  | Obrig. | Rej. | 1152 1154 1155 1156 | Certificado Digital da assinatura inválido. | - |
|  |  |  | Certificado Digital da assinatura fora do padrão estabelecido pelo Sistema Nacional NFS-e Via: - Versão diferente de 3; - Se informado, Basic Constraint deve ser true (não pode ser Certificado de AC); - KeyUsage não define 'Assinatura Digital' e 'Não Recusa'; - Falta a extensão de CNPJ (OtherName - OID=2.16.76.1.3.3) ou CPF (OtherName - OID=2.16.76.1.3.1); - Certificado Raiz difere da 'ICP-Brasil'. |  | Obrig. | Rej. | 1149 1150 1151 1153 | Certificado Digital fora do padrão estabelecido. | - |
|  |  |  | A assinatura deve ser feita com o certificado digital da Concessionária |  | Obrig. | Rej. | 1157 | Certificado utilizado na assinatura da NFS-e Via não autorizado. | - |
|  |  | dhReg | Prazo para aceitação de uma NFS-e Via - Comparar a Data da Recepção do documento de NFS-e Via com a Data de Emissão da NFS-e Via que está sendo enviada. |  | Obrig. | Rej. | 1165 | Prazo de recepção para a data de competência da NFS-e Via excedido. | - |

## Planilha: LEIAUTE_EVENTO_CANC_NFS-e_Via

| # | CAMINHO NO XML | CAMPO | ELE | TIPO | OCOR. | TAM. | DESCRIÇÃO | OBSERVAÇÕES DE NEGÓCIO |
|---|---|---|---|---|---|---|---|---|
| 1 |  | evento | Raiz | - | - | - | TAG raiz | - |
| 2 | evento/ | versao | A | C | 1-1 | 1-4V2 | Versão do leiaute do evento | - |
| 3 | evento/ | infEvento | G | - | 1-1 | - | c |  |
| 4 | evento/infEvento/ | id | ID | C | 1-1 | 62 | O identificador do evento é composto pela concatenação de campos que constam no leiaute. A formação deste identificador considera o literal "EVT" associado a outras 59 posições numéricas, conforme descrito abaixo: "EVT" + Chave de acesso da NFS-e Via (50) + Código do Evento (06) + Número sequencial do evento (nSeqEvento) (03) O código do evento corresponde ao valor informado na tag infEvento sem a primeira posição: Cancelamento de NFS-e Via - tag e101101 - código do evento 101101 Cancelamento de NFS-e Via por substituição - tag e105102 - código do evento 105102 | - |
| 5 | evento/infEvento/ | verAplic | E | C | 0-1 | 1-20 | Versão do aplicativo que gerou o evento. | - |
| 6 | evento/infEvento/ | nSeqEvento | E | N | 1-1 | 3 | Número sequencial do evento para o mesmo tipo de evento. Para os eventos que ocorrem somente uma vez, como é o caso do cancelamento, o nSeqEvento = 001. Para os eventos que possam existir mais de um evento do mesmo tipo o ambiente gerador deverá numerar de forma sequencial. |  |
| 7 | evento/infEvento/ | chNFSeVia | CE | N | 1-1 | 50 | Identificador da NFS-e a qual o evento será vinculada. | - |
| 8 | evento/infEvento/ | dhEvento | E | D | 1-1 | - | Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time, onde TZD pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, -02:00 e -03:00. Ex.: 2010-08-19T13:00:15-03:00. | - |
| 9 | evento/infEvento/ | tpAmb | E | N | 1-1 | 1 | Tipo de ambiente: 1 - Produção; 2 - Homologação; | - |
| 10 | evento/infEvento/ | e101101 | CG | - | 1-1 | - | Parte Específica do Registro de Evento Evento Cancelamento de NFS-e | - |
| 11 | evento/infEvento/e101101/ | xDesc | E | C | 1-1 | 5-60 | Descrição do evento: "Cancelamento de NFS-e" | - |
| 12 | evento/infEvento/e101101/ | cMotivo | E | N | 1-1 | 1 | Código de justificativa de cancelamento: 2 - Serviço não Prestado; | - |
| 13 | evento/infEvento/e101101/ | xMotivo | E | C | 1-1 | 15-255 | Descrição para explicitar o motivo indicado neste evento. | - |
| 14 | evento/infEvento/ | e105102 | CG | - | 1-1 | - | Parte Específica do Registro de Evento Cancelamento de NFS-e por Substituição | - |
| 15 | evento/infEvento/e105102/ | xDesc | E | C | 1-1 | 5-60 | Descrição do evento: "Cancelamento de NFS-e por Substituição" | - |
| 16 | evento/infEvento/e105102/ | cMotivo | E | N | 1-1 | 1 | Código de justificativa de cancelamento substituição: 1 - Erro na Emissão | - |
| 17 | evento/infEvento/e105102/ | xMotivo | E | C | 0-1 | 15-255 | Descrição para explicitar o motivo indicado neste evento. | - |
| 18 | evento/infEvento/e105102/ | chSubstituta | E | C | 1-1 | 50 | Chave de Acesso da NFS-e substituta. | - |
| 19 | evento/ | Signature | G | - | 1-1 | - | Assinatura do registro segundo o Padrão XML Digital Signature. | - |
|  |  | dhReg |  |  |  |  | Data/Hora da recepção do Evento de NFS-e Via. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD |  |
|  |  | nReg |  |  |  |  | "Número do Registro" do Evento da NFS-e Via |  |

## Planilha: RN_EVENTO_CANC_NFS-e_Via

| # | CAMINHO NO XML | CAMPO | REGRAS DE NEGÓCIO | - | APLIC. | EFEITO | CÓD. ERRO | MSG. ERRO | OBSERVAÇÕES DE NEGÓCIO | - | - | - | - | - | - | - | - | - |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | evento |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |
| 2 | evento/ | versao | Prazo de aceitação da versão do leiaute do evento ultrapassado. |  | Obrig. | Rej. | E----- | O prazo de aceitação da versão do leiaute da NFS-e expirou. | - |  |  |  |  |  |  |  |  |  |
| 3 | evento/ | infEvento |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |
| 4 | evento/infEvento/ | id | Campo identificador do Evento inválido. Identificador do evento difere da concatenação dos campos correspondentes existente no leiaute evento. |  | Obrig. | Rej. | 1138 | Falha na composição da chave de acesso. | - |  |  |  |  |  |  |  |  |  |
|  |  |  | O id do evento compartilhado já existe no ADN. |  | Obrig. | Rej. | 1136 | Evento de cancelamento já existente para a chave de acesso. | - |  |  |  |  |  |  |  |  |  |
| 5 | evento/infEvento/ | verAplic | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 6 | evento/infEvento/ | nSeqEvento | Para eventos de Cancelamento e Cancelamento por Substiituição o campo deve possuir o valor igual a 001 |  | Obrig. | Rej. | 1168 | O número sequencial para eventos de cancelamento (101101 e 105102) deve ser 001. | - |  |  |  |  |  |  |  |  |  |
| 7 | evento/infEvento/ | chNFSeVia | O registro de evento não pode ser validado pois a NFS-e Via indicada não existe no ADN NFS-e Via. |  | Obrig. | Rej. | 1135 | Chave de acesso inexistente. | - |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |
|  |  |  | Somente é permitido um único evento do tipo Cancelamento de NFS-e Via. |  | Obrig. | Rej. | 1136 | Evento de cancelamento já existente para a chave de acesso. | - |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | 1137 | Evento de cancelamento para substituição já existente para a chave de acesso. | - |  |  |  |  |  |  |  |  |  |
|  |  |  | A chave de acesso da NFS-e Via deve ser uma chave válida e o CNPJ que compõe a chave deve ser igual ao CNPJ da Concessionária que está enviando o evento. |  | Obrig. | Rej. | 1146 | CNPJ da concessionária no metadado é diferente do CNPJ da concessionária no documento vinculado. | - |  |  |  |  |  |  |  |  |  |
|  |  |  | Quando se tratar de evento de Cancelamento por substituição (105102), a chave de acesso informada deve ser igual ao campo chSubstda da NFS-e Via vinculado a esse evento. |  | Obrig. | Rej. | 1170 | Chave de acesso informada no evento de cancelamento diferente da nota informada como substituida. |  |  |  |  |  |  |  |  |  |  |
| 8 | evento/infEvento/ | dhEvento | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 9 | evento/infEvento/ | tpAmb | Tipo do ambiente informado difere do ambiente utilizado. |  | Obrig. | Rej. | 1133 | Ambiente inválido. | - |  |  |  |  |  |  |  |  |  |
| 10 | evento/infEvento/ | e101101 | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 11 | evento/infEvento/e101101/ | xDesc | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 12 | evento/infEvento/e101101/ | cMotivo | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 13 | evento/infEvento/e101101/ | xMotivo | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 14 | evento/infEvento/ | e105102 | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 15 | evento/infEvento/e105102/ | xDesc | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 16 | evento/infEvento/e105102/ | cMotivo | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 17 | evento/infEvento/e105102/ | xMotivo | - |  | - | - | - | - | - |  |  |  |  |  |  |  |  |  |
| 18 | evento/infEvento/e105102/ | chSubstituta | A chave de acesso da NFS-e Via Substituta informada no Cancelamento por Substituição deve ser igual a chave da NFS-e Via de substituição vinculada. |  | Obrig. | Rej. | 1142 | Chave de acesso da NFS-e Via Substituta informada no cancelamento por substituição é diferente da chave de acesso da NFS-e Via substituta vinculada. | - |  |  |  |  |  |  |  |  |  |
| 19 | evento/ | Signature | A assinatura do Evento deve ser válida. |  | Obrig. | Rej. | 1114 | Arquivo enviado com erro na assinatura. | - |  |  |  |  |  |  |  |  |  |
|  |  |  | Certificado Digital da assintura inválido: - Validade do Certificado (data início e data fim); - Verifica a Cadeia de Certificação; - Certificado do Transmissor revogado; - LCR indisponível ou inválida. |  | Obrig. | Rej. | 1152 1154 1155 1156 | Certificado Digital da assinatura inválido. |  |  |  |  |  |  |  |  |  |  |
|  |  |  | Certificado Digital da assinatura fora do padrão estabelecido pelo Sistema Nacional NFS-e Via: - Versão diferente de 3; - Se informado, Basic Constraint deve ser true (não pode ser Certificado de AC); - KeyUsage não define 'Assinatura Digital' e 'Não Recusa'; - Falta a extensão de CNPJ (OtherName - OID=2.16.76.1.3.3) ou CPF (OtherName - OID=2.16.76.1.3.1); - Certificado Raiz difere da 'ICP-Brasil'. |  | Obrig. | Rej. | 1149 1150 1151 1153 | Certificado Digital fora do padrão estabelecido. | - |  |  |  |  |  |  |  |  |  |
|  |  |  | A assinatura deve ser feita com o certificado digital da Concessionária Emissora do Evento. |  | Obrig. | Rej. | 1158 | Certificado utilizado na assinatura da Evento Via não autorizado. | - |  |  |  |  |  |  |  |  |  |
|  |  | dhReg | Prazo para aceitação de um cancelamento - Comparar a Data da Recepção do documento de Cancelamento com a Data de Competência da NFS-e Via que está sendo cancelada/cancelada por substituição. |  | Obrig. | Rej. | 1166 | Prazo de recepção do cancelamento para a data de competência da NFS-e Via excedido. | - |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Obrig. | Rej. | 1167 | Prazo de recepção de substituição para a data de competência da NFS-e Via excedido. | - |  |  |  |  |  |  |  |  |  |

## Planilha: LEIAUTE_EVENTO_MANIFE_NFS-e_Via

| # | CAMINHO NO XML | CAMPO | ELE | TIPO | OCOR. | TAM. | DESCRIÇÃO |
|---|---|---|---|---|---|---|---|
| 1 |  | evento | Raiz | - | - | - | TAG raiz |
| 2 | evento/ | versao | A | C | 1-1 | 1-4V2 | Versão do leiaute do evento |
| 3 | evento/ | infEvento | G | - | 1-1 | - | c |
| 4 | evento/infEvento/ | id | ID | C | 1-1 | 62 | O identificador do evento é composto pela concatenação de campos que constam no leiaute. A formação deste identificador considera o literal ""EVT"" associado a outras 59 posições numéricas, conforme descrito abaixo: ""EVT"" + Chave de acesso da NFS-e Via (50) + Código do Evento (06) + Número sequencial do evento (nSeqEvento) (03) O código do evento de Manifestaçao corresponde ao valor tag infEvento sem a primeira posição: Manifestação do Adquirente da NFS-e Via - Aceite - tag e203202 - código do evento 203202 Manifestação do Adquirente da NFS-e Via - Rejeição - tag e203204 - código do evento 203204 |
| 5 | evento/infEvento/ | verAplic | E | C | 0-1 | 1-20 | Versão do aplicativo que gerou o evento. |
| 6 | evento/infEvento/ | nSeqEvento | E | N | 1-1 | 3 | Número sequencial do evento para o mesmo tipo de evento. Para os eventos que possam existir mais de um evento do mesmo tipo o ambiente gerador deverá numerar de forma sequencial. |
| 7 | evento/infEvento/ | chNFSeVia | CE | N | 1-1 | 50 | Identificador da NFS-e a qual o evento será vinculada. |
| 8 | evento/infEvento/ | dhEvento | E | D | 1-1 | - | Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time, onde TZD pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, -02:00 e -03:00. Ex.: 2010-08-19T13:00:15-03:00. |
| 9 | evento/infEvento/ | tpAmb | E | N | 1-1 | 1 | Tipo de ambiente: 1 - Produção; 2 - Homologação; |
| 10 | evento/infEvento/ | e203202 | CG | - | 1-1 | - | Parte Específica do Registro de Evento de Manifestação de NFS-e Via - Com Aceite. |
| 11 | evento/infEvento/e203202/ | xDesc | E | C | 1-1 | 5-60 | Descrição do evento: "Manifestação de Informação do Adquirente da NFS-e Via - Com Aceite" |
| 12 | evento/infEvento/e203202/ | tpNi | E | N | 1-1 | 1 | Tipo de Identificação do Adquirente: 1 - CPF 2 - CNPJ |
|  | evento/infEvento/e203202/ | CNPJCPF | E | C | 1-1 | 11-14 | CNPJ ou CNPF do Adquirente da NFS-e Via. |
| 13 | evento/infEvento/e203202/ | xRazaoSocial | E | C | 1-1 | 02-60 | Nome ou Razão Social do Adquirente. |
| 14 | evento/infEvento/ | e203204 | CG | - | 1-1 | - | Parte Específica do Registro de Evento de Manifestação de NFS-e Via - Com Rejeição. |
| 15 | evento/infEvento/e203204/ | xDesc | E | C | 1-1 | 5-60 | Descrição do evento: "Manifestação de Informação do Adquirente da NFS-e Via - Com Rejeição" |
| 16 | evento/infEvento/e203204/ | tpNi | E | N | 1-1 | 1 | Tipo de Identificação do Adquirente: 1 - CPF 2 - CNPJ |
| 17 | evento/infEvento/e203204/ | CNPJCPF | E | C | 1-1 | 11-14 | CNPJ ou CNPF do Adquirente da NFS-e Via. |
| 18 | evento/infEvento/e203204/ | xRazaoSocial | E | C | 1-1 | 02-60 | Nome ou Razão Social do Adquirente. |
| 19 | evento/infEvento/e203204/ | cMotivo | E | N | 1-1 | 1 | Motivo da Rejeição da NFS-e Via: 1 - NFS-e Via em duplicidade; 2 - Não ocorrência da passagem do veículo; 3 – Data da passagem do veículo; 4 – Categoria do Veículo; 5 - Placa do veículo; 6 – Valor do serviço; 7 – Modo de Pagamento; 8 – Valor das deduções; 99 - Outros; |
| 20 | evento/infEvento/e203204/ | xMotivoRejeita | E | C | 0-1 | 15-55 | Descrição para explicar o Motivo da Rejeição da NFS-e Via pelo adquirente do Serviço de Exploração de via. |
| 21 | evento/ | Signature | G | - | 1-1 | - | Assinatura do registro segundo o Padrão XML Digital Signature. |
|  |  | dhReg |  |  |  |  | Data/Hora da recepção do Evento de NFS-e Via. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD |
|  |  | nReg |  |  |  |  | "Número do Registro" do Evento da NFS-e Via |

## Planilha: RN_EVENTO_MANIFEST_NFS-e_VIA

| # | CAMINHO NO XML | CAMPO | REGRAS DE NEGÓCIO | APLIC. | EFEITO | CÓD. ERRO | MSG. ERRO | OBSERVAÇÕES DE NEGÓCIO |
|---|---|---|---|---|---|---|---|---|
| 1 |  | evento | - | - | - | TAG raiz |  | - |
| 2 | evento/ | versao | Prazo de aceitação da versão do leiaute do evento ultrapassado. | Obrig. | Rej. | E----- | O prazo de aceitação da versão do leiaute da NFS-e expirou. | - |
| 3 | evento/ | infEvento | - | - | - | c |  |  |
| 4 | evento/infEvento/ | id | Campo identificador do Evento inválido. Identificador do evento difere da concatenação dos campos correspondentes existente no leiaute evento. | Obrig. | Rej. | 1138 | Falha na Composição da Chave de Acesso. |  |
|  |  |  | O id do evento compartilhado já existe no ADN. | Obrig. | Rej. | 1176 | Documento já manifestado para a chave de acesso |  |
| 5 | evento/infEvento/ | verAplic | - | - | - | - | - |  |
| 6 | evento/infEvento/ | nSeqEvento | Para eventos de Manifestação do Adquirente o campo deve possuir o valor igual a 001 | Obrig. | Rej. | 1191 | O número sequencial para eventos de manifestação (203202 e 203204) deve ser 001. |  |
| 7 | evento/infEvento/ | chNFSeVia | Somente é permitido um único evento de Manifestação do Adquirente de NFS-e Via de Aceitação. | Obrig. | Rej. | 1176 | Documento já manifestado com aceite para a chave de acesso {0} |  |
|  |  |  | Somente é permitido um único evento de Manifestação do Adquirente de NFS-e Via de Rejeição. | Obrig. | Rej. | 1183 | Documento já manifestado com rejeição para a chave de acesso {0} |  |
|  |  |  | O registro do Evento de Manifestação não pode ser validado pois a NFS-e Via indicada não existe no ADN NFS-e Via. | Obrig. | Rej. | 1177 | Chave de acesso {0} inexistente para manifestação |  |
|  |  |  | O registro do Evento de Manifestação não pode ser validado pois a NFS-e Via indicada possui Evento de Cancelamento. | Obrig. | Rej. | 1178 | Não é possível manifestar em documento cancelado para a chave de acesso {0} |  |
|  |  |  | O registro do Evento de Manifestação não pode ser validado pois a NFS-e Via indicada possui Evento de Cancelamento por Substituição. | Obrig. | Rej. | 1179 | Não é possível manifestar em documento cancelado por substituição para a chave de acesso {0}" |  |
|  |  |  | O registro do Evento de Manifestação não pode ser validado pois a NFS-e Via indicada foi Substituída. | Obrig. | Rej. | 1180 | Não é possível manifestar em documento substituído para a chave de acesso {0} |  |
| 8 | evento/infEvento/ | dhEvento | A data do evento deve ser maior ou igual a 01 de janeiro de 2026. | Obrig. | Rej. | 1193 | Data de competência inválida menor que 2026. |  |
| 15 | evento/infEvento/ | tpAmb | Tipo do ambiente informado difere do ambiente utilizado. | Obrig. | Rej. | 1133 | Ambiente inválido. |  |
| 10 | evento/infEvento/ | e203202 | - | - | - | - | - |  |
| 17 | evento/infEvento/e203202/ | xDesc | - | - | - | - | - |  |
| 18 | evento/infEvento/e203202/ | tpNi | - | - | - | - | - |  |
|  | evento/infEvento/e203202/ | CNPJCPF | O campo deve ser preenchido com um CPF válido se o campo tpNi for igual a 1. O campo deve ser preenchido com um CNPJ válido se o campo tpNi for igual a 2. |  |  | 1187 1188 | CPF da manifestação de aceite inválido. CNPJ da manifestação de aceite inválido. |  |
| 19 | evento/infEvento/e203202/ | xRazaoSocial | - | - | - | - | - |  |
| 14 | evento/infEvento/ | e203204 | - | - | - | - | - |  |
| 15 | evento/infEvento/e203204/ | xDesc | - | - | - | - | - |  |
| 16 | evento/infEvento/e203204/ | tpNi | - | - | - | - | - |  |
| 17 | evento/infEvento/e203204/ | CNPJCPF | O campo deve ser preenchido com um CPF válido se o campo tpNi for igual a 1. O campo deve ser preenchido com um CNPJ válido se o campo tpNi for igual a 2. |  |  | 1189 1190 | CPF da manifestação de rejeição inválido. CNPJ da manifestação de rejeição inválido. |  |
| 24 | evento/infEvento/e203204/ | xRazaoSocial | - | - | - | - | - |  |
| 19 | evento/infEvento/e203204/ | cMotivo | - | - | - | - | - |  |
| 20 | evento/infEvento/e203204/ | xMotivoRejeita | O campo somente pode ser informado quando o campo cMotivo for igual a 99. | Obrig. | Rej. | 1186 | O campo somente pode ser preenchido pelo Adquirente quando o campo de Motivo da Rejeição da NFS-e Via for igual a 99 - Outros. |  |
| 21 | evento/ | Signature | A assinatura do Evento deve ser válida. | Obrig. | Rej. | 1114 | Arquivo enviado com erro na assinatura. |  |
|  |  |  | Certificado Digital da assintura inválido: - Validade do Certificado (data início e data fim); - Verifica a Cadeia de Certificação; - Certificado do Transmissor revogado; - LCR indisponível ou inválida. | Obrig. | Rej. | 1152 1154 1155 1156 | Certificado Digital da assinatura inválido. |  |
|  |  |  | Certificado Digital da assinatura fora do padrão estabelecido pelo Sistema Nacional NFS-e Via: - Versão diferente de 3; - Se informado, Basic Constraint deve ser true (não pode ser Certificado de AC); - KeyUsage não define 'Assinatura Digital' e 'Não Recusa'; - Falta a extensão de CNPJ (OtherName - OID=2.16.76.1.3.3) ou CPF (OtherName - OID=2.16.76.1.3.1); - Certificado Raiz difere da 'ICP-Brasil'. | Obrig. | Rej. | 1149 1150 1151 1153 | Certificado Digital fora do padrão estabelecido. |  |
|  |  |  | A assinatura deve ser feita com o certificado digital do: - Adquirente informado dentro da Manifestação. - Procurador Legal do Adquirente informado dentro da Manifestação. - Representante Legal do Adquirente informado dentro da Manifestação. | Obrig. | Rej. | E--- | Certificado utilizado na assinatura da Evento Via não autorizado. |  |
|  |  | dhReg | Prazo para aceitação de uma Manifestação - Comparar a Data da Recepção do documento de Manifestação com a Data de Competência da NFS-e Via que está sendo manifestada. | Obrig. | Rej. | 1182 | Prazo de manifestação {0} para a data de competência {1} da NFS-e Via excedido |  |
