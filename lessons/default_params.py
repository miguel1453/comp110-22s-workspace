"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Example of a deafault paramter where y and z are 0 by default."""
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))