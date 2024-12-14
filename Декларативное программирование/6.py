# BEGIN
def my_map(function, source):
    for arg in source:
        yield function(arg)


def my_filter(condition, source):
    for arg in source:
        if condition(arg):
            yield arg


def replicate_each(number, source):
    for value in source:
        yield from (value for _ in range(number))
