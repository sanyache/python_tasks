"""
Розпакувати рядок
22D7AC18FGD
DDDDDDDDDDDDDDDDDDDDDDAAAAAAACFFFFFFFFFFFFFFFFFFGD
"""
s = input()
number = ''
unzip = ''
for char in s:
    if char.isdigit():
        number += char
    elif number:
        unzip += char*int(number)
        number = ''
    else:
        unzip += char
for i in range(0, len(unzip), 40):
    print(unzip[i:40+i])

