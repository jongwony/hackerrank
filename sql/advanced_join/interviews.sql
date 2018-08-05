-- https://www.hackerrank.com/challenges/interviews/problem
select C.contest_id, C.hacker_id, C.name, Q.TS, Q.TAS, Q.TV, Q.TUV
from Contests C
       join (select CT.contest_id,
                    IFNULL(sum(SS.total_submissions), 0)          TS,
                    IFNULL(sum(SS.total_accepted_submissions), 0) TAS,
                    IFNULL(sum(VS.total_views), 0)                TV,
                    IFNULL(sum(VS.total_unique_views), 0)         TUV
             from Contests CT
                    join Colleges CLG on CLG.contest_id = CT.contest_id
                    left join Challenges CHL on CHL.college_id = CLG.college_id
                    left join View_Stats VS on VS.challenge_id = CHL.challenge_id
                    left join Submission_Stats SS on SS.challenge_id = CHL.challenge_id
             group by CT.contest_id) Q on C.contest_id = Q.contest_id
where Q.TS + Q.TAS + Q.TV + Q.TUV > 0
