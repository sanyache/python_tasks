"""
Два учні вирішували задачі в 5 різних категоріях.
Перемога над іншим в категорії дає 1 бал
Хто переміг в контесті?
3 4 5 1 2
3 3 3 4 1
first
1 2 3 4 5
5 4 3 2 1
draw

"""
first = list(map(int, input().split()))
second = list(map(int, input().split()))
score_1 = 0
score_2 = 0
for i in range(5):
    if first[i] > second[i]:
        score_1 += 1
    if first[i] < second[i]:
        score_2 += 1
winner = "nobody"
if score_1 > score_2:
    winner = "first"
if score_1 < score_2:
    winner = "second"
print("winner is a {} student".format(winner))
