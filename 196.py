# Nested if..else Conditional Statements in Python.

# Nested if..else means an if-else statement inside another if statement. Or in simple words first, there is an outer if statement, and inside it another if-else statement is present and such type of statement is known as nested if statement.

# if..else chain statement
letter = "A"

if letter == "B":
    print("letter is B")

else:
    if letter == "C":
        print("letter is C")
    else: 
        
        if letter == "A":
           print("letter is A")
           
        else:
            print("letter isn't A, B and C") 