CREATE VIEW vw_monthly_revenue AS
SELECT
    TO_CHAR(
        CAST(order_purchase_timestamp AS TIMESTAMP),
        'YYYY-MM'
    ) AS order_month,
    ROUND(
        SUM(CAST(price AS NUMERIC)),
        2
    ) AS revenue
FROM ecommerce_master
GROUP BY order_month
ORDER BY order_month;