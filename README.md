# Medallion Architecture - Tutorial e Guia AWS

![Diagrama da Arquitetura](architecture-diagram.svg)

## Estrutura do Projeto

O projeto segue o padrão Medallion Architecture, dividido em três camadas principais:

- **Bronze (01-bronze-raw):**
  - Armazena dados brutos, como arquivos CSV e JSON.
  - Exemplo: `cep_info.csv`, `products.json`, `users.csv`

- **Silver (02-silver-validated):**
  - Contém dados validados e processados, geralmente em formato Parquet.
  - Exemplo: `cep_info.parquet`, `products.parquet`, `users.parquet`

- **Gold (03-gold-enriched):**
  - Dados enriquecidos e prontos para análises e relatórios.
  - Exemplo: `query.sql`

- **Data Access:**
  - Scripts, notebooks e banco de dados para análise e visualização dos dados.
  - Exemplo: `db.py`, `data-view.ipynb`, `Amazon Redshift`

Veja o diagrama da arquitetura em `architecture-diagram.mmd`.

---

## Guia Rápido para Subir na AWS

Cada camada do projeto pode ser implementada usando os seguintes serviços AWS:

- **Bronze:**
  - Suba os arquivos brutos para um **Amazon S3 Bucket**.

- **Silver:**
  - Use o **AWS Glue** para processar, validar e catalogar os dados, salvando-os novamente no S3.

- **Gold:**
  - Utilize **Amazon Athena** para consultas analíticas sobre os dados processados no S3.

- **Data Access:**
  - Importe os dados finais para um **Amazon Redshift** para análises avançadas.
  - Visualize os dados com **Amazon QuickSight** conectando ao Redshift.

 