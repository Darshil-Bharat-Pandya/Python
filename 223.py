# Using else statement with While Loop in Python = The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won't be executed.

# Syntax:
# while condition:
#       execute these statements
# else:
#       execute these statements

# Example: The code prints "Hello Geek" three times using a "while" loop and then, after the loop, it prints "In Else Block" because there is an "else" block associated with the "while" loop. 

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geeks")
else: 
    print("In Else Block")