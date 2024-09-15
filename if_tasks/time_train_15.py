"""
Дано час відправки потяга і час його слідування. Визначити час прибуття
(можливо на інші сутки)

00:00
10 10    10:10
01:02
4 6      05:08
11:00
22 0    09:00
"""
# from datetime import datetime, timedelta
# start = input()
# road = ':'.join(input().split())
# departure_time = datetime.strptime(start, '%H:%M')
# duration = datetime.strptime(road, '%H:%M')
# arrival_time = departure_time + timedelta(hours=duration.hour, minutes=duration.minute)
# print(datetime.strftime(arrival_time, "%H:%M"))
h_dep, m_dep = map(int, input().split(':'))
h_road, m_road = map(int, input().split())
amount_m = (h_dep*60+m_dep+h_road*60+m_road)
h = amount_m//60 % 24
m = amount_m % 60
print("{:02d}:{:02d}".format(h, m))
