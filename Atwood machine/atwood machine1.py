import turtle
from math import *
import time


win = turtle.Screen()
win.bgcolor('white')
win.setup(500,900)
win.tracer(0)
win.title("Atwood machine simulation")


discA = turtle.Turtle()
discA.shape('circle')
discA.color('red')
discA.shapesize(3,3)
discA.up()
discA.goto(0,300)

pen1 = turtle.Turtle()
pen1.ht()
pen1.color('black')
pen1.up()
pen1.goto(-200,380) # Ceiling
pen1.down()
pen1.pensize(10)
pen1.goto(200,380)
pen1.up()
pen1.goto(-200,-300) #Floor
pen1.down()
pen1.goto(200,-300)
pen1.pensize(1)
pen1.up()
pen1.goto(0,380)
pen1.down()
pen1.color('blue')  # Rope to pulley
pen1.goto(0,300)

pen = turtle.Turtle()
pen.ht()
pen.up()

starty = 0
massA = 2     # CHANGE MASS OF BOXES
massB = 1

boxA = turtle.Turtle()
boxA.shape('square')
boxA.color('green')
boxA.shapesize(massA,massA)
boxA.up()
boxA.goto(-100,starty)
boxA.down()
boxA.goto(100,starty)
boxA.goto(-30,starty)
boxA.up()


boxB = turtle.Turtle()
boxB.shape('square')
boxB.color('green')
boxB.shapesize(massB,massB)
boxB.up()
boxB.goto(30,starty)


top_rope = 300
start_time = time.time()
g = -9.8
vA = 0
uA = 0
vB = 0
uB = 0

net_force = massA*g - massB*g # if positive A will drop
print("Net force: ",net_force)
aA = net_force/(massA+massB)
print("a for box A = ",aA)
aB = -aA

pen2 = turtle.Pen()
pen2.ht()
pen2.up()

Game_over = False
count = 0

while not Game_over:
    t = time.time() - start_time
    count+=1
    
    vA =  aA*t
    vB =  aB*t
    
    yA = (uA*t + 1/2*aA*t*t + starty)*5 # start height or s0
    yB = (uB*t + 1/2*aB*t*t + starty)*5

    boxA.goto(boxA.xcor(),yA)
    boxB.goto(boxB.xcor(),yB)

    
    # Draw rope
    pen.clear()
    pen.up()
    pen.goto(boxA.xcor(),boxA.ycor())
    pen.down()
    pen.goto(boxA.xcor(),top_rope)
    pen.lt(90)
    pen.goto(boxB.xcor(),top_rope)
    pen.goto(boxB.xcor(),boxB.ycor())

    #Write Data:
    if count%40==0:
        pen2.clear()
        pen2.goto(0,400)
        pen2.write("time: {:.2f}s".format(t),align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-330)
        pen2.write("mass A: {}kg\tmass B: {}kg".format(massA,massB),align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-360)
        pen2.write("Va: {:.2f}m/s\tVb: {:.2f}m/s".format(vA,vB),align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-390)
        pen2.write("Aa: {:.2f}m/s^2\tAb: {:.2f}m/s^2".format(aA,aB),align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-420)
        pen2.write("distance: {:.2f}m".format((yA-starty)/5),align='center',font = ('Courier',15, 'normal'))
    win.update()
        
    if boxA.ycor()<=-250 or boxB.ycor()<=-250:
        print('done')
        Game_over = True


#Final figures:
        
pen2.clear()
pen2.goto(0,400)
pen2.write("time: {:.2f}s".format(t),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-330)
pen2.write("mass A: {}kg\tmass B: {}kg".format(massA,massB),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-360)
pen2.write("Va: {:.2f}m/s\tVb: {:.2f}m/s".format(vA,vB),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-390)
pen2.write("Aa: {:.2f}m/s^2\tAb: {:.2f}m/s^2".format(aA,aB),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-420)
pen2.write("distance: {:.2f}m".format((yA-starty)/5),align='center',font = ('Courier',15, 'normal'))

 
    
