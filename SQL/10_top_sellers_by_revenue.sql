SELECT
    seller_id,
    ROUND(
        SUM(CAST(price AS NUMERIC)),
        2
    ) AS revenue
FROM ecommerce_master
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 10;