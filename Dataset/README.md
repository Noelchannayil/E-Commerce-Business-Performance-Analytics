# Dataset

## Overview

This folder contains the raw datasets used in the **E-Commerce Business Performance Analytics** project along with the final analytical dataset generated after the data cleaning and integration process.

The datasets are based on the Brazilian Olist E-Commerce public dataset and cover customer information, orders, products, sellers, payments, reviews and marketing data. These datasets were processed using Python, integrated into PostgreSQL and later visualized in Power BI for business intelligence reporting.

---

# Dataset Files

| Dataset | Description |
|----------|-------------|
| olist_customers_dataset.csv | Customer information including customer ID, city, state and unique customer identifier. |
| olist_orders_dataset.csv | Order lifecycle including purchase date, approval, shipping and delivery status. |
| olist_order_items_dataset.csv | Product-level order details including seller, freight value and product price. |
| olist_order_payments_dataset.csv | Payment information including payment type, installments and payment value. |
| olist_order_reviews_dataset.csv | Customer review scores and review timestamps. |
| olist_products_dataset.csv | Product information including category and physical dimensions. |
| olist_sellers_dataset.csv | Seller information including seller city and state. |
| olist_geolocation_dataset.csv | Geographic reference data based on ZIP code prefixes. |
| product_category_name_translation.csv | Portuguese-to-English product category translation table. |
| olist_marketing_qualified_leads_dataset.csv | Marketing qualified lead information. |
| olist_closed_deals_dataset.csv | Closed sales opportunity dataset used for business analysis. |
| master_ecommerce_dataset.csv | Generated analytical dataset created by running Python/08_master_dataset.py. |

---

# Dataset Workflow

```text
Raw CSV Files
      │
      ▼
Data Cleaning (Python)
      │
      ▼
Missing Value Handling
      │
      ▼
Data Transformation
      │
      ▼
Dataset Integration
      │
      ▼
master_ecommerce_dataset.csv
      │
      ▼
PostgreSQL Database
      │
      ▼
Power BI Dashboard
```

---

# Final Analytical Dataset

The project combines multiple datasets into a single analytical dataset named:

```
master_ecommerce_dataset.csv
```

The merged dataset contains information from:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers

This dataset serves as the primary source for SQL analysis and Power BI dashboard development.

---

# Data Preparation

The datasets were processed using Python to perform:

- Data cleaning
- Missing value handling
- Duplicate checks
- Data type conversion
- Data transformation
- Dataset merging
- Feature engineering
- Exploratory Data Analysis (EDA)

---
---

# Large Dataset Files

GitHub's web interface restricts uploading large files. As a result, the following datasets are hosted externally.

| Dataset | Description |
|---------|-------------|
| `master_ecommerce_dataset.csv` | Final merged analytical dataset created during the ETL pipeline. |
| `olist_geolocation_dataset.csv` | Original Olist geolocation reference dataset. |

## Download

The datasets can be downloaded from the Google Drive folder below:

**Google Drive Folder**

👉 **https://drive.google.com/drive/u/3/folders/1ETrzZhfke-oO3XVl1mlV0l3j34CKimpZ**

After downloading, place the files inside the project's **Dataset** folder.

```
Dataset/
│
├── master_ecommerce_dataset.csv
├── olist_geolocation_dataset.csv
```

Once added, the repository will contain the complete set of datasets required to reproduce the entire ETL pipeline, SQL analysis and Power BI dashboard.

---

---

# Output

The prepared datasets enable analysis of:

- Revenue Performance
- Customer Behaviour
- Product Performance
- Seller Performance
- Geographic Analysis
- Delivery Performance
- Payment Trends
- Executive Business KPIs

---
