from random import randint
from turtle import *
from math import sin, cos
from time import sleep


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950


class Planet(Turtle):
    def __init__(self, shapesize, planet_color, radius, star, increase_angle, name='star'):
        Turtle.__init__(self, shape='circle')
        self.name = name
        self.speed(0)
        self.shapesize(*shapesize)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.angle = 0
        self.increase_angle = increase_angle
        self.radius = radius
        self.star = star

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle


class Asteroid(Planet):
    start_angle = 0.001
    increase_start_angle = 0.012421

    def __init__(self, star, distance, increase_angle):
        Planet.__init__(self, (0.1, 0.1), 'white', distance, star, increase_angle)
        self.angle += self.start_angle
        Asteroid.start_angle += increase_angle


def move_objects(objects):
    for object in objects:
        if object.name == 'saturn':
            saturn_circle.down()
            saturn_circle.goto(object.xcor(), object.ycor() - 50)
            saturn_circle.circle(50)
        object.move()


window = Screen()
window.bgcolor('black')
window.title('Solar system be @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

sun = Turtle(shape='circle')
sun.color('yellow')
sun.shapesize(5, 5)

earth = Planet((1.0, 1.0), 'blue', 150, sun, 0.02)
moon = Planet((0.5, 0.5), 'gray', 25, earth, 0.08)

saturn = Planet((2.0, 2.0), 'orange', 200, sun, 0.005, name='saturn')

mars = Planet((0.8, 0.8), 'red', 300, sun, 0.007)
phobos = Planet((0.3, 0.3), 'grey', 40, mars, 0.06)
deimos = Planet((0.2, 0.2), 'white', 25, mars, 0.08)

planets = [earth, moon, saturn, mars, phobos, deimos]

asteroids = [Asteroid(sun, randint(400, 600), 0.012421) for _ in range(500)]

saturn_circle = Turtle()
saturn_circle.up()
saturn_circle.hideturtle()
saturn_circle.width(5)
saturn_circle.speed(0)
saturn_circle.color('white', 'white')


window.listen()
while True:
    saturn_circle.clear()
    move_objects(planets)
    move_objects(asteroids)
    window.update()
