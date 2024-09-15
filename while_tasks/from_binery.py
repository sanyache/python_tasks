binary = input()
print(int(binary, 2))
nb = '0b' + binary
print(eval(nb))
binary = int(binary)
decimal = 0
pow = 1
while binary:
    decimal += (binary % 10)*pow
    binary //= 10
    pow *= 2
print(decimal)
