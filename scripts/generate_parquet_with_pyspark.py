"""Generate a small Parquet payment sample with PySpark.

Run this in Azure Databricks or any local environment where PySpark is already available.
This script does not require secrets and writes only synthetic sample data.
"""

from pathlib import Path


def main():
    from pyspark.sql import SparkSession

    output_path = Path(__file__).resolve().parents[1] / "data" / "sample" / "payments_parquet"
    spark = (
        SparkSession.builder.appName("generate-retail-payments-parquet")
        .master("local[*]")
        .getOrCreate()
    )

    rows = [
        ("PAY0001", "ORD0001", "Card", "Settled", 936.45, "2025-04-01"),
        ("PAY0002", "ORD0002", "UPI", "Settled", 1073.90, "2025-04-02"),
        ("PAY0003", "ORD0003", "Wallet", "Authorized", 1211.35, "2025-04-03"),
        ("PAY0004", "ORD0004", "Card", "Settled", 1348.80, "2025-04-04"),
        ("PAY0005", "ORD0005", "NetBanking", "Refunded", 1486.25, "2025-04-05"),
        ("PAY0006", "ORD0006", "UPI", "Settled", 1623.70, "2025-04-06"),
        ("PAY0007", "ORD0007", "Card", "Failed", 1761.15, "2025-04-07"),
        ("PAY0008", "ORD0008", "Wallet", "Settled", 1898.60, "2025-04-08"),
        ("PAY0009", "ORD0009", "UPI", "Settled", 2036.05, "2025-04-09"),
        ("PAY0010", "ORD0010", "Card", "Authorized", 2173.50, "2025-04-10"),
    ]
    columns = [
        "payment_id",
        "order_id",
        "payment_method",
        "payment_status",
        "payment_amount",
        "payment_date",
    ]

    df = spark.createDataFrame(rows, columns)
    df.write.mode("overwrite").parquet(str(output_path))
    print(f"Generated payments Parquet at {output_path}")
    spark.stop()


if __name__ == "__main__":
    main()
