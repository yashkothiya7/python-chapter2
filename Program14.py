# Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average.

user_input = input("Enter tuple elements separated by commas: ")

my_tuple = tuple(map(int, user_input.split(",")))

print("Tuple:", my_tuple)
print("Minimum:", min(my_tuple))
print("Maximum:", max(my_tuple))
print("Sum:", sum(my_tuple))
print("Average:", sum(my_tuple) / len(my_tuple))