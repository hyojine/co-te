-- https://school.programmers.co.kr/learn/courses/30/lessons/151138

SELECT HISTORY_ID, CAR_ID, date_format(start_date,'%Y-%m-%d') START_DATE, 
date_format(end_date,'%Y-%m-%d') END_DATE,
if(DATEDIFF(end_date,start_date)+1>=30, '장기 대여','단기 대여') RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where year(start_date)= '2022' and month(start_date) = '09'
order by history_id desc
