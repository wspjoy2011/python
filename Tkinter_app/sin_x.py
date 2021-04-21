from tkinter import *
import math

width, height = 1040, 640

root = Tk()
root.title('y = sin(x)')
root.geometry(f'{width+360}x{height}')

canvas = Canvas(root, width=width+20, height=height, bg='navy')
sin_line = None

for y in range(21):
    k = 50 * y
    canvas.create_line(5+k, height, 5+k, 1, width=1, fill='blue')

for x in range(13):
    k = 50 * x
    canvas.create_line(1, 10+k, width, 10+k, width=1, fill='blue')

canvas.create_line(10, 1, 10, height, width=2, arrow=FIRST, fill='white')
canvas.create_line(1, height//2-10, width, height//2-10, width=2, arrow=LAST,fill='white')

canvas.create_text(40, 10, text='300', fill='white')
canvas.create_text(40, height-10, text='-300', fill='white')
canvas.create_text(30, height//2-20, text='0', fill='white')
canvas.create_text(width-20, height//2 - 20, text='1000', fill='white')


label_w = Label(root, text='Cyclic frequency: ', font='Helvetica 10 bold')
label_w.place(x=0, y=10)
label_phi = Label(root, text='X shift of the graph: ', font='Helvetica 10 bold')
label_phi.place(x=0, y=40)
label_A = Label(root, text='Amplitude: ', font='Helvetica 10 bold')
label_A.place(x=0, y=70)
label_dy = Label(root, text='Y shift of the graph: ', font='Helvetica 10 bold')
label_dy.place(x=0, y=100)

entry_w = Entry(root)
entry_w.insert(END, '0.0209')
entry_w.place(x=160, y=10)
entry_phi = Entry(root)
entry_phi.insert(END, '20')
entry_phi.place(x=160, y=40)
entry_A = Entry(root)
entry_A.insert(END, '200')
entry_A.place(x=160, y=70)
entry_dy = Entry(root)
entry_dy.insert(END, '320')
entry_dy.place(x=160, y=100)


def sinus(w, phi, A, dy):
    clean()
    global sin_line
    xy = []
    for x in range(1000):
        y = math.sin(x*w)
        xy.append(x+phi)
        xy.append(y*A+dy)
    sin_line = canvas.create_line(xy, fill='red')


def clean():
    canvas.delete(sin_line)


btn_calc = Button(root, text='Calculate')
btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()),
                                            float(entry_phi.get()),
                                            float(entry_A.get()),
                                            float(entry_dy.get())))
btn_calc.place(x=10, y= 140)

btn_cln = Button(root, text='Clean')
btn_cln.bind('<Button-1>', lambda event: clean())
btn_cln.place(x=280, y= 140)


canvas.pack(side='right')
root.mainloop()
