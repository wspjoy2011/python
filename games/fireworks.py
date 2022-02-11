from turtle import *
from random import random, randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
is_click = False
click = 1

def explode(x, y):
    global is_click, click
    if is_click:
        return 0
    is_click = True
    click += 1
    fireworks = [Turtle(shape='circle') for _ in range(40)]
    direction = 0
    for firework in fireworks:
        firework.up()
        firework.hideturtle()
        firework.goto(x, y)
        firework.setheading(direction)
        firework.shapesize(0.15, 0.15)
        direction += 9
        firework.delta = randint(1, 7) / 10 * click
        firework.distance = 0
        firework.speed(0)
        firework.color((random(), random(), random()))
        firework.showturtle()

    run = True
    while run:
        for firework in fireworks:
            firework.forward(firework.delta)
            firework.distance += firework.delta
            if firework.distance > 100:
                run = False
        window.update()

    while fireworks:
        fireworks[0].color('white')
        del fireworks[0]
    window.update()
    is_click = False


window = Screen()
window.title('Fireworks by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.onclick(explode, btn=1)
window.tracer(0, 0)

window.listen()
window.mainloop()
