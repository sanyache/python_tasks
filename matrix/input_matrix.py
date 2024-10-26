"""
create matrix with input data
n - rows
m - columns
"""

matrix = []
n,m = map(int, input("Enter dimension of the matrix row and columns ").split())
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)
for row in matrix:
    for data in row:
        print(data, end=' ')
    print()
