# This program finds the largest among three numbers

# Get the three numbers from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Find the largest number
largest_number = max(number1, number2, number3)

# Print the largest number
print("The largest number is", largest_number)