-- https://school.programmers.co.kr/learn/courses/30/lessons/144856

SELECT a.author_id, a.author_name, b.category, sum(b.price*bs.sales) total_sales
from author a
join book b
on a.author_id= b.author_id
join book_sales bs
on b.book_id=bs.book_id
where bs.sales_date like '2022-01%'
group by a.author_id, b.category
order by a.author_id, b.category desc
