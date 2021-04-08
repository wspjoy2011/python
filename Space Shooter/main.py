import pygame
import os
import time
import random
pygame.font.init()

pygame.init()
pygame.mixer.init()
music = os.path.join('assets', 'background.mp3')
laser_sound = pygame.mixer.Sound(os.path.join('assets', 'laser.wav'))
hit_sound = pygame.mixer.Sound(os.path.join('assets', 'hit.wav'))
game_over_sound = os.path.join('assets', 'game_over.mp3')


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')
FPS = 60


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(height >= self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                hit_sound.play()
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            laser_sound.play()
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y + self.ship_img.get_height() + 10,
                                      self.ship_img.get_width(), 10))
        pygame.draw.rect(window, GREEN, (self.x, self.y + self.ship_img.get_height() + 10,
                        self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
    COLOR_MAP = {
            'red': (RED_SPACE_SHIP, RED_LASER),
            'blue': (BLUE_SPACE_SHIP, BLUE_LASER),
            'green': (GREEN_SPACE_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.color = None

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = round(obj2.x - obj1.x)
    offset_y = round(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def main():
    run = True
    game_over = False
    lost_count = 0
    clock = pygame.time.Clock()
    level = 0
    lives = 5
    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('comicsans', 70)
    player_vel = 5
    player = Player(round(WIDTH / 2 - YELLOW_SPACE_SHIP.get_width() / 2),
                    round(HEIGHT - YELLOW_SPACE_SHIP.get_height() - player_vel) - 20)

    laser_vel = 5
    enemies = []
    wave_length = 5
    enemy_vel = 1

    def redraw_window(lost):
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f'Lives: {lives}', 1, WHITE)
        level_label = main_font.render(f'Level:  {level}', 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        if lost:
            lost_label = lost_font.render('You lost!', 1, WHITE)
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2,
                                  HEIGHT/2 - lost_label.get_height()/2))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window(game_over)


        if lives <= 0 or player.health <= 0:
            game_over = True
            lost_count += 1

        if game_over:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                color = random.choice(['red', 'green', 'blue'])
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                              color)
                enemy.color = color
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0 + player_vel:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y < HEIGHT - (player_vel + player.get_height() + 20):
            player.y += player_vel
        if keys[pygame.K_LEFT] and player.x > 0 + player_vel:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x < WIDTH - (player_vel + player.get_width()):
            player.x += player_vel
        if keys[pygame.K_o]:
            player.health = 100
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            if enemy.color == 'red':
                enemy.move(1.3)
            else:
                enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 3*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                hit_sound.play()
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)


def main_menu():
    title_font = pygame.font.SysFont('comicsans', 70)
    run = True

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, WHITE)
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

    pygame.quit()


main_menu()
