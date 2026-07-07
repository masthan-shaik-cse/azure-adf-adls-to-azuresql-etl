# Architecture

This project demonstrates a beginner-friendly Azure ingestion flow for synthetic retail files.

```text
CSV / JSON / Parquet files
          |
          v
ADLS Gen2 or Azure Blob Storage
          |
          v
Azure Data Factory pipeline
  - Lookup active sources from Azure SQL control table
  - ForEach active source
  - If Condition based on file_type
  - Copy Data activity for CSV, JSON, or Parquet
          |
          v
Azure SQL Database staging tables
  - stg.customers
  - stg.orders
  - stg.payments
          |
          v
Audit and monitoring
  - audit.pipeline_audit
  - ADF Monitor
  - Logic Apps webhook placeholder for failure notification
```

The design uses placeholders for all Azure resource names. This keeps the repository safe to publish and easy to adapt for a personal Azure lab.
