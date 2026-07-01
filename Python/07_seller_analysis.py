"""
Project: E-Commerce Business Performance Analytics

Script:
07_seller_analysis.py

Author:
Noel Channayil

Description:
Loads the Olist sellers dataset and checks for duplicate
seller records to validate data quality.

Dataset:
Dataset/olist_sellers_dataset.csv
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

sellers = pd.read_csv(
    DATASET_DIR / "olist_sellers_dataset.csv"
)

# -------------------------------------------------------------------
# Duplicate Seller Analysis
# -------------------------------------------------------------------

duplicate_count = sellers.duplicated().sum()

# -------------------------------------------------------------------
# Display Results
# -------------------------------------------------------------------

print("\nDuplicate Seller Records\n")
print(duplicate_count)