-- https://school.programmers.co.kr/learn/courses/30/lessons/131113#

SELECT order_id, product_id, date_format(out_date,'%Y-%m-%d'),
case
when out_date<'2022-05-02' then '출고완료'
when out_date is null then '출고미정'
else '출고대기'
end as 출고여부
from food_order
order by order_id
