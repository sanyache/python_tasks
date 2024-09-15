"""
Задано перший і другий член арифметичної прогресії
Вивестий n член
1 5 3 - 9
"""
a1, a2, n = map(int, input().split())
d = a2 - a1
i = 1
an = a1
while i < n:
    an += d
    i += 1
print(an)
print(a1 + d*(n-1))
