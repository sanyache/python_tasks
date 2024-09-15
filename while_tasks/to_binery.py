n = int(input())
python_bin = bin(n)[2:]
binary = ''
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
if binary == python_bin:
    print(binary)
else:
    print("you have a mistake")

