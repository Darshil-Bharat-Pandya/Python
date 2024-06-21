def rail_fence_encrypt(plaintext, rail_count):
    fence = [[] for _ in range(rail_count)]
    direction = 1  # 1 for downward, -1 for upward

    row = 0
    for char in plaintext:
        fence[row].append(char)
        row += direction

        if row == rail_count:
            direction = -1
            row -= 2
        elif row == -1:
            direction = 1
            row += 2

    encrypted_text = ''.join([''.join(row) for row in fence])
    return encrypted_text

# Example usage:
plaintext = "HELLO WORLD"
rail_count = 2

ciphertext = rail_fence_encrypt(plaintext, rail_count)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
