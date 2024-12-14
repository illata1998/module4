# BEGIN
def non_empty_truths(list_of_lists):
    return [
        truths for truths in
        [[elem for elem in one_list if elem]  # noqa: WPS335
         for one_list in list_of_lists
         ]
        if truths
    ]
# END
