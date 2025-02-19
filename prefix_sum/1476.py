n, k = map(int, input().split())
numbers = [int(x) for x in input().split()]
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + numbers[i-1]
max_sum = 0
for i in range(k, n+1):
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-k])
print(max_sum)
