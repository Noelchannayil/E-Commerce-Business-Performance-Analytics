# Database Design

## Overview

This folder contains the database schema and Entity Relationship Diagram (ERD) used in the **E-Commerce Business Performance Analytics** project.

The database was designed in PostgreSQL to support efficient querying, business analysis and dashboard reporting.

---

## Database Diagram

**File**

```
er_diagram.png
```

---

## Database Tables

The analytical database consists of the following primary datasets:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Product Category Translation

These tables are integrated into a unified analytical dataset for reporting.

---

## Database Relationships

The relational model connects datasets using the following keys:

| Primary Table | Related Table | Key |
|--------------|---------------|-----|
| Customers | Orders | customer_id |
| Orders | Payments | order_id |
| Orders | Order Items | order_id |
| Order Items | Products | product_id |
| Order Items | Sellers | seller_id |

---

## SQL Views

Several reusable SQL views were created to simplify reporting, including:

- KPI Summary
- Monthly Revenue
- State Revenue
- Category Revenue

These views were directly connected to Power BI for visualization.

---

## Purpose

The database design provides a structured foundation for analytical reporting by maintaining relationships between transactional datasets and enabling efficient SQL-based business analysis.
