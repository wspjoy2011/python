import turtle
import random
import time

colors = ["red", "blue", "yellow", "pink", "green", "DeepSkyBlue", "chartreuse", "DarkMagenta"]

ball_speed = 10
WINDOW_MAIN_GAME_HEIGHT = 1000
WINDOW_MAIN_GAME_WIDTH = 800
BORDER_LEFT = -400
BORDER_RIGHT = 400
BORDER_TOP = 500
BORDER_BOT = -500

life = 3

wn = turtle.Screen()
wn.title("BREAKOUT - By: Wspjoy")
wn.bgcolor("black")
wn.setup(WINDOW_MAIN_GAME_WIDTH, WINDOW_MAIN_GAME_HEIGHT)

block1 = turtle.Turtle()
block1.shape("square")
block1.speed(0)
block1.shapesize(2, 4)

blocks_row1 = [block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(),
               block1.clone(), block1.clone(), block1.clone()]

blocks_row2 = [block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(),
               block1.clone(), block1.clone(), block1.clone()]

blocks_row3 = [block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(), block1.clone(),
               block1.clone(), block1.clone(), block1.clone()]

all_blocks = [blocks_row1, blocks_row2, blocks_row3]


def starting_block_positions():
    for n in range(len(all_blocks)):
        for i in range(len(blocks_row1)):
            all_blocks[n][i].penup()

            all_blocks[n][i].color(random.choice(colors))
            all_blocks[n][i].goto(((BORDER_LEFT + 50) + (85 * i)), ((BORDER_TOP - 40) - (n * 45)))


paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.speed(0)
paddle.shapesize(2, 8)
paddle_position_x = paddle.xcor()
paddle_position_y = paddle.ycor()


def starting_paddle_position():
    paddle.penup()
    paddle.goto(0, BORDER_BOT + 30)


def move_left():
    if paddle.xcor() > (BORDER_LEFT + 20):
        paddle.setx(paddle.xcor() - 10)


def move_right():
    if paddle.xcor() < (BORDER_RIGHT - 20):
        paddle.setx(paddle.xcor() + 10)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.fillcolor("white")
ball.speed(0)


def starting_ball_position():
    ball.hideturtle()
    ball.penup()
    ball.goto(0, 0)
    ball.setheading(270)


def moving_ball():
    ball.forward(ball_speed)


def side_limit_check():
    if ball.xcor() <= (BORDER_LEFT + 10) or ball.xcor() >= (BORDER_RIGHT - 10):
        ball.setheading(180 + -ball.heading())
        ball.forward(ball_speed)


def bot_limit_check():
    global life
    if ball.ycor() <= BORDER_BOT:
        life -= 1
        draw_life()
        starting_ball_position()
        return life


def top_limit_check():
    if ball.ycor() >= BORDER_TOP:
        ball.setheading(-ball.heading())
        ball.forward(ball_speed)


def collision_block_check():
    global game_score
    for n in range(len(all_blocks)):
        for i in range(len(blocks_row1)):
            if (abs(ball.xcor() - all_blocks[n][i].xcor()) < 40) and \
                    (abs(ball.ycor() - all_blocks[n][i].ycor()) < 20) and all_blocks[n][i].isvisible():
                all_blocks[n][i].hideturtle()
                ball.setheading(-ball.heading())
                ball.forward(ball_speed)
                game_score += 1
                draw_game_score()


def collision_paddle_check():
    if (abs((abs(ball.xcor()) - abs(paddle.xcor()))) < (160 / (life + 1))) and (ball.ycor() <= (paddle.ycor() + 20)):
        if ball.heading() == 270 or -270:
            ball.setheading(random.randint(45, 135))
        else:
            ball.setheading(-ball.heading())
            ball.forward(ball_speed)


game_score = 0
show_game_score = turtle.Turtle()
show_game_score.penup()
show_game_score.pencolor("DarkRed")
show_game_score.speed(0)
show_game_score.goto(300, -480)
show_game_score.color("DarkRed")
show_game_score.write("SCORE: " + str(game_score), font=("Arial", 10, "bold"))


def draw_game_score():
    global game_score
    show_game_score.clear()
    show_game_score.write("SCORE: " + str(game_score), font=("Arial", 10, "bold"))


def score_control():
    global game_score
    if game_score == 27:
        wn.clear()
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.pencolor("black")
        game_over.speed(0)
        game_over.goto((BORDER_LEFT + 10), 0)
        game_over.write("YOU WON!", font=("Arial", 50, "bold"))
        time.sleep(5)


show_life = turtle.Turtle()
show_life.penup()
show_life.pencolor("black")
show_life.speed(0)
show_life.goto((BORDER_LEFT + 2), (BORDER_BOT + 10))
show_life.color("DarkRed")


def draw_life():
    global life
    show_life.clear()
    show_life.write("Lives: " + str(life), font=("DarkRed", 20, "bold"))


def life_control():
    global life
    if life == 3:
        width_paddle = 8 / life
        paddle.shapesize(2, width_paddle)
        return
    elif life == 2:
        width_paddle = 8 / life
        paddle.shapesize(2, width_paddle)
        return

    elif life == 1:
        width_paddle = 8
        paddle.shapesize(2, width_paddle / life)
        return

    else:
        wn.clear()
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.pencolor("black")
        game_over.speed(0)
        game_over.goto((BORDER_LEFT + 10), 0)
        game_over.write("GAME OVER!", font=("Arial", 50, "bold"))
        time.sleep(5)


starting_block_positions()
starting_paddle_position()
starting_ball_position()
draw_life()

while 1 == 1:
    life_control()
    score_control()
    ball.showturtle()
    side_limit_check()
    if ball.ycor() > 350:
        top_limit_check()
        collision_block_check()
    elif ball.ycor() < -350:
        collision_paddle_check()
        bot_limit_check()

    moving_ball()

    wn.onkeypress(move_left, "a")
    wn.onkeypress(move_left, "Left")
    wn.onkeypress(move_right, "Right")
    wn.onkeypress(move_right, "d")
    wn.listen()
