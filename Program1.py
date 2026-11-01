# Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays

from array import array

# Create an array
arr = array('i', [10, 20, 30, 40, 50, 60])

# Display the original array
print("Original Array:", arr)

# Retrieve and display elements using indexing
print("Element at index 2:", arr[2])

# Retrieve and display a range of elements using slicing
print("Elements from index 1 to 4:", arr[1:5])

# Update a range of elements using slicing
arr[1:4] = array('i', [200, 300, 400])

# Display the updated array
print("Array after updating:", arr)