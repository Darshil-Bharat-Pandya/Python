# Initialize counters
positive_count = 0
zero_count = 0
negative_count = 0

# Infinite loop to read numbers until -1 is encountered
while True:
    try:
        # Read a number from the user
        num = int(input("Enter a number (-1 to quit): "))
        
        # Check if the number is -1 to exit the loop
        if num == -1:
            break
        
        # Count positive, zero, and negative numbers
        if num > 0:
            positive_count += 1
        elif num == 0:
            zero_count += 1
        else:
            negative_count += 1
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display the counts
print("Positive numbers:", positive_count)
print("Zeroes:", zero_count)
print("Negative numbers:", negative_count)
