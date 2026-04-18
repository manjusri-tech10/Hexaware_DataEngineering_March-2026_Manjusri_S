total = 0

with open("data.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print("Total =", total)