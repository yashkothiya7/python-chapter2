#Write a program to sort the array elements using bubble sort technique. 

from array import array

# Number of elements
n = int(input("Enter number of elements: "))

# Create an empty array
arr = array('i')

# Take array elements from user
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original Array:", arr)

# Bubble Sort
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)