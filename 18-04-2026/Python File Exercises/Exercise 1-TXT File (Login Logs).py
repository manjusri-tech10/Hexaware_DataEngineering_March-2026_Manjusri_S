with open("logins.txt", "r") as file:
    logins = file.read().splitlines()
# 1
print("All login names:")
for name in logins:
    print(name)
# 2
print("\nTotal login records:", len(logins))

# 3
login_count = {}
for name in logins:
    if name in login_count:
        login_count[name] += 1
    else:
        login_count[name] = 1

print("\nLogin count per user:")
for user, count in login_count.items():
    print(user, ":", count)

# 4
max_user = max(login_count, key=login_count.get)
print("\nUser with highest logins:", max_user)

# 5
unique_users = set(logins)
print("\nUnique users:", unique_users)