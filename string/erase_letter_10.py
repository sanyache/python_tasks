"""
Дано  порядковий номер символу і слово відокремлене деякою кількістю пробілів.
Видалити символ за даним номером.
5 HelloWorld - HellWorld
"""
n, w = input().strip().split()
n = int(n)
new_word = w[:n-1] + w[n:]
print(new_word)
