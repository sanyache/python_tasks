def bubble_sort(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        is_swapped = False
        for j in range(0, n-1 -i):
            cnt += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if not is_swapped:
            break
        print(arr)
    return cnt
nums = [11, 12, 13, 15, 17, 90, 18]

cnt  = bubble_sort(nums)
print(nums)
print(cnt)