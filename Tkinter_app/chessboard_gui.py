from turtle import *
from string import ascii_uppercase
from tkinter import messagebox
import time

size = 40
start_x = -200
start_y = -100
cords = {}
cells = []
counter = 0
chessboard_size = 8


def make_cells():
    for digit in range(chessboard_size):
        for letter in range(chessboard_size):
            cells.append(ascii_uppercase[letter] + str(digit + 1))


def draw_cell():
    for i in range(4):
        pen.forward(size)
        pen.left(90)


def mark_cell(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.color('red')
    draw_cell()
    time.sleep(0.5)
    pen.color('black')
    draw_cell()


def check_pos(x, y):
    for key, item in cords.items():
        if item['x'][0] <= x <= item['x'][1] and item['y'][0] <= y <= item['y'][1]:
            mark_cell(item['x'][0], item['y'][0])
            messagebox.showinfo(f'Your cell', f'{key}\nColor: {item["color"].upper()}')
            break


def normalization_array():
    for key, item in cords.items():
        cords[key]['x'] = [round(min(item['x'])), round(max(item['x']))]
        cords[key]['y'] = [round(min(item['y'])), round(max(item['y']))]
    window.onclick(check_pos, btn=1)


def make_digits(index):
    x, y = pen.pos()
    pen_text.up()
    pen_text.goto(x - 15, y + 5)
    pen_text.down()
    pen_text.write(str(index + 1), align="right", font=("Arial", 12, "normal"))


def make_letters(index):
    x, y = pen.pos()
    pen_text.up()
    pen_text.goto(x + 25, y - 25)
    pen_text.down()
    pen_text.write(ascii_uppercase[index], align="right", font=("Arial", 12, "normal"))


def make_cell(cell_color):
    global counter
    for i in range(4):
        pen.forward(size)
        pen.left(90)
        if cells[counter] not in cords:
            cords[cells[counter]] = {'x': [], 'y': [], 'color': cell_color}
        cords[cells[counter]]['x'].append(pen.pos()[0])
        cords[cells[counter]]['y'].append(pen.pos()[1])
    counter += 1


def make_chessboard():
    global start_y
    for line in range(chessboard_size):
        pen.up()
        pen.goto(start_x, start_y)
        pen.down()
        for cell in range(chessboard_size):
            if line % 2 == 0:
                if cell % 2 == 0:
                    pen.fillcolor('black')
                    cell_color = 'black'
                else:
                    pen.fillcolor('white')
                    cell_color = 'white'
            else:
                if cell % 2 == 0:
                    pen.fillcolor('white')
                    cell_color = 'white'
                else:
                    pen.fillcolor('black')
                    cell_color = 'black'
            pen.begin_fill()
            make_cell(cell_color)
            if line == 0:
                make_letters(cell)
            if cell == 0:
                make_digits(line)
            pen.end_fill()
            pen.fd(size)

        start_y += size


window = Screen()
window.setup(500, 450)
window.onkey(exit, 'Escape')

pen = Pen()
pen.width(2)
pen.hideturtle()
pen.speed(0)

pen_text = Pen()
pen.speed(0)
pen_text.hideturtle()

pen.up()
pen.goto(-200, -100)
pen.down()

make_cells()
make_chessboard()
normalization_array()

window.listen()
window.mainloop()
