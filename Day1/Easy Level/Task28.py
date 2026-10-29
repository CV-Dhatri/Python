# Task 28 
# Replace spaces in file names with underscores. 

file_names = ["my file.txt", "your file.txt", "our file.txt"]

for i, file_name in enumerate(file_names):
    file_names[i] = file_name.replace(" ", "_")

print(file_names)