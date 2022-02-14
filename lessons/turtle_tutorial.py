from turtle import Turtle, colormode, done
colormode(255)

side_length: float = 300

leo: Turtle = Turtle()

leo.fillcolor(255, 100, 255)
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(side_length)
    leo.right(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.goto(0, 0)
bob.color(200, 100, 255)
bob.speed(50)
i: int = 0
while i < 1000:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.right(120.5)
    i += 1

done()
