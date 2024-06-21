a = int(input("\n Enter the value of a: "))
b = int(input("\n Enter the value of b: "))

if a > 0 and b > 0:
    print("\n Both the values of a and b are greater than 0.")
    
elif a > 0 and b < 0:
    print("\n The value of a is greater than 0, but the value of b is less than 0.")
    
elif a < 0 and b > 0:
    print("\n The value of a is less than 0, but the value of b is greater than 0.")

elif a < 0 and b < 0:
    print("\n Both the values of a and b are less than 0.")
    
else:
    print("\n Both the values of a and b ar equal to 0.")