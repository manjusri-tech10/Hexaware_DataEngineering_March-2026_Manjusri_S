from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task 1
def create_marks_file():
    with open('/tmp/student_marks.txt', 'w') as f:
        f.write("Math,80\n")
        f.write("Science,75\n")
        f.write("English,90\n")
        f.write("Python,95\n")

# Task 2
def read_marks_file():
    with open('/tmp/student_marks.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip())

# Task 3
def calculate_total():
    total = 0

    with open('/tmp/student_marks.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        mark = int(line.strip().split(',')[1])
        total += mark

    print(f"Total Marks = {total}")

    with open('/tmp/total.txt', 'w') as f:
        f.write(str(total))

# Bonus Task
def percentage_calculation():
    with open('/tmp/total.txt', 'r') as f:
        total = int(f.read())

    percentage = total / 4

    print(f"Percentage = {percentage}")

    with open('/tmp/percentage.txt', 'w') as f:
        f.write(str(percentage))

# Task 4
def generate_result():
    with open('/tmp/total.txt', 'r') as f:
        total = int(f.read())

    result = "PASS" if total >= 140 else "FAIL"

    with open('/tmp/result.txt', 'w') as f:
        f.write("Student Result Summary\n")
        f.write(f"Total Marks = {total}\n")
        f.write(f"Result = {result}\n")

# DAG Definition
with DAG(
    dag_id='student_marks_workflow',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='create_marks_file',
        python_callable=create_marks_file
    )

    task2 = PythonOperator(
        task_id='read_marks_file',
        python_callable=read_marks_file
    )

    task3 = PythonOperator(
        task_id='calculate_total',
        python_callable=calculate_total
    )

    task4 = PythonOperator(
        task_id='percentage_calculation',
        python_callable=percentage_calculation
    )

    task5 = PythonOperator(
        task_id='generate_result',
        python_callable=generate_result
    )

    # Dependencies
    task1 >> task2 >> task3 >> task4 >> task5