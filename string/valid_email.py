"""
Чи є email  адреса валідною?
"""
def is_valid_email(string):
    counter_a = 0
    for ind, letter in enumerate(string):
        if letter == '@':
            counter_a +=1
            string = string[ind+1:]
            break
    else:
        return False
    for ind, symbol in enumerate(string):
        if symbol == '.':
            string = string[ind+1:]
            break
    else:
        return False
    if len(string) <= 1 or len(string) > 3:

        return False
    if '.' in string:
        return False
    return True

email = input()
print("Yes" if is_valid_email(email) else "No")