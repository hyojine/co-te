-- https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT car_type, count(*) as cars
from CAR_RENTAL_COMPANY_CAR
WHERE  OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
group by car_type
order by car_type
