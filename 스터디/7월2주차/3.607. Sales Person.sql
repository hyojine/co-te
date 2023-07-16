-- https://leetcode.com/problems/sales-person/submissions/

select name from salesperson 
where name not in ( select s.name
                    from salesperson s
                    join orders o
                    on s.sales_id=o.sales_id
                    join company c 
                    on o.com_id=c.com_id
                    where c.name = 'RED')
