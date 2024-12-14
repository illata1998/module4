# BEGIN
def each2d(test, matrix):
    return all(
        test(cell)
        for row in matrix
        for cell in row
    )


def some2d(test, matrix):
    return any(
        test(cell)
        for row in matrix
        for cell in row
    )


def sum2d(test, matrix):
    return sum(
        cell
        for row in matrix
        for cell in row if test(cell)
    )
# END
