#Write  programs to demonstrate the use of Positional Argument, keyword argument , default arguments , variable length arguments

def Position_argument(name, age, grade):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")

def keyword_argument(name, age, grade):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")

def Default_arguments(name, message="hello guys"):
    print(f"{name} said that : {message}")

def variable_length_argument(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

while True:
    print("|-----------MENU---------|")
    print("1.Position argument ")
    print("2. keyword argument ")
    print("3. Default argument ")
    print("4. variable length argument")
    print("5. Exit form menu")
    print()
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        Position_argument("Aakash", 18, "A")
        
    elif choice == 2:
        keyword_argument(grade="A", name="Aakash", age=18)
        
    elif choice == 3:
        Default_arguments("Aakash")
        Default_arguments("Rutvi", "Goon night!")
        
    elif choice == 4:
        result = variable_length_argument(1,2,3,4,5,6,7)
        print("Sum of numbers : ", result)

    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:





Positional Argument
def positional(name, age):
    print("Positional Arguments:")
    print("Name:", name)
    print("Age:", age)


Keyword Argument
def keyword(name, age):
    print("\nKeyword Arguments:")
    print("Name:", name)
    print("Age:", age)


Default Argument
def default(name, age=20):
    print("\nDefault Arguments:")
    print("Name:", name)
    print("Age:", age)


Variable Length Argument
def variable(*numbers):
    print("\nVariable Length Arguments:")
    for num in numbers:
        print(num)


Function calls

positional("Om", 20)

keyword(age=20, name="Om")

default("Om")

variable(10, 20, 30, 40)