print("----------------DIVISION METHOD-------------------------------")

num = int(input("Enter number: "))

print("Factors are:")
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i = i + 1


print("\nPrime factors:")
for x in range(2, num + 1):
    if num % x == 0:
        is_prime = True
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            print(x, end=" ")
