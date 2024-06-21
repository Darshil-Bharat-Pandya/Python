# Set in Python

# A Set is the collection of the unordered items.
# Each element in the set must be unique and immutable.

# nums = {1, 2, 3, 4}

# set2 = (1, 2, 2, 2)
# repeated elements are stored only once, so it is resolved to {1, 2}

# null_set = set() = empty set syntax.

# Boolean Values, Integers, Floating Point Numbers, Strings and Tuples can be included inside the Set because, these all values are Immutable.

# List and Dictionaries can not be included inside the Sets because they are Mutable.

# Set ignores the duplicate values.

collection = {1, 2, 2, 2, 3, 4, "hello", "world", "world", 4}

print(collection)
print(type(collection))
print(len(collection)) #Total Number of items.

empty_set = set() #Syntax of an Empty Set.
print(empty_set)
print(type(empty_set))
print(len(empty_set))

empty_dict = {} ##Syntax of a Empty Dictionary.
print(empty_dict)
print(type(empty_dict))
print(len(empty_dict))