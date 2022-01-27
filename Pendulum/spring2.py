
import turtle
from math import *

win = turtle.Screen()
win.title("SHM vertical spring")
win.setup(700,800)
win.bgcolor('cyan')
win.tracer(0)


spring = turtle.Turtle()
spring.shape('square')
spring.color('red')
spring.up()
spring.goto(0,300)
spring.down()

m = turtle.Turtle()
m.shape('square')
m.color('black')
m.up()
m.goto(300,330)
m.down()
m.pensize(10)
m.goto(-300,330)
m.up()

pen = turtle.Pen()
pen.color('red')
pen.ht()
pen.up()
pen.goto(0,-300)

def spring_length(number,stretch):
    spring.clear()
    for i in range(number):
        angle = 0
        while angle<=2*pi:
            angle = angle+0.01
            x = 0.2*cos(angle)
            y = 0.2*sin(angle)
            spring.goto(spring.xcor()+x,spring.ycor()+y-stretch)
    spring.goto(spring.xcor(),spring.ycor()-20)
    

length = 30  # Spring length at equilibrium

spring_length(15,length/1000)
m.goto(spring.xcor(),spring.ycor())
m.down()
m.pensize(1)
m.color('white')
m.goto(-200,m.ycor())
m.goto(200,m.ycor())
m.shapesize(0.1,1)
m.color('blue')
spring.up()
spring.goto(0,300)
spring.down()

omega = 2
t = 0

while True:

    t += 0.1
    y = 10*cos(omega*t+pi)
    v = -10*omega*sin(omega*t+pi)
    a = -10*omega*omega*cos(omega*t+pi)
    
    length = 30 - y
    
    s = length/1000
    spring_length(15,s)
    m.goto(m.xcor(),spring.ycor())
    pen.write("y = {:.2f}\tVy = {:.2f}\tAy = {:.2f}".format(y,v,a),align='center',font=('Courier',15,'normal'))
    win.update()
    spring.clear()
    spring.goto(0,300)
    pen.clear()
    
