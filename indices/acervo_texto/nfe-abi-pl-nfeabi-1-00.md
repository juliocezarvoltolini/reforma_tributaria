---
id: nfe-abi-pl-nfeabi-1-00
titulo: Schemas XML NFeABI - Pacote de Liberação 1.00 (ZIP) - Publicado em 02/09/2026
tipo: schema
versao: '1.00'
data: '2026-09-02'
documento_fiscal: NF-e ABI
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=p9XiwqPUDKo=
arquivo_original: fontes/acervo/nfe-abi-pl-nfeabi-1-00.zip
sha256_original: 8c1a33ef15b353b2a552f3da99fc9d4acbea1ff01029a9452e118e75847e4e26
gerado_por: pipeline/acervo_texto.py
versao_gerador: 2
aviso: Tabela lida mecanicamente dos XSD do pacote (pipeline/acervo_texto.py).
sha256_corpo: e4c0fd952411bbb91832396e6e9c5aabbdf70ab5adcae22c80c50199a72114bc
---

## Arquivos do pacote

- PL_NFeABI_1.00/
- PL_NFeABI_1.00/consSitNFeABITiposBasico_v1.00.xsd
- PL_NFeABI_1.00/consSitNFeABI_v1.00.xsd
- PL_NFeABI_1.00/consStatServNFeABITiposBasico_v1.00.xsd
- PL_NFeABI_1.00/consStatServNFeABI_v1.00.xsd
- PL_NFeABI_1.00/DFeTiposBasicos_v1.00.xsd
- PL_NFeABI_1.00/evApropCredIndNFeABI_v1.00.xsd
- PL_NFeABI_1.00/evCancNFeABI_v1.00.xsd
- PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd
- PL_NFeABI_1.00/eventoNFeABI_v1.00.xsd
- PL_NFeABI_1.00/evPagParcelaNFeABI_v1.00.xsd
- PL_NFeABI_1.00/LEIA-ME.txt
- PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd
- PL_NFeABI_1.00/NFeABI_v1.00.xsd
- PL_NFeABI_1.00/procEventoNFeABI_v1.00.xsd
- PL_NFeABI_1.00/procNFeABI_v1.00.xsd
- PL_NFeABI_1.00/retConsSitNFeABI_v1.00.xsd
- PL_NFeABI_1.00/retConsStatServNFeABI_v1.00.xsd
- PL_NFeABI_1.00/retEventoNFeABI_v1.00.xsd
- PL_NFeABI_1.00/retNFeABI_v1.00.xsd
- PL_NFeABI_1.00/tiposGeralNFeABI_v1.00.xsd
- PL_NFeABI_1.00/xmldsig-core-schema_v1.01.xsd

## Campos de IBS, CBS e IS (lidos dos XSD)

| caminho | tipo | ocorrencia | tamanho | enumeracao | padrao | descricao | arquivo |
|---|---|---|---|---|---|---|---|
| evPagParcelaNFeABI/CST | TCSTIBSCBS | 1-1 |  |  | [0-9]{3} |  | PL_NFeABI_1.00/evPagParcelaNFeABI_v1.00.xsd |
| evPagParcelaNFeABI/cClassTrib | TcClassTribIBSCBS | 1-1 |  |  | [0-9]{6} |  | PL_NFeABI_1.00/evPagParcelaNFeABI_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS | TGIBSCBSEventoPagParcela | 1-1 |  |  |  |  | PL_NFeABI_1.00/evPagParcelaNFeABI_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/vOperacIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/vRedAjusteIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/vRedSocialIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/vBC | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF | TGIBSUF | 1-1 |  |  |  |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF/pIBSUF | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSUF/vIBSUF | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun | TGIBSMun | 1-1 |  |  |  |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun/pIBSMun | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gIBSMun/vIBSMun | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS | TGCBS | 1-1 |  |  |  |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS/pCBS | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gCBS/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov | TGTribCompraGov | 0-1 |  |  |  |  | PL_NFeABI_1.00/eventoNFeABITiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| evPagParcelaNFeABI/gIBSCBS/gTribCompraGov/vTribCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS | TIBSCBS | 1-1 |  |  |  |  | PL_NFeABI_1.00/NFeABI_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/CST | xs:string | 1-1 | 3-3 |  | [0-9]{3} |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/cClassTrib | xs:string | 1-1 | 6-6 |  | [0-9]{6} |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS | TGIBSCBS | 0-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/vOperacIndiv | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/vTornaIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/vRedAjusteIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/vRedSocialIndiv | TDec_1302 | 0-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/vBC | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF | TGIBSUF | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF/pIBSUF | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSUF/vIBSUF | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun | TGIBSMun | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun/pIBSMun | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gIBSMun/vIBSMun | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS | TGCBS | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS/pCBS | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS/gRed | TGRed | 1-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS/gRed/pRedAliq | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS/gRed/pAliqEfet | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gCBS/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov | TGTribCompraGov | 0-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSUF | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSUF | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/pAliqIBSMun | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/vTribIBSMun | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/pAliqCBS | TDec_0304 | 1-1 |  |  | 0\|0\.[0-9]{1,4}\|[1-9][0-9]{0,2}(\.[0-9]{1,4})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gIBSCBS/gTribCompraGov/vTribCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gEstornoCred | TGEstornoCred | 0-1 |  |  |  |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gEstornoCred/vIBSEstCred | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/gInfTrib/IBSCBS/gEstornoCred/vCBSEstCred | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/nfeabiTiposBasico_v1.00.xsd |
| NFeABI/infNFeABI/total/tribTot/vIBSUF | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/NFeABI_v1.00.xsd |
| NFeABI/infNFeABI/total/tribTot/vIBSMun | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/NFeABI_v1.00.xsd |
| NFeABI/infNFeABI/total/tribTot/vCBS | TDec_1302 | 1-1 |  |  | 0\|0\.[0-9]{2}\|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})? |  | PL_NFeABI_1.00/NFeABI_v1.00.xsd |
