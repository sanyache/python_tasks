"""
Дано сторони трьох відрізків. Чи можуть вони бути сторонами невиродженого трикутника
3 4 5 - yes
1 1 5 - no
"""
a, b, c = map(int, input().split())
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")
