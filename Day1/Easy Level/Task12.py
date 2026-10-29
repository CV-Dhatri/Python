# Task 12 
# Skip weekend days while processing calendar days. 

weekend_days = ["Saturday", "Sunday"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    if day in weekend_days:
        print(f"Skipping {day}.")
        continue
    print(f"Processing {day}.")