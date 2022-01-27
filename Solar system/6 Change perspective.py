import turtle
import time
from math import *
import random

win = turtle.Screen()
win.setup(1500,1100)
win.bgcolor('black')
win.tracer(0)
win.listen()

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(5,5)
sun.color('yellow')

pen = turtle.Pen()
pen.color('red')
pen.up()
pen.hideturtle()
pen.goto(0,500)
pen.write("Press up and down arrows to change perspective", align='center', font=('Courier', 24, 'normal'))

class Planet(turtle.Turtle):
    def __init__(self,radius, color, size, star, offset):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size,size)
        self.up()
        self.angle = 0
        self.star = star
        self.offset = offset
        self.ellipse = 0.3
        self.draw = 'on'

    def move(self):
        x = self.offset +  self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle)*self.ellipse 

        self.goto(self.star.xcor()+x,self.star.ycor()+y)


earth = Planet(300,'blue', 1, sun, 100)
mercury = Planet(110, 'grey', 0.6, sun, 0)
venus = Planet(180, 'orange', 0.8, sun, 50)
mars = Planet(400, 'red', 0.9, sun, 100)

moon = Planet(40, 'grey', 0.2, earth, 0) # Moon a 'planet' that revolves around earth
phobos = Planet(40, 'grey', 0.2, mars,0)
deimos = Planet(35, 'white', 0.2, mars, 0)

myList = [mercury, venus, earth, moon, mars, phobos, deimos]

for i in myList:
    i.penup()
    i.goto(i.radius+i.offset, 0)
    if i.star == sun:
        i.pendown()

asteroid_list = []
angle = 0.001

for i in range(500):
    asteroid = Planet(random.randint(550, 700), 'grey', 0.1, sun,0)
    asteroid.penup()
    asteroid_list.append(asteroid)
    asteroid.angle += angle
    angle += 0.012421 # Scatter 500 asteroids radius 550-700 all around sun

def move_up():
    for i in asteroid_list:
        if i.ellipse < 1:
            i.ellipse += 0.1

    for i in myList:
        if i.ellipse < 1:
            i.draw = 'off'
            i.ellipse += 0.1
            


def move_down():
    for i in asteroid_list:
        if i.ellipse > 0.1:
            i.ellipse -= 0.1

    for i in myList:
        if i.ellipse >0.1:
            i.draw = 'off'
            i.ellipse -= 0.1
            
            

win.onkey(move_up, 'Up')
win.onkey(move_down, 'Down')

while True:
    win.update()
    for i in myList:
        i.move()
        if i.draw == 'off':
            i.clear()
            i.draw = 'on'

    # Increase the angle by 0.0x radians (further away - smaller angle change)
    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    for i in asteroid_list:
        i.move()
        i.angle += 0.002

    time.sleep(0.01)
    
    
