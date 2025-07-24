# Medallion Architecture

Este projeto demonstra como implementar a arquitetura Medallion na AWS, dividida em três camadas (Bronze, Silver e Gold), utilizando serviços como S3, Glue, Athena e Redshift para criar um pipeline robusto de ingestão, transformação e análise de dados.

## 🎯 Objetivos

* [x] Armazenar dados brutos (CSV, JSON) de forma segura e escalável
* [x] Validar e transformar os dados para formatos otimizados (Parquet)
* [x] Enriquecer os dados para análises e dashboards
* [x] Utilizar serviços gerenciados da AWS para orquestração e consulta
* [x] Fornecer um ambiente acessível para análise exploratória e visualização

## 🛠️ Tecnologias Utilizadas

* Python
* SQL
* Docker
* AWS (S3, Glue, Athena, Redshift, QuickSight)

## 🧱 Estrutura do Projeto

```
medallion-architecture/
│
├── 01-bronze-raw/            # Dados brutos (CSV, JSON)
│   ├── cep_info.csv
│   ├── products.json
│   └── users.csv
│
├── 02-silver-validated/      # Dados limpos e validados (Parquet)
│   ├── cep_info.parquet
│   ├── products.parquet
│   └── users.parquet
│
├── 03-gold-enriched/         # Dados prontos para análise
│   └── query.sql
│
├── data-access/              # Scripts e notebooks de acesso aos dados
│   ├── db.py
│   └── data-view.ipynb
│
└── architecture-diagram.mmd  # Diagrama da arquitetura
```

## 🚀 Como Executar

1. Clone o repositório:

   ```
   git clone https://github.com/aureliowozhiak/medallion-architecture.git
   cd medallion-architecture
   ```

2. Instale as dependências (se houver `requirements.txt`):

   ```
   pip install -r requirements.txt
   ```

3. Execute os scripts conforme a camada:

   * Bronze: Suba arquivos no S3
   * Silver: Rode os jobs no AWS Glue
   * Gold: Faça consultas no Athena
   * Acesso: Utilize Redshift ou visualize no QuickSight

## ☁️ Guia Rápido na AWS

* **Bronze:**
  Armazene os dados brutos em buckets S3

* **Silver:**
  Use AWS Glue para validar e transformar os dados (Parquet)

* **Gold:**
  Faça queries com Athena diretamente nos dados prontos no S3

* **Data Access:**
  Importe os dados no Amazon Redshift e conecte ao Amazon QuickSight para dashboards

## 📸 Screenshots

![Diagrama da Arquitetura](architecture-diagram.svg)

## 🔗 Links

* [📂 Código no GitHub](https://github.com/aureliowozhiak/medallion-architecture)
