# In Python, we cannot directly print the body or code of a function as we might print a string or vairable. However, we can achieve a similar result using various techniques, such as printing the function's source code if it is available, or printing its name and documentation.

def example_functon():
    """ 
    This is an example function.
    """
    print("Hello, world !")
    
# Print function name
print(example_functon.__name__)

# Print function docstring
print(example_functon.__doc__)

# Printing the Function Object: While this won't show the code of the function, but it can provide information about the function itself.

def example_function2():
    """
    This is an example function. 
    """
    print("Hello, world!")
    
# Print the function object
print(example_function2)

# Recursion in Python = The term recursion can be defined as the process of defining something in terms of itself. In simple words, it is a process in which a function calls directly or indirectly.