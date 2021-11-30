#!/usr/bin/python

from tkinter import *


class YesNo:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.frame = Frame(self.slave)
        self.frame.pack(side=BOTTOM)
        self.yes_button = Button(self.frame,
                                 text='yes',
                                 command=self.yes)
        self.yes_button.pack(side=LEFT)
        self.no_button = Button(self.frame,
                                text='no',
                                command=self.no)
        self.no_button.pack(side=RIGHT)
        self.label = Label(self.slave)
        self.label.pack(side=TOP,
                        fill=BOTH,
                        expand=YES)
        self.slave.protocol('WM_DELETE_WINDOW', self.no)

    def go(self, title='question',
           message='[question goes here]',
           geometry='200x70+300+265'):
        self.slave.title(title)
        self.slave.geometry(geometry)
        self.label.configure(text=message)
        self.boolean_value = TRUE
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        return self.boolean_value

    def yes(self):
        self.boolean_value = TRUE
        self.slave.destroy()

    def no(self):
        self.boolean_value = FALSE
        self.slave.destroy()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    myTest = YesNo(root)
    if myTest.go(message='Is it working?'):
        print('Yes')
    else:
        print('No')
