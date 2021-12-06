import turtle

# Основные цвета для персонажа
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'

# Главный объект
t = turtle.Turtle()


# Метод для рисования тела
def body():
    t.pensize(30) # Размер кисти

    t.fillcolor(BODY_COLOR) # Цвет заполнения
    t.begin_fill()

    # Сторона справа
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # Голова
    t.right(180)
    t.circle(100, -180)

    # Сторона слева
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()


# Рисуем очки
def glass():
    # Передвигаем черепашку
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()

    # Устанавливаем цвет
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


# Рисуем рюкзак
def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)
    t.end_fill()


# Вызываем все необходимые методы
body()
glass()
backpack()

turtle.done()
