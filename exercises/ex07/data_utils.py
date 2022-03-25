"""Dictionary related utility functions."""

__author__ = "730472629"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, 'r', encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of strings of all values in a given column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-orientated table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        result[column] = column_values(table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        n_list: list[str] = []
        i: int = 0
        while i < N and i < len(table):
            n_list.append(table[column][i])
            i += 1
        result[column] = n_list
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns a columb-based table with only specfic subset of columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two columb-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(column: list[str]) -> dict[str, int]:
    """Produces a dict with the count of each list value."""
    result: dict[str, int] = {}
    for item in column:
        if item in result:
            result[item] += 1
        else:   
            result[item] = 1
    return result
