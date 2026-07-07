-- Create staging tables for CSV, JSON, and Parquet source files.
IF OBJECT_ID('stg.customers', 'U') IS NULL
CREATE TABLE stg.customers (
    customer_id NVARCHAR(20) NOT NULL,
    first_name NVARCHAR(100) NULL,
    last_name NVARCHAR(100) NULL,
    city NVARCHAR(100) NULL,
    state NVARCHAR(100) NULL,
    signup_date DATE NULL,
    loyalty_tier NVARCHAR(30) NULL,
    load_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    source_file_name NVARCHAR(260) NULL
);
GO

IF OBJECT_ID('stg.orders', 'U') IS NULL
CREATE TABLE stg.orders (
    order_id NVARCHAR(20) NOT NULL,
    customer_id NVARCHAR(20) NOT NULL,
    order_date DATE NULL,
    order_status NVARCHAR(30) NULL,
    order_channel NVARCHAR(30) NULL,
    order_amount DECIMAL(12, 2) NULL,
    load_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    source_file_name NVARCHAR(260) NULL
);
GO

IF OBJECT_ID('stg.payments', 'U') IS NULL
CREATE TABLE stg.payments (
    payment_id NVARCHAR(20) NOT NULL,
    order_id NVARCHAR(20) NOT NULL,
    payment_method NVARCHAR(50) NULL,
    payment_status NVARCHAR(30) NULL,
    payment_amount DECIMAL(12, 2) NULL,
    payment_date DATE NULL,
    load_datetime DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    source_file_name NVARCHAR(260) NULL
);
GO
