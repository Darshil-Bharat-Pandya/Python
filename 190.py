# This code checks that if any of the variables a, b, or c has a boolean value as True. If the any of them has the boolean value True, then it will print that "At least one number has a boolean value as True". Otherwise it will print that "All the numbers have the boolean value as False".

a = int(input("\n Please Enter the Value of a: "))
b = int(input("\n Please Enter the Value of b: "))
c = int(input("\n Please Enter the Value of c: "))

if a or b or c == 0:
    print("\n At least one number has a boolean value as True.")
else: 
    print("\n All the numbers have the boolean value as False.")