-- Write your query below
select name from
(
select o.customer_id, c.name, o.id as order_id
from customers c left join orders o
on c.id = o.customer_id )
where order_id is null