import  requests
import json
# licey.lit@gmail.com
def is_valid_email(email):
    response = requests.get(f' https://api.2ip.ua/email.json?email={email}')
    email_api = response.json()
    print(json.dumps(email_api, indent=4, sort_keys=True))
    return email_api['exist']

str_email = input()
print("Yes" if is_valid_email(str_email) else "No")