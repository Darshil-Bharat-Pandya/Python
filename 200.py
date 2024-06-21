# Nested-if statement in Python.

# In Python a Nested if statement, we can have an if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming. Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting.

# We can use a simple Python if statement inside another if or if...else statement. It can be used to check multiple if statements. In this case, an if condition is present inside another if conditions. We can have multiple if conditions inside an if condition. The inner if condition will only be executed if and only if the outer if condition is True.

# Syntax
# If(condition):
# {
#   // if body
#   // Statements to execute if condition is true.  
# }

a = int(input("\n Please Enter the value of a: "))

if a > 10:
    print("\n The value of a is greater than 10.")
    
if a == 10:
    print("\n The value of a is equal to 10.")

if a < 10:
    print("\n The value of a is lesser than 10.")