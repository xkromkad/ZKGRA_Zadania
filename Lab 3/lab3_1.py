# author: David Kromka
# Define the 6x6 Polybius square with letters and numbers
polybius_square = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]

# Function to encode a message using the Polybius square
def polybius_encode(message, square):
    encoded_message = []
    for char in message:
        # Convert characters to uppercase
        char = char.upper()
        # Find the coordinates of the character in the Polybius square
        for row_idx, row in enumerate(square):
            if char in row:
                col_idx = row.index(char)
                # Add 1 to row and column indices to make it 1-based index
                encoded_message.append(str(row_idx + 1) + str(col_idx + 1))
    return ' '.join(encoded_message)

# Messages to encode
message_a = "ENCRYPT ME 2 DAY"
message_b = "Kromka"

# Encode messages using the Polybius square
encoded_message_a = polybius_encode(message_a, polybius_square)
encoded_message_b = polybius_encode(message_b, polybius_square)

# Print encoded messages
print("Encoded message a):", encoded_message_a)
print("Encoded message b):", encoded_message_b)
