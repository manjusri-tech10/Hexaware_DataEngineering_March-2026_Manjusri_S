# Tuple
numbers = (10, 20, 30, 40)
print(numbers)

fruits = ("apple", "banana", "mango")
print(fruits[0])
print(fruits[2])

fruits = ("apple", "banana", "mango")
print(fruits[-1])
print(fruits[-2])

numbers = (10, 20, 30, 40, 50)
print(len(numbers))

numbers = (10, 20, 30, 40)
for n in numbers:
    print(n)

numbers = (10, 20, 30)
# Cannot happen because Tuples are immutable
numbers[1] = 200
