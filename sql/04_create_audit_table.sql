-- Audit table for ADF pipeline execution records.
IF OBJECT_ID('audit.pipeline_audit', 'U') IS NULL
CREATE TABLE audit.pipeline_audit (
    audit_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    pipeline_name NVARCHAR(200) NOT NULL,
    run_id NVARCHAR(100) NOT NULL,
    source_name NVARCHAR(100) NULL,
    target_table NVARCHAR(200) NULL,
    rows_copied BIGINT NULL,
    status NVARCHAR(50) NOT NULL,
    error_message NVARCHAR(MAX) NULL,
    load_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO
