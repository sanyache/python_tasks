def bin_gen(i , prefix=''):
    if i == 0:
        print(prefix)
        return
    bin_gen(i-1, prefix + '0')
    bin_gen(i-1, prefix + '1')

n = int(input())
bin_gen(n)