-- https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT name, count(*) as name_freq
from animal_ins
group by name
having count(name)>1
order by name