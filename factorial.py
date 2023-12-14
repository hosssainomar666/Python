# This program calculates the factorial of a number.
#
# Input: A number
#
# Output: The factorial of the number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
	factorial = factorial * i
print("The factorial of {} is {}".format(number, factorial))