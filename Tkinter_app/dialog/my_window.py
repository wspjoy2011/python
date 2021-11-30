#!/usr/bin/python

from tkinter import *
from my_boolean import *
from my_dialog import *


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('main')
        self.master.geometry('400x300+200+150')
        self.button = Button(self.master,
                             text='dialog',
                             command=self.open_dialog)
        self.button.pack(side=BOTTOM)
        self.text = Text(self.master,
                          background='white')
        self.text.pack(side=TOP,
                       fill=BOTH,
                       expand=YES)
        self.master.protocol('WM_DELETE_WINDOW',
                             self.exit_method)
        self.master.mainloop()

    def open_dialog(self):
        self.dialog = Dialog(self.master)
        self.send_value = self.text.get('0.0', END)
        self.return_value = self.dialog.go(self.send_value)
        if self.return_value:
            self.text.delete('0.0', END)
            self.text.insert('0.0', self.return_value)

    def exit_method(self):
        self.dialog = YesNo(self.master)
        self.my_mssg = 'Do you want to exit?'
        self.return_value = self.dialog.go(message = self.my_mssg)
        if self.return_value:
            self.master.destroy()


root = Tk()
Main(root)
