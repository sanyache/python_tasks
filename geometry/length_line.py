"""
Обчислити довжину відрізка заданого координатами x1,y1,x2,y2
3 4 8 4 - 5
"""
import math
x1, y1, x2, y2 = map(float, input().split())
length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(length)
