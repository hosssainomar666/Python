# This program iterates over a dictionary using a for loop and takes the values from the user.

# Create an empty dictionary.
dictionary = {}

# Get the values from the user.
for key in ["name", "age", "gender"]:
    value = input("Enter the value for {}: ".format(key))
    dictionary[key] = value

# Iterate over the dictionary and print the key and value for each key.
for key, value in dictionary.items():
    print(key, ":", value)