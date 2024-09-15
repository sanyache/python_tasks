"""
Визначити чи квиток є щасливим(сума перших трьох дор сумі трьох останніх)
385916 - Yes
123456 - No
"""
ticket = [int(x) for x in input()]
if sum(ticket[:3]) == sum(ticket[3:]):
    print("YES")
else:
    print("NO")
