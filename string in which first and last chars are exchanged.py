# Input string
input_string = "Python"

# Check if the input string has at least two characters
if len(input_string) >= 2:
    # Extract the first and last characters
    first_char = input_string[0]
    last_char = input_string[-1]

    # Create the new string with first and last characters exchanged
    new_string = last_char + input_string[1:-1] + first_char

    # Print the new string
    print(new_string)
else:
    print("Input string should have at least 2 characters.")
