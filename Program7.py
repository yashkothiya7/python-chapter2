# Write a program to pass a list to a function and display it. 

def display_list(my_list):
    print("The list elements are:")
    for item in my_list:
        print(item)

size = int(input("Enter the number of elements in the list: "))

my_list = []

print(f"Enter {size} elements:")
for i in range(size):
    value = int(input(f"Element {i+1}: "))
    my_list.append(value)

print("List : ",my_list)

display_list(my_list)