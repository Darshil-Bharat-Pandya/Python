def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_large_numbers(num1, num2):
    # Convert the input strings to integers
    a = int(num1)
    b = int(num2)

    # Find the GCD using the Euclidean algorithm
    result = euclidean_gcd(a, b)

    return result

# Example usage:
num1 = input("Enter the first large number: ")
num2 = input("Enter the second large number: ")

result_gcd = gcd_of_large_numbers(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result_gcd}")