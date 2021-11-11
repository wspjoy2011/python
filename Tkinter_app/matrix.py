import tkinter as tk
import random
import time


win = tk.Tk()
win.title('Matrix')
win.geometry('700x700+250+250')
win.resizable(False, False)
win.bind('<Escape>', quit)

c = tk.Canvas(win, width=700, height=700, bg='black')
c.pack()

chars = 'qwertyuiop[]!@#$%^&*()-=_+1234567890asdfghjkl;|zxcvbnm<>'
chars = list(chars)
length = len(chars)


height = 0
while True:
    c.delete('t' + str(height))
    for i in range(1, length):
        r = random.randint(0, length - 1)
        create_text = c.create_text(i * 20, height, text=chars[r], fill='lime', font=('Comic Sans MS', 11),
                                    tag='t' + str(height))
        rdm = random.randint(1, 10)
        for j in range(10):
            c.move(create_text, 0, rdm)
    c.update()
    height += 25
    if height >= 650:
        height = 0

    time.sleep(0.01)

