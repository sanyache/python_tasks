"""
Визначити день програміста у вказаному році. Відзначається в 256 день року
Якщо високосний - то 13/09/2000
інакше - 12/09/2009
високосний рік - якщо номер року ділиться на 400
або ділиться на 4, але не ділиться на 100
"""
year = int(input())
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    day = 13
else:
    day = 12
print(f'{day}/09/{year}')
