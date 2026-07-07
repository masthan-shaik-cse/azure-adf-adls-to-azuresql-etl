# Data Dictionary

## customers.csv
| Column | Description |
| --- | --- |
| customer_id | Synthetic customer identifier |
| first_name | Customer first name |
| last_name | Customer last name |
| city | Customer city |
| state | Customer state |
| signup_date | Date the synthetic customer signed up |
| loyalty_tier | Bronze, Silver, Gold, or Platinum |

## orders.json
| Column | Description |
| --- | --- |
| order_id | Synthetic order identifier |
| customer_id | Customer associated with the order |
| order_date | Order date |
| order_status | Created, Shipped, Delivered, or Cancelled |
| order_channel | Web, Mobile, or Store |
| order_amount | Order amount before payment processing |

## payments.parquet
| Column | Description |
| --- | --- |
| payment_id | Synthetic payment identifier |
| order_id | Related order identifier |
| payment_method | Card, UPI, Wallet, or NetBanking |
| payment_status | Authorized, Settled, Failed, or Refunded |
| payment_amount | Payment amount |
| payment_date | Payment date |

## SQL Technical Columns
| Column | Description |
| --- | --- |
| load_datetime | UTC timestamp when the row was loaded |
| source_file_name | Source file name used for traceability |
