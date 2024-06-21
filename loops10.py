# Define the number of rows
num_rows = 4

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Print leading spaces
    for j in range(num_rows - i):
        print(" ", end=" ")
    
    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print numbers in descending order (excluding 1)
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    # Move to the next line after each row
    print()
