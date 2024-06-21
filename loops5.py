# Input a number from the user
num = int(input("Enter a number: "))

# Initialize variables
reverse_num = 0
original_num = num

# Reverse the number
while num > 0:
    remainder = num % 10
    reverse_num = (reverse_num * 10) + remainder
    num = num // 10

# Display the reverse of the number
print(f"The reverse of {original_num} is {reverse_num}")
