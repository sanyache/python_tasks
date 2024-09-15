"""
Вивести послідовність у зворотньому порядку.
"""
numbers = list(map(int, input().split()))
print(numbers[::-1])
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=' ')
print('')
numbers.reverse()
print(numbers)
