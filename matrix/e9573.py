"""
Дано двохвимірний масив розміром n x m.
Знайти суму додатних елементів у непарних рядках двохвимірного масиву.
4 5
1 3 2 4 5
4 2 7 6 5
9 2 3 5 1
7 8 1 7 2
Output:
35
"""

n,m = map(int, input().split())
matrix = [[int(x) for x in input().split() if int(x) > 0] for _ in range(n)]
s = 0
for ind, row in enumerate(matrix):
    if (ind+1)%2 != 0:
        s += sum(row)
print(s)