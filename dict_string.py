"""
Скласти програму яка визначає чи із заданого набору букв
можна утворити задані слова
"""
from collections import Counter
n = int(input())
words = [input() for _ in range(n)]
letters = input()
counter =0
map_letters = Counter(letters)
for word in words:
    map_word = Counter(word)
    if all([map_word[letter] <= map_letters[letter] for letter in word]):
        counter += 1
print(counter)
