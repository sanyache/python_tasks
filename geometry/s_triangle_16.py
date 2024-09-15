"""
Знайти площу трикутника за заданими цілочисельними координатами
x1 y1 x2 y2 x3 y3
2 1 2 4 6 1 - 6
0 0 0 3 3 0 - 4.5
"""
coord_list = list(map(int, input().split()))
x1, x2, x3 = coord_list[0], coord_list[2], coord_list[4]
y1, y2, y3 = coord_list[1], coord_list[3], coord_list[5]
s = abs((x1-x2)*(y3-y2)-(y1-y2)*(x3-x2))/2
print(s if s % 1 else int(s))

