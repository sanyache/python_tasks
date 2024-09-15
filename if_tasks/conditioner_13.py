"""
В кондиціонера можливі режими роботи:
freeze - охолодження, якщо температура в приміщенні вища, то понижує температуру
heat - обігрів, якщо температура в приміщенні нижча, то підвищує
auto -  підвищує або понижає температуру, якщо в цьому є потреба
fan - вентиляція приміщення без зміни температури.
За годину кондиціонер зможе змінити будь яку температуру до бажаної.
Дано: t_room, t_cond,
      mode
Визначити температуру через годину у приміщенні.
10 20
heat    - 20
10 20
freeze  - 10
"""
t_room, t_cond = map(int, input().split())
mode = input()
t_after = t_room
if mode == "heat":
    if t_room < t_cond:
        t_after = t_cond
elif mode == "freeze":
    if t_room > t_cond:
        t_after = t_cond
elif mode == "auto":
    t_after = t_cond
print(t_after)
t_after = t_room
match mode:
    case "heat":
        if t_room < t_cond:
            t_after = t_cond
    case "freeze":
        if t_room > t_cond:
            t_after = t_cond
    case "auto":
        t_after = t_cond
print(t_after)