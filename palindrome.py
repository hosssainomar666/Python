# This program gets an integer input from a user. If the number is odd, then find the factorial of a number and find the number of digits in the factorial of the number. If the number is even, then check the given number is palindrome or not.

# Get the input from the user
number = int(input("Enter an integer: "))

# Check if the number is odd or even
if number % 2 == 1:
    # The number is odd

    # Find the factorial of the number
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    # Find the number of digits in the factorial of the number
    digit_count = 0
    while factorial > 0:
        digit_count += 1
        factorial //= 10

    print("The factorial of the number has", digit_count, "digits.")

else:
    # The number is even

    # Check if the number is palindrome
    palindrome = True
    number_string = str(number)
    for i in range(len(number_string) // 2):
        if number_string[i] != number_string[-i - 1]:
            palindrome = False
            break

    if palindrome:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")