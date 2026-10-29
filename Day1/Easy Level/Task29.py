# Task 29 
# Count how many Gmail accounts exist. 

emails = ["arjun@gmail.com", "yudishtira@yahoo.com", "bheema@gmail.com", "nakula@hotmail.com", "sahadeva@gmail.com"]

count = 0
for email in emails:
    if email.endswith("@gmail.com"):
        count += 1

print(f"Number of Gmail accounts: {count}")