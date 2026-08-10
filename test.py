def fib(n):
    if n==1 or n==0:
        return n
    f1 = fib(n-1)
    f2 = fib(n-2)
    return f1 + f2

print(fib(5))
