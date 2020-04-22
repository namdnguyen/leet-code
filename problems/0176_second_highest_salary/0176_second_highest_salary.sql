SELECT CASE WHEN salary IS NULL THEN NULL
       WHEN salary = max_salary.max_salary THEN NULL
       ELSE CAST(salary AS UNSIGNED) END AS SecondHighestSalary
  FROM employee,
       (SELECT MAX(salary) AS max_salary
          FROM employee) max_salary
 ORDER BY SecondHighestSalary DESC
 LIMIT 1
