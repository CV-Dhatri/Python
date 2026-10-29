# Task 14 
# Print employees whose salary is greater than ₹50,000. 

employees = [
    {"name": "Arjun", "salary": 50000},
    {"name": "Akshaya", "salary": 60000},
    {"name": "Bharadwaj", "salary": 70000},
    {"name": "Dhatri", "salary": 80000}
]

for employee in employees:
    if employee["salary"] > 50000:
        print(f"Employee: {employee['name']}, Salary: {employee['salary']}")