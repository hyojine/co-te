-- https://leetcode.com/problems/rising-temperature/description/

select w.id
from weather w, weather ww
where datediff(w.recordDate ,ww.recordDate )=1 and w.temperature > ww.temperature
