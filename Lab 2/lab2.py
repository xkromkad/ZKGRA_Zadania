# author: David Kromka
# personal key: 11

def caesar_encrypt(plaintext, key):
    encrypted_text = []
    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def caesar_decrypt(ciphertext, key):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


# Encrypt the message with key 11
original_message = input("Write message to encrypt: ")
encryption_key = 11
encrypted_message = caesar_encrypt(original_message, encryption_key)
print("Encrypted Message:", encrypted_message)

# Decrypt the message with key 11
print("Decryption Table:")
for i in range(1, 27):
    decrypted_message = caesar_decrypt(encrypted_message, i)
    print(f"Key {i}: {decrypted_message}")
