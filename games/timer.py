from turtle import *
import winsound

SCREEN_SIZE = 600
start_time = 5
font = ('Arial', 56, 'bold')
press_start = False
press_stop = False


def check_user_time():
    global start_time
    if user_time:
        if user_time.isdigit():
            start_time = int(user_time)


def new_user_time():
    global user_time
    print('F1')
    user_time = window.textinput(title="Timer", prompt="Enter number of seconds:")
    check_user_time()


def draw_button():
    button.speed(0)
    button.hideturtle()
    button.up()
    button.goto(-200, -500)
    button.width(5)
    button.down()
    button.fillcolor('sky blue')
    button.begin_fill()
    for _ in range(2):
        print(button.pos())
        button.forward(400)
        button.left(90)
        button.forward(100)
        button.left(90)
    button.end_fill()
    button.up()
    text.goto(0, -470)
    text.write('start', font=('Arial', 16, 'bold'), align='center')


def click_start(x, y):
    global press_stop, press_start
    if -200 <= x <= 200 and -500 <= y <= -400:
        if not press_start:
            press_stop = False
            press_start = True
            text.clear()
            text.write('stop', font=('Arial', 16, 'bold'), align='center')
            start_timer()
        else:
            text.clear()
            text.write('start', font=('Arial', 16, 'bold'), align='center')
            press_stop = True
            press_start = False


def parse_time():
    second = start_time % (24 * 3600)
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    if second < 10:
        second = '0' + str(second)
    return hour, minute, second


def start_timer():
    global start_time, press_start
    pen.clear()
    hour, minute, second = parse_time()
    pen.write(f'{hour}:{minute}:{second}', font=font, align='center')
    start_time -= 1
    if start_time >= 0:
        if not press_stop:
            window.ontimer(start_timer, 1000)
    else:
        winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
        start_time = 5
        check_user_time()
        press_start = False
        text.clear()
        text.write('start', font=('Arial', 16, 'bold'), align='center')


window = Screen()
window.title('Timer by @wspjoy')
window.setup(SCREEN_SIZE, SCREEN_SIZE)
window.setworldcoordinates(-SCREEN_SIZE, -SCREEN_SIZE, SCREEN_SIZE, SCREEN_SIZE)
window.onkey(exit, 'Escape')
window.onclick(click_start, btn=1)
window.tracer(0)
user_time = window.textinput(title="Timer", prompt="Enter number of seconds:")
check_user_time()

pen = Pen()
pen.hideturtle()
pen.up()
pen.color('red')

button = Pen()
text = Pen()
text.up()
text.hideturtle()
draw_button()

window.onkey(new_user_time, 'F1')
window.update()
window.listen()
window.mainloop()
