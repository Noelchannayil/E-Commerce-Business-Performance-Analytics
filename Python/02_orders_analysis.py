"""
Project: E-Commerce Business Performance Analytics

Script:
02_orders_analysis.py

Author:
Noel Channayil

Description:
Loads the Olist orders dataset, converts date columns into datetime format,
creates a monthly order period, and analyzes the monthly order trend.

Dataset:
Dataset/olist_orders_dataset.csv
"""

from pathlib import Path
import pandas as pd

# -------------------------------------------------------------------
# Define project directory
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

# -------------------------------------------------------------------
# Load dataset
# -------------------------------------------------------------------

orders = pd.read_csv(
    DATASET_DIR / "olist_orders_dataset.csv"
)

# -------------------------------------------------------------------
# Convert date columns
# -------------------------------------------------------------------

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

# -------------------------------------------------------------------
# Create Month column
# -------------------------------------------------------------------

orders["order_month"] = (
    orders["order_purchase_timestamp"]
    .dt.to_period("M")
)

# -------------------------------------------------------------------
# Monthly order trend
# -------------------------------------------------------------------

monthly_orders = (
    orders["order_month"]
    .value_counts()
    .sort_index()
)

print("\nMonthly Order Trend\n")
print(monthly_orders)