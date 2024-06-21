# Slicing
# It is used to access some specific parts of a string.

# str[ starting_idx : ending_idx ] #ending idx is not included
# str = "ApnaCollege"
# str[ 1 : 4 ] is "pna"
# str[ : 4 ] is same as str[ 0 : 4 ]
# str [ 1 : ] is same as str[ 1: len(str) ]

str = "apna college"
print(str[0:4])
print(str[5:len(str)])
print(str[3:8])
print(str[0:])
print(str[:12])

# Negative Index in String Slicing
str2 = "apple"
print("\n",str2[-5:-2])
print(str2[-5:len(str2)])
print(str2[:-4:-2])