"""
The email address must have only one symbol @.
After this symbol @ may be one or two symbols '.'
The length of the name of the top-level domain maybe two or three symbols.
"""
def is_valid_email(string):
    if string.count('@') == 1:
        string = string[string.find('@')+1:]
    else:
        return False
    dots = string.split('.')
    if  not(1 < len(dots) <= 3) or not(2 <= len(dots[-1]) <= 3):
        return False
    return True
email = input()
print("Yes" if is_valid_email(email) else "No")