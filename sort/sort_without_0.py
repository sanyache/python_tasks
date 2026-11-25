#nums = [-6, 5, 0, 0, 3, 4, 0, 1, 2, -2]
nums = [int(x) for x in input().split()]
n = len(nums)
for i in range(n-1):
    if nums[i] == 0:
        continue
    min_ind = i
    for j in range(i+1, n):
        if nums[j] != 0 and nums[min_ind] > nums[j]:
            min_ind = j
    nums[min_ind], nums[i] = nums[i], nums[min_ind]

print(nums)