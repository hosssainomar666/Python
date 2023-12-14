# This program checks if a number is an Armstrong number.

# Get the number from the user.
number = int(input("Enter a number: "))

# Initialize the sum of the digits.
sum = 0

# Iterate over the digits of the number.
while number > 0:
  # Get the current digit.
  digit = number % 10

  # Add the digit to the sum.
  sum += digit ** 3

  # Remove the current digit from the number.
  number //= 10

# Check if the sum is equal to the number.
if sum == number:
  # The number is an Armstrong number.
  print("The number is an Armstrong number.")
else:
  # The number is not an Armstrong number.
  print("The number is not an Armstrong number.")