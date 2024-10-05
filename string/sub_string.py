"""
Знаходження кількості входжень підрядка. Тривіальний метод
aaabcccababcaabcc
abc    3
"""
s = input()
sub = input()
counter = 0
for i in range(len(s) - len(sub) + 1):
    for j in range(len(sub)):
        if not s[i+j] == sub[j]:
            break
    else:
        counter += 1
print(counter)
print(s.count(sub))