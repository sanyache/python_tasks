"""
Дано речення порахувати кількість слів.
Hello, world!  2
"""
s = [x for x in input().split() if not
     (len(x)== 1 and not x.isalnum()) ]
print(len(s))