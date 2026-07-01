"""
Project: E-Commerce Business Performance Analytics

Script:
08_master_dataset.py

Author:
Noel Channayil

Description:
Creates the master analytical dataset by merging customers, orders,
payments, order items, products, and sellers into a single dataset
for SQL analysis and Power BI dashboard development.

Datasets:
- olist_customers_dataset.csv
- olist_orders_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_items_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv

Output:
Dataset/master_ecommerce_dataset.csv
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

customers = pd.read_csv(
    DATASET_DIR / "olist_customers_dataset.csv"
)

orders = pd.read_csv(
    DATASET_DIR / "olist_orders_dataset.csv"
)

payments = pd.read_csv(
    DATASET_DIR / "olist_order_payments_dataset.csv"
)

order_items = pd.read_csv(
    DATASET_DIR / "olist_order_items_dataset.csv"
)

products = pd.read_csv(
    DATASET_DIR / "olist_products_dataset.csv"
)

sellers = pd.read_csv(
    DATASET_DIR / "olist_sellers_dataset.csv"
)

# -------------------------------------------------------------------
# Data Cleaning
# -------------------------------------------------------------------

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("Unknown")
)

# -------------------------------------------------------------------
# Merge Customers with Orders
# -------------------------------------------------------------------

master = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="left"
)

print("After Orders + Customers:", master.shape)

# -------------------------------------------------------------------
# Merge Payments
# -------------------------------------------------------------------

master = pd.merge(
    master,
    payments,
    on="order_id",
    how="left"
)

print("After Payments:", master.shape)

# -------------------------------------------------------------------
# Merge Order Items
# -------------------------------------------------------------------

master = pd.merge(
    master,
    order_items,
    on="order_id",
    how="left"
)

print("After Order Items:", master.shape)

# -------------------------------------------------------------------
# Merge Products
# -------------------------------------------------------------------

master = pd.merge(
    master,
    products,
    on="product_id",
    how="left"
)

print("After Products:", master.shape)

# -------------------------------------------------------------------
# Merge Sellers
# -------------------------------------------------------------------

master = pd.merge(
    master,
    sellers,
    on="seller_id",
    how="left"
)

print("After Sellers:", master.shape)

# -------------------------------------------------------------------
# Final Dataset Summary
# -------------------------------------------------------------------

print("\nFinal Dataset Information")
print("-" * 50)
print("Rows and Columns :", master.shape)

print("\nColumns")
print(master.columns.tolist())

# -------------------------------------------------------------------
# Export Master Dataset
# -------------------------------------------------------------------

output_file = DATASET_DIR / "master_ecommerce_dataset.csv"

master.to_csv(
    output_file,
    index=False
)

print("\nMaster dataset exported successfully.")
print(f"Location: {output_file}")