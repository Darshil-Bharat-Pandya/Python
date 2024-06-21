# Can we use "else" clause for loops ? = Unlike languages like C, CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If a break statement is executed inside the for loop then the "else" part is skipped. Note that the "else" part is executed even if there is a continue statement.

# Prints out 0, 1, 2, 3, 4 and then it prints "count value reached 5"

count = 0
while (count < 5):
    print(count)
    count += 1
    
else:
    print("The value reached 5.")