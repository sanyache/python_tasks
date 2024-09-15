"""
Шулер поклав кульку під лівий ковпачок. Він здійснює декілька перестановок
визначте під яким ковпачком буде кулька після всіх перестановок.
Перестановки
А - змінити місцями лівий та цетральний
В - змінити місцями правий та центральний
С - змінити місцями лівий та правий
CBABCACCC	1
"""
permutations = input()
caps = [1, 0, 0]
for per in permutations:
    if per == 'A':
        caps[0], caps[1] = caps[1], caps[0]
    elif per == 'B':
        caps[1], caps[2] = caps[2], caps[1]
    else:
        caps[0], caps[2] = caps[2], caps[0]
for ind, el in enumerate(caps):
    if el == 1:
        print(ind+1)
        break
print(caps.index(1)+1)