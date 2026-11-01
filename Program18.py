#Create a python function to accept python function as a dictionary and display its elements. 

def display_dict(data_dict):
    print("\n--- Dictionary Elements ---")
    for key, value in data_dict.items():
        print(f"{key}: {value}")

def main():
    my_dict = {
        "name": "ABCD",
        "age": 25,
        "city": "Ahmedabad"
    }
    display_dict(my_dict)

main()
