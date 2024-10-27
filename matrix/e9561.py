"""
Дано двомірний масив. Для кожного стовпця знайти найбільший елемент.
4 5
1 3 2 4 5
4 2 7 6 5
9 2 3 5 1
7 8 1 7 2          9 8 7 7 5
"""
n,m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n) ]
transposed_matrix = [max([row[i] for row in matrix]) for i in range(m)]
print(*transposed_matrix)

