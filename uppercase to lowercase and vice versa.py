# Input a character from the user
char = input("Enter a character: ")

# Check if the entered character is in lowercase
if char.islower():
    converted_char = char.upper()
    print(f"The uppercase of {char} is {converted_char}")
# Check if the entered character is in uppercase
elif char.isupper():
    converted_char = char.lower()
    print(f"The lowercase of {char} is {converted_char}")
# If it's neither uppercase nor lowercase
else:
    print(f"{char} is not a valid alphabet character.")
