# Ternary Expression Conditional Statements in Python.

# The Python ternary Expression determines if a condition is true or false and then returns the appropriate value in accordance with the result. The ternary Expression is useful in cases where we need to assign a value to a variable based on a simple condition, and we want to keep our code more concise-all in just one line of code.

# Syntax of Ternary Expression
# [on_true] if [expression] else [on_false]
# expression: conditional_expression | lambda_expr

a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")