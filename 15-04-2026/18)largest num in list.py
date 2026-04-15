numbers = [5, 12, 3, 99, 47]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)