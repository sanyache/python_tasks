def reverse_str(s, i):
    if i < 1:
        return ''
    if i == 1:
        return s[0]
    return s[i-1] + reverse_str(s, i -1)

s = input()
print(reverse_str(s, len(s)))