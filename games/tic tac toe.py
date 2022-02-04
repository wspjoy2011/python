from turtle import *
from math import pi

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_board():
    for i in range(2):
        drawer.up()
        drawer.goto(-SCREEN_WIDTH // 2, 100 - 200 * i)
        drawer.down()
        drawer.forward(SCREEN_WIDTH)

    drawer.right(90)

    for i in range(2):
        drawer.up()
        drawer.goto(-100 + 200 * i, 300)
        drawer.down()
        drawer.forward(SCREEN_WIDTH)

    num = 1
    for i in range(3):
        for j in range(3):
            drawer.up()
            drawer.goto(-290 + j * 200, 260 - i * 200)
            drawer.down()
            drawer.write(num, font=('Arial', 16, 'bold'))
            num += 1


def draw_x(x, y):
    drawer.up()
    drawer.goto(x, y)
    drawer.down()

    drawer.setheading(60)

    for i in range(2):
        drawer.forward(75)
        drawer.back(150)
        drawer.forward(75)
        drawer.left(60)
    window.update()


def draw_o(x, y):
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)

    for i in range(180):
        drawer.forward((150 * pi) / 180)
        drawer.right(2)
    window.update()


def add_x(row, column):
    announcer.clear()
    if board[row][column] == 'x' or board[row][column] == 'o':
        announcer.write('That spot is taken!', font=('Arial', 36, 'bold'), align='center')
        window.update()
    else:
        draw_x(-200 + 200 * column, 200 - 200 * row)
        board[row][column] = 'x'
        if check_won('x'):
            announcer.goto(0, 0)
            announcer.write('You win!', font=('Arial', 36, 'bold'), align='center')
            window.update()
            deactivate_keys()
        else:
            add_o()
            if check_won('o'):
                announcer.goto(0, 0)
                announcer.write('You lost!', font=('Arial', 26, 'bold'), align='center')
                window.update()
                deactivate_keys()
            elif check_draw():
                announcer.goto(0, 0)
                announcer.write('It\'s a tie!', font=('Arial', 26, 'bold'), align='center')
                window.update()
                deactivate_keys()


def add_o():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                if check_won('o'):
                    draw_o(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = ' '

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'x'
                if check_won('x'):
                    board[i][j] = 'o'
                    draw_o(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = ' '

    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                draw_o(-200 + 200 * j, 200 - 200 * i)
                return


def square_one():
    add_x(0, 0)


def square_two():
    add_x(0, 1)


def square_three():
    add_x(0, 2)


def square_four():
    add_x(1, 0)


def square_five():
    add_x(1, 1)


def square_six():
    add_x(1, 2)


def square_seven():
    add_x(2, 0)


def square_eight():
    add_x(2, 1)


def square_nine():
    add_x(2, 2)


def activate_keys():
    for i in range(9):
        window.onkey(functions[i], str(i + 1))


def deactivate_keys():
    for i in range(9):
        window.onkey(None, str(i+1))


def check_won(letter):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and\
                board[i][0] == letter:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and\
                board[0][i] == letter:
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and\
            board[0][0] == letter:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and\
            board[0][2] == letter:
        return True
    return False


def check_draw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'x':
                count += 1

    if count > 3:
        return True
    return False


def check_click(x, y):
    print(x, y)
    if check_draw() or check_won('x') or check_won('o'):
        return
    if -300 < x < -110 and 110 < y < 300:
        add_x(0, 0)
    elif -94 < x < 94 and 107 < y < 298:
        add_x(0, 1)
    elif 106 < x < 294 and 110 < y < 300:
        add_x(0, 2)
    elif -299 < x < -107 and -92 < y < 95:
        add_x(1, 0)
    elif -94 < x < 94 and -91 < y < 93:
        add_x(1, 1)
    elif 105 < x < 295 and -91 < y < 95:
        add_x(1, 2)
    elif -300 < x < -106 and -290 < y < -104:
        add_x(2, 0)
    elif -92 < x < 94 and -290 < y < - 104:
        add_x(2, 1)
    elif 107 < x < 295 and -290 < y < - 104:
        add_x(2, 2)


functions = [square_one, square_two, square_three, square_four, square_five, square_six, square_seven,
             square_eight, square_nine]

window = Screen()
window.title('Tic tac toe by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.onclick(check_click, btn=1)
window.tracer(0)

announcer = Turtle()
announcer.speed(0)
announcer.hideturtle()
announcer.up()
announcer.goto(0, 0)
announcer.color('red')

drawer = Turtle()
drawer.hideturtle()
drawer.width(10)

board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(' ')
    board.append(row)

activate_keys()
draw_board()

window.update()
window.listen()
window.mainloop()