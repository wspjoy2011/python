import pygame

pygame.init()


win = pygame.display.set_mode((500, 480))

pygame.display.set_caption('Goblin fight')

icon = pygame.image.load("assets/ico.png")
pygame.display.set_icon(icon)

# Score

score = 0
font = pygame.font.Font('assets/font/regionaire.ttf', 42)
textX = 10
textY = 10

################
walkRight = [pygame.image.load('assets/main_character/R1.png'), pygame.image.load('assets/main_character/R2.png'),
             pygame.image.load('assets/main_character/R3.png'),
             pygame.image.load('assets/main_character/R4.png'), pygame.image.load('assets/main_character/R5.png'),
             pygame.image.load('assets/main_character/R6.png'),
             pygame.image.load('assets/main_character/R7.png'), pygame.image.load('assets/main_character/R8.png'),
             pygame.image.load('assets/main_character/R9.png')]
walkLeft = [pygame.image.load('assets/main_character/L1.png'), pygame.image.load('assets/main_character/L2.png'),
            pygame.image.load('assets/main_character/L3.png'),
            pygame.image.load('assets/main_character/L4.png'), pygame.image.load('assets/main_character/L5.png'),
            pygame.image.load('assets/main_character/L6.png'),
            pygame.image.load('assets/main_character/L7.png'), pygame.image.load('assets/main_character/L8.png'),
            pygame.image.load('assets/main_character/L9.png')]
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/main_character/standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('assets/sounds/bullet.wav')
hitSound = pygame.mixer.Sound('assets/sounds/hit.wav')

music = pygame.mixer_music.load('assets/sounds/music.mp3')
pygame.mixer.music.play(-1)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif man.right:
                win.blit(walkRight[man.walkCount // 3], (man.x, man.y))
                man.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 415
        self.walkCount = 0
        fontHit = pygame.font.SysFont('comicsans', 100)
        textHit = fontHit.render('-5', 1, (255, 0, 0))
        win.blit(textHit, (250 - (textHit.get_width() / 2), 240 - (textHit.get_height() / 2)))
        win.blit(char, (self.x, self.y))

        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()





class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy(object):
    walkRight = [pygame.image.load('assets/enemy_character/R1E.png'), pygame.image.load('assets/enemy_character/R2E.png'),
                 pygame.image.load('assets/enemy_character/R3E.png'),
                 pygame.image.load('assets/enemy_character/R4E.png'), pygame.image.load('assets/enemy_character/R5E.png'),
                 pygame.image.load('assets/enemy_character/R6E.png'),
                 pygame.image.load('assets/enemy_character/R7E.png'), pygame.image.load('assets/enemy_character/R8E.png'),
                 pygame.image.load('assets/enemy_character/R9E.png'),
                 pygame.image.load('assets/enemy_character/R10E.png'), pygame.image.load('assets/enemy_character/R11E.png')]
    walkLeft = [pygame.image.load('assets/enemy_character/L1E.png'), pygame.image.load('assets/enemy_character/L2E.png'),
                pygame.image.load('assets/enemy_character/L3E.png'),
                pygame.image.load('assets/enemy_character/L4E.png'), pygame.image.load('assets/enemy_character/L5E.png'),
                pygame.image.load('assets/enemy_character/L6E.png'),
                pygame.image.load('assets/enemy_character/L7E.png'), pygame.image.load('assets/enemy_character/L8E.png'),
                pygame.image.load('assets/enemy_character/L9E.png'),
                pygame.image.load('assets/enemy_character/L10E.png'), pygame.image.load('assets/enemy_character/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 20, self.y, 28, 64)
        self.health = 9
        self.visible = True

    def draw(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.velocity > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))
            self.hitbox = [self.x + 17, self.y + 2, 31, 57]
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            self.hitbox[0] = 0
            self.hitbox[1] = 0
            self.hitbox[2] = 0
            self.hitbox[3] = 0

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print(score)


def show_score(x, y):
    score_show = font.render('Score: ' + str(score), True, (255, 0, 0))
    win.blit(score_show, (x, y))


man = Player(50, 415, 64, 64)
goblin = Enemy(100, 420, 64, 64, 450)
shootLoop = 0
bullets = []


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    show_score(textX, textY)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


running = True

while running:
    clock.tick(27)

    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.right:
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6,
                                      (0, 0, 0), facing))
        shootLoop = 1

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT]:
        if man.x > 0:
            man.x -= man.velocity
            man.left = True
            man.right = False
            man.standing = False
    elif keys[pygame.K_RIGHT]:
        if man.x < 500 - man.width:
            man.x += man.velocity
            man.right = True
            man.left = False
            man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_DOWN]:
            if man.y < 480 - man.height - man.velocity:
                man.y += man.velocity
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0

    else:
        neg = 1
        if man.jumpCount < 0:
            neg = -1
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
