# 3. Strong Number 
# Take input from the user. 
# Calculate the factorial of each digit. 
# Find the sum of the factorials of all digits. 
# Check whether the number is a Strong Number. 
# Display an appropriate message. 
# Example: 
# Input: 145 
# Output: 145 is a Strong Number

number = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
if sum_of_factorials == number:
    print(f"{number} is a Strong Number")
else:
    print(f"{number} is not a Strong Number")