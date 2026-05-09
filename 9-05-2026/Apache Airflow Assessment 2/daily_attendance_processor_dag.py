from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
def create_attendance_file():
    data = """Aarav,Present
Priya,Present
Rahul,Absent
Sneha,Present
Kiran,Absent
Ananya,Present
Vikram,Present
Meera,Absent
Farhan,Present
Divya,Present"""

    with open('/tmp/attendance.txt', 'w') as file:
        file.write(data)

    print("Attendance file created successfully")
def read_attendance_file():
    with open('/tmp/attendance.txt', 'r') as file:
        records = file.readlines()

    print("Attendance Records:")
    for record in records:
        print(record.strip())

def count_total_students(ti):
    with open('/tmp/attendance.txt', 'r') as file:
        records = file.readlines()

    total_students = len(records)

    print(f"Total Students = {total_students}")

    ti.xcom_push(key='total_students', value=total_students)

def count_present_students(ti):
    present_count = 0

    with open('/tmp/attendance.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        name, status = record.strip().split(',')

        if status == "Present":
            present_count += 1

    print(f"Present Students = {present_count}")

    ti.xcom_push(key='present_students', value=present_count)
def count_absent_students(ti):
    absent_count = 0

    with open('/tmp/attendance.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        name, status = record.strip().split(',')

        if status == "Absent":
            absent_count += 1

    print(f"Absent Students = {absent_count}")

    ti.xcom_push(key='absent_students', value=absent_count)
def calculate_attendance_percentage(ti):
    total_students = ti.xcom_pull(
        task_ids='count_total_students',
        key='total_students'
    )

    present_students = ti.xcom_pull(
        task_ids='count_present_students',
        key='present_students'
    )

    percentage = (present_students / total_students) * 100

    print(f"Attendance Percentage = {percentage}%")

    ti.xcom_push(key='attendance_percentage', value=percentage)
def list_absent_students():
    print("Absent Students List")

    with open('/tmp/attendance.txt', 'r') as file:
        records = file.readlines()

    for record in records:
        name, status = record.strip().split(',')

        if status == "Absent":
            print(name)
def generate_attendance_report(ti):

    total_students = ti.xcom_pull(
        task_ids='count_total_students',
        key='total_students'
    )

    present_students = ti.xcom_pull(
        task_ids='count_present_students',
        key='present_students'
    )

    absent_students = ti.xcom_pull(
        task_ids='count_absent_students',
        key='absent_students'
    )

    percentage = ti.xcom_pull(
        task_ids='calculate_attendance_percentage',
        key='attendance_percentage'
    )

    if percentage >= 75:
        status = "Good"
    else:
        status = "Needs Improvement"

    report = f"""Daily Attendance Report
Total Students = {total_students}
Present Students = {present_students}
Absent Students = {absent_students}
Attendance Percentage = {percentage}%
Status = {status}"""

    with open('/tmp/attendance_report.txt', 'w') as file:
        file.write(report)

    print("Attendance report generated successfully")
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1)
}

dag = DAG(
    dag_id='daily_attendance_processor_dag',
    default_args=default_args,
    schedule=None,
    catchup=False
)

task1 = PythonOperator(
    task_id='create_attendance_file',
    python_callable=create_attendance_file,
    dag=dag
)

task2 = PythonOperator(
    task_id='read_attendance_file',
    python_callable=read_attendance_file,
    dag=dag
)

task3 = PythonOperator(
    task_id='count_total_students',
    python_callable=count_total_students,
    dag=dag
)

task4 = PythonOperator(
    task_id='count_present_students',
    python_callable=count_present_students,
    dag=dag
)

task5 = PythonOperator(
    task_id='count_absent_students',
    python_callable=count_absent_students,
    dag=dag
)

task6 = PythonOperator(
    task_id='calculate_attendance_percentage',
    python_callable=calculate_attendance_percentage,
    dag=dag
)

task7 = PythonOperator(
    task_id='list_absent_students',
    python_callable=list_absent_students,
    dag=dag
)

task8 = PythonOperator(
    task_id='generate_attendance_report',
    python_callable=generate_attendance_report,
    dag=dag
)

task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7 >> task8