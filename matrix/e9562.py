"""
Дано двовимірний масив розміром n * m. Знайдіть суму елементів підмасиву.

4 5
1 3 2 4 5
4 2 7 6 5
9 2 3 5 1
7 8 1 7 2
2 2 3 4
Output
25
"""
n,m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
x1,y1,x2,y2 = map(int, input().split())
s = 0
for i in range(x1-1, x2):
    for j in range(y1-1, y2):
        s += matrix[i][j]
print(s)
