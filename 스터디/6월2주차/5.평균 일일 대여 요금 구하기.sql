-- 평균 일일 대여 요금 구하기

SELECT round(sum(daily_fee)/count(car_id),0) average_fee
from car_rental_company_car
where car_type='suv'
