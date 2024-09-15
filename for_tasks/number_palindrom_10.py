"""
Визначити чи є число паліндромом. Паліндромон — слово, число,
набір символів, словосполучення або віршований рядок,
що однаково читається в обох напрямках.
12345 - No
12321 - Yes
"""


def is_palindrom(n):
    for i in range(0, len(n)//2):
        if n[i] != n[len(n)-i-1]:
            return False
    return True


number = input()
if number == number[::-1]:
    print("Yes")
else:
    print("No")
print(is_palindrom(number))
