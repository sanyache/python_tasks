"""
Написати програму, яка повертає  всі індекси входження в рядок
заданого символу, використовуючи ф-цію find_el(у функцію додати третій параметр - індекс, з якого
починати пошук). Якщо такого немає то повертає -1
"""
def find_el(s, el, pos=0):
    f_ind = -1
    for ind, letter in enumerate(s[pos:]):
        if letter == el:
            f_ind = ind + pos
            break
    return f_ind

string = input()
symbol = input()
position = 0
is_find = False
while position < len(string):
    position = find_el(string, symbol, position)
    if position == -1:
        break
    else:
        is_find = True
    print(position, end=' ')
    position += 1
if not is_find:
    print(-1)
