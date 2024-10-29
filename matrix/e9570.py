"""
Дано прямокутний двохвимірний масив розміром n x m.
Відобразіть його відносно вертикальної осі симетрії
Input
2 3
1 2 3
4 5 6
Output
3 2 1
6 5 4
"""
n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()][::-1] for _ in range(n)]
for row in matrix:
    print(*row)