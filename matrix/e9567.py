"""
Дано двомірний масив  n x m. Зсуньте всі нульові елементи праворуч
у кожному рядку.
4 5
1 5 0 2 4
0 4 0 2 0
6 0 0 9 5
8 9 4 0 0
Output
8 9 4 0 0
1 5 2 4 0
4 2 0 0 0
6 9 5 0 0
"""
n, m = map(int, input().split())
matrix = [[int(x) for x in input().split() if int(x) != 0] for _ in range(n)]
for row in matrix:
    if len(row) != m:
        row.extend([0]*(m - len(row)))
    print(*row)

