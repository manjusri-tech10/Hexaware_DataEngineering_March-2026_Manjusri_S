with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# 1
print("All numbers:", numbers)

# 2
print("Sum:", sum(numbers))

# 3
print("Maximum:", max(numbers))

# 4
print("Minimum:", min(numbers))

# 5
count = sum(1 for num in numbers if num > 50)
print("Numbers greater than 50:", count)