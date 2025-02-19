numbers = [1 if x =='R' else -1 for x in input()]
n = len(numbers)
prefix_sum = 0
sum_map = {0 : 1}
counter = 0
for i in range(1, n+1):
    prefix_sum += numbers[i-1]
    if prefix_sum in sum_map:
        counter += sum_map[prefix_sum]
        sum_map[prefix_sum] += 1
    else:
        sum_map[prefix_sum] = 1
print(counter)
