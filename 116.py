# Practice Question

# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("\nPlease Enter the Value of num1: "))
num2 = int(input("\nPlease Enter the Value of num2: "))
num3 = int(input("\nPlease Enter the Value of num3: "))

if (num1 > num2 and num1 > num3) :
    print("\nThe Greatest Number is num1.")
elif (num2 > num1 and num2 > num3) :
    print("\nThe Greatest Number is num2.")
else :
    print("\nThe Greatest Number is num3.")