# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number can be divided by the first number without remainder
if num1 != 0:
    result = int(num2 / num1)
    print(f"{num2} can be divided by {num1} {result} times without remainder.")
else:
    print("Division by zero is not allowed.")
