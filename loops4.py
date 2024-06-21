# Initialize counters
uppercase_count = 0
lowercase_count = 0

# Infinite loop to read characters until '*' is encountered
while True:
    char = input("Enter a character (* to quit): ")

    # Check if the character is an asterisk to exit the loop
    if char == '*':
        break

    # Check if the character is uppercase
    if char.isupper():
        uppercase_count += 1
    # Check if the character is lowercase
    elif char.islower():
        lowercase_count += 1

# Display the counts
print("Uppercase characters:", uppercase_count)
print("Lowercase characters:", lowercase_count)
