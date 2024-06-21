# String Functions

# str = "I am a Coder."

# str.endswith("er.") = It returns True if the string ends with substr.
# str.capitalize() = It capitalizes the 1st char.
# str.replace(old, new) = It replaces all the occurrences of old with new.
# str.find(word) = It returns 1st index of 1st occurrer.
# str.count("am") = It counts the occurrence of substr.

# Negative Indexes are only Available in Slicing.

str = "I am Studying Python from ApnaCollege"
print("\n",str.endswith("ege"))

str2 = "i am Studying Python from ApnaCollege"
str2 = str2.capitalize()
print("\n",str2)

str3 = "I am Studying Python from ApnaCollege"
print("\n", str3.replace("Python", "Javascript"))

str4 = "I am Studying Python from ApnaCollege"
print("\n", str4.find("o"))
print("\n",str4.find("t"))
print("\n",str4.find("P"))

str5 = "I am Studying Python from ApnaCollege"
print("\n", str5.count("a"))
print("\n", str5.count("o"))
print("\n", str5.count("y"))