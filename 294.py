# Python Function with Parameters = The return type of a function is and data type of arguments are possible in Python.

# Syntax:
# def function_name(parameters: data_type) -> return_type:
#   """ Docstring """
#   body of the function
#   return expression

def add(num1: int, num2: int) -> int:
    """ Add two numbers """
    num3 = num1 + num2
    
    return  num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")