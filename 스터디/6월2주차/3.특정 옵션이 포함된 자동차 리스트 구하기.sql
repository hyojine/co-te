-- https://school.programmers.co.kr/learn/courses/30/lessons/157343

SELECT car_id, car_type, daily_fee, options
from CAR_RENTAL_COMPANY_CAR
where options like '%네비게이션%' 
order by car_id desc
