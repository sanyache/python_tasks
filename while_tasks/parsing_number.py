# n = int(input())
# while n > 0:
#     print(n % 10, end=' ')
#     n //= 10
# n = input()
# s = 0
# for dig in n:
#     s += int(dig)
# print(s)
n = [x for x in input() if int(x) % 2 != 0]
number = ''
for dig in n:
    number += dig
print(int(number))
# print(sum(n))
