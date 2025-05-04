import math
print("----------------Farnet_DOS-------------------------------")
n = int(input("Enter a number: "))

a = int(math.sqrt(n)) + 1
print("Starting from a =", a)

while True:
    b2 = a*a - n
    b = math.sqrt(b2)
    if b == int(b):
        break
    a += 1

b = int(b)
print("a is", a)
print("b is", b)
print("Now factors are:")
print(a + b, "and", a - b)
