CREATE VIEW vw_category_revenue AS
SELECT
    product_category_name,
    ROUND(
        SUM(CAST(price AS NUMERIC)),
        2
    ) AS revenue
FROM ecommerce_master
WHERE product_category_name IS NOT NULL
GROUP BY product_category_name
ORDER BY revenue DESC;