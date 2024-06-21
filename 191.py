# Python NOT Operator

# The Boolean NOT Operator works with a single boolean value. If the boolan value is True, then it will return the value as False and vice-versa.

# This code checks that if a is divisible by either 3 or 5, otherwise, it prints a message indicating that it is not.

a = 10

if not a:
    print("Boolean value is True.")

if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else: print("10 is divisible by either 3 or 5.")