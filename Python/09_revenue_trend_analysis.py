"""
Project: E-Commerce Business Performance Analytics

Script:
09_revenue_trend_analysis.py

Author:
Noel Channayil

Description:
Loads the Olist orders and order payments datasets, merges them,
and analyzes the monthly revenue trend.

Datasets:
- olist_orders_dataset.csv
- olist_order_payments_dataset.csv
"""

from pathlib import Path
import pandas as pd

# -------------------------------------------------------------------
# Define project directory
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

# -------------------------------------------------------------------
# Load datasets
# -------------------------------------------------------------------

orders = pd.read_csv(
    DATASET_DIR / "olist_orders_dataset.csv"
)

payments = pd.read_csv(
    DATASET_DIR / "olist_order_payments_dataset.csv"
)

# -------------------------------------------------------------------
# Convert Order Purchase Date
# -------------------------------------------------------------------

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

# -------------------------------------------------------------------
# Create Order Month
# -------------------------------------------------------------------

orders["order_month"] = (
    orders["order_purchase_timestamp"]
    .dt.to_period("M")
)

# -------------------------------------------------------------------
# Merge Orders and Payments
# -------------------------------------------------------------------

revenue_df = pd.merge(
    orders,
    payments,
    on="order_id",
    how="left"
)

# -------------------------------------------------------------------
# Monthly Revenue Analysis
# -------------------------------------------------------------------

monthly_revenue = (
    revenue_df
    .groupby("order_month")["payment_value"]
    .sum()
    .round(2)
)

# -------------------------------------------------------------------
# Display Results
# -------------------------------------------------------------------

print("\nMonthly Revenue Trend\n")
print(monthly_revenue)