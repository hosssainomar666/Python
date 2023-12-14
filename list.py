# This program uses list for positive and negative indexing and also to check if the given list is in Ascending order or Not.

# Create a list
list1 = [1, 2, 3, 4, 5]

# Print the list using positive indexing
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

# Print the list using negative indexing
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])

# Check if the list is in Ascending order
if list1 == sorted(list1):
    print("The list is in Ascending order.")
else:
    print("The list is not in Ascending order.")