def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
   
    if gcd != 1:
        raise ValueError(f"The inverse does not exist for {a} mod {m}")

    return (x % m + m) % m

# Example usage:
num = int(input("Enter the number: "))
modulus = int(input("Enter the modulus: "))

inverse = mod_inverse(num, modulus)
print(f"The multiplicative inverse of {num} mod {modulus} is: {inverse}")
