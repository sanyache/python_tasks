n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()
counter = 0
for ind in range(0, len(numbers), 2):
    counter += numbers[ind+1] - numbers[ind]
print(counter)
