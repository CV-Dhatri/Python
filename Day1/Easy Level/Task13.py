# Task 13 
# Validate mobile numbers and print valid/invalid. 

mobile_numbers = ["9876543210", "1234567890", "98765", "98765432101", "abcdefghij"]

for number in mobile_numbers:
    if len(number) == 10 and number.isdigit():
        print(f"Mobile number {number} is valid.")
    else:
        print(f"Mobile number {number} is invalid.")