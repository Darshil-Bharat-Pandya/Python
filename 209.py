# Ternary Operator in Nested if else

# Syntax: true_value if condition1 else (true_value if condition2 else false_value)

a = int(input("\n Enter the value of a: ")) 
b = int(input("\n Enter the value of b: "))

result = "\n a is maximum" if a > b else "\n b is maximum" if b > a else "\n a and b are having the equal values."

print(result)