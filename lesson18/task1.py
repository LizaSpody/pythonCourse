# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check
# if the passed email parameter is a valid email string.

import re


class CheckEmail:
    def __init__(self, email):
        self.email = CheckEmail.validate(email)

    @staticmethod
    def validate(email):
        pattern = r"^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return email
        raise ValueError('Email not valid')


a = CheckEmail('abc.def@mail-archive.com')
b = CheckEmail('abc.def@mail.c')
print(a.email)
