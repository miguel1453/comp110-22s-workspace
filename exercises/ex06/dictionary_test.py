"""Tests for dictionary functions."""


__author__ = "730472629"


from dictionary import invert, favorite_color, count


# Tests for invert function
def test_invert_use_case() -> None:
    """Normal use test for invert function."""
    dictionary: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(dictionary) == {"b": "a", "d": "c"}


def test_invert_use_case_1() -> None:
    """Another normal use test for invert function."""
    dictionary: dict[str, str] = {'hello': 'goodbye', 'hola': 'adios', 'miguel': 'villasenor'}
    assert invert(dictionary) == {'goodbye': 'hello', 'adios': 'hola', 'villasenor': 'miguel'}


def test_invert_edge_case() -> None:
    """Edge case for invert fucntion."""
    dictionary: dict[str, str] = dict()
    assert invert(dictionary) == {}


# Tests for favorite_color function
def test_color_use_case() -> None:
    """Norma use test for favorite_color."""
    dictionary: dict[str, str] = {'miguel': 'blue', 'timothy': 'red', 'ethan': 'blue'}
    assert favorite_color(dictionary) == "blue"


def test_color_use_case_1() -> None:
    """Another use case for favorite_color function."""
    dictionary: dict[str, str] = {'timothy': 'red', 'flash': 'red', 'miguel': 'yellow', 'kris': 'blue', 'azul': 'yellow'}
    assert favorite_color(dictionary) == 'red'


def test_color_edge_case() -> None:
    """Edge case for favorite_color function."""
    dictionary: dict[str, str] = dict()
    assert favorite_color(dictionary) == ""


# Tests for count function
def test_count_use_case() -> None:
    """Use case for count function."""
    xs: list[str] = ['1', '2', '1', '1', '3', '4', '4']
    assert count(xs) == {'1': 3, '2': 1, '3': 1, '4': 2}


def test_count_use_case_1() -> None:
    """Another use case for count function."""
    xs: list[str] = ['blue', 'blue', 'red', 'orange', 'purple', 'red']
    assert count(xs) == {'blue': 2, 'red': 2, 'orange': 1, 'purple': 1}


def test_count_edge_case() -> None:
    """Edge case for count function."""
    xs: list[str] = list()
    assert count(xs) == {}
