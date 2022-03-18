"""Main function for Ex06: invert, favorite_color, and count."""


__author__ = "730472629"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Makes a new dictionary that is the original one but inverted."""
    inverted: dict[str, str] = dict()
    for key in original:
        if original[key] in inverted:
            raise KeyError("Cannot have the same key more than once in dictionaries!")
        inverted[original[key]] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Outputs top favorite color."""
    colors: dict[str, int] = dict()
    for name in dictionary:
        if dictionary[name] in colors: 
            colors[dictionary[name]] += 1
        else:
            colors[dictionary[name]] = 1
    winner: str = ""
    for key in colors:
        if winner == "":
            winner = key
        if colors[key] > colors[winner]:
            winner = key
    return winner


def count(xs: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dict of a count of each key."""
    dictionary: dict[str, int] = dict()
    for key in xs:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary