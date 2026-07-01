SELECT
ROUND(
(
    COUNT(
        CASE
            WHEN CAST(order_delivered_customer_date AS TIMESTAMP)
                 >
                 CAST(order_estimated_delivery_date AS TIMESTAMP)
            THEN 1
        END
    ) * 100.0
)
/
COUNT(*)
,2) AS late_delivery_percent
FROM ecommerce_master
WHERE order_delivered_customer_date IS NOT NULL;