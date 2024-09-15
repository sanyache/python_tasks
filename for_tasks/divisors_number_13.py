"""
Знайти суму  чисел на яке натуральне  число nоділиться без остачі
6 - 12
10 - 18
"""

n = int(input())
s = 0
for x in range(1, n+1):
    if n % x == 0:
        s += x
print(s)
print(sum(x for x in range(1, n+1) if n % x == 0))
if n == 1:
    s = 1
else:
    s = 0
    x = 1
    while x*x < n:
        if n % x == 0:
            s += x + n//x
        x += 1
    if x*x == n:
        s += x
print(s)
