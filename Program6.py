#program removes repeated items from a list so each item appears at most once.the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]. 

def remove_duplicates(my_list):
    result = []

    for item in my_list:
        if item not in result:
            result.append(item)

    return result


# Take list from user
user_input = input("Enter list elements separated by commas: ")

my_list = []

for item in user_input.split(","):
    my_list.append(int(item))


# Remove duplicates
unique_list = remove_duplicates(my_list)

print("Original List:", my_list)
print("List after removing duplicates:", unique_list)