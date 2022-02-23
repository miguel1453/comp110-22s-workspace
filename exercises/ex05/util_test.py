"""Tests for util.py."""


__author__ = "730472629"


from utils import only_evens, sub, concat


# tests for only_evens function
def test_no_list() -> None: 
    """Test for empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_list_no_even() -> None:
    """Test for list being all odd."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_list_all_even() -> None:
    """Tests for all values being even."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


# tests for sub function
def test_four_nums() -> None:
    """Basic use test."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_negative_start() -> None:
    """Negative start test."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -1, 4) == [10, 20, 30, 40]


def test_list_empty() -> None:
    """Empty list test."""
    xs: list[int] = []
    assert sub(xs, 1, 3) == []


def test_start_greater_len_list() -> None:
    """Test for when the start is greater than length of list."""
    xs: list[int] = [10, 20, 30]
    assert sub(xs, 4, 6) == []


def test_end_greater_len_list() -> None:
    """Test for when the end value is greater than len of list."""
    xs: list[int] = [10, 20, 30]
    assert sub(xs, 0, 6) == [10, 20, 30]


def test_end_negative() -> None:
    """Test for when the end is less than 0."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, -2) == []


def test_list_unmutated() -> None:
    """Test to make sure original lists are left unaltered."""
    xs: list[int] = [10, 20, 30, 40]
    sub(xs, 1, 3)
    assert xs == [10, 20, 30, 40]


# tests for concat function
def test_two_lists() -> None:
    """Basic use test."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_empt_lists() -> None:
    """Test for when list is empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_one_empty_list() -> None:
    """Tests for when one list is empty."""
    xs: list[int] = []
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [4, 5, 6]


def test_two_new_lists() -> None:
    """Another basic use test."""
    xs: list[int] = [1, 2, 3, 3, 2, 1]
    ys: list[int] = [4, 5, 6, 9, 10]
    assert concat(xs, ys) == [1, 2, 3, 3, 2, 1, 4, 5, 6, 9, 10]


def test_no_mutation() -> None:
    """Tests to see that there has been no mutations fone to og lists."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    concat(xs, ys)
    assert xs == [1, 2, 3] and ys == [4, 5, 6]