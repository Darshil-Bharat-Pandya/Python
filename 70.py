# Entering the values in both X and Y.
X = int(input("\nPlease Enter the Value of X: "))
Y = int(input("\nPlease Enter the Value of Y: "))

# Condition 1: If the Value of X is not Equal to the Value of Y.
if X != Y:
    if X > Y:
        print("\nThe Value of X is Greater than Y.")
    else:
        print("\nThe Value of Y is Greater than X.")

# Condition 2: If the Value of X is Equal to the Value of Y. 
else:
    print("\nThe Value of X is Equal to the Value of Y.")