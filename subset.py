# This program checks if a set is a subset of another set

# Define the two sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

# Check if set1 is a subset of set2
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")