SELECT
    customer_city,
    ROUND(
        SUM(CAST(payment_value AS NUMERIC)),
        2
    ) AS revenue
FROM (
    SELECT DISTINCT
        order_id,
        customer_city,
        payment_value
    FROM ecommerce_master
    WHERE customer_city IS NOT NULL
) t
GROUP BY customer_city
ORDER BY revenue DESC
LIMIT 10;