# Task 11 
# Stop processing when an empty student name is found. 

students = [
    {"name": "Arjun", "marks": 45},
    {"name": "Akshaya", "marks": 30},
    {"name": "Bharadwaj", "marks": 25},
    {"name": "", "marks": 50}  
]

for student in students:
    if student["name"] == "":
        print("Found an empty student name. Stopped processing.")
        break
    print(f"Student: {student['name']}, Marks: {student['marks']}")