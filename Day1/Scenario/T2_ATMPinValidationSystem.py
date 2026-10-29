# *Task 2 – ATM PIN Validation System* 
# Scenario 
# An ATM allows only 3 PIN attempts. 
# Requirements 
# Store the correct PIN as 1234. 
# Ask the user to enter the PIN. 
# If PIN is correct: 
# Display "Login Successful". 
# Display account balance. 
# If PIN is incorrect: 
# Display "Wrong PIN". 
# Allow only 3 attempts using a loop. 
# If all 3 attempts fail: 
# Display "Account Blocked". 
# Count and display total attempts used.

pin = "1234"
attempts = 0

while attempts < 3:
    user_pin = input("Enter PIN: ")
    if user_pin == pin:
        print("Login Successful")
        print("Account Balance: $1000")
        break
    else:
        print("Wrong PIN")
        attempts += 1

if attempts == 3:
    print("Account Blocked")

print("Total attempts used:", attempts)