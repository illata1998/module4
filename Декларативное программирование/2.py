# BEGIN
def odds(source):
    is_odd_position = lambda pair: pair[0] % 2 == 0  # noqa: E731
    get_value = lambda pair: pair[1]  # noqa: E731
    return list(map(
        get_value,
        (filter(is_odd_position, enumerate(source)))
    ))


def odds_from_odds(list_of_lists):
    return list(map(odds, odds(list_of_lists)))
