# List Methods in Python

# list = [2, 1, 3]

# list.append(4) = It adds one element at the end. [2, 1, 3, 4]
# list.sort() = It sorts in ascending order. [1, 2, 3]
# list.sort(reverse = True) = It sorts in descending order [3, 2, 1] 
# list.reverse() = It reverses the list. [3, 1, 2]
# list.insert(idx, el) = It inserts an element at index.

# list = [2, 1, 3, 1]

# list.remove(1) = It removes the first occurrence of an element. [2, 3, 1]
# list.pop(idx) = It removes an element at idx.

list = [1, 7, 3, 9, 5]
print("\n",list)

list.append(11)
print("\n",list)

list.sort()
print("\n",list)

list.sort(reverse=True)
print("\n",list)

list.reverse()
print("\n",list)

list.insert(3, 8)
print("\n",list)

list.insert(4, 8)
print("\n",list)

list.remove(8)
print("\n",list)

list.pop(3)
print("\n",list)