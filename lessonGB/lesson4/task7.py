from math import factorial


def fact(n):
    for i in range(n):
        yield factorial(i + 1)


n = int(input("Enter a number: "))

for el in fact(n):
    print(el)
