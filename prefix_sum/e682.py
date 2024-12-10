n = int(input())
numbers = [int(x) for x in input().split()]
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + numbers[i-1]
m = int(input())
requests = []
for _ in  range(m):
    l, r = map(int, input().split())
    requests.append((l,r))
for l,r in requests:
    print(prefix_sum[r]- prefix_sum[l-1])
