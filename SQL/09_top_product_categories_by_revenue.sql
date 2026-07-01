SELECT
    product_category_name,
    ROUND(
        SUM(CAST(price AS NUMERIC)),
        2
    ) AS revenue
FROM ecommerce_master
GROUP BY product_category_name
ORDER BY revenue DESC
LIMIT 10;