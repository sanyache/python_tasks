"""
Дано поле n*m. Скільки варіантів розставити однопалубних кораблів
якщо сусудні поля не зайняті. Сусідні мають спільну сторону.
* - зайняте поле
. - вільне
4 4
* * * *
* * . .
* . . .
* . . .
4
* * * *
. . . .
. . . .
* * * *
0
"""
n, m = map(int, input().split())
matrix = [[x == '.' for x in input() ] for _ in range(n)]
neighbors = [(-1,0), (1, 0), (0, -1), (0, 1)]
counter = 0
for x in range(n):
    for y in range(m):
        if not matrix[x][y]:
            continue
        ngh_counter = 0
        for ngh in neighbors:
            dx = x + ngh[0]
            dy = y + ngh[1]
            if 0 <= dx < n and 0 <= dy < m:
                if matrix[dx][dy]:
                    ngh_counter += 1
            else:
                ngh_counter += 1
        if ngh_counter == 4:
            counter += 1
print(counter)
