-- https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD AS '진료과 코드', COUNT(PT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE MONTH(APNT_YMD)=05
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO), MCDP_CD