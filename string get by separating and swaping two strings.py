# Input strings
string1 = "Hello"
string2 = "World"

# Check if both strings have at least 2 characters
if len(string1) >= 2 and len(string2) >= 2:
    # Swap the first two characters of each string
    new_string = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]

    # Print the result
    print(new_string)
else:
    print("Both strings should have at least 2 characters.")
