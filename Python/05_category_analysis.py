"""
Project: E-Commerce Business Performance Analytics

Script:
05_category_analysis.py

Author:
Noel Channayil

Description:
Loads the Olist products and order items datasets, handles missing
product categories, merges both datasets, and analyzes the number
of orders by product category.

Datasets:
Dataset/olist_products_dataset.csv
Dataset/olist_order_items_dataset.csv
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

products = pd.read_csv(
    DATASET_DIR / "olist_products_dataset.csv"
)

order_items = pd.read_csv(
    DATASET_DIR / "olist_order_items_dataset.csv"
)

# -------------------------------------------------------------------
# Handle Missing Product Categories
# -------------------------------------------------------------------

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("Unknown")
)

# -------------------------------------------------------------------
# Merge Products with Order Items
# -------------------------------------------------------------------

merged = pd.merge(
    order_items,
    products,
    on="product_id",
    how="left"
)

# -------------------------------------------------------------------
# Orders by Product Category
# -------------------------------------------------------------------

category_orders = (
    merged
    .groupby("product_category_name")
    .size()
    .sort_values(ascending=False)
)

# -------------------------------------------------------------------
# Display Results
# -------------------------------------------------------------------

print("\nTop 20 Product Categories by Number of Orders\n")
print(category_orders.head(20))