# SET
numbers = {10, 20, 30, 40}
print(numbers)

numbers = {10, 20, 20, 30, 40, 40}
print(numbers)

# List to Set
numbers = [10, 20, 20, 30, 40, 40]
unique_numbers = set(numbers)
print(unique_numbers)

# Add
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# Update
numbers = {10, 20}
numbers.update([30, 40, 50])
print(numbers)

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.union(set2)
print(result)

result = set1.difference(set2)
print(result)

result = set1.intersection(set2)
print(result)
