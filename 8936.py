
# for i in range(len(numbers)):
#     print(numbers[len(numbers)-1 - i], end=' ')
# numbers.reverse()
# print(numbers)
# for number in numbers[::-1]:
#     print(number, end=' ')
# for i, number in enumerate(numbers):
#     print(i, number)
a, b = map(int, input().split())
result = [str(i) for i in range(b, a-1, -2) if i % 2 == 0]
print(result)
#print(' '.join(result))