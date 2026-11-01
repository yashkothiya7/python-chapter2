#Write a program to create nested list and display its elements. 

# Create a nested list
my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# Display the nested list
print("Nested List:", my_list)

# Display each element
print("Elements of Nested List:")

for row in my_list:
    for element in row:
        print(element, end=" ")
    print()