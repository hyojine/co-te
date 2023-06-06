-- https://school.programmers.co.kr/learn/courses/30/lessons/151138

SELECT history_id, car_id, date_format(start_date,'%Y-%m-%d') start_date, 
date_format(end_date,'%Y-%m-%d') end_date, if(end_date-start_date>=30, '장기 대여','단기 대여') rent_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) = 9
order by history_id desc
