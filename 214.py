# Ternary Operator using Python Lambda

# Syntax: (lambda: false_value, lambda; true_value) [condition] ()

a = 10
b = 20

print((lambda: "b is minimum", lambda: "a is minimum")[a < b]())