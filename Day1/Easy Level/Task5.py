# Task 5 
# Remove extra spaces from employee names before processing. 

employees = [" Rachel ", " Ross ", " Chandler ", " Monica ", " Joey ", " Phoebe "]

for employee in employees:
    cleaned_name = employee.strip() 
    print(cleaned_name)