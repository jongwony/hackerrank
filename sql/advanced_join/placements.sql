-- https://www.hackerrank.com/challenges/placements/problem
select s1.name
from Students s1
       join Friends f on s1.id = f.id
       join Packages p1 on p1.id = s1.id
       join Students s2 on s2.id = f.friend_id
       join Packages p2 on p2.id = f.friend_id
where p1.salary <= p2.salary
order by p2.salary;
