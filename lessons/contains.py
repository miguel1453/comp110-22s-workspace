"""Example of a Function that searches through a list."""


def main() -> None:
    print(contains("Kevin", ["Kanye West", "Pete Davidson"]))


# define a function names contians
# Two parameters:
#  1.needle - the string we're searching for
def contains(needle: str, haystack: list[str]) -> bool:

    #  2. haystack - the list we're searching through
    # Algorithm:
    #  For each item in the haystack
    #   Test if it is equal to the needle
    #       If so, return True
    for item in haystack:
        if item == needle:
            return True
    #  After testing all items, return False, because not found
    # Returns true if needle in haytack, false otherwise. 
    return False


# This allows to call certain functions without running through main.
if __name__ == "__main__":
    main()
