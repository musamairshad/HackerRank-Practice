-- 1st Method:
select a.roll_number,a.name
from student_information a, examination_marks b
where a.roll_number = b.roll_number
group by b.roll_number
having sum(b.subject_one + b.subject_two + b.subject_three) < 100;


-- 2nd Method:
-- select a.roll_number,a.name
-- from student_information a
-- inner join examination_marks b
-- on a.roll_number = b.roll_number
-- group by b.roll_number
-- having sum(b.subject_one + b.subject_two + b.subject_three) < 100;
