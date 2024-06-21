def caesar_cipher_fixed_key(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_cipher_variable_key(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

def monoalphabetic_cipher(text, mapping):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += mapping[char]
            else:
                result += mapping[char.lower()].upper()
        else:
            result += char
    return result

# Example usage:
fixed_key_cipher = caesar_cipher_fixed_key("Hello, World!", 3)
print(f"Fixed Key Caesar Cipher: {fixed_key_cipher}")

variable_key_cipher = caesar_cipher_variable_key("Hello, World!", 5)
print(f"Variable Key Caesar Cipher: {variable_key_cipher}")

monoalphabetic_mapping = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
                          'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
                          'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}
monoalphabetic_cipher_text = monoalphabetic_cipher("Hello, World!", monoalphabetic_mapping)
print(f"Monoalphabetic Cipher: {monoalphabetic_cipher_text}")
