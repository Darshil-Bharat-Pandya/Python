# This code checks that if all the veriables a, b, and c evaluate to True, then it will print the message according to it.

a = int(input("\n Please Enter the Value of a: "))
b = int(input("\n Please Enter the Value of b: "))
c = int(input("\n Please Enter the Value of c: "))

if a and b and c != 0:
    print("\n All the Values are True. ")
else: 
    print("\n At least one Value is False.")