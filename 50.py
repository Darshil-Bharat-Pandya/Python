# Conditional Statements
# Single Line If/Ternary Operator

# <var> = <val1> if <condition> else <val2>
food = input("food: ")
eat = "Yes" if food == "cake" else "no"
print(eat)

# <stt1> if <condition> else <stt2>
food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")