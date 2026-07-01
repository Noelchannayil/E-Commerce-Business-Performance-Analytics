"""
Project: E-Commerce Business Performance Analytics

Script:
10_revenue_trend_chart.py

Author:
Noel Channayil

Description:
Loads the Olist orders and payments datasets, calculates monthly
revenue, and visualizes the monthly revenue trend using Matplotlib.

Datasets:
- olist_orders_dataset.csv
- olist_order_payments_dataset.csv
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

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
# Merge Orders with Payments
# -------------------------------------------------------------------

revenue_df = pd.merge(
    orders,
    payments,
    on="order_id",
    how="left"
)

# -------------------------------------------------------------------
# Calculate Monthly Revenue
# -------------------------------------------------------------------

monthly_revenue = (
    revenue_df
    .groupby("order_month")["payment_value"]
    .sum()
)

# -------------------------------------------------------------------
# Remove Incomplete Months
# -------------------------------------------------------------------

monthly_revenue = monthly_revenue[
    monthly_revenue.index < "2018-09"
]

# -------------------------------------------------------------------
# Plot Monthly Revenue Trend
# -------------------------------------------------------------------

plt.figure(figsize=(12, 6))

monthly_revenue.plot(
    linewidth=2
)

plt.title("Monthly Revenue Trend", fontsize=16)

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.show()