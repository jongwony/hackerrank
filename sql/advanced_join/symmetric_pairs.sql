-- https://www.hackerrank.com/challenges/symmetric-pairs/problem
select f1.x, f1.y from Functions f1
join Functions f2
on f1.x = f2.y and f1.y = f2.x
group by f1.x, f1.y
having count(*) > 1 or f1.x < f1.y;
