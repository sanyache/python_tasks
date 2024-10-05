"""
Видалити з натурального числа всі непарні цифри
і роздрукувати отримане чило.
"""
n = [x for x in input() if int(x) % 2 == 0]
s = ''.join(n)
print(int(s))
# print(''.join([ x for x in input() if int(x) % 2 == 0]))
# for ch in n:
#     s += ch
