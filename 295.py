# Python Function Arguments = Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

# In this example, we will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.

def evenodd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
        
# Driver code to call the function
evenodd(2)
evenodd(3)
