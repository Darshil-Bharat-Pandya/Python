# Set Data Type in Python = In Python Data Types, a Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

# Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a 'comma'. The type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.

set1 = set()
print("\nInitial blank set: ", set1)

set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ", set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ", set1)

set1 = set([1, 2, "Geeks", 4, "For", 6, "Geeks"])
print("\nSet with the use of Mixed Values", set1)

print("\n")