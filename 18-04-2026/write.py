with open("data.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Sneha\n")
    file.write("Arjun\n")

# append
with open("data.txt", "a") as file:
    file.write("Priya\n")

# write lines
languages = ["Python\n", "Java\n", "C++\n"]

with open("data.txt", "w") as file:
    file.writelines(languages)