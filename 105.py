# Slicing in Python
# It is used to access some specific parts of a String.

# str[ standing_idx : ending_idx ] #ending idx is not included.
# str = "Apna College"
# pna from str will have index number 1,2 and 3.
# [ 1 : 4 ] is "pna"
# [ : 4 ] is same as str[ 0 : 4 ]
# str [ 1 : ] is same as str [ 1 : len(str) ]
# We have to increment one number in the last value at the ending of the slicing.
# For Example : A string = "Darshil" has 7 characters so the last index position of the slicing value will be 8.

# We cannot change or re-assign a value in the Slicing in Python.

string = "apna college"
print(string[1:5])
print(string[2:7])
print(string[0:12])
print(string [:4]) # [0:4]
print(string [5:]) # [5 : len(str)]
print(string[5:len(string)])

# Negative Indexing

string2 = "Apple"
print(string2)
print(string2[-3:-1])
print(string2[-5:-2])
print(string2[-5:])
print(string2[:-1])
print(string2[-2:-4])