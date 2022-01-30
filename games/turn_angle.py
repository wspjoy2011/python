from turtle import *
from math import atan2, pi

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def change_heading(x, y):
    x1 = x
    y1 = y

    x2 = player.xcor()
    y2 = player.ycor()

    heading = atan2(y1 - y2, x1 - x2)
    heading = heading * 180.0 / pi

    player.setheading(round(heading))


window = Screen()
window.title('Heading onclick')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onclick(change_heading, btn=1)

player = Turtle(shape='turtle')
player.color('red')
player.shapesize(2.0, 2.0)


window.listen()
window.mainloop()