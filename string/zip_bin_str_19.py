"""
Дано бінарну послідовність. Застосуйте такий спосіб стиснення:
1 a, 01 - b, 001 - c, 0001 - d і так до z
Input:
101
Output:
ab
Input:
101001
Output:
abc
"""
s = input()
z = 0
for i in s:
    if i == '0':
        z += 1
    else:
        print(chr(z + 97), end='')
        z = 0