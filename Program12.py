# list of 7 elements and implement the List methods mentioned: append, insert, copy, extend, count, remove,pop, sort, reverse and clear.

def display_list(my_list):
    print("Your list : ")
    for i in my_list:
        print(i,end=" ")
    print("\n")

simple_list = [] 
size = 7
while True: 
    print("------------MENU-----------")
    print("1. create list ")
    print("2. Append value in list ")
    print("3. Insert value in list ")
    print("4. Copy list ")
    print("5. Extend list ")
    print("6. Count list element ")
    print("7. Remove element from list ")
    print("8. Pop element from list ")
    print("9. Sort the list ")
    print("10. reverse list ")
    print("11. Clear list ")
    print("12. Exit from the list ")

    try:
        choice = int(input("Enter your choice between 1 to 12 : "))
    except:
        print("Please enter choice between 1 to 12. ")
        continue

    if(choice == 1):
        for i in range(size):
            val = int(input(f"Enter value {i+1}: "))
            simple_list.append(val)
        print("\n")
        display_list(simple_list)

    elif(choice == 2):
        n = int(input("Enter value to append in list : "))
        simple_list.append(n)
        display_list(simple_list)

    elif(choice == 3):
        n = int(input("Enter value to insert in list : "))
        idx = int(input("Enter index number : "))
        simple_list.insert(idx,n)
        display_list(simple_list)
        
    elif(choice == 4):
        copy_list = simple_list.copy()
        print("copied list : ")
        display_list(copy_list)
        
    elif (choice == 5):
        new_elements = input("Enter values to extend list (comma-separated): ").split(",")
        simple_list.extend(new_elements)
        display_list(simple_list)
        
    elif(choice == 6):
        val = int(input("Enter value to count : "))
        cnt = simple_list.count(val)
        print(f"{val} appears {cnt} times in the list.")
        
    elif(choice == 7):
        n = int(input("Enter value to remove : "))
        if n in simple_list:
            simple_list.remove(n)
            display_list(simple_list)
        else:
            print("this element does not exist in list! ")
            
    elif(choice == 8):
        if simple_list:
            pop_ele = simple_list.pop()
            print("popped element is : ",pop_ele)
        else:
            print("list is empty!")
        display_list(simple_list)
        
    elif(choice == 9):
        simple_list.sort()
        display_list(simple_list)
        
    elif(choice == 10):
        simple_list.reverse()
        display_list(simple_list)
        
    elif(choice == 11):
        simple_list.clear()
        display_list(simple_list)
        
    elif(choice == 12):
        print("You Exit from list! ")
        break
    
    else:
        print("Invalid input! please enter valid input!")