"""Night sky scene using turtle."""

__author__ = "730472629"

from turtle import Turtle, Vec2D, colormode, tracer, update, done
from random import randint
colormode(255)

"""Here I use turtles to make a skyline! I coded this to where 
there will always be a random number of buildings (3 - 6) each time
this program is run. I also had to find my own ways on how to center
the drawings on the screen no matter the number of buildings randomly
assigned. I had to google around to find what Vec2D was to use position
in turtle, I hope that's okay! It made making the stars so much easier.
It also wouldn't let me put this whole doc string at the top so I put it here."""


SCREEN_WIDTH: float = 750


def main() -> None:
    """Entrypoint of my scene."""
    tracer(0, 0)  # disable all turtle's delay
    backround(SCREEN_WIDTH)
    stars()
    towers(SCREEN_WIDTH * .6)
    towers(SCREEN_WIDTH * .3)
    done()
    
    
def backround(width: float) -> None:
    """Creates the night sky."""
    atlas: Turtle = Turtle()
    atlas.hideturtle()
    atlas.color(25, 7, 95)
    atlas.begin_fill()
    atlas.goto((0 - (width / 2)), (width / 2))
    i: int = 0
    while i < 4:
        atlas.forward(width)
        atlas.right(90)
        i += 1
    atlas.end_fill()
    update()


def stars() -> None:
    """Creates stars on the backround."""
    zeus: Turtle = Turtle()
    zeus.hideturtle()
    zeus.color("white", "black")
    zeus.penup()
    zeus.goto((SCREEN_WIDTH / -2), (SCREEN_WIDTH / -2))
    iteration: int = 0
    distance: float = 0
    while iteration < SCREEN_WIDTH * .015:  # draws 10 lines of stars
        distance += SCREEN_WIDTH * .09
        count: int = 0
        while count < SCREEN_WIDTH * .1:  # draws a row of stars
            return_pos: Vec2D = zeus.position()
            i: int = 0
            while i < 10:  # draws a singular star
                zeus.pendown()
                zeus.forward(20)
                zeus.right(160)
                zeus.penup()
                i += 1
            zeus.goto(return_pos)
            zeus.setheading(0.0)
            zeus.forward(SCREEN_WIDTH * .1)
            count += 1
        zeus.setheading(0.0)
        zeus.goto((SCREEN_WIDTH / -2), (SCREEN_WIDTH / -2) + distance)
        iteration += 1
    update()


def towers(height: float) -> None:
    """Function for the towers."""
    hephaestus: Turtle = Turtle()
    hephaestus.color("black", (79, 77, 76))
    hephaestus.pensize(5)
    hephaestus.penup()
    hephaestus.home()
    hephaestus.goto((SCREEN_WIDTH / -2), (SCREEN_WIDTH / -2))
    num_buildings: int = randint(3, 10)
    space_available: float = SCREEN_WIDTH / num_buildings
    tower_buffer = space_available * .10
    tower_width: float = space_available - (tower_buffer)
    i: int = 0
    while i < num_buildings:
        hephaestus.begin_fill()
        hephaestus.pendown()
        hephaestus.begin_fill()
        hephaestus.left(90)
        hephaestus.forward(height)
        hephaestus.right(90)
        hephaestus.forward(tower_width)
        hephaestus.right(90)
        hephaestus.forward(height)
        hephaestus.end_fill()
        hephaestus.setheading(0.0)
        hephaestus.forward(tower_buffer)
        i += 1
    update()
    tower_windows(tower_width, tower_buffer, height, num_buildings)
    

def tower_windows(tower_width: float, tower_buffer: float, height: float, num_buildings: int) -> None: 
    """Puts the windows on the buildings."""
    hephaestus: Turtle = Turtle()
    hephaestus.hideturtle()
    hephaestus.pensize(3)
    hephaestus.color("black", "yellow")
    hephaestus.penup()
    hephaestus.goto((SCREEN_WIDTH / -2), (SCREEN_WIDTH / -2))
    width_available: float = tower_width * .25
    height_available: float = height / 5
    window_width_buffer: float = width_available * .4
    window_height_buffer: float = height_available * .4
    window_width: float = width_available * .6
    window_height: float = height_available * .6
    iteration: int = 0
    hephaestus.goto(((SCREEN_WIDTH / -2) - (window_width_buffer / 2)), ((SCREEN_WIDTH / -2) - (window_height_buffer / 2)))
    while iteration < num_buildings:
        count: int = 0
        while count < 5:
            i: int = 0
            while i < 4:
                hephaestus.forward(window_width_buffer)
                hephaestus.left(90)
                hephaestus.forward(window_height_buffer)
                hephaestus.right(90)
                hephaestus.pendown()
                hephaestus.begin_fill()
                hephaestus.forward(window_width)
                hephaestus.left(90)
                hephaestus.forward(window_height)
                hephaestus.left(90)
                hephaestus.forward(window_width)
                hephaestus.left(90)
                hephaestus.forward(window_height)
                hephaestus.left(90)
                hephaestus.end_fill()
                hephaestus.penup()
                hephaestus.backward(window_width_buffer)
                hephaestus.right(90)
                hephaestus.forward(window_height_buffer)
                hephaestus.left(90)
                hephaestus.forward(width_available)
                i += 1
            hephaestus.backward(tower_width)
            hephaestus.left(90)
            hephaestus.forward(height_available)
            hephaestus.right(90)
            count += 1
        update()
        hephaestus.forward(tower_buffer + tower_width)
        hephaestus.right(90)
        hephaestus.forward(height)
        hephaestus.left(90)
        iteration += 1

    
if __name__ == "__main__":
    main()