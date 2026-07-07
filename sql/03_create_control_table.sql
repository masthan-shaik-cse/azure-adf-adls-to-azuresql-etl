-- Control table for metadata-driven source ingestion.
IF OBJECT_ID('meta.source_control', 'U') IS NULL
CREATE TABLE meta.source_control (
    source_id INT IDENTITY(1,1) PRIMARY KEY,
    source_name NVARCHAR(100) NOT NULL,
    file_type NVARCHAR(20) NOT NULL,
    source_folder_path NVARCHAR(500) NOT NULL,
    source_file_name NVARCHAR(260) NOT NULL,
    target_schema NVARCHAR(50) NOT NULL,
    target_table NVARCHAR(100) NOT NULL,
    active_flag BIT NOT NULL DEFAULT 1,
    created_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO

IF NOT EXISTS (SELECT 1 FROM meta.source_control)
INSERT INTO meta.source_control (
    source_name,
    file_type,
    source_folder_path,
    source_file_name,
    target_schema,
    target_table,
    active_flag
)
VALUES
    ('customers', 'csv', 'retail/raw/customers/', 'customers.csv', 'stg', 'customers', 1),
    ('orders', 'json', 'retail/raw/orders/', 'orders.json', 'stg', 'orders', 1),
    ('payments', 'parquet', 'retail/raw/payments/', 'payments_parquet', 'stg', 'payments', 1);
GO
