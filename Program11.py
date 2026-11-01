# Write a program to create a list using range functions and perform append, update and delete elements operations in it. 

# Create a list using range()
my_list = list(range(1, 6))

print("Original List:", my_list)

# Append an element
my_list.append(6)
print("After Append:", my_list)

# Update an element
my_list[2] = 30
print("After Update:", my_list)

# Delete an element
del my_list[2]
print("After Delete:", my_list)