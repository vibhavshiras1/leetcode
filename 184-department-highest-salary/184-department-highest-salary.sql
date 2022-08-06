# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary
from Employee as e, Department as d
where e.departmentid=d.id
and e.salary = (select max(salary) from Employee where departmentId=e.departmentId group by departmentId);