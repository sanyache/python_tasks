"""
Дано  n. Послідовність будується за принципом:
112123123412345123456123456712345678123456789123456789101234567891011123456
Вивести цифр, яка стоїть на n позиції.
3 -2
20 -5
"""
n = int(input())
s = ''
cur = ''
cur_len = 1
while len(s)<n:
    cur = ''
    for i in range(1, cur_len):
        cur += str(i)
    s += cur
    cur_len += 1
print(s[n-1])