# This program gets two strings and prints whether the second string can be obtained from the first by deletion of none, one or more characters.

# Get the two strings from the user.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first by deletion of none, one or more characters.
if string2 in string1:
    print("YES")
else:
    print("NO")
    