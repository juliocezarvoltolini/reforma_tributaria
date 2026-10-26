---
id: nfse-nfse-esquemas-xsd-v1-01-20260209
titulo: NFSe-ESQUEMAS_XSD-v1.01-20260209
tipo: schema
versao: '1.01'
documento_fiscal: NFS-e
url: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual/nfse-esquemas_xsd-v1-01-20260209.zip
arquivo_original: fontes/acervo/nfse-nfse-esquemas-xsd-v1-01-20260209.zip
sha256_original: e7935cbd9470527c6cc32984c1b2263e614183bf0139ce2733eaaed2de9a8072
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: c35c45ce0bc8cbe8b84491cf22bad2cbea28e046cd4bd193299972efef38a27c
---

## Arquivos do pacote

- Schemas/
- Schemas/1.00/
- Schemas/1.00/CNC_v1.00.xsd
- Schemas/1.00/DPS_v1.00.xsd
- Schemas/1.00/evento_v1.00.xsd
- Schemas/1.00/NFSe_v1.00.xsd
- Schemas/1.00/pedRegEvento_v1.00.xsd
- Schemas/1.00/tiposCnc_v1.00.xsd
- Schemas/1.00/tiposComplexos_v1.00.xsd
- Schemas/1.00/tiposEventos_v1.00.xsd
- Schemas/1.00/tiposSimples_v1.00.xsd
- Schemas/1.00/xmldsig-core-schema.xsd
- Schemas/1.01/
- Schemas/1.01/CNC_v1.00.xsd
- Schemas/1.01/DPS_v1.01.xsd
- Schemas/1.01/evento_v1.01.xsd
- Schemas/1.01/NFSe_v1.01.xsd
- Schemas/1.01/pedRegEvento_v1.01.xsd
- Schemas/1.01/tiposCnc_v1.00.xsd
- Schemas/1.01/tiposComplexos_v1.01.xsd
- Schemas/1.01/tiposEventos_v1.01.xsd
- Schemas/1.01/tiposSimples_v1.01.xsd
- Schemas/1.01/xmldsig-core-schema.xsd
- Schemas/Componente_recepcao/
- Schemas/Componente_Schemas/

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| DPS/infDPS/IBSCBS | TCRTCInfoIBSCBS | 0-1 |  |  |  | Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/finNFSe | TSRTCFinNFSe | 1-1 |  | 0 |  | Indicador da finalidade da emissão de NFS-e | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indFinal | TSRTCIndFinal | 0-1 |  | 0, 1 |  | Indica operação de uso ou consumo pessoal (art. 57) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/cIndOp | TSRTCCodIndOp | 1-1 |  |  | [0-9]{6} | Código indicador da operação de fornecimento, conforme tabela "código indicador de operação" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpOper | TSRTCTpOper | 0-1 |  | 1, 2, 3, 4, 5 |  | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe | TCInfoRefNFSe | 0-1 |  |  |  | Grupo de NFS-e referenciadas | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe/refNFSe | TSChaveNFSe | 1-99 | -50 |  | [0-9]{50} | Chave da NFS-e referenciada | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpEnteGov | TSRTCTpEnteGov | 0-1 |  | 1, 2, 3, 4 |  | Tipo de ente governamental | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indDest | TSRTCIndDest | 1-1 |  | 0, 1 |  | A respeito do Destinatário dos serviços | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest | TCRTCInfoDest | 0-1 |  |  |  | Grupo de informações relativas ao Destinatário | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/NIF | TSNIF | 1-1 | 1-40 |  |  | Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Nome Empresarial do do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end | TCEndereco | 0-1 |  |  |  | Grupo de informações do endereço do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac | TCEnderNac | 1-1 |  |  |  | Grupo de informações específicas de endereço nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/cMun | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código do município, conforme Tabela do IBGE | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt | TCEnderExt | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cPais | TSCodPaisISO | 1-1 |  |  | [A-Z]{2} | Código do país (Tabela de Países ISO) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/fone | TSTelefone | 0-1 |  |  | [0-9]{6,20} | Número do telefone do Destinatário do serviço (Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/email | TSEmail | 0-1 | 1-80 |  |  | E-mail do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel | TCRTCInfoImovel | 0-1 |  |  |  | Grupo de informações de operações relacionadas a bens imóveis, exceto obras | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/inscImobFisc | TSInscImobFisc | 0-1 | 1-30 |  |  | Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/cCIB | TSCodCIB | 1-1 | 8 |  |  | Código do Cadastro Imobiliário Brasileiro - CIB | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end | TCEnderObraEvento | 1-1 |  |  |  | Grupo de informações do endereço da obra do serviço prestado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt | TCEnderExtSimples | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores | TCRTCInfoValoresIBSCBS | 1-1 |  |  |  | Grupo de informações relativas aos valores do serviço prestado para IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes | TCRTCInfoReeRepRes | 0-1 |  |  |  | Grupo de informações relativas a valores incluídos neste documento e recebidos por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos | TCRTCListaDoc | 1-1000 |  |  |  | Grupo relativo aos documentos referenciados nos casos de reembolso, repasse e ressarcimento que serão considerados na base de cálculo do ISSQN, do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional | TCRTCListaDocDFe | 1-1 |  |  |  | Grupo de informações de documentos fiscais eletrônicos que se encontram no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/tipoChaveDFe | TSRTCTipoChaveDFe | 1-1 |  | 1, 2, 3, 9 |  | Documento fiscal a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/xTipoChaveDFe | TSDesc255 | 0-1 | 1-255 |  |  | Descrição da DF-e a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional Deve ser preenchido apenas quando "tipoChaveDFe = 9 (Outro)" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/chaveDFe | TSRTCChaveDFe | 1-1 | 1-50 |  |  | Chave do Documento Fiscal eletrônico do repositório nacional referenciado para os casos de operações já tributadas | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro | TCRTCListaDocFiscalOutro | 1-1 |  |  |  | Grupo de informações de documento fiscais, eletrônicos ou não, que não se encontram no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/cMunDocFiscal | TSNum7Dig | 1-1 | -7 |  | [0-9]{7} | Código do município emissor do documento fiscal que não se encontra no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/nDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento fiscal que não se encontra no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/xDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro | TCRTCListaDocOutro | 1-1 |  |  |  | Grupo de informações de documento não fiscal. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/nDoc | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento não fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/xDoc | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento não fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec | TCRTCListaDocFornec | 0-1 |  |  |  | Grupo de informações do fornecedor do documento referenciado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/NIF | TSNIF | 1-1 | 1-40 |  |  | Este elemento só deverá ser preenchido para fornecedores não residentes no Brasil | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Razão Social do do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtEmiDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da emissão do documento dedutível Ano, mês e dia (AAAA-MM-DD) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtCompDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da competência do documento dedutível Ano, mês e dia (AAAA-MM-DD) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/tpReeRepRes | TSRTCTpReeRepRes | 1-1 |  | 01, 02, 03, 04, 99 |  | Tipo de valor incluído neste documento, recebido por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/xTpReeRepRes | TSDesc150 | 0-1 | 1-150 |  |  | Descrição do reembolso ou ressarcimento quando a opção é "99 – Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem de terceiro" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/vlrReeRepRes | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (total ou parcial, conforme documento informado) utilizado para não inclusão na base de cálculo do ISS e do IBS e da CBS da NFS-e que está sendo emitida (R$) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib | TCRTCInfoTributosIBSCBS | 1-1 |  |  |  | Grupo de informações relacionados aos tributos IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS | TCRTCInfoTributosSitClas | 1-1 |  |  |  | Grupo de informações relacionadas ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/CST | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cClassTrib | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código de Classificação Tributária do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cCredPres | TSRTCCodCredPres | 0-1 |  |  | [0-9]{2} | Código e Classificação do Crédito Presumido: IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular | TCRTCInfoTributosTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/CSTReg | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/cClassTribReg | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código da Classificação Tributária do IBS e da CBS de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif | TCRTCInfoTributosDif | 0-1 |  |  |  | Grupo de informações relacionadas ao diferimento para IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifUF | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifMun | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifCBS | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para a CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS | TCRTCIBSCBS | 0-1 |  |  |  | Grupo de informações geradas pelo sistema referentes ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/cLocalidadeIncid | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código IBGE da localidade de incidência do IBS/CBS (local da operação) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/xLocalidadeIncid | TSDesc600 | 1-1 | 1-600 |  |  | Nome da localidade de incidência do IBS/CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/pRedutor | TSDec2V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Percentual de redução de aliquota em compra governamental | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores | TCRTCValoresIBSCBS | 1-1 |  |  |  | Grupo de valores brutos referentes ao IBS/CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vBC | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto vBC = vServ - descIncond – vCalcReeRepRes – vISSQN – vPIS - vCOFINS (até 2026) ou vBC = vServ - descIncond – vCalcReeRepRes – vISSQN (até 2032) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vCalcReeRepRes | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (R$) total relativo ao fornecimento próprio de bens materiais ou relacionados a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados e que não integram da base de cálculo (BC) do ISSQN, do IBS e da CBS. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf | TCRTCValoresIBSCBSUF | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da UF para IBS da localidade de incidência parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pRedAliqUF | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pAliqEfetUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 - pRedutor) Se pRedAliqUF não for informado na DPS, então pAliqEfetUF é a própria pIBSUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun | TCRTCValoresIBSCBSMun | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do Município para IBS da localidade de incidência parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pRedAliqMun | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pAliqEfetMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x (1 - pRedutor) Se pRedAliqMun não for informado na DPS, então pAliqEfetMun é a própria pIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed | TCRTCValoresIBSCBSFed | 1-1 |  |  |  | Grupo de Informações relativas aos valores da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da União para CBS parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pRedAliqCBS | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual da redução de alíquota da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pAliqEfetCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - pRedutor) Se pRedAliqCBS não for informado na DPS, então pAliqEfetCBS é a própria pCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS | TCRTCTotalCIBS | 1-1 |  |  |  | Grupo de Totalizadores | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/vTotNF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor Total da NF considerando os impostos por fora: IBS e CBS O IBS e a CBS são por fora, por isso seus valores devem ser adicionados ao valor total da NF vTotNF = vLiq (em 2026) vTotNF = vLiq + vCBS + vIBSTot (a partir de 2027) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS | TCRTCTotalIBS | 1-1 |  |  |  | Grupo de valores referentes ao IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/vIBSTot | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do IBS. vIBSTot = vIBSUF + vIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres | TCRTCTotalIBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/pCredPresIBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para o IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/vCredPresIBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido para o IBS vCredPresIBS = vBC x pCredPresIBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot | TCRTCTotalIBSUF | 1-1 |  |  |  | Grupo de valores referentes ao IBS Estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vDifUF | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS estadual vDifUF = vIBSUF x pDifUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS estadual vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot | TCRTCTotalIBSMun | 1-1 |  |  |  | Grupo de valores referentes ao IBS Municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vDifMun | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS municipal vDifMun = vIBSMun x pDifMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS municipal vIBSMun = vBC x (pIBSMun ou pAliqEfetMun) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS | TCRTCTotalCBS | 1-1 |  |  |  | Grupo de valores referentes à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres | TCRTCTotalCBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/pCredPresCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para a CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/vCredPresCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido da CBS vCredPresCBS = vBC x pCredPresCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vDifCBS | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento CBS vDifCBS = vCBS x pDifCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor da CBS da União vCBS = vBC x (pCBS ou pAliqEfetCBS) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular | TCRTCTotalTribRegular | 0-1 |  |  |  | Grupo de informações de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS estadual vTribRegIBSUF = vBC x pAliqEfeRegIBSUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS municipal vTribRegIBSMun = vBC x pAliqEfeRegIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular da CBS vTribRegCBS = vBC x pAliqEfeRegCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov | TCRTCTotalTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Estado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS da UF calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Município | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS do Município calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo da CBS calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS | TCRTCInfoIBSCBS | 0-1 |  |  |  | Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/finNFSe | TSRTCFinNFSe | 1-1 |  | 0 |  | Indicador da finalidade da emissão de NFS-e | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indFinal | TSRTCIndFinal | 0-1 |  | 0, 1 |  | Indica operação de uso ou consumo pessoal (art. 57) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/cIndOp | TSRTCCodIndOp | 1-1 |  |  | [0-9]{6} | Código indicador da operação de fornecimento, conforme tabela "código indicador de operação" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpOper | TSRTCTpOper | 0-1 |  | 1, 2, 3, 4, 5 |  | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe | TCInfoRefNFSe | 0-1 |  |  |  | Grupo de NFS-e referenciadas | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/gRefNFSe/refNFSe | TSChaveNFSe | 1-99 | -50 |  | [0-9]{50} | Chave da NFS-e referenciada | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/tpEnteGov | TSRTCTpEnteGov | 0-1 |  | 1, 2, 3, 4 |  | Tipo de ente governamental | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/indDest | TSRTCIndDest | 1-1 |  | 0, 1 |  | A respeito do Destinatário dos serviços | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest | TCRTCInfoDest | 0-1 |  |  |  | Grupo de informações relativas ao Destinatário | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/NIF | TSNIF | 1-1 | 1-40 |  |  | Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Nome Empresarial do do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end | TCEndereco | 0-1 |  |  |  | Grupo de informações do endereço do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac | TCEnderNac | 1-1 |  |  |  | Grupo de informações específicas de endereço nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/cMun | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código do município, conforme Tabela do IBGE | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endNac/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt | TCEnderExt | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cPais | TSCodPaisISO | 1-1 |  |  | [A-Z]{2} | Código do país (Tabela de Países ISO) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/fone | TSTelefone | 0-1 |  |  | [0-9]{6,20} | Número do telefone do Destinatário do serviço (Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/dest/email | TSEmail | 0-1 | 1-80 |  |  | E-mail do Destinatário do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel | TCRTCInfoImovel | 0-1 |  |  |  | Grupo de informações de operações relacionadas a bens imóveis, exceto obras | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/inscImobFisc | TSInscImobFisc | 0-1 | 1-30 |  |  | Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/cCIB | TSCodCIB | 1-1 | 8 |  |  | Código do Cadastro Imobiliário Brasileiro - CIB | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end | TCEnderObraEvento | 1-1 |  |  |  | Grupo de informações do endereço da obra do serviço prestado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/CEP | TSCEP | 1-1 |  |  | [0-9]{8} | Número do CEP | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt | TCEnderExtSimples | 1-1 |  |  |  | Grupo de informações específicas de endereço no exterior | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/cEndPost | TSCodigoEndPostal | 1-1 | 1-11 |  |  | Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xCidade | TSCidade | 1-1 | 1-60 |  |  | Nome da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/endExt/xEstProvReg | TSEstadoProvRegiao | 1-1 | 1-60 |  |  | Estado, província ou região da cidade no exterior do prestador do serviço. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xLgr | TSLogradouro | 1-1 | 1-255 |  |  | Tipo e nome do logradouro da localização do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/nro | TSNumeroEndereco | 1-1 | 1-60 |  |  | Número do imóvel | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xCpl | TSComplementoEndereco | 0-1 | 1-156 |  |  | Complemento do endereço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/imovel/end/xBairro | TSBairro | 1-1 | 1-60 |  |  | Bairro | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores | TCRTCInfoValoresIBSCBS | 1-1 |  |  |  | Grupo de informações relativas aos valores do serviço prestado para IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes | TCRTCInfoReeRepRes | 0-1 |  |  |  | Grupo de informações relativas a valores incluídos neste documento e recebidos por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos | TCRTCListaDoc | 1-1000 |  |  |  | Grupo relativo aos documentos referenciados nos casos de reembolso, repasse e ressarcimento que serão considerados na base de cálculo do ISSQN, do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional | TCRTCListaDocDFe | 1-1 |  |  |  | Grupo de informações de documentos fiscais eletrônicos que se encontram no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/tipoChaveDFe | TSRTCTipoChaveDFe | 1-1 |  | 1, 2, 3, 9 |  | Documento fiscal a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/xTipoChaveDFe | TSDesc255 | 0-1 | 1-255 |  |  | Descrição da DF-e a que se refere a chaveDfe que seja um dos documentos do Repositório Nacional Deve ser preenchido apenas quando "tipoChaveDFe = 9 (Outro)" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dFeNacional/chaveDFe | TSRTCChaveDFe | 1-1 | 1-50 |  |  | Chave do Documento Fiscal eletrônico do repositório nacional referenciado para os casos de operações já tributadas | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro | TCRTCListaDocFiscalOutro | 1-1 |  |  |  | Grupo de informações de documento fiscais, eletrônicos ou não, que não se encontram no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/cMunDocFiscal | TSNum7Dig | 1-1 | -7 |  | [0-9]{7} | Código do município emissor do documento fiscal que não se encontra no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/nDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento fiscal que não se encontra no repositório nacional | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docFiscalOutro/xDocFiscal | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro | TCRTCListaDocOutro | 1-1 |  |  |  | Grupo de informações de documento não fiscal. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/nDoc | TSDesc255 | 1-1 | 1-255 |  |  | Número do documento não fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/docOutro/xDoc | TSDesc255 | 1-1 | 1-255 |  |  | Descrição do documento não fiscal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec | TCRTCListaDocFornec | 0-1 |  |  |  | Grupo de informações do fornecedor do documento referenciado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CNPJ | TSCNPJ | 1-1 | -14 |  | [0-9]{14} | Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/CPF | TSCPF | 1-1 | -11 |  | [0-9]{11} | Número da inscrição no Cadastro de Pessoa Física (CPF) do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/NIF | TSNIF | 1-1 | 1-40 |  |  | Este elemento só deverá ser preenchido para fornecedores não residentes no Brasil | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/cNaoNIF | TSCodNaoNIF | 1-1 |  | 0, 1, 2 |  | Motivo para não informação do NIF: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/fornec/xNome | TSDesc150 | 1-1 | 1-150 |  |  | Nome / Razão Social do do Fornecedor do serviço | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtEmiDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da emissão do documento dedutível Ano, mês e dia (AAAA-MM-DD) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/dtCompDoc | TSData | 1-1 |  |  | (((20(([02468][048])\|([13579][26]))-02-29))\|(20[0-9][0-9])-((((0[1-9])\|(1[0-2]))-((0[1-9])\|(1\d)\|(2[0-8])))\|((((0[13578])\|(1[02]))-31)\|(((0[1,3-9])\|(1[0-2]))-(29\|30))))) | Data da competência do documento dedutível Ano, mês e dia (AAAA-MM-DD) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/tpReeRepRes | TSRTCTpReeRepRes | 1-1 |  | 01, 02, 03, 04, 99 |  | Tipo de valor incluído neste documento, recebido por motivo de estarem relacionadas a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/xTpReeRepRes | TSDesc150 | 0-1 | 1-150 |  |  | Descrição do reembolso ou ressarcimento quando a opção é "99 – Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem de terceiro" | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/gReeRepRes/documentos/vlrReeRepRes | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (total ou parcial, conforme documento informado) utilizado para não inclusão na base de cálculo do ISS e do IBS e da CBS da NFS-e que está sendo emitida (R$) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib | TCRTCInfoTributosIBSCBS | 1-1 |  |  |  | Grupo de informações relacionados aos tributos IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS | TCRTCInfoTributosSitClas | 1-1 |  |  |  | Grupo de informações relacionadas ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/CST | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cClassTrib | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código de Classificação Tributária do IBS e da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/cCredPres | TSRTCCodCredPres | 0-1 |  |  | [0-9]{2} | Código e Classificação do Crédito Presumido: IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular | TCRTCInfoTributosTribRegular | 0-1 |  |  |  | Grupo de informações da Tributação Regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/CSTReg | TSRTCCodSitTrib | 1-1 |  |  | [0-9]{3} | Código de Situação Tributária do IBS e da CBS de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gTribRegular/cClassTribReg | TSRTCCodClassTrib | 1-1 |  |  | [0-9]{6} | Código da Classificação Tributária do IBS e da CBS de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif | TCRTCInfoTributosDif | 0-1 |  |  |  | Grupo de informações relacionadas ao diferimento para IBS e CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifUF | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifMun | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para o IBS municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| DPS/infDPS/IBSCBS/valores/trib/gIBSCBS/gDif/pDifCBS | TSDec3V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de diferimento para a CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS | TCRTCIBSCBS | 0-1 |  |  |  | Grupo de informações geradas pelo sistema referentes ao IBS e à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/cLocalidadeIncid | TSCodMunIBGE | 1-1 |  |  | [0-9]{7} | Código IBGE da localidade de incidência do IBS/CBS (local da operação) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/xLocalidadeIncid | TSDesc600 | 1-1 | 1-600 |  |  | Nome da localidade de incidência do IBS/CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/pRedutor | TSDec2V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Percentual de redução de aliquota em compra governamental | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores | TCRTCValoresIBSCBS | 1-1 |  |  |  | Grupo de valores brutos referentes ao IBS/CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vBC | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto vBC = vServ - descIncond – vCalcReeRepRes – vISSQN – vPIS - vCOFINS (até 2026) ou vBC = vServ - descIncond – vCalcReeRepRes – vISSQN (até 2032) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/vCalcReeRepRes | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor monetário (R$) total relativo ao fornecimento próprio de bens materiais ou relacionados a operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, já tributados e aqui referenciados e que não integram da base de cálculo (BC) do ISSQN, do IBS e da CBS. | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf | TCRTCValoresIBSCBSUF | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da UF para IBS da localidade de incidência parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pRedAliqUF | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/uf/pAliqEfetUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 - pRedutor) Se pRedAliqUF não for informado na DPS, então pAliqEfetUF é a própria pIBSUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun | TCRTCValoresIBSCBSMun | 1-1 |  |  |  | Grupo de Informações relativas aos valores do IBS Municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do Município para IBS da localidade de incidência parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pRedAliqMun | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual de redução de alíquota municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/mun/pAliqEfetMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x (1 - pRedutor) Se pRedAliqMun não for informado na DPS, então pAliqEfetMun é a própria pIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed | TCRTCValoresIBSCBSFed | 1-1 |  |  |  | Grupo de Informações relativas aos valores da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da União para CBS parametrizada no sistema | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pRedAliqCBS | TSDec3V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})? | Percentual da redução de alíquota da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/valores/fed/pAliqEfetCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1 - pRedutor) Se pRedAliqCBS não for informado na DPS, então pAliqEfetCBS é a própria pCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS | TCRTCTotalCIBS | 1-1 |  |  |  | Grupo de Totalizadores | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/vTotNF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor Total da NF considerando os impostos por fora: IBS e CBS O IBS e a CBS são por fora, por isso seus valores devem ser adicionados ao valor total da NF vTotNF = vLiq (em 2026) vTotNF = vLiq + vCBS + vIBSTot (a partir de 2027) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS | TCRTCTotalIBS | 1-1 |  |  |  | Grupo de valores referentes ao IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/vIBSTot | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor total do IBS. vIBSTot = vIBSUF + vIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres | TCRTCTotalIBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/pCredPresIBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para o IBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSCredPres/vCredPresIBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido para o IBS vCredPresIBS = vBC x pCredPresIBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot | TCRTCTotalIBSUF | 1-1 |  |  |  | Grupo de valores referentes ao IBS Estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vDifUF | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS estadual vDifUF = vIBSUF x pDifUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSUFTot/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS estadual vIBSUF = vBC x (pIBSUF ou pAliqEfetUF) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot | TCRTCTotalIBSMun | 1-1 |  |  |  | Grupo de valores referentes ao IBS Municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vDifMun | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento do IBS municipal vDifMun = vIBSMun x pDifMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gIBS/gIBSMunTot/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor do IBS municipal vIBSMun = vBC x (pIBSMun ou pAliqEfetMun) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS | TCRTCTotalCBS | 1-1 |  |  |  | Grupo de valores referentes à CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres | TCRTCTotalCBSCredPres | 0-1 |  |  |  | Grupo de valores referentes ao crédito presumido para CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/pCredPresCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do crédito presumido para a CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/gCBSCredPres/vCredPresCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Crédito Presumido da CBS vCredPresCBS = vBC x pCredPresCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vDifCBS | TSDec15V2 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total do Diferimento CBS vDifCBS = vCBS x pDifCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gCBS/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Total valor da CBS da União vCBS = vBC x (pCBS ou pAliqEfetCBS) | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular | TCRTCTotalTribRegular | 0-1 |  |  |  | Grupo de informações de tributação regular | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS estadual | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS estadual vTribRegIBSUF = vBC x pAliqEfeRegIBSUF | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular do IBS municipal | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular do IBS municipal vTribRegIBSMun = vBC x pAliqEfeRegIBSMun | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/pAliqEfeRegCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota efetiva de tributação regular da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribRegular/vTribRegCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor da tributação regular da CBS vTribRegCBS = vBC x pAliqEfeRegCBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov | TCRTCTotalTribCompraGov | 0-1 |  |  |  | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSUF | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Estado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSUF | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS da UF calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pIBSMun | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota do IBS de competência do Município | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vIBSMun | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo do IBS do Município calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/pCBS | TSDec2V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})? | Alíquota da CBS | Schemas/1.01/tiposComplexos_v1.01.xsd |
| NFSe/infNFSe/IBSCBS/totCIBS/gTribCompraGov/vCBS | TSDec15V2 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})? | Valor do Tributo da CBS calculado | Schemas/1.01/tiposComplexos_v1.01.xsd |
