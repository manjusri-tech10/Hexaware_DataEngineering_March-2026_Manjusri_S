import json
import csv
from collections import Counter

# Part 6 — Functions

# Task 23
def load_visits(file):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Task 24
def load_products(file):
    with open(file, "r") as f:
        data = json.load(f)
    product_dict = {}
    for p in data["products"]:
        product_dict[p["product_id"]] = {
            "name": p["name"],
            "price": p["price"]
        }
    return product_dict

# Task 25
def load_orders(file):
    orders = []
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            orders.append({
                "order_id": int(row["order_id"]),
                "customer": row["customer"],
                "product_id": int(row["product_id"]),
                "quantity": int(row["quantity"])
            })
    return orders

# Task 26
def calc_product_revenue(orders, products):
    revenue = {}
    for order in orders:
        name = products[order["product_id"]]["name"]
        price = products[order["product_id"]]["price"]
        revenue[name] = revenue.get(name, 0) + price * order["quantity"]
    return revenue

# Task 27
def calc_customer_spending(orders, products):
    spending = {}
    for order in orders:
        customer = order["customer"]
        price = products[order["product_id"]]["price"]
        spending[customer] = spending.get(customer, 0) + price * order["quantity"]
    return spending

# Task 28
def find_top_customer(spending):
    return max(spending, key=spending.get)


# Part 1 — Website Visit Analysis

# Task 1
visits = load_visits("website_visits.txt")

# Task 2
print("All Visitors:", visits)

# Task 3
print("Total Visits:", len(visits))

# Task 4
unique_visitors = set(visits)
print("Unique Visitors:", unique_visitors)

# Task 5
visit_count = dict(Counter(visits))
print("Visit Count:", visit_count)

# Task 6
most_frequent = max(visit_count, key=visit_count.get)
print("Most Frequent Visitor:", most_frequent)

# Part 2 — Product Catalog Analysis

# Task 7
products = load_products("products.json")

# Task 8
print("\nProduct Names and Prices:")
for pid, info in products.items():
    print(info["name"], "->", info["price"])

# Task 9
print("Product Dictionary:", products)

# Task 10
most_expensive = max(products.values(), key=lambda x: x["price"])
print("Most Expensive Product:", most_expensive["name"], "->", most_expensive["price"])

# Task 11
least_expensive = min(products.values(), key=lambda x: x["price"])
print("Least Expensive Product:", least_expensive["name"], "->", least_expensive["price"])

# Part 3 — Orders Analysis

# Task 12
orders = load_orders("orders.csv")

# Task 13
print("\nAll Orders:")
for order in orders:
    print(order)

# Task 14
qty_per_product = {}
for order in orders:
    name = products[order["product_id"]]["name"]
    qty_per_product[name] = qty_per_product.get(name, 0) + order["quantity"]
print("\nTotal Quantity Sold Per Product:", qty_per_product)

# Task 15
orders_per_customer = {}
for order in orders:
    customer = order["customer"]
    orders_per_customer[customer] = orders_per_customer.get(customer, 0) + 1
print("Total Orders Per Customer:", orders_per_customer)

# Part 4 — Sales Calculation

# Task 16
print("\nRevenue Per Order:")
for order in orders:
    name = products[order["product_id"]]["name"]
    price = products[order["product_id"]]["price"]
    revenue = price * order["quantity"]
    print(f"  Order {order['order_id']} ({order['customer']} - {name}) -> ₹{revenue}")

# Task 17
product_revenue = calc_product_revenue(orders, products)
total_revenue = sum(product_revenue.values())
print("\nTotal Revenue: ₹", total_revenue)

# Task 18
print("Total Revenue Per Product:", product_revenue)

# Task 19
top_product = max(product_revenue, key=product_revenue.get)
print("Highest Selling Product:", top_product, "->", product_revenue[top_product])

# Part 5 — Customer Analysis

# Task 20
customer_spending = calc_customer_spending(orders, products)
print("\nTotal Spending Per Customer:", customer_spending)

# Task 21
top_customer = find_top_customer(customer_spending)
print("Highest Spending Customer:", top_customer)

# Task 22
print("Customers Who Spent More Than ₹50,000:")
for customer, amount in customer_spending.items():
    if amount > 50000:
        print(" ", customer, "->", amount)

# Part 7 — Data Structures

# list → all orders
orders_list = orders

# dictionary → product prices
price_dict = {pid: info["price"] for pid, info in products.items()}

# set → unique visitors
unique_visitors_set = unique_visitors

# tuple → (product_name, revenue) pairs
revenue_tuples = tuple((name, rev) for name, rev in product_revenue.items())

print("\nRevenue Tuples:", revenue_tuples)

# Part 8 — Final Report
with open("sales_report.txt", "w") as f:
    f.write("E-Commerce Sales Report\n")
    f.write("=" * 40 + "\n")
    f.write(f"Total Website Visits: {len(visits)}\n")
    f.write(f"Unique Visitors: {len(unique_visitors)}\n")
    f.write(f"Total Revenue: {total_revenue}\n")
    f.write(f"Top Customer: {top_customer}\n")
    f.write("\nProduct Sales\n")
    for name, rev in product_revenue.items():
        f.write(f"{name} -> {rev}\n")

print("\nSales report written to sales_report.txt")

# Final Challenge

# Task 29 — Visitors who never ordered
customers_who_ordered = set(order["customer"] for order in orders)
never_ordered = unique_visitors - customers_who_ordered
print("\nVisitors Who Never Ordered:", never_ordered)

# Task 30 — Customers who ordered but visited only once
visited_once = set(name for name, count in visit_count.items() if count <= 1)
ordered_but_visited_once = customers_who_ordered & visited_once
print("Ordered But Visited Only Once:", ordered_but_visited_once)
