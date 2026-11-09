---
id: nfse-esquemas-prod-restrita-20261020
titulo: NFSe-ESQUEMAS_XSD-PRODREST-v1.01-20261020
tipo: schema
versao: v1.01-20261020
data: '2026-10-20'
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/producao-restrita/esquemas_prod_restrita_20261020.zip
arquivo_original: fontes/acervo/nfse-esquemas-prod-restrita-20261020.zip
sha256_original: 25fdcecc651a67a216496ab10d7566631e6ed10f721e37d62c7845dadb0ea267
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: c67e432d290edf3ce47464eb8e03660eea704e9e0df6d299b8ae1d01a52ad57c
---

## Arquivos do pacote

- evento_v1.01.xsd
- NFSe_v1.01.xsd
- pedRegEvento_v1.01.xsd
- tiposCnc_v1.00.xsd
- tiposComplexos_v1.01.xsd
- tiposEventos_v1.01.xsd
- tiposSimples_v1.01.xsd
- xmldsig-core-schema.xsd
- CNC_v1.00.xsd
- DPS_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo | escolha |
|---|---|---|---|---|---|---|---|---|
| NFSe/infNFSe/IBSCBS | TCRTCIBSCBS | 0-1 |  |  |  | Grupo de informações geradas pelo sistema referentes ao IBS e à CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/cLocalidadeIncid | TSCodMunIBGE | 0-1 |  |  | [0-9]{7} | Código IBGE da localidade de incidência do IBS/CBS (local da operação) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/xLocalidadeIncid | TSDesc600 | 0-1 | 1-600 |  | [\s\S]*[^\s][\s\S]* | Nome da localidade de incidência do IBS/CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/pRedutor | TSDec2V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Percentual de redução de aliquota em compra governamental | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores | TCRTCValoresIBSCBS | 0-1 |  |  |  | Grupo de valores brutos referentes ao IBS/CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/vBC | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto vBC = vServ - descIncond – (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) – vISSQN – vPIS - vCOFINS (até 2026) ou vBC = vServ - descIncond – (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) – vISSQN (a partir de 2027 até 2032) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/vCalcAjusteBCLocImoveis | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (R$) total relativo aos valores de ajuste (dedução/redução) da Base de Cálculo do IBS e da CBS referentes às operações de locação, cessão onerosa ou arrendamento de bens imóveis. Apenas para os subitens 99.03. | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/vCalcAjusteBCIBSCBS | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (R$) total relativo a glosa de serviços de saúde ou a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, devidamente referenciados, e que não integram da base de cálculo (BC) do IBS e da CBS. | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/uf | TCRTCValoresIBSCBSUF | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Estadual | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/uf/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da UF para IBS da localidade de incidência parametrizada no sistema | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/uf/pRedAliqUF | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota estadual | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/uf/pAliqEfetUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 - pRedutor) Se pRedAliqUF não for informado na DPS, então pAliqEfetUF é a própria pIBSUF | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/mun | TCRTCValoresIBSCBSMun | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Municipal | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/mun/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do Município para IBS da localidade de incidência parametrizada no sistema | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/mun/pRedAliqMun | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota municipal | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/mun/pAliqEfetMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x (1 - pRedutor) Se pRedAliqMun não for informado na DPS, então pAliqEfetMun é a própria pIBSMun | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/fed | TCRTCValoresIBSCBSFed | 1-1 |  |  |  | Grupo de Informações relativas aos valores da CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/fed/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da União para CBS parametrizada no sistema | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/fed/pRedAliqCBS | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual da redução de alíquota da CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/valores/fed/pAliqEfetCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - pRedutor) Se pRedAliqCBS não for informado na DPS, então pAliqEfetCBS é a própria pCBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS | TCRTCTotalCIBS | 1-1 |  |  |  | Grupo de Totalizadores | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/vTotNF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor Total da NF considerando os impostos por fora: IBS e CBS O IBS e a CBS são por fora, por isso seus valores devem ser adicionados ao valor total da NF vTotNF = vLiq (em 2026) vTotNF = vLiq + vCBS + vIBSTot (a partir de 2027) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS | TCRTCTotalIBS | 0-1 |  |  |  | Grupo de valores referentes ao IBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/vIBSTot | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do IBS. vIBSTot = vIBSUF + vIBSMun | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres | TCRTCTotalIBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para IBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/pCredPresIBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para o IBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/vCredPresIBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido para o IBS vCredPresIBS = vBC x pCredPresIBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot | TCRTCTotalIBSUF | 1-1 |  |  |  | Grupo de valores referentes ao IBS Estadual | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vDifUF | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS estadual vDifUF = vIBSUF x pDifUF | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS estadual vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot | TCRTCTotalIBSMun | 1-1 |  |  |  | Grupo de valores referentes ao IBS Municipal | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vDifMun | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS municipal vDifMun = vIBSMun x pDifMun | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS municipal vIBSMun = vBC x (pIBSMun ou pAliqEfetMun) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS | TCRTCTotalCBS | 0-1 |  |  |  | Grupo de valores referentes à CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres | TCRTCTotalCBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/pCredPresCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para a CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/vCredPresCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido da CBS vCredPresCBS = vBC x pCredPresCBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vDifCBS | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento CBS vDifCBS = vCBS x pDifCBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor da CBS da União vCBS = vBC x (pCBS ou pAliqEfetCBS) | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular | TCRTCTotalTribRegular | 0-1 |  |  |  | Grupo de informações de tributação regular | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS estadual | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS estadual vTribRegIBSUF = vBC x pAliqEfeRegIBSUF | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS municipal | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS municipal vTribRegIBSMun = vBC x pAliqEfeRegIBSMun | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular da CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular da CBS vTribRegCBS = vBC x pAliqEfeRegCBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov | TCRTCTotalTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Estado | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS da UF calculado | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Município | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS do Município calculado | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da CBS | tiposComplexos_v1.01.xsd |  |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo da CBS calculado | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS | TCRTCInfoIBSCBS | 0-1 |  |  |  | Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/indFinal | TSRTCIndFinal | 0-1 |  | 0, 1 |  | Indica operação de uso ou consumo pessoal (art. 57) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/cIndOp | TSRTCCodIndOp | 0-1 |  |  | [0-9]{6} | Código indicador da operação de fornecimento, conforme tabela "código indicador de operação" | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/tpOper | TSRTCTpOper | 0-1 |  | 1, 2, 3, 4, 5 |  | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/gRefNFSe | TCInfoRefNFSe | 0-1 |  |  |  | Grupo de NFS-e referenciadas | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/gRefNFSe/refNFSe | TSChaveNFSe | 1-99 | -50 |  | [0-9]{6}([0-9A-Z]{14})[0-9]{30} | Chave da NFS-e referenciada | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/tpEnteGov | TSRTCTpEnteGov | 0-1 |  | 1, 2, 3, 4 |  | Tipo de ente governamental | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/indDest | TSRTCIndDest | 1-1 |  | 0, 1 |  | A respeito do Destinatário dos serviços | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest | TCRTCInfoDest | 0-1 |  |  |  | Grupo de informações relativas ao Destinatário | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9A-Z]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Destinatário do serviço | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Destinatário do serviço | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/NIF | TSNIF | 1-1 | 1-40 |  |  | Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/xNome | TSDesc150 | 1-1 | 1-150 |  | [\s\S]*[^\s][\s\S]* | Nome / Nome Empresarial do do Destinatário do serviço | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end | TCEndereco | 0-1 |  |  |  | Grupo de informações do endereço do Destinatário do serviço | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endNac | TCEnderNac | 1-1 |  |  |  | Grupo de informações específicas de endereço nacional | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/end/endNac/cMun | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código do município, conforme Tabela do IBGE | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endNac/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endExt | TCEnderExt | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/dest/end/endExt/cPais | TSCodPaisISO | 1-1 |  |  | [A-Z]{2} | Código do país (Tabela de Países ISO) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/fone | TSTelefone | 0-1 |  |  | [0-9]{6,20} | Número do telefone do Destinatário do serviço (Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/dest/email | TSEmail | 0-1 | 1-80 |  |  | E-mail do Destinatário do serviço | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel | TCRTCInfoImovel | 0-1 |  |  |  | Grupo de informações de operações relacionadas a bens imóveis, exceto obras | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/cMun | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código do município do endereço do imóvel (Tabela do IBGE) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao | TCRTCLocacaoImovel | 0-1 |  |  |  | Grupo de informações relativas às operações de locação, cessão onerosa ou arrendamento de bens imóveis | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao/pCopropriedade | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de Copropriedade (Caso só haja um locador, cedente ou arrendador, informar o Percentual de Copropriedade de 100%) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao/vTotOper | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total da operação com bem imóvel (Informar o valor total da operação de locação, cessão onerosa ou arrendamento de bens imóveis, associado ao aluguel, renda ou equivalente, conforme art. 255 da LC 214/2025). Não deverá ser inserido neste campo o valor proporcional do coproprietário. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao/vDescIncondTot | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do Desconto Incondicionado (Informar o valor total do desconto incondicionado na operação de locação, cessão onerosa ou arrendamento de bens imóveis) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao/vDescCondTot | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do Desconto Condicionado (Informar o valor total do desconto incondicionado na operação de locação, cessão onerosa ou arrendamento de bens imóveis) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gLocacao/dVencOrig | TSData | 0-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data de vencimento original Ano, Mês e Dia (AAAA-MM-DD) (Informar data de vencimento original do aluguel, renda ou equivalente na operação de locação, cessão onerosa ou arrendamento de bens imóveis) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob | TCRTCUnidadesImobiliarias | 0-99 |  |  |  | Grupo de informações relativas às unidades imobiliárias objeto da operação | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/inscImobFisc | TSInscImobFisc | 0-1 | 1-30 |  |  | Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/cCIB | TSCodCIB | 1-1 | 8 |  |  | Código do Cadastro Imobiliário Brasileiro - CIB | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end | TCEnderImovel | 1-1 |  |  |  | Grupo de informações do endereço do imóvel. | tiposComplexos_v1.01.xsd | sim |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Código numérico do Endereçamento Postal nacional (CEP) do endereço do imóvel. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro do endereço do imóvel. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número no logradouro do endereço do imóvel. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço do imóvel. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/end/xBairro | TSBairro | 0-1 | 1-60 |  |  | Bairro do endereço do imóvel. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/gAjusteBCLocImoveis | TCRTCValoresBCImoveis | 0-1000 |  |  |  | Grupo de informações relativas a valores de ajuste (dedução/redução) da Base de Cálculo do IBS e da CBS referentes às operações de locação, cessão onerosa ou arrendamento de bens imóveis | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/gAjusteBCLocImoveis/tpAjusteBCLocImoveis | TSAjusteBCLocImoveis | 1-1 |  | 01, 02, 03, 04, 99 |  | Tipo de parcela não integrante da base de cálculo do IBS e da CBS; 01 = Tributos inclusos no aluguel ou equivalente (Ex.: IPTU, Contribuição de melhoria) - apenas para NBS 1.1002.10.00 ou 1.1002.20.00; 02 = Emolumento incluso no aluguel ou equivalente - apenas para NBS 1.1002.10.00 ou 1.1002.20.00; 03 = Condomínio incluso no aluguel ou equivalente - apenas para NBS 1.1002.10.00 ou 1.1002.20.00; 04 = Redutor Social - apenas para a NBS 1.1002.10.00; 99 = Outras parcelas inclusas no aluguel ou equivalente; | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/gAjusteBCLocImoveis/xTpAjusteBCLocImoveis | TSDesc150 | 0-1 | 1-150 |  | [\s\S]*[^\s][\s\S]* | Descrição do tipo de parcela não integrante da base de cálculo do IBS e da CBS quando a opção for "99 = Outras parcelas inclusas no aluguel ou equivalente". | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/imovel/gUnidImob/gAjusteBCLocImoveis/vAjusteBCLocImoveis | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário utilizado para não inclusão na base de cálculo do IBS e da CBS da NFS-e que está sendo emitida (R$). (Informar o valor total da parcela não integrante da base de cálculo - IPTU, Condomínio, Redutor social, etc. -, não devendo ser inserido o valor proporcional do coproprietário) | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/bensMoveis | TCRTCInfoBensMoveis | 0-1000 |  |  |  | Grupo de informações relativas aos bens móveis objetos de locação | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/bensMoveis/cNCMBemMovel | TSNCM | 1-1 | -8 |  | [0-9]{8} | Código da Nomenclatura Comum do Mercosul (NCM) do bem móvel objeto da locação. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/bensMoveis/xNCMBemMovel | TSDesc150 | 1-1 | 1-150 |  | [\s\S]*[^\s][\s\S]* | Descrição do Bem Móvel objeto da locação. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/bensMoveis/qtdNCMBemMovel | TSNum3Dig | 1-1 | -3 |  | [0-9]{1}[0-9]{0,2} | Quantidade do Bem Móvel objeto da locação. | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores | TCRTCInfoValoresIBSCBS | 1-1 |  |  |  | Grupo de informações relativas aos valores do serviço prestado para IBS e CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib | TCRTCInfoTribIBSCBS | 1-1 |  |  |  | Grupo de informações de tributação do IBS e da CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/CST | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/cClassTrib | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código de Classificação Tributária do IBS e da CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS | TCRTCInfoTributosSitClas | 0-1 |  |  |  | Grupo de informações relacionadas ao IBS e à CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cCredPres | TSRTCCodCredPres | 0-1 |  |  | [0-9]{2} | Código e Classificação do Crédito Presumido: IBS e CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular | TCRTCInfoTributosTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/CSTReg | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS de tributação regular | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/cClassTribReg | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código da Classificação Tributária do IBS e da CBS de tributação regular | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif | TCRTCInfoTributosDif | 0-1 |  |  |  | Grupo de informações relacionadas ao diferimento para IBS e CBS | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifUF | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS estadual | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifMun | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS municipal | tiposComplexos_v1.01.xsd |  |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifCBS | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para a CBS | tiposComplexos_v1.01.xsd |  |
