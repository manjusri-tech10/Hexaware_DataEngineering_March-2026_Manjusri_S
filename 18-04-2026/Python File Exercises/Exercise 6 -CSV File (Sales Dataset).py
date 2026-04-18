import csv
sales = []
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = int(row["price"])
        sales.append(row)

# 1
total_revenue = sum(item["quantity"] * item["price"] for item in sales)
print("Total Revenue:", total_revenue)

# 2
qty_per_product = {}
for item in sales:
    product = item["product"]
    qty_per_product[product] = qty_per_product.get(product, 0) + item["quantity"]

print("\nQuantity per product:")
for product, qty in qty_per_product.items():
    print(product, ":", qty)

# 3
revenue_per_product = {}
for item in sales:
    product = item["product"]
    revenue = item["quantity"] * item["price"]
    revenue_per_product[product] = revenue_per_product.get(product, 0) + revenue

top_product = max(revenue_per_product, key=revenue_per_product.get)
print("\nHighest Sales Product:", top_product)

# 4
print("\nRevenue per product:")
for product, revenue in revenue_per_product.items():
    print(product, ":", revenue)

# 5
print("\nProducts with revenue > 50000:")
for product, revenue in revenue_per_product.items():
    if revenue > 50000:
        print(product)

# Bonus Challenge Output
print("\nProduct Sales Summary")
for product in qty_per_product:
    print(f"{product} → Qty: {qty_per_product[product]} Revenue: {revenue_per_product[product]}")