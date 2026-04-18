#1
logins = [
("Rahul","10:00"),
("Sneha","10:10"),
("Rahul","11:00"),
("Arjun","11:15"),
("Sneha","11:30")
]
login_count = {}

#2
for user, _ in logins:
    login_count[user] = login_count.get(user, 0) + 1

print(login_count)