"""
Хлопчику дістався майже щасливий квиток. Сума перших трьох цифр
відрізнялася лише на 1 від суми наступних трьох цифр.
Мабуть наступний чи попередній квиток щасливи? Так це чи ні?
3
715068 Yes
445219 No
012200 Yes
"""


def is_lucky(num):
    if len(num) < 6:
        num = '0'*(6 - len(num)) + num
    ticket = [int(x) for x in num]
    return sum(ticket[:3]) == sum(ticket[3:])


n = int(input())
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
for number in numbers:
    if is_lucky(str(number+1)) or is_lucky(str(number-1)):
        print("Yes")
    else:
        print("No")
