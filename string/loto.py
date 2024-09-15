"""
Дано лотерейний номер без ведучих нулів. Викрислити дві цифри,
щоб отрималось найбільше значення.
995051 9955
324710  4710
9876543 98765
"""
s = input()
delete_counter = 0
i = 0
while i < len(s)-1:
    if s[i] < s[i+1]:
        s = s.replace(s[i], '')
        delete_counter += 1
        i = max(0, i-1)
    else:
        i += 1
    if delete_counter == 2:
        break
if delete_counter < 2:
    s = s[:-(2-delete_counter)]
print(s)
