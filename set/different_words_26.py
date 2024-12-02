"""
Дано рядок. Визначити скільки в ньому може бути записано різних
слів довжини m
10 3
bbaabbbabb
Output
6
"""
n, m = map(int, input().split())
s = input()
words = [s[i:i+m] for i in range(len(s)-m + 1)]
set_words = set()
set_words.update(words)
print(len(set_words))