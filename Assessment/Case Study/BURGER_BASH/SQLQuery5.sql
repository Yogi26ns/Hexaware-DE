-- How many Vegetarian and Meatlovers were ordered by each customer
SELECT 
  c.customer_id,
  b.burger_name,
  COUNT(*) AS order_count
FROM customer_orders c
JOIN burger_names b ON c.burger_id = b.burger_id
GROUP BY c.customer_id, b.burger_name
HAVING b.burger_name IN ('Vegetarian', 'Meatlovers');
