# *task 2* 
# Username Validation 
# Conditions 
# Starts with alphabet 
# Minimum 5 characters 
# Maximum 15 
# Only letters, numbers and underscore

username = input("Enter a username: ")
def validate_username(username):
    if not username[0].isalpha():
        return False
    if len(username) < 5 or len(username) > 15:
        return False
    if not all(char.isalnum() or char == "_" for char in username):
        return False
    return True