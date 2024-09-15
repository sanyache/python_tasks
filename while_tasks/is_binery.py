"""
визначити чи є задане невід'ємне ціле число бінарним(степінь двійки)

128 -   YES
125 - NO
"""
number = int(input())
if number == 0:
    print("NO")
else:
    while number % 2 == 0:
        number /= 2
    if number == 1:
        print("YES")
    else:
        print("NO")
