# Input string
S2 = "His name is John. John lives in U.S.A"

# Substring to search for
substring = "John"

# Find the last position of the substring
last_position = S2.rfind(substring)

# Check if the substring was found
if last_position != -1:
    print(f"The last position of '{substring}' is at index {last_position}.")
else:
    print(f"'{substring}' not found in the string.")
