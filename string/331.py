"""
Задано деякий абзац тексту на невідомій мові. Назвемо речення чемпіоном,
якщо кількість слів паліндромів у ньому максимальна.
Якщо таких речень декілька, то чемпіоном є те речення, яке зустрілось першим.
 Літерами алфавіту у невідомій мові є літери латинського алфавіту
 та арабські цифри. Гарантується, що інші символи, крім пропусків
 та розділових знаків, у тексті відсутні.
 Oo, it aaa is not bb. More ana more non abc. 1

Flud!  Oow, it aaaw is not bbw... Aw bw cw dw ew!!!
 A-aw,  b-bw,  cc-ccw  de-edw  Dedw  IOIw.
 Abaw bababw madamw madamw - MIMw Mimw mIMw!!!
Eeeew uuuw aaw bbbw cw cccw dddw swsw. More anaw more nonw abc.
 Aaw bbw ccw ddw eew?!     0
"""

import re

def is_palindrome(word):
    return word == word[::-1]

s = input()
s0 = [ x.strip() for x in (re.split(r"[!.?]", s)) if x]
max_palindrome = 0
max_counter = 0
for index, sentence in enumerate(s0):
    counter = 0
    for item in sentence.split():
        if not item[-1].isalnum():
            item = item[:-1]
        if item and is_palindrome(item.casefold()):
            counter += 1
    if counter > max_counter:
        max_counter = counter
        max_palindrome = index + 1

print(max_palindrome)