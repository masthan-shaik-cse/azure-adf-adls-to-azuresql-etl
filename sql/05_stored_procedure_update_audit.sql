-- Insert one audit record for each pipeline source execution.
CREATE OR ALTER PROCEDURE audit.usp_upsert_pipeline_audit
    @pipeline_name NVARCHAR(200),
    @run_id NVARCHAR(100),
    @source_name NVARCHAR(100),
    @target_table NVARCHAR(200),
    @rows_copied BIGINT = NULL,
    @status NVARCHAR(50),
    @error_message NVARCHAR(MAX) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO audit.pipeline_audit (
        pipeline_name,
        run_id,
        source_name,
        target_table,
        rows_copied,
        status,
        error_message,
        load_datetime
    )
    VALUES (
        @pipeline_name,
        @run_id,
        @source_name,
        @target_table,
        @rows_copied,
        @status,
        @error_message,
        SYSUTCDATETIME()
    );
END;
GO
