-- Write query to get number of assignments for each state
SELECT state, COUNT(*) AS assignmentCount FROM assignments 
GROUP BY state;
