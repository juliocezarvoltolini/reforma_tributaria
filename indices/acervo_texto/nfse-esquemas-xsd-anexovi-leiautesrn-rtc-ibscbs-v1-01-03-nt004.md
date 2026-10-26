---
id: nfse-esquemas-xsd-anexovi-leiautesrn-rtc-ibscbs-v1-01-03-nt004
titulo: Esquemas XSD - AnexoVI-LeiautesRN_RTC_IBSCBS-V1.01.03 - NT004
tipo: schema
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/producao-restrita/nfse-esquemas_xsd-rtc-v1-00-20251210.zip
arquivo_original: fontes/acervo/nfse-esquemas-xsd-anexovi-leiautesrn-rtc-ibscbs-v1-01-03-nt004.zip
sha256_original: 04662996e290add36f118c4457d8efed17848eb65d64e8b7ab56c6983c2429ad
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: 8bb2fefb2d5e721a9088dbd479134258b0cff52ff1c268cab1e21ba1c12aeda8
---

## Arquivos do pacote

- tiposCnc_v1.00.xsd
- tiposComplexos_v1.01.xsd
- tiposEventos_v1.01.xsd
- tiposSimples_v1.01.xsd
- xmldsig-core-schema.xsd
- CNC_v1.00.xsd
- DPS_v1.01.xsd
- evento_v1.01.xsd
- NFSe_v1.01.xsd
- pedRegEvento_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| DPS/infDPS/IBSCBS | TCRTCInfoIBSCBS | 0-1 |  |  |  | Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/finNFSe | TSRTCFinNFSe | 1-1 |  | 0 |  | Indicador da finalidade da emissão de NFS-e | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indFinal | TSRTCIndFinal | 0-1 |  | 0, 1 |  | Indica operação de uso ou consumo pessoal (art. 57) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/cIndOp | TSRTCCodIndOp | 1-1 |  |  | [0-9]{6} | Código indicador da operação de fornecimento, conforme tabela "código indicador de operação" | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpOper | TSRTCTpOper | 0-1 |  | 1, 2, 3, 4, 5 |  | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe | TCInfoRefNFSe | 0-1 |  |  |  | Grupo de NFS-e referenciadas | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe/refNFSe | TSChaveNFSe | 1-99 | -50 |  | [0-9]{50} | Chave da NFS-e referenciada | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpEnteGov | TSRTCTpEnteGov | 0-1 |  | 1, 2, 3, 4 |  | Tipo de ente governamental | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indDest | TSRTCIndDest | 1-1 |  | 0, 1 |  | A respeito do Destinatário dos serviços | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest | TCRTCInfoDest | 0-1 |  |  |  | Grupo de informações relativas ao Destinatário | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Destinatário do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Destinatário do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/NIF | TSNIF | 1-1 | 1-40 |  |  | Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Nome Empresarial do do Destinatário do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end | TCEndereco | 0-1 |  |  |  | Grupo de informações do endereço do Destinatário do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac | TCEnderNac | 1-1 |  |  |  | Grupo de informações específicas de endereço nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/cMun | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código do município, conforme Tabela do IBGE | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt | TCEnderExt | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cPais | TSCodPaisISO | 1-1 |  |  | [A-Z]{2} | Código do país (Tabela de Países ISO) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/fone | TSTelefone | 0-1 |  |  | [0-9]{6,20} | Número do telefone do Destinatário do serviço (Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/email | TSEmail | 0-1 | 1-80 |  |  | E-mail do Destinatário do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel | TCRTCInfoImovel | 0-1 |  |  |  | Grupo de informações de operações relacionadas a bens imóveis, exceto obras | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/inscImobFisc | TSInscImobFisc | 0-1 | 1-30 |  |  | Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/cCIB | TSCodCIB | 1-1 | 8 |  |  | Código do Cadastro Imobiliário Brasileiro - CIB | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end | TCEnderObraEvento | 1-1 |  |  |  | Grupo de informações do endereço da obra do serviço prestado | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt | TCEnderExtSimples | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores | TCRTCInfoValoresIBSCBS | 1-1 |  |  |  | Grupo de informações relativas aos valores do serviço prestado para IBS e CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes | TCRTCInfoReeRepRes | 0-1 |  |  |  | Grupo de informações relativas a valores incluídos neste documento e recebidos por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos | TCRTCListaDoc | 1-1000 |  |  |  | Grupo relativo aos documentos referenciados nos casos de reembolso, repasse e ressarcimento que serão considerados na base de cálculo do ISSQN, do IBS e da CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional | TCRTCListaDocDFe | 1-1 |  |  |  | Grupo de informações de documentos fiscais eletrônicos que se encontram no repositório nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/tipoChaveDFe | TSRTCTipoChaveDFe | 1-1 |  | 1, 2, 3, 9 |  | Documento fiscal a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/xTipoChaveDFe | TSDesc255 | 0-1 | 1-255 |  |  | Descrição da DF-e a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional Deve ser preenchido apenas quando "tipoChaveDFe = 9 (Outro)" | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/chaveDFe | TSRTCChaveDFe | 1-1 | 1-50 |  |  | Chave do Documento Fiscal eletrônico do repositório nacional referenciado para os casos de operações já tributadas | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro | TCRTCListaDocFiscalOutro | 1-1 |  |  |  | Grupo de informações de documento fiscais, eletrônicos ou não, que não se encontram no repositório nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/cMunDocFiscal | TSNum7Dig | 1-1 | -7 |  | [0-9]{7} | Código do município emissor do documento fiscal que não se encontra no repositório nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/nDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento fiscal que não se encontra no repositório nacional | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/xDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento fiscal | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro | TCRTCListaDocOutro | 1-1 |  |  |  | Grupo de informações de documento não fiscal. | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/nDoc | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento não fiscal | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/xDoc | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento não fiscal | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec | TCRTCListaDocFornec | 0-1 |  |  |  | Grupo de informações do fornecedor do documento referenciado | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Fornecedor do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Fornecedor do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/NIF | TSNIF | 1-1 | 1-40 |  |  | Este elemento só deverá ser preenchido para fornecedores não residentes no Brasil | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Razão Social do do Fornecedor do serviço | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtEmiDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da emissão do documento dedutível Ano, mês e dia (AAAA-MM-DD) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtCompDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da competência do documento dedutível Ano, mês e dia (AAAA-MM-DD) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/tpReeRepRes | TSRTCTpReeRepRes | 1-1 |  | 01, 02, 03, 04, 99 |  | Tipo de valor incluído neste documento, recebido por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/xTpReeRepRes | TSDesc150 | 0-1 | 1-150 |  |  | Descrição do reembolso ou ressarcimento quando a opção é "99 – Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem de terceiro" | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/vlrReeRepRes | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (total ou parcial, conforme documento informado) utilizado para não inclusão na base de cálculo do ISS e do IBS e da CBS da NFS-e que está sendo emitida (R$) | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib | TCRTCInfoTributosIBSCBS | 1-1 |  |  |  | Grupo de informações relacionados aos tributos IBS e CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS | TCRTCInfoTributosSitClas | 1-1 |  |  |  | Grupo de informações relacionadas ao IBS e à CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/CST | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cClassTrib | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código de Classificação Tributária do IBS e da CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cCredPres | TSRTCCodCredPres | 0-1 |  |  | [0-9]{2} | Código e Classificação do Crédito Presumido: IBS e CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular | TCRTCInfoTributosTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/CSTReg | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS de tributação regular | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/cClassTribReg | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código da Classificação Tributária do IBS e da CBS de tributação regular | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif | TCRTCInfoTributosDif | 0-1 |  |  |  | Grupo de informações relacionadas ao diferimento para IBS e CBS | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifUF | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS estadual | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifMun | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS municipal | tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifCBS | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para a CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS | TCRTCIBSCBS | 0-1 |  |  |  | Grupo de informações geradas pelo sistema referentes ao IBS e à CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/cLocalidadeIncid | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código IBGE da localidade de incidência do IBS/CBS (local da operação) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/xLocalidadeIncid | TSDesc600 | 1-1 | 1-600 |  |  | Nome da localidade de incidência do IBS/CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/pRedutor | TSDec2V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Percentual de redução de aliquota em compra governamental | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores | TCRTCValoresIBSCBS | 1-1 |  |  |  | Grupo de valores brutos referentes ao IBS/CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vBC | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto vBC = vServ - descIncond – vCalcReeRepRes – vISSQN – vPIS - vCOFINS (até 2026) ou vBC = vServ - descIncond – vCalcReeRepRes – vISSQN (até 2032) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vCalcReeRepRes | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (R$) total relativo ao fornecimento próprio de bens materiais ou relacionados a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados e que não integram da base de cálculo (BC) do ISSQN, do IBS e da CBS. | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf | TCRTCValoresIBSCBSUF | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Estadual | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da UF para IBS da localidade de incidência parametrizada no sistema | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pRedAliqUF | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota estadual | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pAliqEfetUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 - pRedutor) Se pRedAliqUF não for informado na DPS, então pAliqEfetUF é a própria pIBSUF | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun | TCRTCValoresIBSCBSMun | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Municipal | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do Município para IBS da localidade de incidência parametrizada no sistema | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pRedAliqMun | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota municipal | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pAliqEfetMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x (1 - pRedutor) Se pRedAliqMun não for informado na DPS, então pAliqEfetMun é a própria pIBSMun | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed | TCRTCValoresIBSCBSFed | 1-1 |  |  |  | Grupo de Informações relativas aos valores da CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da União para CBS parametrizada no sistema | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pRedAliqCBS | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual da redução de alíquota da CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pAliqEfetCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - pRedutor) Se pRedAliqCBS não for informado na DPS, então pAliqEfetCBS é a própria pCBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS | TCRTCTotalCIBS | 1-1 |  |  |  | Grupo de Totalizadores | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/vTotNF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor Total da NF considerando os impostos por fora: IBS e CBS O IBS e a CBS são por fora, por isso seus valores devem ser adicionados ao valor total da NF vTotNF = vLiq (em 2026) vTotNF = vLiq + vCBS + vIBSTot (a partir de 2027) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS | TCRTCTotalIBS | 1-1 |  |  |  | Grupo de valores referentes ao IBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/vIBSTot | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do IBS. vIBSTot = vIBSUF + vIBSMun | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres | TCRTCTotalIBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para IBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/pCredPresIBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para o IBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/vCredPresIBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido para o IBS vCredPresIBS = vBC x pCredPresIBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot | TCRTCTotalIBSUF | 1-1 |  |  |  | Grupo de valores referentes ao IBS Estadual | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vDifUF | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS estadual vDifUF = vIBSUF x pDifUF | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS estadual vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot | TCRTCTotalIBSMun | 1-1 |  |  |  | Grupo de valores referentes ao IBS Municipal | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vDifMun | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS municipal vDifMun = vIBSMun x pDifMun | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS municipal vIBSMun = vBC x (pIBSMun ou pAliqEfetMun) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS | TCRTCTotalCBS | 1-1 |  |  |  | Grupo de valores referentes à CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres | TCRTCTotalCBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/pCredPresCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para a CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/vCredPresCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido da CBS vCredPresCBS = vBC x pCredPresCBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vDifCBS | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento CBS vDifCBS = vCBS x pDifCBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor da CBS da União vCBS = vBC x (pCBS ou pAliqEfetCBS) | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular | TCRTCTotalTribRegular | 0-1 |  |  |  | Grupo de informações de tributação regular | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS estadual | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS estadual vTribRegIBSUF = vBC x pAliqEfeRegIBSUF | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS municipal | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS municipal vTribRegIBSMun = vBC x pAliqEfeRegIBSMun | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular da CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular da CBS vTribRegCBS = vBC x pAliqEfeRegCBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov | TCRTCTotalTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Estado | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS da UF calculado | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Município | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS do Município calculado | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da CBS | tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo da CBS calculado | tiposComplexos_v1.01.xsd |
