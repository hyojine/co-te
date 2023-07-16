-- https://leetcode.com/problems/customers-who-never-order/description/

select c.name as customers
from customers c
left outer join orders o
on c.id=o.customerid
where o.id is null
