#1
sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]
total_sales = {}

for item in sales:
    p = item["product"]
    total_sales[p] = total_sales.get(p, 0) + item["qty"]

#2
top_product = max(total_sales, key=total_sales.get)
print(total_sales)
print(top_product, total_sales[top_product])