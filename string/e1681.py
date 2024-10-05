"""
Підрахувати кількість N-значних натуральних чисел,
у яких суми цифр у двійковій і десятковій системах числення співпадають. (N = 1..7).
"""
def get_sum_binary(number):

    return sum([int(x) for x in bin(number)[2:]])

def get_sum_decimal(number):
    return sum([int(x) for x in str(number)])

n = int(input())
counter = 0
for i in range(pow(10, n-1), pow(10, n)):
    if get_sum_decimal(i) == get_sum_binary(i):
        counter += 1
print(counter)