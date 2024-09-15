"""
get list on numbers from string
"""
import re

s = input()
numbers = []
number = ''
for letter in s:
    if letter.isdigit():
        number += letter
    elif number:
        numbers.append(int(number))
        number = ''
if number:
    numbers.append(int(number))
print(numbers)
list_num = [int(x) for x in re.findall(r'\d+', s)]
print(list_num)
