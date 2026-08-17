With filter_1 as (

select seller_id, 
case 
    when extract(year from sale_date) = '2020' then 1
    else 0
end as flag
from orders
),

filter_2 as (

select seller_id, sum(flag) as sum_flag
from filter_1
group by 1

),

filter_3 as (
select distinct seller_id from filter_2
where sum_flag = 0
)

select seller_name from seller
where seller_id in (select seller_id from filter_3)
