def columnar_transposition_encrypt(plaintext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Determine the number of rows needed in the matrix
    rows = len(plaintext) // len(key) + int(len(plaintext) % len(key) != 0)

    # Create the matrix with 'X' as padding if needed
    matrix = [['X' for _ in range(len(key))] for _ in range(rows)]

    # Populate the matrix with the plaintext in row-major form
    index = 0
    for row in range(rows):
        for col in range(len(key)):
            if index < len(plaintext):
                matrix[row][col] = plaintext[index]
                index += 1

    # Read data in column-major form based on the sorted key order
    encrypted_text = ''.join(matrix[row][col] for col in key_order for row in range(rows))

    return encrypted_text

# Example usage:
plaintext = "HELLO WORLD"
key = [3, 1, 5, 2, 4]  # Example key for column order

ciphertext = columnar_transposition_encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
