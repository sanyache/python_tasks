n, m = map(int, input().split())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(n)]
matrix.sort(key=lambda x: -sum(x[1:]))
for row in matrix:
    print(*row, sum(row[1:]))
