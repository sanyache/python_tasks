"""
Дано двомірний масив n x m . Знайти рядки, які містять мінімальний елемент.
       1 3
"""

n, m = map(int, input().split())
matrix_min_el = [min([int(x) for x in input().split()]) for _ in range(n)]
min_matrix = min(matrix_min_el)
for ind, min_el in enumerate(matrix_min_el):
    if min_el == min_matrix:
        print(ind + 1, end=' ')


