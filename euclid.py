from random import randint
a = input("a の値を入力: ")
b = input("b の値を入力: ")


# TODO

def euclid(high, low):
    if high < low:
        high, low = low, high
    while low != 0:
        low, high = high % low, low
    return high

def mutually_prime(a, b):
    return euclid(a, b) == 1

a = int(a)
b = int(b)

print(euclid(a, b))
print(mutually_prime(a, b))

