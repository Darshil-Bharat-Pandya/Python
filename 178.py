# Type Casting in Python 

# It is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.

# There can be two types of Type Cating in Python:

# 1. Python Implicit Type Conversion
# 2. Python Explicit Type Conversion

# 1. Implicit Type Conversion in Python
# In this method, Python converts the datatype into another datatype automatically. Users don't have to involve in this process.

# Python Program.

# Python automatically converts a to int.
a = int(input("\nPlease Enter the Value of a: "))
print(type(a))

# Python automatically converts b to float.
b = float(input("Please Enter the Value of b: "))
print(type(b))

# Python automatically converts c to float as it is a float addition.
c = a + b
print("The addition of ", a, "and", b, "is", c)
print(type(c))

# Python automatically converts d to float as it is a float multiplication.
d = a * b
print("The multiplication of ", a, "and", b, "is", d)
print(type(d))

print("\n")