# Python OR Operator

# The Boolean OR Operator will return True if any one of the Operand is True.

# This Code checks that if either "a" or "b" is greater than 0 and then prints the message corresponding  to it. Then it checks that if either "b" or "c" is greater than 0 and then prints the message according to it.

a = int(input("\n Please Enter the Value of a: "))
b = int(input("\n Please Enter the Value of b: "))

if a > 0 or b > 0:
    print("\n Either the Value of a or b is greater than 0.")
else: 
    print("\n Both the values of a and b are lesser than 0.")
