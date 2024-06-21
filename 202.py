# Nested If Statement with else Condition.

a = int(input("\n Enter the value of a: "))

if a != 0:
    if a > 0:
        print("\n The value of a is greater than 0.")
    if a < 0:
        print("\n The value of a is lesser than 0.")
else:
    print("\n The value of a is equal to zero.")