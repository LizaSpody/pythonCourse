# Write a class TypeDecorators which has several methods for converting results of functions to a specified type ( if it's possible):
#
# methods:
#
# to_int
#
#
# to_str
#
# to_bool
#
# to_float
#
# Don't forget to use @wraps

from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            try:
                return int(func(*args))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            return str(func(*args))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            return bool(func(*args))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            try:
                return float(func(*args))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        return wrapper


@TypeDecorators.to_int
def do_nothing(string):
    return string

@TypeDecorators.to_str
def do_string(string):
    return string

@TypeDecorators.to_bool
def do_something(string):
    return string

@TypeDecorators.to_float
def do_float(string):
    return string


assert do_nothing('25') == 25
assert do_string(456789) == '456789'
assert do_something('True') is True
assert do_float('3.0') == 3.0
