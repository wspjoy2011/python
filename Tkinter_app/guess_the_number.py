import tkinter as tk
from tkinter import messagebox

WIN_WIDTH = 400
WIN_HEIGHT = 280

win = tk.Tk()
win.title('Guess the number')
win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}+400+100')

screen_height = win.winfo_screenheight()


start = 0
end = 100
guess = ((end - start) // 2) + start

score = 0


def begin_game(message="Начать игру?"):
    begin = messagebox.askquestion('Вопрос', message)
    if begin == 'no':
        exit()


def guess_number(answer):
    global start, end, guess, score
    if answer == "win":
        end_game()
    elif answer == "less":
        end = guess
    elif answer == "more":
        start = guess
    guess = ((end - start) // 2) + start
    set_value(guess)


def set_value(value):
    entry['state'] = tk.NORMAL
    entry.delete(0, tk.END)
    entry.insert(0, value)
    entry['state'] = tk.DISABLED


def make_button(value):
    return tk.Button(text=value, font=('Arial', 10), bd=5, padx=20, command=lambda: guess_number(value))


def create_history():
    with open('history.txt', 'w') as file:
        file.write('')
        print('File history.txt create')


def write_history():
    with open('history.txt', 'a') as file:
        file.write(str(guess) + '\n')


def read_history():
    history_arr = []
    with open('history.txt', 'r') as file:
        for line in file:
            history_arr.append(line.strip() + '\n')
    label_history['text'] = f'History:\n{"".join(history_arr)}'


def end_game():
    global start, end, score, WIN_HEIGHT
    messagebox.showinfo('Результат', f"Компьютер угадал ваше число - {guess}!")
    start = 0
    end = 100
    score += 1
    label_score['text'] = f'Score: {score}'
    begin_game('Продолжить игру?')
    write_history()
    read_history()
    WIN_HEIGHT += 20
    win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}+400+100')
    check_win_height()


def check_win_height():
    global WIN_HEIGHT
    if WIN_HEIGHT > screen_height - 600:
        create_history()
        read_history()
        WIN_HEIGHT = 280
        win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}+400+100')


if begin_game():
    guess_number('less')


label_title = tk.Label(text='Your number:', font=('Arial', 12))
label_title.grid(row=0, column=1)

entry = tk.Entry(win, font=('Arial', 15), justify='center')
entry['state'] = tk.DISABLED
entry.grid(row=1, column=0, columnspan=3, stick='we', padx=50, pady=15)

label_score = tk.Label(text='Score: 0', font=('Arial', 15), pady=15, fg='red')
label_score.grid(row=3, column=1)

label_history = tk.Label(text='History:', font=('Arial', 12), pady=15)
label_history.grid(row=4, column=1)

make_button('less').grid(row=2, column=0)
make_button('win').grid(row=2, column=1)
make_button('more').grid(row=2, column=2)

create_history()
set_value(guess)


win.mainloop()