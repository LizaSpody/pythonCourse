# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def first_func():
    def second_func():
        return 'return second function'

    return second_func()


print(first_func())
