import re


def password_validator(password: str)->bool:
    while True:
        password_regex = re.compile(r'[A-Z]+[a-z]+\d+')
        match_object = password_regex.search(password)
        if match_object:
            return True
        else:
            return False

print(password_validator('Helloooo7'))









