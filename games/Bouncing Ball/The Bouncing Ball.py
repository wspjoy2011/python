from tkinter import *
import random
import time


def tick():
    global touch
    f_temp = "Hit the ball: " + str(touch)
    label1.configure(text=str(f_temp))


start = 1
touch = 0
root = Tk()

root.title('The Bouncing Ball')
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
root.iconbitmap('ico.ico')

canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
my_image = PhotoImage(file='source.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
text = canvas.create_text(100,10,fill="red",font="Times 20 italic bold", text="Click LeftButton to start", anchor="nw")

canvas.pack()
root.update()


label1 = Label(root, width=14, font=("Comic Sans MS", 20), text='0')
label1.pack()


class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def draw(self, speed):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = speed
        if pos[3] >= self.canvas_height:
            self.y = -speed
            if self == ball:
                self.hit_bottom = True
                canvas.create_text(100, 10, fill="red", font="Times 20 italic bold",
                                          text="\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Game Over", anchor="nw")
        if self.hit_paddle(pos) == True:
            self.y = -speed
        if pos[0] <= 0:
            self.x = speed
        if pos[2] >= self.canvas_width:
            self.x = -speed


    def hit_paddle(self, pos):
        global touch
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                if self == ball:
                    touch += 1
                self.x += self.paddle.x
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1
        elif pos[2] >= self.canvas_width:
            self.x = -1

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def start_game(self, evt):
        self.started = True
        canvas.delete(2)


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, 'red', paddle)
ball1 = Ball(canvas, 'lime', paddle)

while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw(1)
        ball1.draw(2)
        paddle.draw()
    tick()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
