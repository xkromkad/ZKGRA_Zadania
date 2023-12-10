#Author: David Kromka

#Task 1
def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i

# Given n = p * q
n = 851

# Factorize n to get p and q
p, q = factorize(n)

print("Task 1")
print(f"p = {p}, q = {q}")


#Task 2
# Given values
p = 3
q = 11
n = p * q
e = 7
d = 3
m = "02"

# Step 1: Calculate the public key (n, e)
public_key = (n, e)

# Step 2: Encrypt the message m to get the cryptogram C
m_int = int(m)
C = pow(m_int, e, n)

# Print the results
print("\nTask 2")
print(f"Public Key (n, e): {public_key}")
print(f"Cryptogram C: {C}")

# Step 3: Decrypt the cryptogram C using the private key (n, d)
m_decrypted = pow(C, d, n)

# Convert the decrypted message to string
m_decrypted_str = str(m_decrypted).zfill(len(m))

print(f"Decrypted Message: {m_decrypted_str}")


#Task 3
def decrypt(ciphergram, key):
    decrypted_text = ''
    for i in range(0, len(ciphergram), 2):
        char_pair = ciphergram[i:i + 2]
        decrypted_text += chr(((int(char_pair) - key - 1) % 26) + ord('A'))
    return decrypted_text

print("\nTask 3")
def brute_force_decrypt(ciphergram):
    for key in range(1, 27):
        decrypted_text = decrypt(ciphergram, key)
        print(f"Key {key}: {decrypted_text}")
        #key is 19

# Given ciphergram
ciphergram = "202412"

# Brute force decryption
brute_force_decrypt(ciphergram)



