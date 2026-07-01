"""
Project: E-Commerce Business Performance Analytics

Script:
04_product_analysis.py

Author:
Noel Channayil

Description:
Loads the Olist products dataset, handles missing values,
and validates the cleaned dataset by checking remaining null values.

Dataset:
Dataset/olist_products_dataset.csv
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

products = pd.read_csv(
    DATASET_DIR / "olist_products_dataset.csv"
)

# -------------------------------------------------------------------
# Handle Missing Product Category
# -------------------------------------------------------------------

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("Unknown")
)

# -------------------------------------------------------------------
# Handle Missing Product Dimensions
# -------------------------------------------------------------------

dimension_columns = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for column in dimension_columns:
    products[column] = (
        products[column]
        .fillna(products[column].median())
    )

# -------------------------------------------------------------------
# Validate Missing Values
# -------------------------------------------------------------------

print("\nRemaining Missing Values\n")
print(products.isnull().sum())