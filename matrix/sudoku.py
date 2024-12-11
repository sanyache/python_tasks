"""
Судоку розміру n із стороною n^2 розділений на n^2 квадратів
Судоку правильний, якщо в кожному рядку і кожному стовпчику і кожному
 з n^2 квадратів зустрічаються всі числа від 1 до n^2
1<=n<=100
3
1 3 2 5 4 6 9 8 7
4 6 5 8 7 9 3 2 1
7 9 8 2 1 3 6 5 4
9 2 1 4 3 5 8 7 6
3 5 4 7 6 8 2 1 9
6 8 7 1 9 2 5 4 3
5 7 6 9 8 1 4 3 2
2 4 3 6 5 7 1 9 8
8 1 9 3 2 4 7 6 5
Correct

1
10
Incorrect
"""
n = int(input())
matrix = []
for i in range(n*n):
    row = list(map(int, input().split()))
    for el  in row:
        if not(1 <= el <= n*n):
            print('Incorrect')
            exit()
    matrix.append(row)
for i in range(n*n):
    A = [0] * 101
    for j in range(n*n):
        ind = matrix[i][j]
        A[ind] += 1
    if A.count(1) != n*n:
        print("Incorrect")
        exit()
for j in range(n*n):
    A = [0] * 101
    for i in range(n*n):
        ind = matrix[i][j]
        A[ind] += 1
    if A.count(1) != n*n:
        print("Incorrect")
        exit()
for i in range(n):
    for j in range(n):
        A = [0] * 101
        for ii in range(i*n, i*n+n):
            for jj in range(j*n, j*n+n):
                ind = matrix[ii][jj]
                A[ind] += 1
        if A.count(1) != n*n:
            print("Incorrect")
            exit()
print("Correct")
