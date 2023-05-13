-- https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT hour(datetime) as HOUR, count(animal_id) as COUNT
from animal_outs
group by hour
having hour between 9 and 19
order by hour