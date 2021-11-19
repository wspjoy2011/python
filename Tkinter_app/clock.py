import tkinter as tk
from time import strftime

WIN_WIDTH = 750
WIN_HEIGHT = 400
BG_COLOR = '#37474F'
FG_COLOR = 'white'
COLOR_H = '#00897b'
COLOR_M = '#4a8fe7'
COLOR_S = '#8e24aa'


def create_obj():
    start_x, start_y = 100, 100
    for _ in range(3):
        label = tk.Label(win, font=('Futura PT', 50), bg=COLOR_H, fg=FG_COLOR, text='13')
        label.place(x=start_x, y=start_y, width=150, height=150)
        start_x += 200
        label_clock.append(label)
    label_clock[1].config(bg=COLOR_M)
    label_clock[2].config(bg=COLOR_S)

    start_x, start_y = 100, 275
    for _ in range(3):
        label = tk.Label(win, font=('Futura PT', 25), bg=COLOR_H, fg=FG_COLOR, text='hours')
        label.place(x=start_x, y=start_y, width=150, height=50)
        start_x += 200
        label_text.append(label)
    label_text[1].config(bg=COLOR_M, text='minutes')
    label_text[2].config(bg=COLOR_S, text='seconds')


def update_clock():
    h = strftime('%H')
    m = strftime('%M')
    s = strftime('%S')

    label_clock[0].config(text=f'{h}')
    label_clock[1].config(text=f'{m}')
    label_clock[2].config(text=f'{s}')
    win.after(1000, update_clock)


win = tk.Tk()
win.title('Clock v 1.0')
win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}+300+200')
win.resizable(False, False)
win.bind('<Escape>', exit)

canvas = tk.Canvas(win, bg=BG_COLOR, width=WIN_WIDTH, height=WIN_HEIGHT)
canvas.place(x=0, y=0)

label_clock = []
label_text = []

create_obj()
update_clock()

win.mainloop()