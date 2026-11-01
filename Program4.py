from array import array

# Create an array
arr = array('i', [10, 20, 30, 40, 50])

print("Array:", arr)

# Take element from user
element = int(input("Enter element to search: "))

# Search the position using index()
if element in arr:
    position = arr.index(element)
    print("Element found at index:", position)
else:
    print("Element not found")