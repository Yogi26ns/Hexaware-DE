-- unique customer orders
SELECT COUNT(DISTINCT order_id) AS unique_orders
FROM customer_orders;
