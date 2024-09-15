n = int(input())
color_list = [0]*10
balls = list(map(int, input().split()))
for ball in balls:
    color_list[ball] += 1
print(n-max(color_list))

