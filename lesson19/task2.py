# Creaend=Noneown implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start, end=None, current=1):
    result = []
    if end is None:
        end = start
        start = 0
    while start < end:
        result.append(start)
        yield start
        start += current
    return result


assert list(in_range(0, 9, 2)) == list(range(0, 9, 2))
