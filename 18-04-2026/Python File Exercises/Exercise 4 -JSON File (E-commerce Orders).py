import json
with open("orders.json", "r") as file:
    data = json.load(file)

orders = data["orders"]

# 1
print("All Orders:")
for o in orders:
    print(o)

# 2
total_revenue = sum(o["amount"] for o in orders)
print("\nTotal Revenue:", total_revenue)

# 3
spending = {}
for o in orders:
    customer = o["customer"]
    if customer in spending:
        spending[customer] += o["amount"]
    else:
        spending[customer] = o["amount"]

print("\nTotal Spending per Customer:")
for customer, amount in spending.items():
    print(customer, ":", amount)

# 4
top_customer = max(spending, key=spending.get)
print("\nHighest Spending Customer:", top_customer)

# 5
order_count = {}
for o in orders:
    customer = o["customer"]
    if customer in order_count:
        order_count[customer] += 1
    else:
        order_count[customer] = 1

print("\nTotal Orders per Customer:")
for customer, count in order_count.items():
    print(customer, ":", count)