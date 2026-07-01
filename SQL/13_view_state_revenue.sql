CREATE VIEW vw_state_revenue AS
SELECT
    customer_state,
    ROUND(
        SUM(CAST(price AS NUMERIC)),
        2
    ) AS revenue
FROM ecommerce_master
GROUP BY customer_state;