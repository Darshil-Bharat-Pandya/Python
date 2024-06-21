# The code initializes variables a, b, and c and then checks that if a and b are greater than 0, if they are greater than 0, then it will print that "The Numbers are greater than 0". It also checks that if all the three variables are greater than 0, then it will print the same message. Otherwise, it print that "At least one number is not greater than 0." 

a = float(input("\n Please Enter the Value of a: "))
b = float(input("\n Please Enter the Value of b: "))
c = float(input("\n Please Enter the Value of c: "))

if a > 0 and b > 0:
    print("\n All the Values are Greater than 0.")
if a > 0 and b > 0 and c > 0:
    print("\n All the Values are Greater than 0.")
else: 
    print("\n At least one value is not Greater than 0.")
    
print("\n")