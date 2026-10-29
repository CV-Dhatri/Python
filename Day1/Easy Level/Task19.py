# Task 19 
# Count vowels in each employee name. 

employee_names = ["Arjun", "Akshaya", "Bharadwaj", "Dhatri"]

for name in employee_names:
    vowel_count = sum(1 for char in name if char.lower() in "aeiou")
    print(f"Employee: {name}, Vowels: {vowel_count}")