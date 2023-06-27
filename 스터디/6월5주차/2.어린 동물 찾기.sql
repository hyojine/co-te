-- https://school.programmers.co.kr/learn/courses/30/lessons/59037

SELECT animal_id, name
from animal_ins
where intake_condition != 'Aged'
order by animal_id
