import math
boys, girls = map(int, input().split())
max_com = math.gcd(boys, girls)
print(max_com)
print(boys//max_com, girls//max_com)