# Azure Portal Setup

This guide describes manual setup for a learning portfolio environment.

## 1. Resource Group
Create a resource group such as `<resource-group-name>` in your preferred Azure region.

## 2. Storage Account
Create a storage account named `<storage-account-name>` and enable hierarchical namespace if you plan to use ADLS Gen2.

## 3. ADLS Container
Create a container named `<container-name>`. Suggested folders:

```text
retail/raw/customers/
retail/raw/orders/
retail/raw/payments/
retail/archive/
retail/error/
```

## 4. Azure SQL Database
Create Azure SQL Server `<server-name>` and database `<database-name>`. Run the scripts in the `sql/` folder in numeric order.

## 5. Azure Data Factory
Create an ADF instance. Import or manually recreate the linked services, datasets, pipeline, and trigger from the `adf/` folder.

## 6. Linked Services
Configure:

- ADLS Gen2 or Blob Storage linked service
- Azure SQL Database linked service
- Azure Key Vault linked service for secret references

## 7. Datasets
Create datasets for customers CSV, orders JSON, payments Parquet, and Azure SQL target tables.

## 8. Pipeline Import
Use `adf/pipelines/pl_ingest_multiformat_to_sql.json` as a template. Replace placeholders with lab resource names.

## 9. Trigger Setup
Use `adf/triggers/tr_daily_retail_ingestion.json` as a daily trigger template. Keep it disabled until linked services and datasets are tested.
