# Set Methods in Python

# set.add(el) = It adds an element.
# set.remove(el) = It removes the element.
# set.clear() = It empties the set.
# set.pop() = It removes a random value.

# A set is mutable, but the elements inside the set are immutable. That's why we can pass tuples inside the set but we cannot pass the list and dictionary inside the set.

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")

collection.remove(1)
print(collection)
print(type(collection))
print(len(collection))