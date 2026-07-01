CREATE VIEW vw_kpi_summary AS
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_unique_id) AS total_customers,
    ROUND(SUM(CAST(price AS NUMERIC)),2) AS total_revenue,
    ROUND(
        SUM(CAST(price AS NUMERIC))
        /
        COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM ecommerce_master;