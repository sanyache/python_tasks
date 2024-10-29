"""
Дано двомірний масив  n x m. Відсортувати кожен стовпець у
порядку спадання зверху до низу.
Input
4 5
1 5 3 2 4
2 4 3 2 2
6 7 8 9 5
8 9 4 2 5
Output
8 9 8 9 5
6 7 4 2 5
2 5 3 2 4
1 4 3 2 2
"""

n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
transposed_matrix = [[row[i] for row in matrix] for i in range(m)]
for row in transposed_matrix:
    row.sort(reverse=True)
matrix = [[row[i] for row in transposed_matrix] for i in range(n)]
for row in matrix:
    print(*row)