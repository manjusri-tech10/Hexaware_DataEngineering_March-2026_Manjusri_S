#1
products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}
for item in products:
    products[item] = int(products[item] * 1.10)

#2
print(products)