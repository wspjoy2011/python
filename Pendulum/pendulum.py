import turtle
from math import *


win = turtle.Screen()
win.bgcolor('black')
win.setup(800,800)
win.tracer(0)
win.title("Simple Pendulum")

t = turtle.Turtle()
t.shape('circle')
t.color('white')
t.shapesize(0.1,0.1)
t.up()
t.goto(-200,300)
t.down()
t.goto(200,300)
t.goto(0,300)
t.rt(90)

for i in range(20):
    t.fd(25)
    if i%2==0:
        t.up()
    else:
        t.down()

line = turtle.Turtle()
line.shape('circle')
line.shapesize(0.05,25)
line.rt(90)
line.color('white')
line.up()
line.goto(0,50)


pen = turtle.Pen()
pen.hideturtle()
pen.up()
pen.goto(-300,-300)
pen.color('red')

att = turtle.Turtle() # to show magnitude and direction of a tangential
att.shape('circle')
att.color('red')
att.shapesize(0.2,0.2)
att.up()
att.goto(0,-250)
att.down()

ball = turtle.Turtle()
ball.shape('circle')
ball.up()
ball.color('blue')

###############################
L = 500    # pixels
m = 0.1  # mass (kg)
g = 9.8

A = 0.2 # radian (max amplitude)
theta = A # start at A
t = 0
################################

ball.goto(L*sin(theta),300 - L*cos(theta))
ball.down()

y = 300-L*cos(theta)
    
E = (y+200)*m*g  # Initial total E = KE (0) + PE

while True:
    t += 0.1
    
    theta = A*cos(sqrt(g/L)*t)      # theta(t) = Acos(wt)
    x = L*sin(theta)
    y =300-L*cos(theta)
    
    line.setheading(90+theta*180/pi)
    line.goto(x/2,y/2+150)
    
    Ug = (y+200)*m*g
    KE = E-Ug
  
    ball.goto(x,y)
    at = -g*sin(theta)
    att.goto(at*30,-250) # show magnitude and direction of at
    pen.write(" theta = {:.3f} rad\t at = {:.2f} m/s^2\tUg: {:.2f} J\tKE: {:.2f} J".format(theta,at,Ug,KE),\
              align='left', font=('Courier',15,'normal'))
    win.update()
    
    pen.clear()
    
    
    
    
    
