-- https://school.programmers.co.kr/learn/courses/30/lessons/131537


SELECT date_format(tbl.SALES_DATE,'%Y-%m-%d') sales_date, tbl.product_id, ifnull(user_id,null), sum(tbl.sales_amount) sales_amount
FROM (select * from ONLINE_SALE
      where date_format(SALES_DATE,'%Y-%m')='2022-03' 
      union
      select OFFLINE_SALE_ID, null as user_id, PRODUCT_ID, SALES_AMOUNT, SALES_DATE from OFFLINE_SALE 
      WHERE date_format(SALES_DATE,'%Y-%m')='2022-03') tbl
group by tbl.sales_date, tbl.product_id, tbl.user_id
order by tbl.sales_date, tbl.product_id, tbl.user_id
