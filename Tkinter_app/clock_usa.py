import tkinter as tk
from time import strftime

time_label = ''
day_label = ''
date_label = ''


def update_clock():
    global time_label, day_label

    time_string = strftime('%I:%M:%S')
    time_label.config(text=time_string)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)

    win.after(1000, update_clock)


def create_clock():
    global time_label, day_label, date_label
    time_label = tk.Label(win, font=('Arial', 50), fg='#00ff00', bg='black')
    time_label.pack()

    day_label = tk.Label(win, font=('Comic Sans MS', 25))
    day_label.pack()

    date_label = tk.Label(win, font=('Comic Sans MS', 30))
    date_label.pack()


win = tk.Tk()
win.title('USA Clock')
win.resizable(False, False)
win.bind('<Escape>', exit)

create_clock()
update_clock()

win.mainloop()