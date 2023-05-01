# Create your own implementation of a built-in function enumerate,
# named `with_index`, which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


arr = [16, 18, 3, 6, 7]

for i in with_index(arr):
    print(i)
