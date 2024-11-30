def split_zero(numbers):
    ind_dig = 0
    for ind, number in enumerate(numbers):
        if number != 0:
            numbers[ind], numbers[ind_dig] = numbers[ind_dig], numbers[ind]
            ind_dig += 1
n, m = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
for row in matrix:
    split_zero(row)
for row in matrix:
    print(*row)