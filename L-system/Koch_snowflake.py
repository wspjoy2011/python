import turtle


W, H = 1200, 900
wn = turtle.Screen()
wn.setup(W, H, 0, 0)
t = turtle.Turtle()
t.speed(100)
t.up()
t.goto(-300, 200)
t.down()


def draw_koch_segment(t, ln):
    if ln > 6:
        ln3 = ln // 3
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
        t.right(120)
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


t.ht()
for i in range(3):
    draw_koch_segment(t, 200)
    t.right(120)
    # t.left(60)

turtle.done()
