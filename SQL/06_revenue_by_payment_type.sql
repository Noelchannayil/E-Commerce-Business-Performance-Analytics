SELECT
    payment_type,
    ROUND(
        SUM(CAST(payment_value AS NUMERIC)),
        2
    ) AS revenue
FROM (
    SELECT DISTINCT
        order_id,
        payment_type,
        payment_value
    FROM ecommerce_master
) t
GROUP BY payment_type
ORDER BY revenue DESC;