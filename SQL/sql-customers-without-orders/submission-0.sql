-- Write your query below
select name from

(
SELECT o.customer_id, c.name, o.id as order_id
FROM customers c left join orders o
on c.id = o.customer_id )
where order_id is null