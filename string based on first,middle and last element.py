# Input string
input_string = "Python"

# Calculate the length of the string
length = len(input_string)

# Check if the string has at least 3 characters
if length >= 3:
    # Get the first, middle, and last characters
    first = input_string[0]
    middle = input_string[length // 2]
    last = input_string[-1]

    # Create the new string
    new_string = first + middle + last

    # Print the new string
    print(new_string)
else:
    print("Input string should have at least 3 characters.")
