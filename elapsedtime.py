from itertools import product

def generate_xor_keys(key_size):
  """Generates all possible keys for XOR encryption with a given key size."""
  possible_values = range(256)  # 256 possible values for a 1-byte key
  keys = list(product(possible_values, repeat=key_size))  # Generate all combinations
  return keys

key_size = 1  # Assuming 1-byte key for XOR
possible_keys = generate_xor_keys(key_size)

print(f"Number of possible keys: {len(possible_keys)}")

# Print some example keys
for key in possible_keys[:10]:
  print(f"Key: {key}")
