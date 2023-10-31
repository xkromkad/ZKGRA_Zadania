#author: David Kromka
# Function to convert hexadecimal to decimal
def hex_to_decimal(hex_string):
    return int(hex_string, 16)

# Elements in direct replacement table
direct_replacement_table = ["01", "03", "04", "05", "06", "0d", "10"]

# Elements in reverse swap decryption table
reverse_swap_table = ["f1", "f3", "f4", "f6", "f8", "ff", "10"]

# Convert elements from hexadecimal to decimal
direct_replacement_decimal = [hex_to_decimal(hex_string) for hex_string in direct_replacement_table]
reverse_swap_decimal = [hex_to_decimal(hex_string) for hex_string in reverse_swap_table]

# Print the results
print("Direct Replacement Table (Decimal Notation):", direct_replacement_decimal)
print("Reverse Swap Decryption Table (Decimal Notation):", reverse_swap_decimal)


