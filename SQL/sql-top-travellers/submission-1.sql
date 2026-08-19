-- Write your query below

select name, COALESCE(sum(distance), 0) as travelled_distance
from  users u left join rides r on u.id = r.user_id
group by u.id, name
order by 2 desc, 1 asc