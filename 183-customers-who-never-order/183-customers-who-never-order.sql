# Write your MySQL query statement below
select c.name as Customers
from Customers as c
where c.id not in (select o.customerid from Orders as o);