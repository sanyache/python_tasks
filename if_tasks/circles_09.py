"""
Чи можна розмістити 2 кола r2, r3 в третьому r1, щоб вони не перетиналися.
Кола r2 і r3 не лежать один в одному
10 10 10 No
10 3 4 Yes
"""
r1, r2, r3 = map(int, input().split())
if r2 + r3 <= r1:
    print("Yes")
else:
    print("No")
