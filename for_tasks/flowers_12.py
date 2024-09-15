"""
У різдвяний вечір на віконці стояло три квіточки, зліва направо:
герань, крокус та фіалка. Щоранку Маша витирала віконце і міняла місцями квітка,
що стоїть праворуч, з центральною квіткою.
А Таня щовечора поливала квіточки і міняла місцями ліву та центральну квітку.
Потрібно визначити порядок квітів вночі після К днів.
G C V
1 - VGC
5 - CVG
"""
flowers = ['G', 'C', 'V']
days = int(input("Enter number of days="))
for _ in range(days):
    flowers[1], flowers[2] = flowers[2], flowers[1]
    flowers[0], flowers[1] = flowers[1], flowers[0]
for flower in flowers:
    print(flower, end=' ')
