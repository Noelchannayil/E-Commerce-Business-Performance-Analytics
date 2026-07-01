SELECT
ROUND(
    AVG(
        EXTRACT(
            DAY FROM
            (
                CAST(order_delivered_customer_date AS TIMESTAMP)
                -
                CAST(order_purchase_timestamp AS TIMESTAMP)
            )
        )
    ),
    2
) AS avg_delivery_days
FROM ecommerce_master
WHERE
order_delivered_customer_date IS NOT NULL;