import math

def f(n):
    if n == 0 or n == 1:
        return 1
    return n * f(n-1)

number = int(input())
print(f(number))
print(math.factorial(number))