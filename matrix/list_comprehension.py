"""
create matrix with list comprehension
"""

n,m = map(int, input("Enter dimension of the matrix row and columns ").split())
matrix = [[int(x) for x in input().split()] for _ in range(n) ]
print(matrix)