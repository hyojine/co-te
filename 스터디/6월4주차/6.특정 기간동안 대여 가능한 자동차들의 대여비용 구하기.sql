-- https://school.programmers.co.kr/learn/courses/30/lessons/157339

SELECT C.CAR_ID, C.CAR_TYPE, ROUND(30*C.DAILY_FEE*(100-CP.DISCOUNT_RATE)/100) AS FEE
FROM (SELECT CAR_ID, CAR_TYPE, DAILY_FEE FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE IN ('세단','SUV')) AS C
JOIN (SELECT CAR_TYPE, DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE ='30일 이상'AND CAR_TYPE IN ('SUV','세단')) AS CP
ON C.CAR_TYPE=CP.CAR_TYPE
WHERE C.CAR_ID IN (SELECT CAR_ID
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   GROUP BY CAR_ID
                   HAVING MAX(START_DATE) > '2022-11-30' OR MAX(END_DATE) <'2022-11-01')
AND ((30*C.DAILY_FEE*(100-CP.DISCOUNT_RATE)/100 >= 500000) AND (30*C.DAILY_FEE*(100-CP.DISCOUNT_RATE)/100 < 2000000))
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC
