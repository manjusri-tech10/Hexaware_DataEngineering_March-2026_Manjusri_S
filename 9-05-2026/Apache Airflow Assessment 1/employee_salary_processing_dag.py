from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
def create_employee_file():
    data = """Rahul,45000
Sneha,52000
Amit,61000
Priya,47000
Kiran,39000"""

    with open('/tmp/employees.txt', 'w') as file:
        file.write(data)

    print("Employee file created successfully")
def read_employee_data():
    with open('/tmp/employees.txt', 'r') as file:
        records = file.readlines()

    print("Employee Records:")
    for record in records:
        print(record.strip())
def calculate_salary_expense(ti):
    total_salary = 0

    with open('/tmp/employees.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        name, salary = record.strip().split(',')
        total_salary += int(salary)

    print(f"Total Salary Expense = {total_salary}")

    ti.xcom_push(key='total_salary', value=total_salary)
def find_highest_salary():
    highest_salary = 0
    employee_name = ""

    with open('/tmp/employees.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        name, salary = record.strip().split(',')
        salary = int(salary)

        if salary > highest_salary:
            highest_salary = salary
            employee_name = name

    print(f"Highest Salary = {highest_salary}")
    print(f"Employee = {employee_name}")
def generate_salary_report(ti):
    total_salary = ti.xcom_pull(
        task_ids='calculate_salary_expense',
        key='total_salary'
    )

    report = f"""Employee Salary Report
Total Employees = 5
Total Salary Expense = {total_salary}
Status = Processed Successfully"""

    with open('/tmp/salary_report.txt', 'w') as file:
        file.write(report)

    print("Salary report generated successfully")
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1)
}

dag = DAG(
    dag_id='employee_salary_processing_dag',
    default_args=default_args,
    schedule=None,
    catchup=False
)
task1 = PythonOperator(
    task_id='create_employee_file',
    python_callable=create_employee_file,
    dag=dag
)

task2 = PythonOperator(
    task_id='read_employee_data',
    python_callable=read_employee_data,
    dag=dag
)

task3 = PythonOperator(
    task_id='calculate_salary_expense',
    python_callable=calculate_salary_expense,
    dag=dag
)

task4 = PythonOperator(
    task_id='find_highest_salary',
    python_callable=find_highest_salary,
    dag=dag
)

task5 = PythonOperator(
    task_id='generate_salary_report',
    python_callable=generate_salary_report,
    dag=dag
)

task1 >> task2 >> task3 >> task4 >> task5