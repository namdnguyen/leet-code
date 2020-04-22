# Problem 176 - Second Highest Salary

https://leetcode.com/problems/second-highest-salary/

## Instructions

Write a SQL query to get the second highest salary from the Employee table.

### SQL Schema

```
+----|--------+
| Id | Salary |
+----|--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----|--------+
```

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

## Solution

Query using MySQL flavored SQL.

```sql
SELECT CASE WHEN salary IS NULL THEN NULL
       WHEN salary = max_salary.max_salary THEN NULL
       ELSE CAST(salary AS UNSIGNED) END AS SecondHighestSalary
  FROM employee,
       (SELECT MAX(salary) AS max_salary
          FROM employee) max_salary
 ORDER BY SecondHighestSalary DESC
 LIMIT 1
```
