# List Slicing

# It is similar to String Slicing.

# list_name[starting_idx : ending_idx] = ending idx is not included.

# marks = [87, 64, 33, 95, 76] in which 87 is at 0th position, 64 is at 1st position, 33 is at 2nd position, 95 is at 3rd position, 76 is at 4th position.

# marks[1 : 4] is [64, 33, 95]
# marks[ : 4] is same as marks[0 : 4]
# marks[1 : ] is same as marks[1 : len(marks)]
# marks[-3 : -1] is [33, 95].

# substring is a small piece of a string.
# sublist is a small piece of a list.

marks = [85, 94, 76, 63, 48]
print("\n",marks[1 : 4])
print(marks[ : 5])
print(marks[0 : ])
print(marks[2 : 4])
print(marks[-3 : -1])
print(marks[ : -1])
print("\n",)