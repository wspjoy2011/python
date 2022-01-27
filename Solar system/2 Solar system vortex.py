import turtle
import math, time

win = turtle.Screen()
win.setup(1100,1100)
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
        #self.up()
        self.angle = 0
        self.star = star

    def move(self):
        x = self.radius*math.cos(self.angle) # radians
        y = self.radius*math.sin(self.angle)

        self.goto(self.star.xcor()+x,self.star.ycor()+y)



earth = Planet(160,'blue', 1, sun)
mercury = Planet(80, 'grey', 0.6, sun)
venus = Planet(120, 'orange', 0.8, sun)
mars = Planet(200, 'red', 0.9, sun)

moon = Planet(40, 'grey', 0.2, earth) # moon a 'planet' that orbits earth
phobos = Planet(40, 'grey', 0.2, mars)
deimos = Planet(35, 'white', 0.2, mars)

myList = [sun, earth, mercury, venus, mars, moon, phobos, deimos]

for i in myList:
    i.up()
    i.goto(-1000,1000)
    i.down()



while True:
    win.update()
    for i in range(1,7):
        myList[i].move()

    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    sun.goto(sun.xcor()+1, sun.ycor()-1)
    
    time.sleep(0.01)
    
    
