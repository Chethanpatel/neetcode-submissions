-- Write your query below

select customer_id 
from (
   select customer_id, year, sum(revenue) as revenue_impact
   from customers
   group by 1,2 
)
where revenue_impact > 0 and year = 2020