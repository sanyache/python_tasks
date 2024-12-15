def slow_pow(a, n):
    if n == 0:
        return 1
    return a* slow_pow(a, n-1)

def quick_pow(a,n):
    if n == 0:
        return 1
    if n%2 == 0:
        return quick_pow(a*a, n/2)
    else:
        return quick_pow(a, n-1)*a

number = float( input())
power = int(input())
#print(slow_pow(number, power))
print((quick_pow(number, power)))