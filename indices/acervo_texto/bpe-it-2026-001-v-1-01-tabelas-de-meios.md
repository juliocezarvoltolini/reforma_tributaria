---
id: bpe-it-2026-001-v-1-01-tabelas-de-meios
titulo: Informe Técnico 2026.001 v.1.01 - meios de pagamento - Publicado em 25/08/2026
tipo: informe.tecnico
versao: '1.01'
data: '2026-08-25'
documento_fiscal: BP-e, CFF (Conformidade Fácil), CT-e/CT-e OS/GTV-e, DC-e, MDF-e, NF-e ABI, NF-e/NFC-e, NF3e, NFAg, NFCom, NFGas, ONE, PES/PAA
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=vZg2QuZtVg0=
arquivo_original: fontes/acervo/bpe-it-2026-001-v-1-01-tabelas-de-meios.pdf
sha256_original: 1e58913755c4e617f30619448909dd9ef82b0c772bcd44dc85774e77bcd28900
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: 10d894b808c36ffd5da2b2f9730eb7b4663ccecf8441ff0bb0e57e5fc5bc393b
---

## Página 1

Reforma Tributária do 
Consumo 
 
Informe Técnico 2026.001 
Versão 1.01 agosto de 2026

## Página 2

Projeto RTC 
Informe Técnico – Tabela de Meios de Pagamento para Vinculação Pgto 
IT 2026.001 v1.01 
 
 
Página 2 / 3 
 
Sumário 
 
Histórico de Alterações / Cronograma .................................................................................... 3 
1 Introdução ....................................................................................................................... 3

## Página 3

Projeto RTC 
Informe Técnico – Tabela de Meios de Pagamento para Vinculação Pgto 
IT 2026.001 v1.01 
 
 
Página 3 / 3 
 
Histórico de Alterações / Cronograma  
Versão Histórico de atualizações Implantação 
Homologação 
Implantação 
Produção 
1.00  Divulgação dos códigos válidos para o campo de Tipo de Meio de 
Pagamento (NTs 2026.001) 
Abril/2026 Maio/2026 
1.01  Adequação do IT para considerar todos os modelos de DFe - - 
1 Introdução 
As Notas Técnicas 2026.001 dos documentos fiscais eletrônicos (CTe, BPe, NF3e, NFCom, 
NFAg e NFGas) e 2026.006 (NFe e NFCe) introduziram o grupo de informações da vinculação 
da transação do pagamento nos DFe. 
 
A estrutura de campos, voltada para as informações que serão utilizadas no sistema do Split 
Payment, possui uma tag para informar o código do Meio de Pagamento utilizado na 
transação. 
 
Existe uma tabela nacional que estabelece os códigos para os meios de pagamento nos 
documentos fiscais eletrônicos, utilizada pelo sistema da Nota Fiscal Eletrônica (NFe) e 
publicada no portal nacional da NFe (https://www.nfe.fazenda.gov.br) e no portal dos DFe da 
SEFAZ Virtual RS (https://dfe-portal.svrs.rs.gov.br). 
 
O grupo de informação da vinculação da transação de pagamento utilizará os seguintes 
códigos estabelecidos nesta tabela: 
 
Código Descrição 
15 Boleto 
17 Pix QRCode 
18 TED 
20 PIX chave ou QRCode estático 
23 Pix automático* 
24 TEF / booktransfer* 
*Novos códigos que serão atualizados na tabela nacional 
 
A utilização de um código diferente dos relacionados acima causará a rejeição 1003 – Tipo 
de Pagamento inválido 
A inclusão de códigos válidos será realizada através de atualizações deste Informe Técnico.
