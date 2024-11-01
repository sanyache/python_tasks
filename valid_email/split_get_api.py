"""
Get API and email validation
"""
import  requests
import json

class CantGetAPI(Exception):
    """unable to receive data from api"""
    def __str__(self):
        return "unable to receive data from api"


def _get_email_valid_api(email):
    try:
        response = requests.get(f' https://api.2ip.ua/email.json?email={email}')

    except:
        raise CantGetAPI
    else:
        email_api = response.json()
        return email_api

# licey.lit@gmail.com
def is_valid_email(email):
    data = _get_email_valid_api(email)
    print(json.dumps(data, indent=4, sort_keys=True))
    return data['exist']

if __name__ == "__main__":
    str_email = input("Enter email address ")
    try:
        is_valid = is_valid_email(str_email)
    except CantGetAPI as e:
        print(f"Error: {e}")
    else:
        print("Yes" if is_valid else "No")