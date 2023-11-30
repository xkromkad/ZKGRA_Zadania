import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


# Function to calculate hash function h(n) = n mod m
def h(n, m):
    return n % m

# Function to calculate hash function h(n) = (h(n1) + h(n2) + h(n3) + h(n4) + h(n5) + h(n6)) mod m
def g(n1, n2, n3, n4, n5, n6, m):
    return (h(n1, m) + h(n2, m) + h(n3, m) + h(n4, m) + h(n5, m) + h(n6, m)) % m

# Function to convert a string of arbitrary length into a hash code
def string_to_hash(string, m):
    hash_value = 0
    for char in string:
        hash_value = (hash_value * 10) + ord(char)
    return hash_value % m

# Function to implement Schnopp's digital signature algorithm
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        ec.ECDSA(hashes.SHA256())
    )
    return signature


def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

# Task 3: Proposing an algorithm to convert a string of arbitrary length into a hash code
def my_hash_function(string, m):
    hash_value = 0
    for i, char in enumerate(string):
        hash_value = (hash_value + (ord(char) * pow(2, i))) % m
    return hash_value

# Table of results
results = []

# Case A: even n and odd m
for n in range(2, 10, 2):
    for m in range(3, 11, 2):
        results.append({
            "n": n,
            "m": m,
            "h(n)": h(n, m),
            "g(n_1, n_2, n_3, n_4, n_5, n_6)": g(n, n - 1, n - 2, n - 3, n - 4, n - 5, m)
        })

# Case C: odd n and even m
for n in range(3, 11, 2):
    for m in range(2, 10, 2):
        results.append({
            "n": n,
            "m": m,
            "h(n)": h(n, m),
            "g(n_1, n_2, n_3, n_4, n_5, n_6)": g(n, n - 1, n - 2, n - 3, n - 4, n - 5, m)
        })

# Print results table
print("Task 1 and 2")
print("Hash Function Results:")
print("----------------------")
print("| n | m | h(n) | g(n_1, n_2, n_3, n_4, n_5, n_6) |")
print("------------------------------------------------------")
for result in results:
    print("|", result["n"], "|", result["m"], "|", result["h(n)"], "|", result["g(n_1, n_2, n_3, n_4, n_5, n_6)"], "|")

# Example usage of Schnopp's digital signature algorithm
message = "Hello, world!"
p = 1021
q = 1023

# Task 4
private_key, public_key = generate_key_pair()
message_to_sign = "Hello, Schnorr!"
signature = sign_message(private_key, message_to_sign)

# Verify the signature
verification_result = verify_signature(public_key, message_to_sign, signature)

print("\nTask 4")
print(f"Message: {message_to_sign}")
print(f"Signature: {signature.hex()}")
print(f"Verification Result: {verification_result}")

#Task 3
# Example usage of my_hash_function
string = "This is a string to be hashed"
m = 1024

hash_value = my_hash_function(string, m)
print("\nTask 3")
print("Hash value for string:", string)
print("Hash value:", hash_value)
