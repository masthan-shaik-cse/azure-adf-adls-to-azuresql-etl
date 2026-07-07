"""Generate small synthetic retail sample files using Python standard library only."""

import csv
import json
from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "sample"


def build_customers():
    names = [
        ("CUST001", "Aarav", "Reddy", "Hyderabad", "Telangana", "2025-01-05", "Gold"),
        ("CUST002", "Diya", "Sharma", "Bengaluru", "Karnataka", "2025-01-11", "Silver"),
        ("CUST003", "Vihaan", "Patel", "Pune", "Maharashtra", "2025-01-18", "Bronze"),
        ("CUST004", "Anika", "Nair", "Kochi", "Kerala", "2025-01-22", "Gold"),
        ("CUST005", "Kabir", "Khan", "Mumbai", "Maharashtra", "2025-02-01", "Platinum"),
        ("CUST006", "Meera", "Iyer", "Chennai", "Tamil Nadu", "2025-02-09", "Silver"),
        ("CUST007", "Rohan", "Das", "Kolkata", "West Bengal", "2025-02-12", "Bronze"),
        ("CUST008", "Sara", "Ali", "Delhi", "Delhi", "2025-02-18", "Gold"),
        ("CUST009", "Arjun", "Mehta", "Ahmedabad", "Gujarat", "2025-02-25", "Silver"),
        ("CUST010", "Nisha", "Gupta", "Jaipur", "Rajasthan", "2025-03-02", "Bronze"),
        ("CUST011", "Ishan", "Verma", "Lucknow", "Uttar Pradesh", "2025-03-08", "Gold"),
        ("CUST012", "Priya", "Menon", "Coimbatore", "Tamil Nadu", "2025-03-15", "Silver"),
        ("CUST013", "Dev", "Joshi", "Indore", "Madhya Pradesh", "2025-03-20", "Bronze"),
        ("CUST014", "Tara", "Kapoor", "Chandigarh", "Chandigarh", "2025-03-25", "Gold"),
        ("CUST015", "Neel", "Bose", "Bhubaneswar", "Odisha", "2025-03-30", "Silver"),
    ]
    return [
        {
            "customer_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "city": row[3],
            "state": row[4],
            "signup_date": row[5],
            "loyalty_tier": row[6],
        }
        for row in names
    ]


def build_orders():
    statuses = ["Delivered", "Shipped", "Created", "Delivered", "Cancelled"]
    channels = ["Web", "Mobile", "Store", "Mobile"]
    orders = []
    for index in range(1, 21):
        customer_num = ((index - 1) % 15) + 1
        orders.append(
            {
                "order_id": f"ORD{index:04d}",
                "customer_id": f"CUST{customer_num:03d}",
                "order_date": f"2025-04-{((index - 1) % 28) + 1:02d}",
                "order_status": statuses[index % len(statuses)],
                "order_channel": channels[index % len(channels)],
                "order_amount": round(799 + (index * 137.45), 2),
            }
        )
    return orders


def write_customers(customers):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / "customers.csv"
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(customers[0].keys()))
        writer.writeheader()
        writer.writerows(customers)


def write_orders(orders):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / "orders.json"
    with path.open("w", encoding="utf-8") as json_file:
        json.dump(orders, json_file, indent=2)
        json_file.write("\n")


def main():
    customers = build_customers()
    orders = build_orders()
    write_customers(customers)
    write_orders(orders)
    print(f"Generated {len(customers)} customers and {len(orders)} orders in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
