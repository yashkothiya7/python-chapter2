#create one array from another array 

def Print_array(original_array):
    new_array = []
    
    for element in original_array:
        new_element = element * 2
        new_array.append(new_element)
    return new_array
        

#declare array 
original_array = [1,2,3,4,5]
print(Print_array(original_array))