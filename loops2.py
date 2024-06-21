def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the total is equal to the original number
    return total == number

# Input from the user
try:
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    
    if is_armstrong_number(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
