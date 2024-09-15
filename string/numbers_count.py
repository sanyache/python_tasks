"""
Підрахувати кількість чисел у рядку.
"""
numbers = input()
counter = 0
flag = False
for letter in numbers:
    if letter.isdigit():
        flag = True
    elif flag:
        flag = False
        counter += 1


if flag:
    counter += 1
print(counter)
