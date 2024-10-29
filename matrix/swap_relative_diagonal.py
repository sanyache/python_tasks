"""
поміняти елементи місцями
відносно головної діагоналі
Input
1 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1
Output
1 1 1 1
0 1 1 1
0 0 1 1
0 0 0 1
"""
l = [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 1, 1, 0],
     [1, 1, 1, 1]]
transposed_matrix = [[row[i] for row in l] for i in range(4)]
for row in transposed_matrix:
    print(*row)
for i in range(3):
    for j in range(i, 4):
        l[i][j],l[j][i] = l[j][i], l[i][j]
for row in l:
    print(*row)
