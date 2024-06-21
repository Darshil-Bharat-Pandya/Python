# Global and Local Variables in Python = The Python Global Variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughput the program and inside every function.

# Python Local Variables = Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function.

def f():
    
    # local variable
    s = "I Love My India"
    print(s)
    
# Driver code
f()