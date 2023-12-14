# This program prints the Fibonacci sequence.

# Initialize the first two terms of the sequence.
a = 0
b = 1

# Print the first two terms of the sequence.
print(a)
print(b)

# Iterate over the sequence, calculating the next term.
for i in range(2, 40):
  c = a + b
  a = b
  b = c

  # Print the current term of the sequence.
  print(c)