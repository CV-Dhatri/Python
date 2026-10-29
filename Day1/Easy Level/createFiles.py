import os

# Loop from 1 to 30
for i in range(1, 31):
    filename = f"Task{i}.py"
    # Create the file in write mode
    with open(filename, "w") as f:
        pass  # Leave the file empty
    print(f"Created: {filename}")
