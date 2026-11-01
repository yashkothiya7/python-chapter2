def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


n = int(input("Enter the limit: "))

print("Prime numbers are:")

for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")