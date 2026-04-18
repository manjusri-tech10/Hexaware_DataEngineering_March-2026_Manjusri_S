with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("data.txt", "r") as file:
    students = file.readlines()

print("Total students:", len(students))