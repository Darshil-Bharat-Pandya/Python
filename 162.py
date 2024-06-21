# Accessing the Set Items = The Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. But we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in the keyword.

set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial Set", set1)

print("\nElements of Set: ")
for i in set1:
    print(i, end=" ")
print("Geeks" in set1)