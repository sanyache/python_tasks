s = "A B R A C A D A B R A"
n = len(s)
for i in range(n, 0, -2):
    print(' '*((n-i)//2) + s[0:i])