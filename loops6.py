# Input a number from the user
num = int(input("Enter a number to display its multiplication table: "))

# Print the multiplication table
print(f"Multiplication table for {num}:")

for i in range(1, 11):  # Loop from 1 to 10
    product = num * i
    print(f"{num} x {i} = {product}")
