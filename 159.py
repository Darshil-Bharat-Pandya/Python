# Tuple Data Type = Just like a list, a tuple is also an ordered collection of Python Objects. The only difference between a tuple and a list is that tuples are immutable i.e. the tuples cannot be modified after it is created. It is represented by a tuple class.

Tuple1 = ()
print("\nInitial empty Tuple:", Tuple1)

Tuple2 = ("Geeks", "For", "Geeks")
print("\nTuple with the use of String:", Tuple2)

list = [1, 2, 4, 5, 6]
print("\nTuple using List: ",tuple(list))

Tuple3 = tuple('Geeks')
print("\nTuple with the use of function:", Tuple3)

Tuple4 = (0, 1, 2, 3)
Tuple5 = ("python", "geek")
Tuple6 = (Tuple4, Tuple5)

print("\nTuple with nested tuples: ")
print(Tuple6)

print("\n")