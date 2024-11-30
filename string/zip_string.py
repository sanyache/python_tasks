"""
DDDDDDDDDDDDDDDDDDDDDDAAAAAAACFFFFFFFFFFFFFFFFFFGD
22D7A1C18F1G1D
"""
s = input()
tmp = ''
number = 0
zip_str = ''
for letter in s:
    if letter == tmp:
        number += 1
        continue
    elif number:
        zip_str += str(number) + tmp
    number = 1
    tmp = letter

print(zip_str + str(number)+tmp)