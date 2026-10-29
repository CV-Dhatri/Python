# Task 16 
# Calculate bonus for employees based on salary. 

employees = [
    {"name": "Arjun", "salary": 50000},
    {"name": "Akshaya", "salary": 60000},
    {"name": "Bharadwaj", "salary": 70000},
    {"name": "Dhatri", "salary": 80000}
]

for employee in employees:
    if employee["salary"] > 60000:
        bonus = employee["salary"] * 0.10
    else:
        bonus = employee["salary"] * 0.05
    print(f"Employee: {employee['name']}, Salary: {employee['salary']}, Bonus: {bonus}")