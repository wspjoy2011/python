import tkinter as tk
from tkinter import messagebox
import os

win = tk.Tk()
win.title('Calculator')
win.geometry('500x550+300+200')
win.resizable(False, False)
win.configure(bg='black')
win.bind('<Escape>', quit)


def clip_board(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def calculate(operation):
    global label_value

    if operation == 'C':
        label_value = ''
    elif operation == 'del':
        label_value = label_value[:-1]
    elif operation == 'X^2':
        try:
            label_value = str(eval(label_value) ** 2)
        except (ZeroDivisionError, SyntaxError):
            messagebox.showinfo('Error', 'Use correct values!')
    elif operation == '+/-':
        print(label_value)
        try:
            label_value = str(eval(label_value) * -1)
        except SyntaxError:
            messagebox.showinfo('Syntax error', 'Value cannot be empty!')
    elif operation == '=':
        try:
            label_value = str(eval(label_value))
        except ZeroDivisionError:
            messagebox.showinfo('Zero division error', 'You cannot divide by zero!')
            label_value = '0'
    elif operation == 'Copy':
        clip_board(label_value)
    else:
        if label_value == '0':
            label_value = ''
        label_value += operation
    label_text.configure(text=label_value)


label_value = '0'
label_text = tk.Label(text=label_value, font=('Roboto', 30, 'bold'), bg='black', fg='white')
label_text.place(x=11, y=50)

buttons = ['C', 'del', '+', '=', '1', '2', '3', '/', '4', '5', '6', '*', '7', '8', '9', '-',
           '+/-', '0', 'Copy', 'X^2']
pad_x = 18
pad_y = 140

for button in buttons:
    get_label = lambda x=button: calculate(x)
    tk.Button(text=button, bg='orange', font=('Roboto', 20), command=get_label).place(x=pad_x, y=pad_y,
                                                                                      width=115, height=79)
    pad_x += 117
    if pad_x > 400:
        pad_x = 18
        pad_y += 81


win.mainloop()
