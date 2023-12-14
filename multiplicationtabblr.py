# This program displays the multiplication table

# Get the input from the user
number = int(input("Enter a number: "))

# Print the multiplication table
for i in range(1,11):
   # print(number, "*", i, "=", number * i)
   print(f"{number} * {i} = {number * i}")
