"""
Create a matrix like this
1 2 3
4 5 6
7 8 9

"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for data in row:
        print(data, end=' ')
    print()