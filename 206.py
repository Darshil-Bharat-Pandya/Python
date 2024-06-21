x = int(input("Enter the value of x: "))

answer = {x > 0: "The value of x is greater than 0.", x < 0: "The value of x is lesser than 0", x == 0: "The value of x is equal to the zero."}

# Note: There are a few important things to keep in mind while using one liner for python if elif else statement. One of them is that, it works on the concept of python dictionary. This means the conditions are stored in the form of dictionary keys and the statement to be executed is stored in the form of dictionary values. One the keys, that is the condition returns True, only then the value of the corresponding key is executed.