"""
В книзі на сторінці може вміститися К рядків. Доно: К і номер рядка в тексті
Вивести сторінку і рядок на сторінці
50 1  - 1 1
20 25 - 2 5
25 50 - 2 25
15 43 - 3 13
"""
k, n = map(int, input().split())
if n % k == 0:
    print(n//k, k)
else:
    print(n//k+1, n % k)

K, N = map(int, input().split())
page = (N - 1) // K + 1
line = (N - 1) % K + 1
print(page, line)


