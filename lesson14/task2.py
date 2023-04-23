# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def wrapper(name):
            newStr = func(name)
            for i in words:
                newStr = newStr.replace(i, '*')
            return newStr
        return wrapper
    return decorator
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
