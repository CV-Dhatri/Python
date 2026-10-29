# 1. Palindrome Number 
# Take input from the user. 
# Check whether the given number is a palindrome or not. 
# Display an appropriate message. 
# Example: 
# Input: 121 
# Output: 121 is a Palindrome Number


number = int(input("Enter a number: "))
number_str = str(number)
if number_str == number_str[::-1]:
    print(f"{number} is a Palindrome Number")
else:
    print(f"{number} is not a Palindrome Number")
