def is_palindrome(num):
    num_str=str(num)
    num_str=num_str[::-1]
    num = input("Enter a digit:")
    if is_palindrome(num):
        print(f"The number {num} is a palindrome number")
    else:
        print("Not palindrome")