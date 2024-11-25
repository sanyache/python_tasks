"""
Задано слово та кросворд.
Визначіть чи міститься слово у кросворді n*n
Input:
5 hello
a b c d e
h e l l o
w o r l d
c d f r h
v t r e t
Output:
Yes
"""
def is_in_crossword(n, word, matrix):
    if len(word) != n:
        return False
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != word[j]:
                break
        else:
            return True
    for i in range(n):
        for j in range(n):
            if matrix[j][i] != word[j]:
                break
        else:
            return True
    return False

dimension, control_word = input().split()
dimension = int(dimension)
crossword = [[x for x in input().split()] for _ in  range(dimension)]
print("Yes" if is_in_crossword(dimension, control_word, crossword) else "No")