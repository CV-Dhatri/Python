# Task 22 
# Convert all .txt files to .csv. 

file_names = ["data1.txt", "report2.txt", "summary3.txt", "notes4.txt"]

for file_name in file_names:
    csv_file_name = file_name.replace(".txt", ".csv")
    print(csv_file_name)