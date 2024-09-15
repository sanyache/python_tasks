"""
Написати функцію, яка повертає індекс першого входження в рядок
заданого символу. Якщо такого немає то повертає -1
"""
def find_el(s, el):
    f_ind = -1
    for ind, letter in enumerate(s):
        if letter == el:
            f_ind = ind
            break
    return f_ind

string = input()
symbol = input()
print(find_el(string, symbol))
