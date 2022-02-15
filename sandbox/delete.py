"""slefmewf"""

from turtle import Turtle, tracer, update, done 

leo: Turtle = Turtle()
leo.speed("fastest")
leo.color("black")
i: int = 0
tracer(0, 0)
width: int = 100
angle: float = 140
while i < 10:
    leo.forward(width)
    leo.right(angle)
    i += 1
update()
done()
