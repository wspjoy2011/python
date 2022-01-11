from turtle import *
from time import sleep
from random import choice
import winsound


def make_paddle_settings(paddle, start_x):
    paddle.hideturtle()
    paddle.speed(0)
    paddle.shape('square')
    paddle.shapesize(5.0, 1.0)
    paddle.color('white')
    paddle.up()
    paddle.goto(start_x, 0)
    paddle.height = 20
    paddle.width = 100
    paddle.showturtle()


def move_paddle(paddle, direction, speed=5):
    y = paddle.ycor()
    if direction == 'up' and y < SCREEN_HEIGHT // 2 - paddle.width // 2 - 10:
        paddle.sety(y + speed)
    elif direction == 'down' and y > -SCREEN_HEIGHT // 2 + paddle.width // 2 + 20:
        paddle.sety(y - speed)


def check_ball_border(ball):
    global score_a, score_b
    x = ball.xcor()
    y = ball.ycor()

    if y > SCREEN_HEIGHT // 2 - ball.size or y < -SCREEN_HEIGHT // 2 + ball.size:
        ball.delta_y *= -1
        winsound.PlaySound('hitting-ball.wav', winsound.SND_ASYNC)

    if x > SCREEN_WIDTH // 2 - ball.size or x < -SCREEN_WIDTH // 2 + ball.size:
        if x < 0:
            score_b += 1
        elif x > 0:
            score_a += 1
        show_score()
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        window.update()
        sleep(1)
        ball.delta_x *= choice([-1, 1])
        ball.delta_y *= choice([-1, 1])


def move_ball(ball):
    x = ball.xcor()
    y = ball.ycor()
    ball.goto(x + ball.delta_x, y + ball.delta_y)


def check_ball_paddle_collision():
    if (SCREEN_WIDTH // 2 - 50 - paddle_b.height < ball.xcor() < SCREEN_WIDTH // 2 - 40 - paddle_b.height) and\
            (paddle_b.ycor() + paddle_b.width // 2 > ball.ycor() > paddle_b.ycor() - paddle_b.width // 2):
        winsound.PlaySound('hitting-ball.wav', winsound.SND_ASYNC)
        ball.setx(SCREEN_WIDTH // 2 - 50 - paddle_b.height)
        ball.delta_x *= -1
    elif (-SCREEN_WIDTH // 2 + 50 + paddle_a.height > ball.xcor() > -SCREEN_WIDTH // 2 + 40 + paddle_a.height) and \
            (paddle_a.ycor() + paddle_a.width // 2 > ball.ycor() > paddle_a.ycor() - paddle_a.width // 2):
        winsound.PlaySound('hitting-ball.wav', winsound.SND_ASYNC)
        ball.setx(-SCREEN_WIDTH // 2 + 50 + paddle_a.height)
        ball.delta_x *= -1


def move_ai_paddle():
    if paddle_b.ycor() < ball.ycor():
        move_paddle(paddle_b, 'up')
    elif paddle_b.ycor() > ball.ycor():
        move_paddle(paddle_b, 'down')


def show_score():
    global score_a, score_b
    pen.clear()
    pen.write(f'Player: {score_a} Computer: {score_b}', align='center', font=('Arial', 16, 'bold'))


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 20

score_a = 0
score_b = 0


window = Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.title('Pong by @wspjoy')
window.bgcolor('black')
window.onkey(window.bye, 'Escape')
window.tracer(0)

window.onkeypress(lambda: move_paddle(paddle_a, 'up', PADDLE_SPEED), 'Left')
window.onkeypress(lambda: move_paddle(paddle_a, 'down', PADDLE_SPEED), 'Right')

pen = Turtle()
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.up()
pen.goto(0, SCREEN_HEIGHT // 2 - 50)

show_score()

paddle_a = Turtle()
make_paddle_settings(paddle_a, -SCREEN_WIDTH // 2 + 50)

paddle_b = Turtle()
make_paddle_settings(paddle_b, SCREEN_WIDTH // 2 - 50)


ball = Turtle()
ball.shape('circle')
ball.up()
ball.color('white')
ball.size = 20
ball.delta_x = 0.3
ball.delta_y = 0.3

window.listen()

while True:
    window.update()
    check_ball_border(ball)
    move_ball(ball)

    check_ball_paddle_collision()

    move_ai_paddle()
