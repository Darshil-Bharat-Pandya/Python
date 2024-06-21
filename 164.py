# Accessing Key-Value in a Dictionary = In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. There is also a method called get() that will also help in accessing the element from a dictionary.

Dict = {1: "Geeks", "name" : "For", 3: "Geeks"}
print("\n",Dict)
print("Accessing an element using key:", Dict["name"])
print("Accessing an element using get: ", Dict.get(3))
print("\n")