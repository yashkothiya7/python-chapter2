# Write a lambda/Anonymous function to find bigger number in two given numbers 

bigger = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Bigger number is:", bigger(num1, num2))
