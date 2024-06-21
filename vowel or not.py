# Input a character from the user
char = input("Enter a character: ")

# Convert the character to lowercase (to handle uppercase input)
char = char.lower()

# Check if the character is a vowel
if char in ('a', 'e', 'i', 'o', 'u'):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")
