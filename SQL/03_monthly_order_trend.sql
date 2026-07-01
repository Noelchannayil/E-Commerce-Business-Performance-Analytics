SELECT
    TO_CHAR(
        CAST(order_purchase_timestamp AS TIMESTAMP),
        'YYYY-MM'
    ) AS order_month,
    COUNT(DISTINCT order_id) AS total_orders
FROM ecommerce_master
GROUP BY order_month
ORDER BY order_month;