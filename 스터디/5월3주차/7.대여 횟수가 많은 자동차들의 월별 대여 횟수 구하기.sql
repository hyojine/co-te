-- https://school.programmers.co.kr/learn/courses/30/lessons/151139

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID 
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE MONTH(START_DATE) BETWEEN 8 AND 10
                 GROUP BY CAR_ID HAVING COUNT(*)>4)
GROUP BY MONTH, CAR_ID
HAVING MONTH BETWEEN 8 AND 10
ORDER BY MONTH ASC, CAR_ID DESC