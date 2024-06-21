# Dictionary Data Type in Python = A dictionary in Python is an unordered collection of data values, used to store data values like a map, unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. Key-value pair is provided in the dictionary to make it more optimized each key-value pair in a Dictionary is separated by a colon:, whereas each key is separated by a 'comma'.

a = {}
print(a)
print(type(a))

b = {1: "Geek", 2: "For", 3: "Geeks"}
print(b)
print(type(b))

c = {1: "Name", "Name": 34, 1: [1, 2, 3, 4, 5]}
print(c)
print(type(c))

d = dict({1: "A", 2: "B", 3: "C", 4: "D", 5: "E"})
print(d)
print(type(d))

e = dict([(1, "Geeks"), (2, "For")])
print(e)
print(type(e))