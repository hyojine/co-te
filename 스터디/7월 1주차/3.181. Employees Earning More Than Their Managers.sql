-- https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/986199313/

select e.name as employee
from employee e, employee ee
where e.managerid= ee.id and e.salary> ee.salary
