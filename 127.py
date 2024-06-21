# Tuple Methods in Python

# tup = (2, 1, 3, 1)

# tup.index(el) = It returns the index of first occurrence. = tup.index(1) is 1.
# tup.count(el) = It counts the total number of occurrences. = tup.count(1) is 2.

tup = (1, 2, 3, 4, 5, 2, 3, 2, 4, 4, 2, 2, 2, 2)
print("\n", tup)
print(tup.index(1))
print(tup.index(2))
print(tup.index(3))
print(tup.index(4))
print(tup.index(5))

print("\n", tup.count(1))
print(tup.count(2))
print(tup.count(3))
print(tup.count(4))
print(tup.count(5))