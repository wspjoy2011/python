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

pen3 = turtle.Turtle() # To show values that do not change
pen3.up()
pen3.ht()

starty = 0
endy = -270

# Values for the masses and pulley  (Assuming no friction in pulley)
#################################
#################################

massA = 1.02     # CHANGE MASS OF BOXES (kg) (can be 0)
massB = 1.00
massPulley = 1
radiusPulley = 0.02
I = 0.5*massPulley*(radiusPulley*radiusPulley)
distance = 1  #  distance to travel in m
distance_pixels = 270/distance  #pixels/m

##################################
##################################

boxA = turtle.Turtle()
boxA.shape('square')
boxA.color('green')
if massA==0:
    boxA.ht()
else:
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
if massB == 0:
    boxB.ht()
else:
    boxB.shapesize(massB,massB)
boxB.up()
boxB.goto(30,starty)


top_rope = 300  # top point of the rope
start_time = time.time()
g = -9.8
vA = 0
vB = 0


net_force = massA*g - massB*g # if positive A will drop
#print("Net force: ",net_force)

#Angular acceleration:
alpha = ((massA-massB)*g/(massA+massB+0.5*massPulley))/radiusPulley
aA = alpha*radiusPulley
aB = -aA

pen3.goto(0,-390)
pen3.write("Aa: {:.4f} m/s^2\tAb: {:.4f} m/s^2".format(aA,aB),align='center',font = ('Courier',15, 'normal'))
pen3.goto(0,-330)
pen3.write("mass A: {} kg\tmass B: {} kg".format(massA,massB),align='center',font = ('Courier',15, 'normal'))
pen3.goto(-130,300)
pen3.write("mass Pulley: {} kg\nRadius = {:.04f} m\nI = {:.6f} kgm^2\nalpha: {:.4f} rad/s^2".format(massPulley,radiusPulley,I,alpha),\
           align='center',font = ('Courier',15, 'normal'))

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
    
    yA = 1/2*aA*t*t 
    yB = 1/2*aB*t*t

    boxA.goto(boxA.xcor(),yA*270/distance)
    boxB.goto(boxB.xcor(),yB*270/distance)

    
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
    if count%30==0:
        pen2.clear()
        pen2.goto(0,400)
        pen2.write("time: {:.4f} s".format(t),align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-360)
        pen2.write("Vt: {:.4f} m/s\tOmega: {:.4f} rad/s".format(-vA,-vA/radiusPulley),\
                   align='center',font = ('Courier',15, 'normal'))
        pen2.goto(0,-420)
        pen2.write("distance: {:.4f} m".format(abs(yA)),align='center',font = ('Courier',15, 'normal'))
    win.update()
        

    if yA >= distance or yB>= distance:
        Game_over = True
        print("done")
        


#Final figures:
t = sqrt(abs(2*distance/aA))
s = 0.5*aA*t*t
v = aA*t
omega = v/radiusPulley

print("t = ",t)
print("s = ",s)
print("Va = ",v)
print("Vt = ",-v)
print("omega = ",-omega)
print("Note: Vt/omega positive for CCW with speed = |Vt|")
pen2.clear()
pen2.goto(0,400)
pen2.write("time: {:.4f} s".format(t),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-360)
pen2.write("Vt: {:.4f} m/s\tOmega: {:.4f} rad/s".format(-v,-omega),align='center',font = ('Courier',15, 'normal'))
pen2.goto(0,-420)
pen2.write("distance: {:.4f} m".format(abs(s)),align='center',font = ('Courier',15, 'normal'))

 
    
