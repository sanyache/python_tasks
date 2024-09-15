"""
Формула спитру C2H5OH - з неї видно, що одна молекула складається з 2 атомів вуглецю,
6 атомів водню і одного кисню. По данній кількості атомів визначити скільки молекул
 спирту може утворитися
 2 6 1 - 1
 10 5 12 - 0
 18 35 3 - 3
"""
c, h, o = map(int, input().split())
print(min(c//2, h//6, o))
