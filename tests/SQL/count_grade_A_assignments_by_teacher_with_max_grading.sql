-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) as GradeACount
FROM assignments
WHERE state = 'GRADED' AND grade = 'A'
GROUP BY teacher_id
ORDER BY GradeACount DESC
LIMIT 1;

