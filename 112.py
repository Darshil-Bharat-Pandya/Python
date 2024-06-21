# Conditional Statements

# Syntax = if-elif-else

# if(condition):
#      Statement1
# elif(condition): 
#      Statement2
# else:
#      StatementN

# Indentation = It is used in python to maintain proper spaces between different lines of code. It is also used to follow the proper rules of Coding Convention in Python.

Light_Colour= input("\nPlease Enter the Colour of Traffic Light: ")

if (Light_Colour == "Red"):
    print("\nPlease Stop.")
elif (Light_Colour == "Yellow"):
    print("\nPlease Look.")
elif (Light_Colour == "Green"):
    print("\nPlease Go.")
else:
    print("\nThe Tarffic Light is Broken.")