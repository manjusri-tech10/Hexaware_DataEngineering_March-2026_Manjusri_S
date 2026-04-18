#1
students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}
topper = max(students, key=students.get)
print(topper, students[topper])

#2
avg = sum(students.values()) / len(students)
print(avg)

#3
for name, marks in students.items():
    if marks > 85:
        print(name)