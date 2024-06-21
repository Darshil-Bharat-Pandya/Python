division = lambda x, y: x / y if y != 0 else "Division by zero is undefined"

result = division(10, 2)
print(result)  # Output will be 5.0

result = division(10, 0)
print(result)  # Output will be "Division by zero is undefined"
