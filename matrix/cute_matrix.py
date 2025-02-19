"""
Дано матрицю n*m заповнену 1 та 0
Матриця називається симпатичною, якщо в неї немає підматриці 2*2
повністю заповненою 0 чи 1. Вивести YES - якшо симпатична, інакше -  NO
Дано: кількість матриць. Для кожної матриці її розмірність і сама матриця.
3
1 1
0
4 4
1 0 1 0
1 1 1 0
0 1 0 1
0 0 0 0
3 3
0 0 1
0 0 1
1 1 1
YES
YES
NO

"""
k = int(input())
rez = []
for _ in range(k):
    flag = True
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    for i in range(0, n-1):
        s = 0
        for j in range(0, m-1):
            s = matrix[i][j] + matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
            if s == 0 or s == 4:
                rez.append("NO")
                flag = False
                break
        if  not flag:
            break
    if flag:
        rez.append("YES")
for r in rez:
    print(r)