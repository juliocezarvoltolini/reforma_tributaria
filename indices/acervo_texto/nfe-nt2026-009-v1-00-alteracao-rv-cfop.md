---
id: nfe-nt2026-009-v1-00-alteracao-rv-cfop
titulo: Nota Técnica 2026.009 v.1.00 - Publicada em 09/09/2026
tipo: nota.tecnica
versao: '1.00'
data: '2026-09-09'
documento_fiscal: NF-e/NFC-e
url: https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ADlgg2xjMZI=
arquivo_original: fontes/acervo/nfe-nt2026-009-v1-00-alteracao-rv-cfop.pdf
sha256_original: 50b7dec40bba8928b4d544feb4fdbd8c8bac16e37c99d926ddb2834cf246f15d
gerado_por: pipeline/acervo_texto.py
versao_gerador: 3
aviso: 'Texto extraído do PDF (pypdf), página a página. Tabelas podem sair com as colunas embaralhadas: para campos do leiaute, use o texto do pacote de schemas da mesma versão; para o resto, confira no original.'
sha256_corpo: b77caa84fb2b2caa6bd6b51561d8f18352391c7e2b327b708d729239ffc880da
---

## Página 1

Alteração de Regra de Validação de 
CFOP 
 
Nota Técnica 2026.009 - Versão 1.00 
Setembro de 2026

## Página 2

Nota Fiscal Eletrônica - NF-e 
Alteração de Regra de Validação de CFOP 
NT 2026.009 
 
 
  
 
Página 2 / 5 
Sumário 
1. Introdução ................................ ................................ ................................ ................................ ... 4 
2. Regras de Validação ................................ ................................ ................................ ................... 5 
2.1. Grupo I. Produtos e Serviços da NF-e ................................ ................................ .................. 5

## Página 3

Nota Fiscal Eletrônica - NF-e 
Alteração de Regra de Validação de CFOP 
NT 2026.009 
 
 
  
 
Página 3 / 5 
Controle de Versões 
Versão Publicação Descrição 
1.00 09/2026 Alteração da regra de validação I08-140. 
 
Histórico de Alterações / Cronograma 
Versão Histórico de atualizações Implantação 
Teste 
Implantação 
Produção 
1.00 Alteração da regra de validação I08-140, ampliando a aceitação dos CFOP 
1.949 e 2.949 para as situações previstas na regra. Até 17/09/2026 Até 17/09/2026

## Página 4

Nota Fiscal Eletrônica - NF-e 
Alteração de Regra de Validação de CFOP 
NT 2026.009 
 
 
  
 
Página 4 / 5 
1. Introdução 
Esta Nota Técnica altera a regra de validação I08-140 da Nota Fiscal Eletrônica (NF-e), modelo 55, 
para permitir a utilização dos CFOP 1.949 e 2.949 em todas as situações abrangidas pela própria 
regra. 
 
A alteração é pontual e não modifica o leiaute da NF -e nem os schemas XML. A disponibilização 
imediata da correção nos ambientes autorizadores é necessária porque nem todos os CFOPs de 
saída existentes possuem CFOPs de devolução correspondentes. Por essa razão, esta Nota 
Técnica trata exclusivamente da alteração da referida  regra de validação, de modo a permitir a 
utilização dos CFOPs 1.949 e 2.949 nas situações nela previstas. 
 
As datas de implantação nos ambientes de homologação e de produção estão indicadas no 
Histórico de Alterações / Cronograma.

## Página 5

Nota Fiscal Eletrônica - NF-e 
Alteração de Regra de Validação de CFOP 
NT 2026.009 
 
 
  
 
Página 5 / 5 
2. Regras de Validação 
2.1. Grupo I. Produtos e Serviços da NF-e 
Campo Modelo Regra de Validação Aplic. Msg Descrição Erro 
I08-140 55 Para NF-e com as finalidades abaixo, somente serão aceitos CFOPs de devolução de 
mercadoria: 
   - Devolução de mercadoria (tag: finNFe = 4); 
   - ou Nota de Crédito (tag: finNFe=5) do tipo “03=Retorno por Recusa Total na Entrega 
ou Por Não Localização do Destinatário na Tentativa de Entrega” (tag: 
tpNFCredito=03); 
   - ou Nota de Crédito (tag: finNFe=5) do tipo “06=Retorno por Recusa Parcial na Entrega” 
(tag: tpNFCredito=06); 
Observação 1: Vide relação de CFOP de devolução de mercadoria na tabela de apoio 
publicada no Portal da NF-e (Tabela CFOP, indDevol=1). 
Exceção 1: Aceitar os CFOP 1.949 e 2.949. na devolução de venda. Para estes CFOP 
verificar a condição: 
   - Devolução de mercadoria (tag: finNFe = 4) (NT 2015.002); 
Exceção 2: Aceitar os CFOP 5.949 e 6.949 na devolução simbólica de gás natural (NCM 
27112100) nos termos do Ajuste SINIEF nº 22/21 (NT 2021.004) 
Obrig. 327 Rejeição: CFOP inválido para Nota Fiscal de devolução 
ou de retorno de mercadoria [nItem: 999]
