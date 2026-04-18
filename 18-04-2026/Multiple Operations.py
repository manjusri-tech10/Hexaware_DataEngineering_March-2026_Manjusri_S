# Insert
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)

# Remove
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

# Remove Last Element
numbers.pop()
print(numbers)
print(len(numbers))

numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)

fruits = ["apple", "banana", "mango"]
if "banana" in fruits:
    print("Banana exists")