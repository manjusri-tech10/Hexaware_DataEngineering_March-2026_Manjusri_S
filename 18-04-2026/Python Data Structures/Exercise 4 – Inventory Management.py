#1
inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}
inventory["monitor"] = 8

#2
inventory["laptop"] -= 2

#3
for item, stock in inventory.items():
    if stock < 10:
        print(item)