import turtle
import datetime
import math

screen = turtle.Screen()
screen.title('Continuous Clock by @wspjoy')
screen.bgcolor('sky blue')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)


class Clock:
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second
        self.microsecond = 0
        self.face = turtle.Turtle()
        self.hand = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

    def draw(self):
        self.draw_face()
        self.draw_hand()

    def draw_face(self):
        self.face.clear()
        self.face.up()
        self.face.goto(0, -700)
        self.face.pensize(4)
        self.face.down()
        self.face.fillcolor('white')
        self.face.begin_fill()
        self.face.circle(700, steps=100)
        self.face.end_fill()
        self.face.up()
        self.face.goto(0, 0)
        self.face.dot(10)
        self.face.pensize(2)
        for angle in range(0, 360, 6):
            self.face.up()
            self.face.goto(0, 0)
            self.face.seth(90 - angle)
            self.face.fd(620)
            self.face.down()
            self.face.fd(30)

        self.face.pensize(3)
        for angle in range(0, 360, 30):
            self.face.up()
            self.face.goto(0, 0)
            self.face.seth(90 - angle)
            self.face.fd(600)
            self.face.down()
            self.face.fd(50)

        self.face.pensize(4)
        for angle in range(0, 360, 90):
            self.face.up()
            self.face.goto(0, 0)
            self.face.seth(90 - angle)
            self.face.fd(580)
            self.face.down()
            self.face.fd(70)

    def draw_hand(self):
        self.hand.clear()
        self.hand.up()
        self.hand.goto(0, 0)
        self.hand.seth(90 - math.floor(((self.hour % 12) * 60 * 60 * 1000000 + self.minute * 60 * 1000000 + self.second
                                        * 1000000 + self.microsecond) / 3600000000 * 30))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(6)
        self.hand.fd(300)

        self.hand.up()
        self.hand.goto(0, 0)
        self.hand.seth(
            90 - math.floor((self.minute * 60 * 1000000 + self.second * 1000000 + self.microsecond) / 60000000 * 6))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(400)

        self.hand.up()
        self.hand.color('red')
        self.hand.goto(0, 0)
        self.hand.dot(5)
        self.hand.seth(90 - (self.second * 1000000 + self.microsecond) / 1000000 * 6)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(570)


def animate():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second, c.microsecond = d.hour, d.minute, d.second, d.microsecond
    c.draw_hand()
    screen.update()
    screen.ontimer(animate, 100)


d = datetime.datetime.now()
c = Clock(d.hour, d.minute, d.second)
c.draw_face()
screen.update()
animate()
screen.mainloop()
