"""An example of Unione types."""


from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that ca be called with _either_ an int or a str argument."""
    if isinstance(info, str): 
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")


log("Hello, World")
log(110)