# Input a binary number from the user
binary_number = input("Enter a binary number: ")

# Check if the input is a valid binary number
if not set(binary_number).issubset({'0', '1'}):
    print("Invalid input. Please enter a valid binary number (0s and 1s only).")
else:
    # Convert binary to decimal
    decimal_number = int(binary_number, 2)
    
    # Display the result
    print("Decimal equivalent:", decimal_number)