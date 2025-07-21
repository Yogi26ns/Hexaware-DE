use burger_bash;

-- 1. For each customer, how many total burgers did they order?
select customer_id, count(*) as total_burgers_ordered 
from customer_orders group by customer_id;

-- 2. What is the average distance travelled by each runner?
select runner_id,avg(distance) as avg_distance_travelled
from runner_orders 
group by runner_id;

-- 3.  Find the minimum and maximum delivery time for each runner.
select runner_id,min(duration) as min_time,max(duration) as max_time 
from runner_orders where duration is not null
group by runner_id;

-- 4. Which menu item was ordered the most number of times?
select top 1 burger_id,count(*) as most_ordered
from customer_orders
group by burger_id
order by most_ordered desc;

-- 5. Find the average number of burgers ordered per customer, but only include customers who ordered more than 2 times.
select customer_id, count(*) as total_orders, avg(burger_id*1.0) as avg_order_value
from customer_orders
group by customer_id
having count(*) > 2;
