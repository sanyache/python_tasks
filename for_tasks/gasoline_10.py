"""
Дано ціни бензину 3 марок і три ємності різного об'єму.
 Яку найбільшу вартість можливо сплатити.
 1 2 3
 3 2 1
 14
"""
prices = list(map(int, input().split()))
volumes = list(map(int, input().split()))
prices.sort()
volumes.sort()
amount = 0
for price, volume in zip(prices, volumes):
    amount += price * volume
print(amount)
