"""
 Скільки банок фрби потрібно, щоб пофарбувати кімнату стіни у якої довжиною L,
 шириною W і висотою H, якщо одніє банки вистачить на 16м кв.
 8 8 2 - 4
 1 1 3 - 1
"""
L, W, H = map(int, input().split())
S = 2*H*(L + W)
if S % 16 != 0:
    print((S//16)+1)
else:
    print(S//16)
