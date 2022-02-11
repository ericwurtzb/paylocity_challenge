-- 1. Write a SQL report that gives us the average salary for all employees
SELECT AVG(Salary) as AverageEmployeeSalary
FROM Employee


-- 2. Update previous query to give us the average salary for each company
SELECT c.Name as CompanyName, AVG(e.Salary) as AverageSalary
FROM Employee e
JOIN Company c on c.CompanyID = e.CompanyID
GROUP BY c.Name


-- 3. Let’s assume your previous query was long running how would you go about debugging 
-- it and finding the root causes of its sluggishness.

-- Possibly there's an indexing issue? If our partition - company `Name` - is not indexed then the query would run slower
-- I would delve into this by creating an index on company `Name` and see if that improves runtime

