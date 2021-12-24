from turtle import *
from random import randint, random


class Ball:
    def __init__(self):
        self.ball = Pen()
        self.ball.touch_vertical_border = False
        self.ball.touch_horizontal_border = False


def make_window():
    window.setup(600, 600)
    window.title('Bouncing ball')
    window.onkey(exit, 'Escape')


def make_pen():
    border.speed(0)
    border.color('red')
    border.width(5)
    border.hideturtle()
    border.up()
    border.goto(BORDER_COORDINATES, BORDER_COORDINATES)
    border.down()


def draw_border(color):
    border.color(color)
    for _ in range(4):
        border.fd(SIZE)
        border.left(90)


def make_ball(ball):
    ball.shape('circle')
    ball.color(random(), random(), random())
    ball.hideturtle()
    ball.up()
    ball.goto(randint(-250, 250), randint(-250, 250))
    ball.showturtle()


def move_ball(x, y, ball):
    if not ball.touch_horizontal_border:
        x += direction
    elif ball.touch_horizontal_border:
        x -= direction

    if not ball.touch_vertical_border:
        y += direction
    elif ball.touch_vertical_border:
        y -= direction

    ball.goto(x, y)


def check_border(x, y, ball):
    if x >= SIZE // 2 - 10:
        ball.touch_horizontal_border = True
    elif x <= SIZE // 2 * -1 + 10:
        ball.touch_horizontal_border = False

    if y >= SIZE // 2 - 10:
        ball.touch_vertical_border = True
    elif y <= SIZE // 2 * -1 + 10:
        ball.touch_vertical_border = False


SIZE = 500
BORDER_COORDINATES = SIZE // 2 * -1
direction = 2
touch_horizontal_border = False
touch_vertical_border = False


window = Screen()

border = Pen()

balls = [Ball() for _ in range(20)]

for i in range(len(balls)):
    make_ball(balls[i].ball)

make_pen()
draw_border('red')


while True:
    for i in range(len(balls)):
        x_red, y_red = balls[i].ball.pos()
        move_ball(x_red, y_red, balls[i].ball)
        check_border(x_red, y_red, balls[i].ball)
        tracer(10)
