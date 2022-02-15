"""Insert here """

__author__ = "730472629"

from turtle import Turtle, colormode, done
from random import randint
colormode(255)


def main() -> None:
    """Entrypoint of my scene"""
    poot: Turtle = Turtle()
    backround(poot, 750)
    stars()
    towers(poot, 400)
    towers(poot, 200)
    done()
    
    
def backround(a_turtle: Turtle, width: float) -> None:
    """"""
    a_turtle.speed(100)
    a_turtle.color(25, 7, 95)
    a_turtle.begin_fill()
    a_turtle.goto((0 - (width / 2)), (width / 2))
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def stars() -> None:
    """Creates stars on the backround!"""
    zeus: Turtle = Turtle()
    zeus.shape("turtle")
    zeus.color("white", "black")
    zeus.penup()
    zeus.speed(0)
    zeus.goto(-375, -340)
    iteration: int = 0
    new_distance: int = 0
    while iteration < 10:
        new_distance += 70
        count: int = 0
        """draws row of stars"""
        while count < 10:
            i: int = 0
            """Draws a singular star"""
            while i < 6:
                zeus.pendown()
                zeus.forward(30)
                zeus.right(144)
                zeus.penup()
                i += 1
            zeus.setheading(0.0)
            zeus.forward(50)
            count += 1
        zeus.setheading(0.0)
        zeus.goto(-375, -340 + new_distance)
        iteration += 1


def towers(a_turtle: Turtle, height: int) -> None:
    """Function for the towers!"""
    a_turtle.color("black", (79, 77, 76))
    a_turtle.pensize(5)
    a_turtle.penup()
    a_turtle.home()
    a_turtle.goto(-375, -375)
    num_buildings: int = randint(3, 10)
    space_available: float = 750 / num_buildings
    tower_buffer = space_available * .10
    tower_width: float = space_available - (tower_buffer)
    i: int = 0
    while i < num_buildings:
        a_turtle.begin_fill()
        a_turtle.pendown()
        a_turtle.begin_fill()
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.right(90)
        a_turtle.forward(tower_width)
        a_turtle.right(90)
        a_turtle.forward(height)
        a_turtle.end_fill()
        a_turtle.setheading(0.0)
        a_turtle.forward(tower_buffer)
        i += 1
    tower_windows(a_turtle, tower_width, tower_buffer, height, num_buildings)
    

def tower_windows(a_turtle: Turtle, tower_width: float, tower_buffer: float, height: float, num_buildings: int) -> None: 
    """Puts the windows on the buildings!"""
    leo: Turtle = Turtle()
    leo.pensize(3)
    leo.shape("turtle")
    leo.color("black", "yellow")
    leo.speed(1000)
    leo.penup()
    leo.goto(-375, -375)
    width_available: float = tower_width * .25
    height_available: float = height / 5
    window_width_buffer: float = width_available * .4
    window_height_buffer: float = height_available * .4
    window_width: float = width_available * .6
    window_height: float = height_available * .6
    iteration: int = 0
    leo.goto((-375 - (window_width_buffer / 2)), (-375 - (window_height_buffer / 2)))
    while iteration < num_buildings:
        count: int = 0
        while count < 5:
            i: int = 0
            while i < 4:
                leo.forward(window_width_buffer)
                leo.left(90)
                leo.forward(window_height_buffer)
                leo.right(90)
                leo.pendown()
                leo.begin_fill()
                leo.forward(window_width)
                leo.left(90)
                leo.forward(window_height)
                leo.left(90)
                leo.forward(window_width)
                leo.left(90)
                leo.forward(window_height)
                leo.left(90)
                leo.end_fill()
                leo.penup()
                leo.backward(window_width_buffer)
                leo.right(90)
                leo.forward(window_height_buffer)
                leo.left(90)
                leo.forward(width_available)
                i += 1
            leo.backward(tower_width)
            leo.left(90)
            leo.forward(height_available)
            leo.right(90)
            count += 1
        leo.forward(tower_buffer + tower_width)
        leo.right(90)
        leo.forward(height)
        leo.left(90)
        iteration += 1

    
if __name__ == "__main__":
    main()