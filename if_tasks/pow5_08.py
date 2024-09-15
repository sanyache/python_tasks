"""
 Щоб піднести до квадрату число, яке закінчується на 5,
потрібно від числа відкинути 5, перемножити число що залишилося
на наступне і добавити 25
наприклад 125**2 -> 12*13=156 -> 15625
"""
number = int(input())
if number == 5:
    print(25)
else:
    cut_number = number//10
    print(str(cut_number*(cut_number+1))+'25')
number //= 10
print(number*(number+1)*100+25)
