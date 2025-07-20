CREATE TABLE runner_orders(
   order_id     INTEGER  NOT NULL PRIMARY KEY 
  ,runner_id    INTEGER  NOT NULL
  ,pickup_time  timestamp
  ,distance     VARCHAR(7)
  ,duration     VARCHAR(10)
  ,cancellation VARCHAR(23)
);

ALTER TABLE runner_orders
DROP COLUMN pickup_time;

ALTER TABLE runner_orders
ADD pickup_time DATETIME;

INSERT INTO runner_orders (
  order_id, runner_id, distance, duration, cancellation, pickup_time
) 
VALUES 
(1, 1, '20km', '32 minutes', NULL, '2021-01-01 18:15:34'),
(2, 1, '20km', '27 minutes', NULL, '2021-01-01 19:10:54'),
(3, 1, '13.4km', '20 mins', NULL, '2021-01-03 00:12:37'),
(4, 2, '23.4', '40', NULL, '2021-01-04 13:53:03'),
(5, 3, '10', '15', NULL, '2021-01-08 21:10:57'),
(6, 3, NULL, NULL, 'Restaurant Cancellation', NULL),
(7, 2, '25km', '25mins', NULL, '2021-01-08 21:30:45'),
(8, 2, '23.4 km', '15 minute', NULL, '2021-01-10 00:15:02'),
(9, 2, NULL, NULL, 'Customer Cancellation', NULL),
(10, 1, '10km', '10minutes', NULL, '2021-01-11 18:50:20');