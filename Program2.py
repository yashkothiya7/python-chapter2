# Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index,tolist and count.

from array import array

arr = array('i', [10, 20, 30, 40, 30])

print("Array elements : ",arr)

arr.append(50)
print("After append value : ",arr)

arr.insert(1,15)
print("after insert value into array  : ",arr)

arr.remove(30)
print("Array after remove first occurrence : ",arr)

pop_ele = arr.pop(3)
print("Array after popped element : ",arr)
print("popped element is  : ", pop_ele)
 
idx = arr.index(30)
print("Index of 30 is : ",idx)

cnt = arr.count(15)
print(f"15 found {cnt} time in list")

convert_list = arr.tolist()
print("list of element : ",convert_list)