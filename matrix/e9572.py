"""
Дано двовимірний масив розміром n⋅m. Знайти кількість парних елементів масиву.
4 5
1 3 2 4 5
4 2 7 6 5
9 2 3 5 1
7 8 1 7 2
Output:
8
"""
n,m = map(int, input().split())
matrix = [len([int(x) for x in input().split() if int(x)%2==0]) for _ in range(n)]
print(sum(matrix))