SELECT
customer_state,
ROUND(
    SUM(CAST(payment_value AS NUMERIC)),
    2
) AS revenue
FROM (
    SELECT DISTINCT
        order_id,
        customer_state,
        payment_value
    FROM ecommerce_master
) t
GROUP BY customer_state
ORDER BY revenue DESC
LIMIT 10;