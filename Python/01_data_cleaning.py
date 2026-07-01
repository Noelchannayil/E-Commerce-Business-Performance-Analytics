"""
Project: E-Commerce Business Performance Analytics

Script:
01_data_cleaning.py

Author:
Noel Channayil

Description:
Loads the Olist customers dataset and displays the top 10 customer cities
based on the number of registered customers.

Dataset:
Dataset/olist_customers_dataset.csv
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

customers = pd.read_csv(
    DATASET_DIR / "olist_customers_dataset.csv"
)

# -------------------------------------------------------------------
# Top 10 customer cities
# -------------------------------------------------------------------

city_count = (
    customers["customer_city"]
    .value_counts()
    .head(10)
)

print("\nTop 10 Customer Cities\n")
print(city_count)