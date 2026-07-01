SELECT
    COUNT(*) AS repeat_customers
FROM
(
    SELECT
        customer_unique_id,
        COUNT(DISTINCT order_id) AS orders
    FROM ecommerce_master
    GROUP BY customer_unique_id
    HAVING COUNT(DISTINCT order_id) > 1
) t;