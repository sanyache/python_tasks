"""
Дано двовимірний масив розміром n⋅m.
Знайти в кожному рядку максимальний елемент
і серед максимальних елементів знайти мінімальний.
4 5
1 5 3 2 4
2 4 3 2 2
6 7 8 9 5
8 9 4 2 5            4
"""
n, m = map(int, input().split())
matrix_max_el = [max([int(x) for x in input().split()]) for _ in range(n)]
print(min(matrix_max_el))
