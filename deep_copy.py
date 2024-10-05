from copy import deepcopy

a = [1,2,3,4,5,6,7,[0,1,2]]
c = a
c[1] = "apple"
print(a)
c = a.copy() # a[:]
c[1] = "orange"
print(a)
b = deepcopy(a)
a[0] = [0,1,2]
a[7][0] = 100
print(b)