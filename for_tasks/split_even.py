"""
Дано список цілих чисел. Не використовуючи додаткової памяті
розділити парні і непарні числа
"""
numbers = [int(x) for x in input().split()]
ind_even = 0
for ind, number in enumerate(numbers):
    if number%2 == 0:
        numbers[ind], numbers[ind_even] = numbers[ind_even], numbers[ind]
        ind_even += 1
print(numbers)
