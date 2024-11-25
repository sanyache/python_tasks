"""
Дано n рядків. в кожному записано час у годинах, хвилинах, секундах.
Відсортуйте час в незростаючому порядку без ведучих нулів.
Input:
4
10 20 30
7 30 00
23 59 59
13 30 30
Output:
7 30 0
10 20 30
13 30 30
23 59 59
"""

n = int(input())
times = []
for _ in range(n):
    time = tuple(map(int, input().split()))
    times.append(time)
sorted_time = sorted(times, key=lambda x: (x[0], x[1], x[2]))
for time in sorted_time:
    print(*time)
