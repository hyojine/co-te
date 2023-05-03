-- https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT i.ingredient_type, sum(f.total_order) as total_order
from first_half f
join icecream_info i
where f.flavor=i.flavor
group by i.ingredient_type