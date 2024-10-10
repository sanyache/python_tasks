import re

n = int(input())
gods = []
for _ in range(n):
    gods.append(input())
m = int(input())
mistakes = []
for _ in range(m):
    mistakes.append(input())
for god in gods:
    counter = 0
    for mistake in mistakes:
        pattern = "'(" + god + ')' + "'"
        print(pattern)
        m = re.findall(god, mistake)
        print(m)