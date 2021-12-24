from turtle import *


def make_ground():
    border.up()
    border.goto(START_COORDINATE, START_COORDINATE)
    border.down()
    border.forward(WINDOW_SIZE - 100)


def move_ball(x, y):
    global gravity_speed
    if not touch_border:
        gravity_speed -= 0.01
    elif touch_border:
        gravity_speed += 0.1
    ball.goto(x, y + gravity_speed)


def check_touch(x, y):
    global touch_border, gravity_speed
    if y <= START_COORDINATE + 150:
        touch_border = True
        gravity_speed += 0.03
        print(y, START_COORDINATE + 15)
    if y >= START_COORDINATE + 15:
        touch_border = False



WINDOW_SIZE = 600
START_COORDINATE = (WINDOW_SIZE // 2 + 50) * -1 + 100

touch_border = False

gravity_speed = 0.01

window = Screen()
window.title('Gravity')
window.setup(WINDOW_SIZE, WINDOW_SIZE)

border = Pen()
border.width(5)
border.color('blue')
border.hideturtle()

ball = Pen()
ball.hideturtle()
ball.up()
ball.goto(0, WINDOW_SIZE // 2 - 50)
ball.showturtle()
ball.shape('circle')
ball.color('red')


make_ground()

while True:
    x, y = ball.pos()
    move_ball(x, y)
    check_touch(x, y)
    tracer(1)