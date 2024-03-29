-- https://school.programmers.co.kr/learn/courses/30/lessons/157339

SELECT C.CAR_ID, C.CAR_TYPE, FLOOR(30*C.DAILY_FEE*(100-DISCOUNT_RATE)/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
ON C.CAR_ID=CH.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CP
ON C.CAR_TYPE=CP.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단','SUV') 
AND 30*C.DAILY_FEE*(100-DISCOUNT_RATE)/100 BETWEEN 500000 AND 1999999
GROUP BY CAR_ID
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC

SELECT C.CAR_ID, C.CAR_TYPE, FLOOR(30*C.DAILY_FEE*(100-DISCOUNT_RATE)/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
ON C.CAR_ID=CH.CAR_ID
RIGHT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CP
ON C.CAR_TYPE=CP.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단','SUV')
AND CH.START_DATE <'2022-12-01' OR CH.END_DATE > '2022-11-01'
AND CP.DURATION_TYPE ='30일 이상'
AND (30*C.DAILY_FEE*(100-cp.DISCOUNT_RATE)/100 BETWEEN 500000 AND 2000000 )
AND (30*C.DAILY_FEE*(100-cp.DISCOUNT_RATE)/100 != 2000000)
GROUP BY C.CAR_ID
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC

