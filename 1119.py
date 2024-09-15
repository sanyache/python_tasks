s, h = input().split()
h = int(h)
print(h*(3*h-1)//2)
for i in range(1, h + 1):
    symbols = 2*i - 1
    print(' ' * (h - i) + s * symbols)