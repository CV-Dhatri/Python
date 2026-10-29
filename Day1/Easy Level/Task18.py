# Task 18 
# Find duplicate values in a list. 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

duplicates = set()
for item in list1:
    if list1.count(item) > 1:
        duplicates.add(item)

print(duplicates)