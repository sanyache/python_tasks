def count_smaller_neighbors(arr):
    n = len(arr)
    left_smaller = [0] * n  # Кількість менших елементів зліва
    right_smaller = [0] * n  # Кількість менших елементів справа
    top = 0

    # Обчислюємо кількість менших елементів зліва
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            left_smaller[i] = left_smaller[i-1] + 1
            if arr[i] < arr[top]:
                left_smaller[top] += 1
            else:
                top = i

    # Очищаємо стек перед другим проходом
    top = n - 1

    # Обчислюємо кількість менших елементів справа
    for i in range(n - 1, 0, -1):
        if arr[i-1] > arr[i]:
            right_smaller[i-1] += right_smaller[i] + 1
            if arr[i-1] < arr[top]:
                right_smaller[top] += 1
            else:
                top = i - 1

    # Повертаємо результати як список пар (менших зліва, менших справа)
    return [left_smaller[i] + right_smaller[i] for i in range(n)]


n, k = map(int, input().split())
numbers = [int(x) for x in input().split()]
result = count_smaller_neighbors(numbers)
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + result[i-1]
max_sum = 0
for i in range(k, n+1):
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-k])
print(max_sum)

