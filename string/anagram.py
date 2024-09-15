"""
Рядок S1 називається анаграмою рядка S2, якщо він утворюється з перестановок
літер S2. Дано 2 рядки, перевірити чи S1 є анаграмою S2.
LISTEN
SILENT  YES
ABBA
BAAA    NO
"""
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

string1 = input()
string2 = input()
if is_anagram(string1, string2) :
   print("YES")
else:
    print("NO")