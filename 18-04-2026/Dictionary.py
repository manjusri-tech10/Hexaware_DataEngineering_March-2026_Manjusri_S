# Dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])
print(student["course"])

# GET
print(student.get("name"))
print(student.get("course"))

# Add a New Pair
student["city"] = "Hyderabad"

print(student)