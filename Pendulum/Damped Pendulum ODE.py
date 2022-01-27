import turtle
from math import *
import scipy.integrate as integrate
import numpy as np
import time

win = turtle.Screen()
win.title("Damped pendulum (SHM) simulation")
win.setup(800,800)
win.bgcolor('cyan')
win.tracer(0)

################## Change initial conditions
L = 200
theta = 80 
g = 9.8
m = 1
omega = 0
b = 0.15
##################

p = turtle.Turtle()
p.shape('circle')
p.color('red')
p.up()
p.shapesize(1.5,1.5)

rod = turtle.Turtle()
rod.shape('circle')
rod.shapesize(0.1,0.1)
rod.pensize(3)
rod.up()

cursor = turtle.Turtle()
cursor.shape('circle');cursor.shapesize(0.5,0.5)
cursor.up()
cursor.color('black')
cursor.goto(-380,-280)
cursor.down()
cursor.dx = 0.1

water = turtle.Turtle()
water.color("blue")
water.up()
water.ht()
water.goto(250,-150)
water.begin_fill()
for i in range(4):
    water.lt(90)
    water.fd(500)
water.end_fill()

dt = 0.005
t = np.arange(0.0,200,dt)
            
def derivs(state, t):

    theta1 = state[0]  # Initial angle
    omega1 = state[1]  # intial angular velocity
    dtheta1 = omega1
    domega1 = -(b/m)*omega1 - g*sin(theta1)  # theta(..) = -(b/m)theta(.) - (k/m)theta
    dydx = [dtheta1,domega1]
    
    return dydx

state = np.radians([theta,omega])
y = integrate.odeint(derivs,state,t)
k = 1

while k<40000:
    x1 = L*sin(y[k][0])
    y1 = -L*cos(y[k][0]) + 200 # to ceiling
   
    p.goto(x1,y1)
    rod.goto(p.xcor(),p.ycor())
    cursor.goto(cursor.xcor()+cursor.dx,-280+x1/2)
   
    win.update()
    
    rod.clear()
    rod.up()
    rod.goto(0,200)
    rod.down()

    k += 1 # How quickly to run through array
    time.sleep(0.001)
    
    


    
