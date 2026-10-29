# Task 30 
# Print only unique names from a list.


names = ["Dean", "Bobby", "Charlie", "Dean", "Sam", "Castiel", "Crowley", "Rowena", "Lucifer", "Sam", "Gabriel", "Michael"]

unique_names = list(set(names))
for name in unique_names:
    print(name)