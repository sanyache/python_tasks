"""
Знайти суму всіх елементів матриці.
"""

# n = int(input("Введіть кількість рядків у таблиці "))
# matrix = [sum([int(x) for x in input().split()]) for _ in range(n)]
# print(sum(matrix))
n,m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
s = 0
for i in range(n):
    for j in range(m):
        s += matrix[i][j]
print(s)
sum_each_row = [sum(row) for row in matrix]
print(sum(sum_each_row))

