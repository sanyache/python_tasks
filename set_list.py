n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
set1 = set()
set2 = set()
set1.update(list1)
set2.update(list2)
if set1 == set2:
    print('1')
else:
    print('0')
