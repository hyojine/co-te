-- https://leetcode.com/problems/biggest-single-number/submissions/

(select num
 from mynumbers
 group by num
 having count(num)=1
 order by num desc
 limit 1)
union
(select null
 from mynumbers
 where not exists (select num
                   from mynumbers
                   group by num
                   having count(num)=1
                   order by num desc
                   limit 1))
