#Laboratory work 4
#Author: David Kromka

#Task 2
print("Task 2")
# 2.1 Form the vector of residuals of the number 4 by modulus 9
number_1 = 4
modulus_1 = 9
residuals_1 = [number_1 % modulus_1]
print("Vector of residuals for", number_1, "mod", modulus_1, "is:", residuals_1)

# 2.2 Form the vector of residuals of the number 15 by modulus 7
number_2 = 15
modulus_2 = 7
residuals_2 = [number_2 % modulus_2]
print("Vector of residuals for", number_2, "mod", modulus_2, "is:", residuals_2)

# 2.3 Form the vector of residuals of the number 32 by modulus 29
number_3 = 32
modulus_3 = 29
residuals_3 = [number_3 % modulus_3]
print("Vector of residuals for", number_3, "mod", modulus_3, "is:", residuals_3)

#Task 3
print("\nTask 3")
# 3.1. Calculate a common secret key in an asymmetric encryption algorithm:

# a) (2^x) mod 4
modulus_a = 4
transmitter_key_a = 6
receiver_key_a = 3
common_key_a = (2 ** transmitter_key_a) % modulus_a
print("Common secret key for (2^x) mod 4:", common_key_a)

# b) (78^x) mod 33
base_b = 78
modulus_b = 33
transmitter_key_b = 6
receiver_key_b = 3
common_key_b = (base_b ** transmitter_key_b) % modulus_b
print("Common secret key for (78^x) mod 33:", common_key_b)

# 3.2. Determine if it's possible to use the function (2^(-1)) mod 6 as a common function:
try:
    base_inverse = pow(2, -1, 6)
    print("Modular inverse of 2 modulo 6:", base_inverse)
except ValueError as e:
    print("Error:", e)
    print("Modular inverse does not exist for the given base and modulus.")


