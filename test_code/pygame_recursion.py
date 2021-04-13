import pygame
import sys
import random

pygame.init()

sc = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Pygame recursion')


def fractal_rect(a, b, c, d, deep=10):
    alpha = 0.2
    if deep < 1:
        return
    for m, n in (a, b), (b, c), (c, d), (d, a):
        r1, r2, r3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        pygame.draw.line(sc, (r1, r2, r3), (m[0], m[1]), (n[0], n[1]), 3)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rect(a1, b1, c1, d1, deep - 1)


while True:
    fractal_rect((100, 100), (500, 100), (500, 500), (100, 500), deep=20)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
