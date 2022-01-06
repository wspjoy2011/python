from turtle import *
from random import randint, random, choice


class Square:
    def __init__(self):
        self.x = []
        self.y = []

    def draw_square(self, size, pos_x, pos_y, square_color):
        pen.up()
        pen.color(square_color)
        pen.goto(pos_x, pos_y)
        pen.down()
        for _ in range(4):
            self.x.append(pen.pos()[0])
            self.y.append(pen.pos()[1])
            pen.forward(size)
            pen.left(90)
        self.x = [min(self.x), max(self.x)]
        self.y = [min(self.y), max(self.y)]


class Ball:
    def __init__(self, delta_x, delta_y):
        self.ball = Pen()
        self.delta_x = delta_x
        self.delta_y = delta_y

    def make_settings(self, ball_color):
        self.ball.up()
        self.ball.ht()
        self.ball.goto(randint(START_POSITION, abs(START_POSITION)),
                       randint(START_POSITION, abs(START_POSITION)))
        self.ball.st()
        self.ball.color(ball_color)
        self.ball.width(5)
        self.ball.shape('circle')

    def check_border(self, x, y):
        if x < START_POSITION:
            self.delta_x *= -1
        elif x > abs(START_POSITION):
            self.delta_x *= -1

        if y < START_POSITION:
            self.delta_y *= -1
        elif y > abs(START_POSITION):
            self.delta_y *= -1

        for square in squares:
            if square.x[0] < x < square.x[1] and square.y[0] - 1 < y < square.y[1] + 1:
                self.delta_y *= -1
            elif square.x[0] - 3 < x < square.x[1] + 3 and square.y[0] + 1 < y < square.y[1] - 1:
                self.delta_x *= -1

    def move(self, x, y):
        x += self.delta_x
        y += self.delta_y

        self.ball.goto(x, y)


def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.left(90)


def draw_border():
    pen.up()
    pen.goto(START_POSITION, START_POSITION)
    pen.down()
    draw_square(WINDOW_SIZE - 100)


def check_balls_collision():
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].ball.distance(balls[j].ball) < 20:
                balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y


WINDOW_SIZE = 900
START_POSITION = ((WINDOW_SIZE // 2) * -1) + 50

window = Screen()
window.setup(WINDOW_SIZE, WINDOW_SIZE)
window.onkey(lambda: window.bye(), 'Escape')
window.tracer(0)

pen = Pen()
pen.speed(0)
pen.ht()
pen.width(5)
pen.color('red')

directions = [-1, 1]

draw_border()

squares = [Square() for _ in range(5)]
squares_coordinates = []
square_size = 100
square_position_start = START_POSITION

for square in squares:
    pos_x = randint(square_position_start, square_position_start + square_size)
    pos_y = randint(square_position_start, square_position_start + square_size)
    squares_coordinates.append((pos_x, pos_y))
    square.draw_square(square_size - 20, pos_x, pos_y, (random(), random(), random()))
    square_position_start += square_size * 1.5

balls = [Ball(randint(2, 5) * choice(directions) / 10, randint(1, 5) * choice(directions) / 10)
         for _ in range(20)]
for ball in balls:
    ball.make_settings((random(), random(), random()))


window.listen()
while True:
    window.update()
    check_balls_collision()
    for ball in balls:
        x, y = ball.ball.pos()
        ball.check_border(x, y)
        ball.move(x, y)