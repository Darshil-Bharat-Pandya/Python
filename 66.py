# Ternary Operator in Python

# The Python ternary operator determines if a condition is true or false and then returns the appropriate value in accordance with the result. The ternary operator is useful in cases where we need to assign a value to a variable based on a simple condition, and we want to keep our code more concise-all in just one line of code. It is particularyly handy when we want to avoid writing multiple lines for a simple if-else situation.

# Simple Method to Use the Ternary Operator

# Program to demonstrate conditional operator
a, b = 10, 20
# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)