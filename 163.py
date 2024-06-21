# Dictionary Data Type in Python = A Dictionary in Python is an unordered collection of data values like a map, unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon:, whereas each key is separated by a 'comma'.

Dict1 = {}
print("\nEmpty Dictionary: ", Dict1)

Dict2 = {1: "Geeks", 2: "For", 3: "Geeks"}
print("\nDictionary with the use of Integer Keys: ", Dict2)

Dict3 = {"Name": "Geeks", 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ",Dict3)

Dict4 = dict({1: "Geeks", 2: "For", 3: "Geeks"})
print("\nDictionary with the use of dict(): ", Dict4)

Dict5 = dict([(1, "Geeks"), (2, "For")])
print("\nDictionary with each item as a pair: ", Dict5)