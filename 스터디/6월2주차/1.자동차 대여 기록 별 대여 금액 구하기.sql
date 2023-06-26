-- https://school.programmers.co.kr/learn/courses/30/lessons/151141

SELECT h.history_id, (round(c.daily_fee*h.days*(100-ifnull(p.discount_rate,'0%'))/100)) fee
from (select car_id, daily_fee, car_type from CAR_RENTAL_COMPANY_CAR where car_type='트럭') c
join (select history_id, car_id, (case when datediff(end_date,start_date)+1 < 7 then '7일 미만'
                                       when datediff(end_date,start_date)+1 between 7 and 29 then '7일 이상' 
                                       when datediff(end_date,start_date)+1 between 30 and 89 then '30일 이상'
                                       when datediff(end_date,start_date)+1 >= 90 then '90일 이상'
                                       end) as duration_type, datediff(end_date
,start_date)+1 as days from CAR_RENTAL_COMPANY_RENTAL_HISTORY) h
on c.car_id=h.car_id
left outer join (select car_type, duration_type, discount_rate from car_rental_company_discount_plan where car_type='트럭') p
on h.duration_type=p.duration_type
order by fee desc, h.history_id desc
