def Bubble_short(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertion_short(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selection_short(arr):
    for i in range(0,len(arr)):
        for j in range (i+1,len(arr)):
            if(arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
    return arr 

def merge_short(arr):
     if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the array elements
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_short(left_half)
        merge_short(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking for any leftover elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        return arr
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # You can also use last element as pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

print("|--------menu--------|")
print("1.Bubble short ")
print("2.insertion short ")
print("3.selection short ")
print("4.merge short ")
print("5.quick short ")
print("6.Exit")

choice = int(input("Enter your choice : "))

size = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements:")
for i in range(size):
    val = int(input(f"Element {i+1}: "))
    arr.append(val)
print("original array is : ",arr)

if(choice == 1):
    print("shorted array : ",Bubble_short(arr))
    
elif(choice == 2):
    print("Insertion short : ", insertion_short(arr))
    
elif(choice == 3):
    print("Selection short : ",selection_short(arr))
    
elif(choice == 4):
    print("Merge short : ",merge_short(arr))
    
elif(choice == 5):
    print("Quick short : ",quick_sort(arr))
else:
    print("Invalid choice.")
    
