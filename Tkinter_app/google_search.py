import tkinter as tk
from tkinter import ttk
import webbrowser


def search():
    webbrowser.open('https://www.google.com.ua/search?q=' + text_field.get())


win = tk.Tk()
win.title('Google search')
win.geometry('590x40+300+200')
win.resizable(False, False)

search_label = ttk.Label(win, text='Google', font=('Roboto', 16, 'bold'))
search_label.grid(row=0, column=0)

text_field = ttk.Entry(win, width=45)
text_field.grid(row=0, column=1)

search_button = ttk.Button(win, text='Search', width=15, command=search)
search_button.grid(row=0, column=2)

win.mainloop()