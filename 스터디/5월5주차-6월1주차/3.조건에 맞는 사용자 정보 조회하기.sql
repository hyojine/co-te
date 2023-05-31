-- https://school.programmers.co.kr/learn/courses/30/lessons/164670

SELECT uu.user_id, uu.nickname, concat(uu.city,' ',uu.street_address1,' ',uu.street_address2) as '전체주소', concat(substr(uu.tlno,1,3),'-',substr(uu.tlno,4,4),'-',substr(uu.tlno,8,4)) as '전화번호'
from used_goods_user uu
join used_goods_board ub
on uu.user_id=ub.writer_id
group by uu.user_id
having count(ub.board_id)>=3
order by uu.user_id desc
