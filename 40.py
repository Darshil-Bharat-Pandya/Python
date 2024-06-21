# List Data Type

# Lists are just like arrays, declared in other languages which is an ordered collection of data. It is a very flexible as the items in a list do not need to be of the same type.

# List is a collection which is ordered and changeable. It allows duplicate members. 

# Lists in Python can be created by just placing the sequence inside the square brackets[].

# Example: This Python code demonstrates list creation and manipulation. It starts with an empty list and prints it. It creates a list containing a single string element and prints it. It creates a list with multiple string elements and prints selected elements from the list. It creates a multi-dimensional list (a list of lists) and prints it. The code showcases various ways to work with lists, including single and multi-dimensional lists.

List = []
print("Initial blank List: ")
print(List)

List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

List = ["Geeks", "For", "Geeks"]
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)