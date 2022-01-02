from turtle import Screen, Turtle
from random import randint

WIDTH, HEIGHT = 750, 400
MAX_HEIGHT = 180
BASELINE = -60

NUMBER_CACTI = 3

FONT = ('Courier', 24, 'normal')

CURSOR_SIZE = 20
CACTUS_WIDTH, CACTUS_HEIGHT = 10, 60


def steady():
    return dino.ycor() == BASELINE + CURSOR_SIZE/2


def jump():
    y = dino.ycor()

    if steady():
        dino.sety(y + 7 * CURSOR_SIZE)
    elif y < MAX_HEIGHT:
        dino.sety(y + 2 * CURSOR_SIZE)


def cactus_move(cactus):
    cactus.setx(cactus.xcor() - CACTUS_WIDTH)


def check_rect_collision(a, b):
    return abs(a.xcor() - b.xcor()) < CURSOR_SIZE/2 + CACTUS_WIDTH/2 and abs(a.ycor() - b.ycor()) < CURSOR_SIZE/2 + CACTUS_HEIGHT/2


def place_cactus(cactus):
    cactus.setx(randint(WIDTH//2, WIDTH))

    while True:
        for other in cacti:
            if other is cactus:
                continue

            if other.distance(cactus) < 5 * CACTUS_WIDTH:
                cactus.setx(randint(0, WIDTH//2))
                break  # for
        else:  # no break
            break  # while

# scoring system
score = 0


def run():
    global score

    score += 1

    pen.clear()
    pen.write("Score: {} ".format(score), align='center', font=FONT)

    for cactus in cacti:
        cactus_move(cactus)

        if check_rect_collision(dino, cactus):
            screen.onkeypress(None, 'space')  # Game Over
            screen.tracer(True)
            return

        if cactus.xcor() < -WIDTH/2:
            place_cactus(cactus)

    if not steady():
        dino.sety(dino.ycor() - CURSOR_SIZE)

    screen.update()
    screen.ontimer(run, 50)


screen = Screen()
screen.title("Dino game in turtle")
screen.bgcolor('white')
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(False)

ground = Turtle()
ground.hideturtle()

ground.penup()
ground.sety(BASELINE)
ground.pendown()

ground.forward(WIDTH/2)
ground.backward(WIDTH)


dino = Turtle()
dino.shape('square')
dino.penup()
dino.goto(-WIDTH/3, BASELINE + CURSOR_SIZE/2)


cacti = []

for _ in range(NUMBER_CACTI):

    cactus = Turtle()
    cactus.shape('square')
    cactus.shapesize(CACTUS_HEIGHT / CURSOR_SIZE, CACTUS_WIDTH / CURSOR_SIZE)
    cactus.color('green')

    cactus.penup()
    cactus.sety(BASELINE + CACTUS_HEIGHT/2)
    place_cactus(cactus)

    cacti.append(cactus)

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.sety(155)

pen.write("Score: 0  High Score: 0", align='center', font=FONT)

screen.onkeypress(jump, 'space')
screen.listen()

run()
screen.mainloop()
