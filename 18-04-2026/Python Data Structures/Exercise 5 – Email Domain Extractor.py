#1
emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]
domains = [email.split("@")[1] for email in emails]

#2
domain_count = {}
for d in domains:
    domain_count[d] = domain_count.get(d, 0) + 1

print(domain_count)