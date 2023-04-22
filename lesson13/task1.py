# Write a Python program to detect the number of local variables declared in a function.

d = 15


def amountLocal():
    a = 2
    b = 3
    return locals()


c = 7

print(amountLocal())
