# Write your MySQL query statement below
select employee_id from Employees e where salary <30000 and manager_id not in
(select employee_id from Employees)
order by e.employee_id