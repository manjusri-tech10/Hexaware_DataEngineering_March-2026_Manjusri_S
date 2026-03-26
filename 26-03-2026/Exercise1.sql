CREATE DATABASE company_training;
USE company_training;
CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
city VARCHAR(50)
);
CREATE TABLE projects (
project_id INT PRIMARY KEY,
emp_id INT,
project_name VARCHAR(100),
project_budget DECIMAL(12,2),
project_status VARCHAR(50)
);
INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');
INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');

select e.emp_name, p.project_name, p.project_budget
from employees e inner join projects p on e.emp_id = p.emp_id;

select e.emp_name, p.project_name from employees e
left join projects p ON e.emp_id = p.emp_id;

select e.emp_name, p.project_name from employees e right join projects p on e.emp_id = p.emp_id;

select e.emp_name, p.project_name from employees e
left join projects p on e.emp_id = p.emp_id union
select e.emp_name, p.project_name from employees e
right join projects p on e.emp_id = p.emp_id;

select e.emp_name, p.project_name from employees e
cross join projects p;

select e.emp_name, e.department, p.project_name from employees e
inner join projects p on e.emp_id = p.emp_id where e.department = 'IT';

select project_name, project_budget from projects
where project_budget > 100000;

select e.emp_name, e.city, p.project_name from employees e 
left join projects p on e.emp_id = p.emp_id where e.city = 'Hyderabad';

select e.emp_name, count(p.project_id) as total_project from employees e
left join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name;

select e.emp_name, sum(p.project_budget) as total_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name;

select e.department, avg(p.project_budget) as avg_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.department;

select e.department, count(p.project_id) as total_project from employees e
left join projects p on e.emp_id = p.emp_id
group by e.department;

select e.department, sum(p.project_budget) as total_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.department;

select city, count(emp_id) as total_employees from employees
group by city;

select e.emp_name, count(p.project_id) as total_projects from employees e 
inner join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name having total_projects > 1;

select e.department, sum(p.project_budget) as total_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.department having total_budget> 150000;

select e.emp_name, sum(p.project_budget) as total_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name having total_budget > 100000;

select e.emp_name, e.department, sum(p.project_budget) as total_project_budget from employees e
inner join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name, e.department having total_project_budget > 100000
order by total_project_budget desc;













