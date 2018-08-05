-- https://www.hackerrank.com/challenges/projects/problem
select start_date, min(end_date)
from (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) a,
     (select end_date from projects where end_date not in (select start_date from projects)) b
where start_date < end_date
group by start_date
order by min(end_date) - start_date, start_date;
