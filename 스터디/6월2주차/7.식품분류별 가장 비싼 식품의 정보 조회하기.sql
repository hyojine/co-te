-- https://school.programmers.co.kr/learn/courses/30/lessons/131116

SELECT CATEGORY, MAX(PRICE) MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자','국','김치','식용유')
GROUP BY CATEGORY
ORDER BY PRICE DESC
