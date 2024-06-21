# Multiple IF Statements in Python.

# Syntax: 
# if (condition1):
#   # It will execute when the condition is True.
#   # if (condition2):
#       # It will execute when the condition is True.

a = int(input("\n Enter the value of a: "))

if a != 0:
    if a > 0:
        print("\n The value of a is Positive.")   
    if a < 0:
        print("\n The value of a is Negative.")
