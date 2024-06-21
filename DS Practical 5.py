import numpy as np

def matrix_inverse(matrix, modulus):
    det = int(np.linalg.det(matrix))
    det_inv = pow(det, -1, modulus)  # Calculate modular inverse of the determinant

    if det_inv == 0:
        raise ValueError("Matrix is not invertible.")

    adj_matrix = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])
    inverse_matrix = (det_inv * adj_matrix) % modulus

    return inverse_matrix.astype(int)

def hill_cipher_encrypt(plaintext, key_matrix, modulus):
    # Convert plaintext to uppercase and remove non-alphabetic characters
    plaintext = "".join(char.upper() for char in plaintext if char.isalpha())
    n = len(plaintext)

    # Pad the plaintext with 'X' if its length is odd
    if n % 2 != 0:
        plaintext += 'X'
        n += 1

    # Convert plaintext characters to numbers (A=0, B=1, ..., Z=25)
    text_numbers = [ord(char) - ord('A') for char in plaintext]

    # Reshape the numbers into a 2xN matrix
    matrix = np.array(text_numbers).reshape(2, n//2)

    # Encrypt using the key matrix
    encrypted_matrix = (key_matrix @ matrix) % modulus

    # Convert encrypted matrix back to a list of numbers
    encrypted_numbers = encrypted_matrix.flatten().tolist()

    # Convert numbers back to characters and concatenate
    ciphertext = ''.join(chr(num + ord('A')) for num in encrypted_numbers)

    return ciphertext

# Example usage:
plaintext = "HELLO"
key_matrix = np.array([[3, 2], [5, 7]])
modulus = 26

ciphertext = hill_cipher_encrypt(plaintext, key_matrix, modulus)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
