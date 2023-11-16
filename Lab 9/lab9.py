from math import gcd

def rsa_encrypt(plaintext, e, n):

    # Encrypt each character using modular exponentiation
    ciphertext_integers = []
    for char in plaintext:
        ciphertext_integers.append(pow(ord(char) - 64, e, n))

    return ciphertext_integers

def rsa_decrypt(ciphertext, d, n):
    # Decrypt each character using modular exponentiation
    plaintext_integers = []
    for char in ciphertext:
        plaintext_integers.append((pow(char, d, n)) + 64)

    # Convert decrypted integers to characters
    plaintext = ''.join(chr(integer) for integer in plaintext_integers)

    return plaintext

def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    public_keys = []

    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            public_keys.append((e, n))

    return public_keys

# Encrypt the plaintext
plaintext = "Bratislava"
p = 7
q = 11
n = p * q
phi = (p - 1) * (q - 1)
# Choose a public key e such that gcd(e, phi) = 1
e = 13
# Calculate the modular inverse of e modulo phi
d = pow(e, -1, phi)

print("Task 1")
ciphertext = rsa_encrypt(plaintext, e, n)
print("Encrypted ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = rsa_decrypt(ciphertext, d, n)
print("Decrypted plaintext:", decrypted_plaintext)

#Task 2
# Encrypt the plaintext
plaintext = "BAQN"
p = 9
q = 11
n = p * q
phi = (p - 1) * (q - 1)
# Choose a public key e such that gcd(e, phi) = 1
e = 13
# Calculate the modular inverse of e modulo phi
d = pow(e, -1, phi)

print("Task 2")
ciphertext = rsa_encrypt(plaintext, d, n)
print("Encrypted ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = rsa_decrypt(ciphertext, e, n)
print("Decrypted plaintext:", decrypted_plaintext)

#Task 4
print("Task 4")
ciphertext = rsa_encrypt(plaintext, e, n)
print("Encrypted ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = rsa_decrypt(ciphertext, d, n)
print("Decrypted plaintext:", decrypted_plaintext)

#Task 3
p = 7
q = 11

public_keys = generate_keys(p, q)

print("Task 3")
print("All possible public keys for p=7, q=11:")
for key in public_keys:
    print(f"e: {key[0]}, n: {key[1]}")

p = 9
q = 11

public_keys = generate_keys(p, q)
print("All possible public keys for p=9, q=11:")
for key in public_keys:
    print(f"e: {key[0]}, n: {key[1]}")
