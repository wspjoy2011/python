from turtle import *
import tkinter as tk


HELP_TEXT = '''Help information
Press <Escape> key to exit.
Press <c> key to open pick color window.
'''
SPEED = 5


class MainWindow:
    def __init__(self):
        self.window = Screen()
        self.window.title('Move turtle')
        self.window.setup(500, 500)
        self.window.bgpic('bg.gif')
        self.key_state = {
            'up_state': False,
            'down_state': False,
            'right_state': False,
            'left_state': False
        }

        self.window.onkey(exit, 'Escape')
        self.window.onkey(self.help_func, 'F1')
        self.window.onkey(self.color_pick, 'c')
        self.window.onkeypress(self.press_up, 'Up')
        self.window.onkeypress(self.press_right, 'Right')
        self.window.onkeypress(self.press_left, 'Left')
        self.window.onkeypress(self.press_down, 'Down')

        self.window.onkeyrelease(self.release_up, 'Up')
        self.window.onkeyrelease(self.release_down, 'Down')
        self.window.onkeyrelease(self.release_left, 'Left')
        self.window.onkeyrelease(self.release_right, 'Right')

        self.window.listen()

    def press_up(self):
        self.key_state['up_state'] = True

    def press_right(self):
        self.key_state['right_state'] = True

    def press_left(self):
        self.key_state['left_state'] = True

    def press_down(self):
        self.key_state['down_state'] = True

    def release_up(self):
        self.key_state['up_state'] = False

    def release_down(self):
        self.key_state['down_state'] = False

    def release_left(self):
        self.key_state['left_state'] = False

    def release_right(self):
        self.key_state['right_state'] = False

    @staticmethod
    def help_func():
        main_help = Help()
        main_help.set_text()

    @staticmethod
    def color_pick():
        color_window = PickColor()
        color_window.window.mainloop()


class PickColor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Pick color')
        self.window.geometry('215x50+700+290')
        self.colors = ['red', 'green', 'blue']
        self.user_choice = 'black'
        self.buttons = [tk.Button(self.window, font=('Arial', 15), text=self.colors[i], bg=self.colors[i],)
                        for i in range(len(self.colors))]
        for i in range(len(self.buttons)):
            self.buttons[i].grid(row=0, column=i)
        self.buttons[0]['command'] = lambda: self.set_user_color(self.colors[0])
        self.buttons[1]['command'] = lambda: self.set_user_color(self.colors[1])
        self.buttons[2]['command'] = lambda: self.set_user_color(self.colors[2])

    def set_user_color(self, color):
        main_pen.set_color(color)
        self.window.destroy()


class MainPen:
    def __init__(self):
        self.pen = Pen()
        self.pen.width(5)
        self.pen.shape('turtle')

    def set_color(self, user_color):
        self.pen.color(user_color)


class Help:
    def __init__(self, help_text=HELP_TEXT):
        self.win_help = tk.Tk()
        self.win_help.title('Help information')
        self.win_help.geometry('500x500+700+290')
        self.win_help.attributes("-topmost", True)
        self.text = tk.Text(self.win_help, width=500, height=500, bg="blue",
                            fg='white', wrap=tk.WORD, font=('Arial', 20, 'bold'))
        self.help_text = help_text

    def set_text(self):
        self.text.insert(1.0, self.help_text)
        self.text['state'] = tk.DISABLED
        self.text.pack()
        self.win_help.mainloop()


class CheckPen:
    def __init__(self, window, turtle):
        self.window = window
        self.turtle = turtle

    def check_state(self):
        x, y = self.turtle.pen.pos()
        if self.window.key_state['up_state'] and self.window.key_state['right_state']:
            self.turtle.pen.setheading(45)
        elif self.window.key_state['up_state'] and self.window.key_state['left_state']:
            self.turtle.pen.setheading(135)
        elif self.window.key_state['left_state'] and self.window.key_state['down_state']:
            self.turtle.pen.setheading(225)
        elif self.window.key_state['right_state'] and self.window.key_state['down_state']:
            self.turtle.pen.setheading(305)
        elif self.window.key_state['down_state']:
            self.turtle.pen.setheading(270)
        elif self.window.key_state['up_state']:
            self.turtle.pen.setheading(90)
        elif self.window.key_state['left_state']:
            self.turtle.pen.setheading(180)
        elif self.window.key_state['right_state']:
            self.turtle.pen.setheading(0)

        if any(self.window.key_state.values()):
            if y < 230 and self.window.key_state['up_state']:
                y += SPEED
            elif y > -230 and self.window.key_state['down_state']:
                y -= SPEED

            if x < 230 and self.window.key_state['right_state']:
                x += SPEED
            elif x > -230 and self.window.key_state['left_state']:
                x -= SPEED
            main_pen.pen.goto(x, y)

        ontimer(self.check_state, 1)


main_pen = MainPen()
main_window = MainWindow()

check = CheckPen(main_window, main_pen)
check.check_state()

main_window.window.mainloop()
