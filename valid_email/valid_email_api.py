import  requests

def is_valid_email(email):
    response = requests.get(f' https://api.2ip.ua/email.json?email={email}')
    email_api = response.json()
    return email_api['exist']

str_email = input()
print("Yes" if is_valid_email(str_email) else "No")