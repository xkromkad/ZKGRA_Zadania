def redundant_encode(message):
    redundant_code = ""
    prev_value = 0

    for symbol in message:
        current_value = (prev_value + int(symbol, 2)) % 2
        redundant_code += str(current_value)
        prev_value = current_value

    return redundant_code

# Given symbols
symbols = {
    'A1': '0',
    'A2': '1',
    'A3': '10',
    'A4': '11',
    'A5': '100',
    'A6': '101'
}

# Message M
message_M = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']

# Convert symbols to binary and concatenate them
binary_message = ''.join([symbols[symbol] for symbol in message_M])

# Encode the message in a redundant code
redundant_code = redundant_encode(binary_message)
print("Task 1")
print(f"Original Message M in Binary: {binary_message}")
print(f"Redundant Code: {redundant_code}")



def huffman_table(symbols, probabilities):
    # Create a list of nodes
    nodes = []
    for symbol, probability in zip(symbols, probabilities):
        node = {
            "symbol": symbol,
            "probability": probability,
            "left": None,
            "right": None
        }
        nodes.append(node)

    # Build the Huffman tree
    while len(nodes) > 1:
        # Sort the nodes by probability
        nodes.sort(key=lambda node: node["probability"])

        # Create a new node with the combined probability
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        parent_node = {
            "symbol": None,
            "probability": left_node["probability"] + right_node["probability"],
            "left": left_node,
            "right": right_node
        }
        nodes.append(parent_node)

    # Assign codes to the symbols
    codes = {}
    def assign_codes(node, code):
        if node["left"] is None and node["right"] is None:
            codes[node["symbol"]] = code
        else:
            assign_codes(node["left"], code + '0')
            assign_codes(node["right"], code + '1')

    assign_codes(nodes[0], '')

    # Construct the Huffman table
    huffman_table = {}
    for symbol, code in codes.items():
        huffman_table[symbol] = code

    return huffman_table

# Example usage
symbols = ['a', 'b', 'c', 'd', 'e']
probabilities = [0.4, 0.3, 0.2, 0.1, 0.0]
huffman_table = huffman_table(symbols, probabilities)
print("\nTask 2")
print("Huffman table:", huffman_table)