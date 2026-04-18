import json
with open("students.json", "r") as file:
    data = json.load(file)

students = data["students"]

# 1
print("Student Names:")
for s in students:
    print(s["name"])

# 2
print("\nStudents in Python course:")
for s in students:
    if s["course"] == "Python":
        print(s["name"])

# 3
top_student = max(students, key=lambda x: x["marks"])
print("\nTop Student:", top_student["name"], "-", top_student["marks"])

# 4
avg_marks = sum(s["marks"] for s in students) / len(students)
print("\nAverage Marks:", avg_marks)

# 5
course_count = {}
for s in students:
    course = s["course"]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1

print("\nStudents per course:")
for course, count in course_count.items():
    print(course, ":", count)