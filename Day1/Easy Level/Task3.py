# Task 3 
# Print only Gmail accounts from a list of emails. 

emails = ["wednesday@gmail.com", "enid@yahoo.com", "taylor@gmail.com", "mortishia@hotmail.com", "thing@gmail.com"]

for email in emails:
    if email.endswith("@gmail.com"):
        print(email)