# This program creates pyramid patterns using *

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Create the pyramid pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()