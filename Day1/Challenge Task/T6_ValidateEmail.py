# *Task 1* 
# Validate Email 
# Conditions 
# Username 
# @ 
# Domain 
# .com/.in/.org

email = input("Enter an email address: ")
def validate_email(email):
    if "@" not in email:
        return False
    username, domain = email.split("@", 1)
    if not username.isalnum():
        return False
    if "." not in domain:
        return False
    domain_name, extension = domain.rsplit(".", 1)
    if not domain_name.isalnum() or extension not in ["com", "in", "org"]:
        return False
    return True