from turtle import *
from random import random, randint, choice
from time import sleep


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)


class CustomTurtle(Sprite):
    def __init__(self, start_x: int, start_y: int, number: int):
        Sprite.__init__(self)
        self.validate_int(start_x)
        self.validate_int(start_y)
        self.validate_int(number)

        self.__speed = choice(speed)
        self.__color = self.random_color()
        self.__number = number
        self.hideturtle()
        self.speed(0)
        self.up()
        self.goto(start_x, start_y)
        self.color(self.__color)
        self.shape('turtle')
        self.showturtle()

    @classmethod
    def validate_int(cls, data):
        if not isinstance(data, int):
            raise TypeError('Argument must be integer type')
        else:
            return data

    @staticmethod
    def random_color():
        turtle_color = random(), random(), random()
        return turtle_color

    @staticmethod
    def random_delta(speed):
        return randint(speed[0] // 10, speed[1] // 10)

    def get_color(self):
        return self.__color

    def get_number(self):
        return self.__number

    def move(self):
        self.forward(self.random_delta(self.__speed))

    def check_border(self):
        if self.xcor() + 20 > Border.FINISH_X:
            return Turtle
        return False


class Border(Sprite):
    START_X = -SCREEN_WIDTH // 2 + 100
    START_Y = SCREEN_HEIGHT // 2 - 30
    FINISH_X = SCREEN_WIDTH // 2 - 100
    FINISH_Y = -SCREEN_HEIGHT // 2 + 30

    def __init__(self):
        Sprite.__init__(self)
        self.hideturtle()
        self.width(5)
        self.speed(0)
        self.draw_start_line()
        self.draw_finish_line()

    def draw_start_line(self):
        self.up()
        self.goto(self.START_X, self.START_Y)
        self.right(90)
        self.down()
        self.forward(SCREEN_HEIGHT - 50)
        self.up()

    def draw_finish_line(self):
        self.left(90)
        self.goto(self.FINISH_X, self.FINISH_Y)
        self.left(90)
        self.down()
        self.forward(SCREEN_HEIGHT - 50)


class Line(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.up()
        self.hideturtle()
        self.speed(0)
        self.width(2)

    def draw_line(self):
        self.down()
        self.forward(SCREEN_WIDTH - 200)
        self.up()


class Number(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.__font = ('Arial', 16, 'bold')
        self.up()
        self.hideturtle()

    def get_font(self):
        return self.__font


def countdown():
    number.goto(0, 0)
    number.color('red')
    for count in range(3, 0, -1):
        window.update()
        number.write(f'{count}', font=('Arial', 30, 'bold'), align='center')
        sleep(1)
        number.clear()
    number.color('blue')


def write_lines(turtle):
    line.color(turtle.get_color())
    line.goto(turtle.xcor() + 50, turtle.ycor() - 10)
    line.draw_line()
    line.goto(turtle.xcor() + 50, turtle.ycor() + 10)
    line.draw_line()


def write_numbers(turtle):
    number.goto(Border.FINISH_X + 20, turtle.ycor() - 20)
    number.write(turtle.get_number(), font=number.get_font(), align='center')


def fill_turtles(qty):
    global start_y, start_x
    for i in range(qty):
        turtles.append(CustomTurtle(start_x, start_y, i + 1))
        write_lines(turtles[i])
        write_numbers(turtles[i])
        start_y -= 50


def game():
    fill_turtles(10)
    while True:
        for turtle in turtles:
            if turtle.check_border():
                number.color('red')
                number.goto(0, SCREEN_HEIGHT // 2 - 40)
                number.write(f'Winner is {turtle.get_number()}', font=number.get_font(), align='center')
                sleep(3)
                window.bye()
            turtle.move()
            window.update()


speed = [(1, 17), (10, 30), (5, 45)]
start_x = -SCREEN_WIDTH // 2 + 50
start_y = SCREEN_HEIGHT // 2 - 50

window = Screen()
window.title('Turtle races by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

number = Number()
countdown()

border = Border()
line = Line()
turtles = []

window.listen()
game()
