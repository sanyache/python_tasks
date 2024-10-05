"""
Археологами знайдено набір стародавніх копій старовинних манускриптів
 із міфами – різними історіями про давніх богів. Переписувачі цих
манускриптів в кожному імені зробити рівно по одній орфографічній помилці - тобто одну
з букв божественного імені замінили якоюсь іншою буквою.
Археологи змогли скласти список правильних написань імен богів. Виведіть для кожного бога
скільки разів його імя зустрічається в манускрипті ( тобто в слові зроблена рівно 1 помилка)
3
ZEUS
POSEIDON
AFINA
4
ZEVS
POSEYDON
AVYNA
ZERS
2 1 0
"""
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
        if len(god) == len(mistake):
            not_match = 0
            for ind in range(len(god)):
                if god[ind] != mistake[ind]:
                    not_match += 1
                if not_match == 2:
                    break
            if not_match == 1:
                counter += 1
    print(counter, end=' ')
