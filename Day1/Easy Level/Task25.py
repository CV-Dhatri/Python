# Task 25 
# Find usernames containing special characters. 

usernames = ["user1", "user2", "user_3", "user-4", "user5"]

for username in usernames:
    if not username.isalnum():
        print(f"Username '{username}' contains special characters.")
        