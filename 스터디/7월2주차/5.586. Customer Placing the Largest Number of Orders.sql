-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

select customer_number
from orders
group by customer_number
having count(order_number) = (select max(a.cnt) from (select count(order_number) cnt from orders group by customer_number)a)
