numbers = [5, 12, 3, 99, 47]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest:", smallest)