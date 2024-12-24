def path(start, stop):
    if start == stop:
        print (start, end=' ')
        return
    path(start, A[stop])
    print(stop, end=' ')


A = [0]*20
A[10] = 7
A[7] = 5
A[5] = 3
A[3] = 1
path(1, 10)