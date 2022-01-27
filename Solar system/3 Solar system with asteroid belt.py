import turtle
import time
from math import *
import random

win = turtle.Screen()
win.setup(1500,1500)
win.bgcolor('black')
win.tracer(0)

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(5,5)
sun.color('yellow')


class Planet(turtle.Turtle):
    def __init__(self,radius, color, size, star):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size,size)
        self.up()
        self.angle = 0
        self.star = star

    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle) 

        self.goto(self.star.xcor()+x,self.star.ycor()+y)


earth = Planet(300,'blue', 1, sun)
mercury = Planet(110, 'grey', 0.6, sun)
venus = Planet(180, 'orange', 0.8, sun)
mars = Planet(500, 'red', 0.9, sun)

moon = Planet(40, 'grey', 0.2, earth) # Moon a 'planet' that revolves around earth
phobos = Planet(40, 'grey', 0.2, mars)
deimos = Planet(35, 'white', 0.2, mars)

asteroid_list = []
angle = 0.001

for i in range(500):
    asteroid = Planet(random.randint(550, 700), 'grey', 0.1, sun)
    asteroid_list.append(asteroid)
    asteroid.angle += angle
    angle += 0.012421 # Scatter 500 asteroids radius 550-700 all around sun
    

myList = [earth, mercury, venus, mars, moon, phobos, deimos]


while True:
    win.update()
    for i in myList:
        i.move()
        
    for i in asteroid_list:
        i.move()
        i.angle += 0.002

    # Increase the angle by 0.0x radians (further away - smaller angle change)
    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    time.sleep(0.01)
    
    
