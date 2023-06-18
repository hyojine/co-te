-- https://school.programmers.co.kr/learn/courses/30/lessons/131116

SELECT CATEGORY, MAX(PRICE) MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY IN ('과자','국','김치','식용유') and price in (select max(price) from food_product group by category)
GROUP BY CATEGORY 
ORDER BY max_PRICE DESC
