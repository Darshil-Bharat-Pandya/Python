# Define the number of rows
num_rows = 5

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Inner loop for columns
    for j in range(i):
        print(i, end=" ")
    print()  # Move to the next line after each row
