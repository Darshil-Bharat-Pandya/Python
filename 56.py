# Ternary Operator in Python

# It determines that if a condition is true or false and then returns the appropriate value in accordance with the result. The ternary operator is useful in cases where we need to assign a value to a variable based on a simple condition, and we want to keep our code more concise-all in just one line of code.

# x, y = 26, 35
# min = x if x<y else y
# print(min) 

num = int(input("Please Enter the Number: "))
even = "Yes" if (num % 2 == 0) else "No"
print(even)