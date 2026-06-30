# 🛒 E-Commerce Business Performance Analytics

An end-to-end Business Performance Analytics project that transforms raw e-commerce transaction data into meaningful business insights using **Python, PostgreSQL, SQL and Power BI**.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

---

## Project Overview

This project was developed to analyze the performance of an e-commerce business by transforming raw transactional data into meaningful business insights through interactive dashboards.

The project follows a complete analytics workflow, beginning with data cleaning and preprocessing in Python, followed by database design and SQL analysis in PostgreSQL. The processed data is then connected to Power BI to create interactive dashboards that provide insights into customers, products, sales performance, payment trends and delivery operations.

Rather than focusing only on dashboard creation, this project demonstrates the complete data analytics lifecycle—from raw data preparation to business reporting and strategic recommendations.

### Project Highlights

- Developed a complete end-to-end analytics solution using Python, PostgreSQL, SQL and Power BI.
- Cleaned and transformed raw e-commerce datasets for accurate analysis.
- Designed a relational PostgreSQL database and created SQL views for business reporting.
- Built five interactive Power BI dashboards using DAX measures and KPIs.
- Analyzed customer behavior, product performance, sales trends and operational efficiency.
- Generated actionable business insights and strategic recommendations.

---

## Table of Contents

- [Dashboard Preview](#dashboard-preview)
- [About the Project](#about-the-project)
- [Business Problem](#business-problem)
- [Project Objectives](#project-objectives)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Dataset Overview](#dataset-overview)
- [ETL Pipeline](#etl-pipeline)
- [Database Design](#database-design)
- [Dashboard Overview](#dashboard-overview)
- [Key Business Insights](#key-business-insights)
- [Repository Structure](#repository-structure)
- [Installation Guide](#installation-guide)
- [Future Enhancements](#future-enhancements)

---

## Dashboard Preview

The Power BI report consists of five interactive dashboards, each designed to analyze a different aspect of the e-commerce business. Together, these dashboards provide a comprehensive view of business performance, customer behavior, product performance, sales trends and operational efficiency.

### Executive Dashboard

Provides a high-level summary of business performance including revenue, orders, customers, average order value, monthly revenue trends and top-performing states and product categories.

![Executive Dashboard](Dashboard%20Screenshots/01_Executive_Dashboard.png)

---

### Customer Analytics Dashboard

Focuses on customer acquisition, repeat customers, geographical distribution and revenue contribution across different cities and states to better understand customer behavior.

![Customer Analytics Dashboard](Dashboard%20Screenshots/02_Customer_Analytics.png)

---

### Product Analytics Dashboard

Analyzes product categories, seller performance, category-wise revenue contribution and product performance to identify high-performing products and growth opportunities.

![Product Analytics Dashboard](Dashboard%20Screenshots/03_Product_Analytics.png)

---

### Sales & Order Intelligence Dashboard

Monitors sales trends, order volume, payment methods, delivery performance and operational KPIs to evaluate overall business efficiency.

![Sales & Order Intelligence Dashboard](Dashboard%20Screenshots/04_Sales_Order_Intelligence.png)

---

### Insights & Recommendations Dashboard

Summarizes the overall analysis using business insights, Pareto analysis, decomposition analysis and strategic recommendations to support data-driven decision-making.

![Insights & Recommendations Dashboard](Dashboard%20Screenshots/05_Insights_Recommendations.png)

---

## About the Project

This project was built to analyze the performance of an e-commerce business by transforming raw transactional data into meaningful business insights. It follows the complete analytics lifecycle, from data preparation and database design to interactive dashboard development and business reporting.

Using publicly available e-commerce datasets, I developed an end-to-end analytics solution to answer important business questions related to customers, products, sales performance, payment behavior, and delivery operations. The objective was not only to visualize business performance but also to uncover trends, identify opportunities and generate insights that support better business decisions.

The project begins with raw e-commerce datasets, which are cleaned and prepared using **Python**. The processed data is then stored in **PostgreSQL**, where SQL is used to create tables, views and business queries for reporting. Finally, the data is connected to **Power BI**, where interactive dashboards are developed using DAX measures to monitor key business metrics.

The final solution consists of five interactive dashboards that provide a comprehensive view of business performance, helping stakeholders monitor revenue, customer behavior, product performance, sales trends, payment preferences and delivery efficiency from a single reporting platform.

---

## Business Problem

E-commerce businesses process thousands of customer orders, payments and product transactions every day. While this data contains valuable information, it is often spread across multiple datasets, making it difficult to gain a complete view of business performance.

Without a centralized analytics solution, decision-makers may struggle to answer important business questions such as:

- Which product categories generate the highest revenue?
- Which states and cities contribute the most to overall sales?
- How are revenue and order volumes changing over time?
- Which payment methods are most preferred by customers?
- How efficient is the order delivery process?
- Which products and sellers contribute the most to business growth?
- What business areas require improvement to increase revenue and customer satisfaction?

To address these challenges, this project brings together data from multiple e-commerce datasets into a single reporting solution. The final dashboards provide stakeholders with a clear view of business performance, enabling them to monitor key metrics, identify trends, evaluate operational efficiency and make informed business decisions with confidence.

---

## Project Objectives

The primary objective of this project was to build an end-to-end business analytics solution that converts raw e-commerce data into meaningful insights for business decision-making. The project focuses on transforming raw business data into meaningful insights through data cleaning, SQL analysis, and interactive dashboard reporting.

The project was designed to:

- Clean and preprocess raw e-commerce datasets to ensure data quality and consistency.
- Design a structured PostgreSQL database for efficient data storage and querying.
- Perform SQL-based analysis to extract meaningful business insights.
- Develop interactive Power BI dashboards to monitor key business performance indicators (KPIs).
- Analyze customer behavior, purchasing patterns, and geographic sales distribution.
- Evaluate product category performance and seller contributions to overall revenue.
- Monitor sales trends, payment preferences and order delivery performance.
- Identify business trends, growth opportunities and operational improvement areas.
- Present insights through intuitive visualizations that support data-driven decision-making.
- Deliver strategic recommendations based on analytical findings.

---

## Technology Stack

The project was developed using a combination of programming, database and business intelligence tools to support the complete analytics workflow.

| Technology | Role in the Project |
|------------|------------------------|
| **Python** | Cleaned and preprocessed raw e-commerce datasets, handled missing values, standardized data formats and performed exploratory data analysis (EDA). |
| **Pandas** | Used for data manipulation, cleaning, merging datasets and feature engineering. |
| **NumPy** | Supported numerical operations and data transformations during preprocessing. |
| **PostgreSQL** | Stored the cleaned data in a structured relational database for efficient querying and reporting. |
| **SQL** | Created tables, views and analytical queries to extract meaningful business insights and prepare reporting datasets. |
| **Power BI** | Developed interactive dashboards, KPIs and visualizations for business performance analysis. |
| **DAX** | Created calculated measures and KPIs to support dynamic reporting and dashboard interactivity. |
| **Visual Studio Code** | Primary IDE used for Python scripting, SQL development and project management. |
| **pgAdmin 4** | Managed the PostgreSQL database, executed SQL scripts and validated query results. |
| **Git & GitHub** | Used for version control, repository management and project documentation. |

---

## Project Architecture

The project follows a structured end-to-end analytics workflow that transforms raw e-commerce transaction data into meaningful business insights. Each stage of the pipeline prepares, processes, and enriches the data before passing it to the next stage, ensuring reliable analysis, interactive reporting, and data-driven decision-making.

```mermaid
flowchart LR

%% =====================================================
%% E-COMMERCE BUSINESS PERFORMANCE ANALYTICS ARCHITECTURE
%% =====================================================

A["<b>Data Source</b><hr/>
<b>Raw E-Commerce Dataset</b><br/><br/>
• Customers<br/>
• Orders<br/>
• Products<br/>
• Payments<br/>
• Sellers"]

B["<b>Data Processing</b><hr/>
<b>Python</b><br/><br/>
• Data Cleaning<br/>
• Missing Value Handling<br/>
• Data Transformation<br/>
• Exploratory Data Analysis"]

C["<b>Data Storage</b><hr/>
<b>PostgreSQL</b><br/><br/>
• Relational Database<br/>
• Tables<br/>
• Relationships"]

D["<b>Business Analytics</b><hr/>
<b>SQL Analytics</b><br/><br/>
• SQL Queries<br/>
• SQL Views<br/>
• KPI Calculations"]

E["<b>Business Intelligence</b><hr/>
<b>Power BI</b><br/><br/>
• Data Model<br/>
• DAX Measures<br/>
• Interactive Reports"]

F["<b>Reporting</b><hr/>
<b>Interactive Dashboards</b><br/><br/>
• Executive Overview<br/>
• Customer Analytics<br/>
• Product Analytics<br/>
• Sales & Order Intelligence<br/>
• Insights & Recommendations"]

G["<b>Business Outcome</b><hr/>
<b>Business Insights</b><br/><br/>
• Revenue Analysis<br/>
• Customer Behaviour<br/>
• Product Performance<br/>
• Strategic Recommendations"]

%% ==========================
%% FLOW
%% ==========================

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G

%% ==========================
%% STYLING
%% ==========================

style A fill:#E8F4FD,stroke:#1565C0,stroke-width:2px,color:#000
style B fill:#EAF7EC,stroke:#2E7D32,stroke-width:2px,color:#000
style C fill:#FFF8E6,stroke:#F9A825,stroke-width:2px,color:#000
style D fill:#F4ECFB,stroke:#6A1B9A,stroke-width:2px,color:#000
style E fill:#E8F7FD,stroke:#0277BD,stroke-width:2px,color:#000
style F fill:#FFF2E8,stroke:#EF6C00,stroke-width:2px,color:#000
style G fill:#FDECF2,stroke:#C2185B,stroke-width:2px,color:#000

linkStyle default stroke:#616161,stroke-width:2px
```
---

## Dataset Overview

The project is based on the **Brazilian E-Commerce Public Dataset (Olist)**, which contains transactional data from a multi-category online marketplace. The dataset captures the complete customer purchasing journey, from order placement and payment to product delivery and customer reviews.

The original dataset consists of multiple related CSV files, each representing a different business entity. These datasets were cleaned, transformed and merged into a unified analytical dataset for SQL analysis and Power BI reporting.

### Source Datasets

| Dataset | Description |
|----------|-------------|
| **Customers** | Customer details, unique customer identifiers and location information. |
| **Orders** | Order lifecycle, purchase timestamps, delivery status and shipping dates. |
| **Order Items** | Product-level information for each order, including seller details and item pricing. |
| **Order Payments** | Payment methods, installment information and payment values. |
| **Order Reviews** | Customer review scores and review timestamps. |
| **Products** | Product categories and product attributes. |
| **Sellers** | Seller information and geographic locations. |
| **Geolocation** | Customer and seller location data based on ZIP codes. |
| **Product Category Translation** | Translation of Portuguese product category names into English. |

### Final Dataset Summary

After data cleaning and transformation, the individual datasets were merged into a single analytical dataset that was used for SQL analysis and Power BI dashboard development.

| Attribute | Value |
|-----------|------:|
| **Source Dataset** | Olist Brazilian E-Commerce Dataset |
| **Number of Source Files** | 9 CSV Files |
| **Final Dataset Size** | **118,434 Rows × 33 Columns** |
| **Primary Business Domain** | E-Commerce |
| **Analysis Period** | September 2016 – August 2018 |

---

## ETL Pipeline

The project follows a structured ETL (Extract, Transform, Load) pipeline that converts raw e-commerce transaction data into a clean, structured and analytics-ready dataset. Each stage of the workflow ensures data quality, consistency and efficient reporting, enabling accurate business analysis and interactive dashboard development.

### ETL Workflow

| Phase | Process | Tools Used |
|--------|---------|------------|
| **Extract** | Imported nine raw CSV datasets containing customer, order, product, payment, seller and review information. | Python, Pandas |
| **Transform** | Cleaned missing values, standardized column names and data types, merged related datasets, created new features and performed exploratory data analysis (EDA). | Python, Pandas, NumPy |
| **Load** | Loaded the processed dataset into PostgreSQL by creating relational tables and importing cleaned data. | PostgreSQL, pgAdmin 4 |
| **Analyze** | Developed SQL queries and analytical views to calculate KPIs and prepare datasets for business reporting. | SQL, PostgreSQL |
| **Visualize** | Connected PostgreSQL to Power BI, built the data model, created DAX measures and developed interactive dashboards. | Power BI, DAX |

### ETL Process Summary

1. Imported raw e-commerce datasets into Python.
2. Cleaned and preprocessed the data by handling missing values and correcting data formats.
3. Merged related datasets into a unified analytical dataset.
4. Performed exploratory data analysis (EDA) to validate data quality and identify business trends.
5. Loaded the processed dataset into PostgreSQL.
6. Created relational tables and analytical SQL views.
7. Connected PostgreSQL to Power BI.
8. Developed DAX measures, KPIs and interactive dashboards for business reporting.

---

## Database Design

A relational PostgreSQL database was designed to store the cleaned e-commerce data and support efficient analytical querying. The database structure enables data integrity, minimizes redundancy and provides a scalable foundation for business reporting and dashboard development.

The cleaned datasets were imported into PostgreSQL, where relational tables were created using primary and foreign key relationships. SQL queries and analytical views were then developed to prepare reporting datasets for Power BI.

### Database Components

| Component | Purpose |
|-----------|---------|
| **Raw Tables** | Store the cleaned transactional data imported from Python. |
| **Relational Tables** | Organize customer, order, product, seller and payment data using structured relationships. |
| **SQL Views** | Simplify complex business queries and prepare reporting datasets. |
| **Analytical Queries** | Calculate KPIs, revenue metrics, customer insights and sales trends. |
| **Reporting Layer** | Provide optimized datasets for Power BI dashboards. |

### Database Workflow

```text
Raw CSV Files
        │
        ▼
Python Data Cleaning
        │
        ▼
PostgreSQL Database
        │
        ▼
Relational Tables
        │
        ▼
SQL Views & Analytical Queries
        │
        ▼
Power BI Dashboards
```

### Key Database Features

- Designed a relational database schema for efficient data storage.
- Created normalized tables to reduce data redundancy.
- Established relationships between business entities using primary and foreign keys.
- Developed SQL views to simplify business reporting.
- Executed analytical SQL queries to calculate KPIs and business metrics.
- Connected PostgreSQL to Power BI for real-time querying and interactive dashboard development.

---

## Dashboard Overview

*Coming Soon*

---

## Key Business Insights

*Coming Soon*

---

## Repository Structure

*Coming Soon*

---

## Installation Guide

*Coming Soon*

---

## Future Enhancements

*Coming Soon*
