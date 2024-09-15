"""
Задано послідовність із символів '<', '-', '>'.
Знайти кількість стріл які є в даній послідовності.
Стріли мають вигляд:  ‘>>-->’ і ‘<--<<’.
<<<<>>--><--<<--<<>>>--><<<<<   4
"""
s = input()
counter = 0
pos = 0
while pos < len(s):
    pos = s.find('>>-->', pos)
    if pos == -1:
        break
    pos += 4
    counter += 1
pos = 0
while pos < len(s):
    pos = s.find('<--<<', pos)
    if pos == -1:
        break
    pos += 4
    counter += 1
print(counter)


