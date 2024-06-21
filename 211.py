# Ternary Operator using Python Tuple

# The ternary operator can also be written by using Python tuples. In this case we declare the False and True values inside a tuple at index 0 and 1 respectively. Based on the condition, if the result is False, that is 0 the value at index 0 gets executed. If the condition results in True, the value at index 1 of the tuple is executed.

# Syntax: (false_value, true_value) [condition]

# Program to demonstrate ternary operator.
a = 10
b = 20

# Python ternary operator using tuple.
print(("b is minimum", "a is minimum") [a < b])