# Tuples in Python

# Lists are mutable.
# Strings and Tuples are immutable.

# It is a built-in data type that lets us create immutable sequences of values.

# tup = (87, 64, 33, 95, 76) = tup[0], tup[1]..
# tup[0] = 43 = It is not allowed in Python.

# tup1 = ( )
# tup2 = (1, )
# tup3 = (1, 2, 3)

tup = (1, 2, 3, 4, 5)
print("\n",tup)
print(type(tup))

print("\n",tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

print("\n",tup[-5])
print(tup[-4])
print(tup[-3])
print(tup[-2])
print(tup[-1])

tup2 = ()
print("\n", tup2)
print(type(tup2))

tup3 = (1,)
print("\n", tup3)
print(type(tup3))

tup4 = (1)
print("\n", tup4)
print(type(tup4))

tup5 = (2, 4, 6, 8)
print("\n", tup5)
print(type(tup5))
print(tup5[0 : 4])
print(tup5[0 : ])
print(tup5[ : 4])
print(tup5[-4 : -1])
print(tup5[-4 : ])
print(tup5[ : -1])
print(tup5[1 : 2])
print(tup5[-4 : -2])