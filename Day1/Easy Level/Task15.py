# Task 15 
# Find all failed students (marks below 35). 

students = [
    {"name": "Arjun", "marks": 45},
    {"name": "Akshaya", "marks": 30},
    {"name": "Bharadwaj", "marks": 25},
    {"name": "Dhatri", "marks": 50}
]

failed_students = [student for student in students if student["marks"] < 35]

for student in failed_students:
    print(f"Student: {student['name']}, Marks: {student['marks']}")