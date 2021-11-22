import tkinter as tk
from tkinter import messagebox
from random import randint


WINDOW_WIDTH = 425
WINDOW_HEIGHT = 240


def begin_game():
    begin = messagebox.askquestion('Вопрос', "Начать игру?")
    if begin == 'no':
        exit()


def set_value(value):
    user_entry['state'] = tk.NORMAL
    user_entry.delete(0, tk.END)
    user_entry.insert(0, items[int(value)])
    user_entry['state'] = tk.DISABLED

    comp = comp_choice()

    comp_entry['state'] = tk.NORMAL
    comp_entry.delete(0, tk.END)
    comp_entry.insert(0, items[int(comp)])
    comp_entry['state'] = tk.DISABLED

    calc_result()


def make_button(value):
    return tk.Button(text=items[int(value)], bd=5, font=('Arial', 10), command=lambda: set_value(value))


def comp_choice():
    return randint(0, 2)


def get_entries():
    user = items.index(user_entry.get())
    comp = items.index(comp_entry.get())
    return {'user': user, 'comp': comp}


def calc_result():
    global user_score, comp_score

    user = get_entries()['user']
    comp = get_entries()['comp']

    if user == comp:
        label_result['text'] = 'Ничья'
        label_result['fg'] = 'lime'
    elif (user == 0 and comp == 1) or (user == 1 and comp == 2) \
            or (user == 2 and comp == 0):
        label_result['text'] = 'Вы выиграли!'
        label_result['fg'] = 'blue'
        user_score += 1
    else:
        label_result['text'] = 'Компютер\nвыиграл!'
        label_result['fg'] = 'red'
        comp_score += 1
    set_score()


def set_score():
    if user_score == 3 or comp_score == 3:
        if user_score == 3:
            winner = 'Игрок'
        else:
            winner = 'Компьютер'
        label_score['text'] = f'{user_score}:{comp_score}'
        messagebox.showinfo('Конец партии', f'{winner} выиграл!')
        clear_score()
    else:
        label_score['text'] = f'{user_score}:{comp_score}'


def clear_score():
    global user_score, comp_score
    label_result['text'] = ''
    label_score['text'] = '0:0'
    user_score, comp_score = 0, 0


win = tk.Tk()
win.title('Game')
win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
win.bind('<Escape>', exit)

begin_game()


items = ['Камень', "Ножницы", "Бумага"]
user_score = 0
comp_score = 0


user_entry = tk.Entry(win, justify=tk.CENTER, font=('Arial', 15), width=15)
user_entry['state'] = tk.DISABLED
user_entry.grid(row=0, column=1)

label_user = tk.Label(text='Игрок', font=('Arial', 10, 'bold'))
label_user.grid(row=0, column=0)

comp_entry = tk.Entry(win, justify=tk.CENTER, font=('Arial', 15), width=15)
comp_entry['state'] = tk.DISABLED
comp_entry.grid(row=2, column=1)

label_comp = tk.Label(text='Компьютер', font=('Arial', 10, 'bold'))
label_comp.grid(row=2, column=0)

label_result = tk.Label(font=('Arial', 15, 'bold'))
label_result.grid(row=3, column=1)

label_score = tk.Label(font=('Arial', 15, 'bold'), text=f'{user_score}:{comp_score}')
label_score.grid(row=4, column=1)

make_button('0').grid(row=1, column=0, stick='wens', padx=15, pady=5)
make_button('1').grid(row=1, column=1, stick='wens', padx=15, pady=5)
make_button('2').grid(row=1, column=2, stick='wens', padx=15, pady=5)


win.mainloop()
