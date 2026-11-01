# Create a program to sort tuple with nested tuples

my_tuple = ((3, "banana"), (1, "apple"), (4, "mango"), (2, "cherry"))

print("Original Tuple:")
print(my_tuple)

sorted_tuple = tuple(sorted(my_tuple, key=lambda x: x[0]))

print("\nSorted Tuple (by first element):")
print(sorted_tuple)

sorted_by_second = tuple(sorted(my_tuple, key=lambda x: x[1]))

print("\nSorted Tuple (by second element):")
print(sorted_by_second)
