"""slefmewf"""

from turtle import Turtle 

leo: Turtle = Turtle()
leo.speed("fastest")
leo.color("black")
i: int = 0
width: int = 100
angle: float = 140
while i < 20:
    leo.forward(width)
    leo.right(angle)
    i += 1
