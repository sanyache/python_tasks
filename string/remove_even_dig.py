"""
Видалити з натурального числа всі непарні цифри
і роздрукувати отримане чило.
"""
n = [x for x in input() if int(x) % 2 == 0]
s = ''
for ch in n:
    s += ch
print(int(s))