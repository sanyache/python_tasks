"""
Дано натуральне число n. Визначити скільки різних трьохзначних чисел може
утворитися видаленням 3 цифр з цого десяткового представлення
12 - 0
111111111110011111111  - 4
"""
from itertools import combinations

s = input()
if len(s) < 3:
    print(0)
    exit()
combs = list(combinations(s, 3))
#print(combs)
set_num = {x for x in combs if 99 < int(''.join(x)) < 1000}
print(set_num)
print(len(set_num))