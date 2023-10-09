# author: David Kromka
import math

# Function to calculate entropy
def calculate_entropy(num_states):
    # Probability of each state in equiprobable distribution
    probability = 1 / num_states
    # Calculate entropy using the formula: H = -Σ(P(x_i) * log2(P(x_i)))
    entropy = -sum(probability * math.log2(probability) for _ in range(num_states))
    return entropy

# System X with 8 states
num_states_8 = 8
entropy_8_states = calculate_entropy(num_states_8)
print(f"Entropy for System X with {num_states_8} states: {entropy_8_states:.2f} bits")

# System X with 128 states
num_states_128 = 128
entropy_128_states = calculate_entropy(num_states_128)
print(f"Entropy for System X with {num_states_128} states: {entropy_128_states:.2f} bits")
