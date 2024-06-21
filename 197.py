# If-elif-else Conditional Statements in Python.

# The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then final "else" statement will be executed.

letter = "A"

if letter == "B":
    print("letter is B")
    
elif letter == "C":
    print("letter is C")
    
elif letter == "A":
    print("letter is A")
    
else:
    print("letter isn't A, B or C")