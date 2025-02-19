import re

n = int(input())
data = []
rez = []
for _ in range(n):
    row = input()
    oper, string = row[0], row[1:]
    if oper == '+':
        data.append(string)
    else:
        counter = 0
        for item in data:
            pattern = '^' + string
            if re.match(pattern, item):
                counter += 1
        rez.append(counter)
for item in rez:
    print(item)
