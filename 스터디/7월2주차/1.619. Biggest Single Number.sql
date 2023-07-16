-- https://leetcode.com/problems/biggest-single-number/submissions/

-- not exists & union 사용 -> not exists이하의 쿼리의 값이 없을 때 의도한 값을 출력함
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

-- 집계함수 사용 -> 서브쿼리에서 하나만 뽑았으므로 avg, min 등 모두 가능
select max(num) num
from (select num
      from mynumbers
      group by num
      having count(num)=1
      order by num desc
      limit 1) a

-- 집계함수 사용(2) -> 어차피 밖에서 max를 뽑을 거라면 order by, limit 필요 없음
select max(num) num
from (select num
      from mynumbers
      group by num
      having count(num)=1) a
