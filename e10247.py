n = int(input())
firsts = [int(x) for x in input().split()]
seconds = [int(x) for x in input().split()]
firsts.sort()
seconds.sort()
rez = list()
for i in range(n//2):
    if firsts[i] < seconds[i + n//2]:
        rez.append((firsts[i], seconds[i+n//2]))
if len(rez) != n//2:
    print('-1')
    exit()
for i in range(n//2, n):
    if firsts[i] > seconds[i- n//2]:
        rez.append((firsts[i], seconds[i-n//2]))
if len(rez) != n:
    print(-1)
    exit()
for pair in rez:
    print(*pair)

