import csv
employees = []
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["salary"] = int(row["salary"])  # convert salary to int
        employees.append(row)

# 1
print("Employee Names:")
for e in employees:
    print(e["name"])

# 2
print("\nEmployees in IT Department:")
for e in employees:
    if e["department"] == "IT":
        print(e["name"])

# 3
avg_salary = sum(e["salary"] for e in employees) / len(employees)
print("\nAverage Salary:", avg_salary)

# 4
top_emp = max(employees, key=lambda x: x["salary"])
print("\nHighest Salary Employee:", top_emp["name"], "-", top_emp["salary"])

# 5
dept_count = {}
for e in employees:
    dept = e["department"]
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

print("\nEmployees per Department:")
for dept, count in dept_count.items():
    print(dept, ":", count)