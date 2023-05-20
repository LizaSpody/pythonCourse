# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def first_func():
    def second_func():
        return 'return second function'

    return second_func


result_func = first_func()
print(result_func())
