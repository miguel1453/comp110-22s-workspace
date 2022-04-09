"""Lessons 25 magic mehthods"""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y, components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def __str__(self) -> str: 
        """Produces a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:  # if you don't define a __str__ the __repr__ method will be called by default
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def scale(self, factor: float) -> Point:
        """Immutable: multiplies components by factor without mutations."""
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called")
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """"""
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError
            

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])

print()
print()

p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)  # Automatically calls __str__
p1_as_a_str: str = str(p1)  # Chekcs and sees if the class for the object has a str method defined in it
print(p1_as_a_str)

p1_repr: str = repr(p1)  # Built in repr!!
print(p1_repr)
