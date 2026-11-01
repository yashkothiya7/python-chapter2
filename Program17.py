# Write a program to convert the elements of two lists into key-value pairs of a dictionary. 

def lists_to_dict(keys, values):
    if len(keys) != len(values):
        return "Error: Lists must have the same length."
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Aakash", 21, "Rajkot"]

result = lists_to_dict(keys, values)

print("Result:", result)
