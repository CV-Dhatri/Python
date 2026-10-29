# *Task 1 – Student Management System* 
# Scenario 
# A school wants to maintain student results. 
# Requirements 
# Ask the user to enter the student name. 
# Ask the user to enter marks for 5 subjects using a loop. 
# Calculate the total marks. 
# Calculate the average marks. 
# Display: 
# Pass if average is 35 or above. 
# Fail if average is below 35. 
# Assign grade: 
# A → Average 90 and above 
# B → Average 75 to 89 
# C → Average 60 to 74 
# D → Average 35 to 59 
# F → Below 35 
# Ask the user whether they want to enter another student. 
# Continue until the user enters "No". 
# Display: 
# Total students processed 
# Total passed students 
# Total failed students 


marks = []
new_student = "Yes"
passed = 0
failed = 0
while new_student.lower() == "yes":
    name = input("Student name: ")
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total_marks = sum(marks)
    average_marks = total_marks / 5

    print(f"Total marks: {total_marks}")
    print(f"Average marks: {average_marks}")

    if average_marks >= 35:
        passed += 1
        print("Pass")
    else:
        failed += 1
        print("Fail")

    if average_marks >= 90:
        print("Grade: A")
    elif average_marks >= 75:
        print("Grade: B")
    elif average_marks >= 60:
        print("Grade: C")
    elif average_marks >= 35:
        print("Grade: D")
    else:
        print("Grade: F")

    new_student = input("Do you want to enter another student? (Yes/No): ")

print("Total students processed:", passed + failed) 
print("Total passed students:", passed) 
print("Total failed students:", failed) 
