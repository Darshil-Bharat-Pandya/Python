# if-elif Statement in Python

# The if-elif statement is shortcut of if..else chain. While using if-elif statement at the end else block is added which is performed if none of the above if-elif statement is true.

# Syntax: if (condition): statement elif (condition): statement..else: statement

# In this example, the code uses an if-elif-else statement to evaluate the value of the variable letter. It prints a corresponding message based on whether letter is "B", "C", "A", or none of the specified values, demonstrating a sequential evaluation of conditions for controlled branching.

letter = input("\n Please Enter the letter: ") 

if letter == "A":
    print("\n The letter you entered is A.")
elif letter == "B":
    print("\n The letter you entered is B.")
elif letter == "C":
    print("\n The letter you entered is C.")
else: 
    print("\n The letter you entered is none from the A, B, and C.")   