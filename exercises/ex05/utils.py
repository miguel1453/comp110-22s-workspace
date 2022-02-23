"""EX05 - various functions that deal with lists."""


__author__ = "730472629"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even numbers in a list."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0:
            xs.pop(i)
        else:
            i += 1
    return xs


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns the subest of the given paramets of a list."""
    i: int = start
    if i < 0:
        i = 0
    sub_list: list[int] = []
    if len(xs) == 0:
        return sub_list
    if end > len(xs):
        end = len(xs)
    while i < end and start < len(xs) and end:
        sub_list.append(xs[i])
        i += 1
    return sub_list


def concat(xs: list[int], ys: list) -> list[int]:
    """Makes new list where second list is added after first list."""
    concat_list: list[int] = []
    concat_list += xs
    concat_list += ys
    return concat_list