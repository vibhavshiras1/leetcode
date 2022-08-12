# Write your MySQL query statement
select u.name as name, ifnull(sum(r.distance),0) as travelled_distance
from Users u left join Rides r
on u.id=r.user_id
group by u.id
order by SUM(r.distance) DESC, u.name ASC