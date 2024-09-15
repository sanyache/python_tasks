"""
В будинку проживає n мешканців. Визначити номер найcтаршого
чоловіка. Якщо є декілька максимального віку, то вивести
першого, якщо чоловіків не має, вивести -1
Дано: n -  кількість мешканців. n пар, що значать вік і стать
0 - жін
1 - чол
--------
input
4
25 1
70 1
100 0
3 1
---------
output
2
"""
n = int(input())
# house = []
max_age = -1
seek_ind = -1
for i in range(n):
    age, gender = map(int, input().split())
    if gender == 1 and age > max_age:
        max_age = age
        seek_ind = i+1
# for ind, people in enumerate(house):
#     if people[1] == 1:
#         if people[0] > max_age:
#             max_age = people[0]
#             seek_ind = ind
print(seek_ind)