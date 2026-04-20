import json
import csv
from collections import Counter

# Part 6-Functions

# Task 26
def read_students(file):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Task 27
def load_marks(file):
    with open(file, "r") as f:
        return json.load(f)["students"]

# Task 28
def load_attendance(file):
    attendance = {}
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            attendance[row["name"]] = {
                "days_present": int(row["days_present"]),
                "total_days": int(row["total_days"])
            }
    return attendance

# Task 29
def calc_avg_marks(marks_list):
    return sum(marks_list) / len(marks_list)

# Task 30
def calc_attendance_percentage(days_present, total_days):
    return (days_present / total_days) * 100

# Task 31
def get_topper(students):
    return max(students, key=lambda x: x["marks"])

# Task 32
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# Part 1-File Handling

# Task 1
students = read_students("students.txt")
print("All Students:", students)

# Task 2
print("Total Entries:", len(students))

# Task 3
unique_students = set(students)
print("Unique Students:", unique_students)

# Task 4
count_dict = dict(Counter(students))
print("Count of Names:", count_dict)

# Task 5
with open("unique_students.txt", "w") as f:
    for name in unique_students:
        f.write(name + "\n")


# Part 2-JSON Handling

# Task 6
marks_data = load_marks("marks.json")

# Task 7
print("\nStudent Marks:")
for s in marks_data:
    print(s["name"], s["marks"])

# Task 8
topper = get_topper(marks_data)
print("Topper:", topper["name"])

# Task 9
lowest = min(marks_data, key=lambda x: x["marks"])
print("Lowest:", lowest["name"])

# Task 10
marks_list = [s["marks"] for s in marks_data]
avg_marks = calc_avg_marks(marks_list)
print("Average Marks:", round(avg_marks, 2))

# Task 11
print("\nPython Students:")
for s in marks_data:
    if s["course"] == "Python":
        print(s["name"])

# Task 12
course_count = {}
for s in marks_data:
    course = s["course"]
    course_count[course] = course_count.get(course, 0) + 1
print("Course Count:", course_count)


# Part 3-CSV Handling

# Task 13
attendance_data = load_attendance("attendance.csv")

# Task 14
print("\nAttendance Details:")
attendance_percent = {}
for name, data in attendance_data.items():
    percent = calc_attendance_percentage(
        data["days_present"], data["total_days"]
    )
    attendance_percent[name] = percent
    print(name, "->", round(percent, 2), "%")

# Task 15 -> already calculated above

# Task 16
print("\nBelow 80% Attendance:")
for name, percent in attendance_percent.items():
    if percent < 80:
        print(name)

# Task 17
best_attendance = max(attendance_percent, key=attendance_percent.get)
print("Best Attendance:", best_attendance)


# Part 4-Data Structures

# Task 18
print("\nMarks Analysis:")
print("Highest:", max(marks_list))
print("Lowest:", min(marks_list))
print("Sum:", sum(marks_list))

# Task 19
courses_tuple = tuple([s["course"] for s in marks_data])
print("Courses Tuple:", courses_tuple)

# Task 20
courses_set = set(courses_tuple)
print("Unique Courses:", courses_set)

# Task 21
marks_dict = {s["name"]: s["marks"] for s in marks_data}
print("Marks Dictionary:", marks_dict)

# Task 22
attendance_dict = {name: round(percent, 2) for name, percent in attendance_percent.items()}
print("Attendance Dictionary:", attendance_dict)


# Part 5-Conditions & Loops

# Task 23
print("\nPass/Fail:")
for name, mark in marks_dict.items():
    print(name, "->", "Pass" if mark >= 50 else "Fail")

# Task 24
print("\nGrades:")
grades = {}
for name, mark in marks_dict.items():
    grade = get_grade(mark)
    grades[name] = grade
    print(name, "->", grade)

# Task 25
print("\nHigh Performers (Marks >80 & Attendance >85):")
for name in marks_dict:
    if marks_dict[name] > 80 and attendance_percent[name] > 85:
        print(name)

# Part 7-Final Combined Analysis

# Task 33
final_data = {}
for s in marks_data:
    name = s["name"]
    final_data[name] = {
        "marks": s["marks"],
        "attendance": round(attendance_percent[name], 2),
        "course": s["course"],
        "grade": get_grade(s["marks"])
    }

# Task 34
print("\nFinal Report:")
for name, data in final_data.items():
    print(f"{name} - Marks: {data['marks']} - Attendance: {data['attendance']}% - Grade: {data['grade']}")

# Task 35 & 36
eligible = []
improvement = []

for name, data in final_data.items():
    if data["marks"] >= 75 and data["attendance"] >= 80:
        eligible.append(name)
    else:
        improvement.append(name)

print("\nEligible Students:", eligible)
print("Needs Improvement:", improvement)

# Part 8-Output File Generation

# Task 37
with open("report.txt", "w") as f:
    f.write("Student Report\n")
    for name, data in final_data.items():
        f.write(f"{name} - Marks: {data['marks']} - Attendance: {data['attendance']}% - Grade: {data['grade']}\n")

# Task 38
with open("eligible_students.txt", "w") as f:
    for name in eligible:
        f.write(name + "\n")

# Final Challenge

# Task 39
print("\n----- FINAL OUTPUT -----")
print("Topper:", topper["name"])
print("Best Attendance:", best_attendance)
print("Average Marks:", round(avg_marks, 2))
print("Eligible Students:", ", ".join(eligible))
print("Students Needing Improvement:", ", ".join(improvement))

# Task 40 →Code is modular using functions
