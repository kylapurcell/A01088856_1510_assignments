import re


def password_validator(password: str)->bool:
    while True:
        password_regex = re.compile(r'[A-Z]+[a-z]+\d+')
        password_regex2 = re.compile(r'^.{7,}$')
        match_object = password_regex.search(password)
        match_object2 = password_regex2.search(password)
        if match_object and match_object2:
            return True
        else:
            return False


print(password_validator('hell00007'))









