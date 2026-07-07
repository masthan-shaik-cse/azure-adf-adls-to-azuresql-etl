# Runbook

## Normal Run
1. Generate sample data locally.
2. Upload sample files to the configured ADLS or Blob folders.
3. Run SQL scripts in the `sql/` folder in numeric order.
4. Validate linked service connections in ADF.
5. Trigger `pl_ingest_multiformat_to_sql` with a load date.
6. Check ADF Monitor and `audit.pipeline_audit`.

## Rerun a Failed Load
1. Identify the failed source from ADF Monitor or the audit table.
2. Fix the input file, permissions, schema mismatch, or linked service issue.
3. Confirm `meta.source_control.active_flag = 1` for the source.
4. Rerun the pipeline for the same `p_load_date`.
5. Confirm rows loaded and audit status is `Succeeded`.

## Common Issues and Fixes
- Storage path not found: verify container, folder, and file name placeholders.
- SQL login failure: verify Key Vault secret reference and firewall rules.
- Schema mismatch: compare source columns with staging table definitions.
- Parquet file unavailable: run the PySpark script in Databricks or skip that source until the file exists.
