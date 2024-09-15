n = int(input())
F_prev = 1
for i in range(1, n+1):
    F = F_prev*3
    F_prev = 1 << i
print(F)
