#1
orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]

total_spend = {}
order_count = {}

for o in orders:
    c = o["customer"]
    total_spend[c] = total_spend.get(c, 0) + o["amount"]
    order_count[c] = order_count.get(c, 0) + 1

#2
top_customer = max(total_spend, key=total_spend.get)

#3
print(total_spend)
print(top_customer, total_spend[top_customer])
print(order_count)