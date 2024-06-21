# Input a number from the user
number = float(input("Enter a number: "))

# Check if the number is negative, positive, or zero
if number < 0:
    print(f"{number} is a negative number.")
elif number > 0:
    print(f"{number} is a positive number.")
else:
    print(f"{number} is equal to zero.")
