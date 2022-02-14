"""Insert here """

__author__ = "730472629"

from turtle import Turtle, colormode, done


def main() -> None:
    """Entrypoint of my scene"""
    poot: Turtle = Turtle()
    backround(poot, 100)
    done()
    
    
def backround(a_turtle: Turtle, width: float) -> None:
    """"""
    a_turtle.color("blue")
    a_turtle.begin_fill()
    a_turtle.goto((0 - (width / 2)), width)
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


if __name__ == "__main__":
    main()