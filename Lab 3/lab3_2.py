# author: David Kromka
# Given values of a, b, and c
a1, b1, c1 = int('1011', 2), int('0110', 2), int('0100', 2)
a2, b2, c2 = int('0101', 2), int('1110', 2), int('1101', 2)

# Perform XOR operations
result = a1 ^ b1 ^ c1 ^ a2 ^ b2

# Convert the result back to binary representation
binary_result = bin(result)[2:]

# Ensure the binary representation has 4 bits (pad with leading zeros if necessary)
binary_result = binary_result.zfill(4)

# Print the result
print("Result of a ^ b ^ c ^ a ^ b:", binary_result)
