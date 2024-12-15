# 56 98 - 14
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

number1, number2  = map(int, input().split())
print(gcd(number1, number2))
print(math.gcd(number1, number2))