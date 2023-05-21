-- https://school.programmers.co.kr/learn/courses/30/lessons/151139

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, SUM(COUNT(*)) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE COUNT(MONTH(START_DATE) BETWEEN 8 AND 10)>4
GROUP BY CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC