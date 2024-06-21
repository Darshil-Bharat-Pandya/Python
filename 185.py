# Python Logical Operators.

# The Python Logical Operators are used to combine conditional statements, allowing you to perform operations based on multiple conditions. These Python Operators, alongside arithmetic operators, are special symbols which are used to carry out computations on values and variables.

# And Operator = It returns True if both the operands are true.
# Or Operator = It returns True if either of the operand is True.
# Not Operator = It Returns True if the operand is False.

# 1. AND Operator in Python.

a = int(input("\n Please Enter the Value of a: "))
b = int(input("\n Please Enter the Value of b: "))
c = int(input("\n Please Enter the Value of c: "))

if a > 0 and b > 0:
    print("\n The numbers are greater than 0.")
if a > 0 and b > 0 and c > 0:
    print("\n The numbers are greater than 0.")
else: 
    print("\n Atleast one number is not greater than 0.")