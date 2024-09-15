"""
Дано рядок. Знайти найдовшу неперервну послідовність 0
00101110000110 4
"""
import re

s = input()
counter = 0
max_counter = 0
for ch in s:
    if ch == '0':
        counter += 1
    else:
        counter = 0
    if counter > max_counter:
        max_counter = counter
print(max_counter)

s0 = [len(x) for x in re.findall(r"0+", s)]
print(max(s0))